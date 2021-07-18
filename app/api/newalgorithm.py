import re
from stemming.porter2 import stem
import math
import psycopg2

class search_modules:

    def preprocessing(self, data: str, tag=False) -> str:
        #     For tokenisation, you can simply split on every non-letter character, or you can have special treatment for some cases (such as - or '). Please explain in your report your selections and why you did so.
        token_ls = re.split(r"[^\w]", data)
        lower_tkls = [i.lower() for i in token_ls]
        if not tag:
            stem_ls = [stem(i) for i in lower_tkls]
        else:
            #     For stopping Please use the stop words list mentioned above.
            with open("englishST.txt") as f:
                stop_words = f.readlines()
            stop_words_ls = [i.strip() for i in stop_words]
            rmst_ls = [i for i in lower_tkls if i not in stop_words_ls]
            #     for stemming, you do NOT need to write your own stemmer. Use any available package for Porter stemmer.
            stem_ls = [stem(i) for i in rmst_ls]
        return " ".join(stem_ls)

    def or_search(self, input_str):
        document_ls = []
        query = self.preprocessing(input_str, True)
        query_ls = query.split()
        for word in query_ls:
            # 这里要接数据库
            db = dbAPI()
            index = db.queryWordWithoutPos(word)
            #         print(index)
            document_ls.append(set(index))
        term_index_ls = set()
        for i in document_ls:
            term_index_ls = term_index_ls | i
        return term_index_ls, query




# 重写搜索模块
class retrieval_modules:

    def __init__(self, db):
        self.db = db
        self.memory_index = {}
        self.total_doc_numbers = db.queryDocNum()

    # 将从数据库中inverted_index表中获得的数据加入到memory中
    def add_to_memory(self, token_name: str, index: str):
        index_list = index.split("\n")
        self.memory_index[token_name] = {}
        for i in index_list:
            doc_pos = i.split(":")
            doc_id = doc_pos[0]
            pos = doc_pos[1]
            self.memory_index[token_name][int(doc_id)] = len(pos.split(","))

    # total_doc_numbers 文档总数
    def cal_TFIDF(self, query: str) -> list:
        query_word_list = []
        for s in query.split(" "):
            res_now = search_modules.preprocessing(search_modules, s)
            if res_now not in self.memory_index:
                query_res = self.db.queryWord(res_now)
                self.add_to_memory(query_res[1], query_res[3])
            # 这里还需要LRU处理内存 防止内存泄漏
            query_word_list.append(res_now)

        res_map = {}
        for word in query_word_list:
            if word in self.memory_index:
                cur_doc_map = self.memory_index[word]
                DF = len(cur_doc_map)
                IDF = math.log(self.total_doc_numbers / DF, 10)
                for doc in cur_doc_map.keys():
                    TF = cur_doc_map[doc]
                    log_TF = 1 + math.log(TF, 10)
                    score = log_TF * IDF
                    if doc not in res_map:
                        res_map[doc] = score
                    else:
                        res_map[doc] += score
        sorted_list = sorted(list(res_map.items()), key=lambda x: x[1], reverse=True)
        return sorted_list

    # words_num_in_docs 记录各个doc长度的list
    # avg_word_num 全部文档的平均长度
    # para_k1 调和系数1 考虑词频的程度 0-完全不考虑词频
    # para_b 调和系数b 考虑文档长度的程度 0-完全不考虑文档长度
    def cal_BM25(self, query: str, words_num_in_docs: list, avg_word_num: float,
                 para_k1: float = 1, para_b: float = 0.75) -> list:
        query_word_list = []
        for s in query.split(" "):
            res_now = search_modules.preprocessing(search_modules, s)
            if res_now not in self.memory_index:
                query_res = self.db.queryWord(res_now)
                self.add_to_memory(query_res[1], query_res[3])
            # 这里还需要LRU处理内存 防止内存泄漏
            query_word_list.append(res_now)

        res_map = {}
        for word in query_word_list:
            if word in self.memory_index:
                cur_doc_map = self.memory_index[word]
                DF = len(cur_doc_map)
                IDF = math.log(len(words_num_in_docs) / DF, 10)
                for doc in cur_doc_map.keys():
                    TF = cur_doc_map[doc]
                    UP = (para_k1 + 1) * TF
                    DOWN = TF + para_k1 * ((1 - para_b) + para_b * (words_num_in_docs[doc] / avg_word_num))
                    score = UP / DOWN * IDF
                    if doc not in res_map:
                        res_map[doc] = score
                    else:
                        res_map[doc] += score
        sorted_list = sorted(list(res_map.items()), key=lambda x: x[1], reverse=True)
        return sorted_list

        