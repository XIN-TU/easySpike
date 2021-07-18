import re
from stemming.porter2 import stem
import math
import psycopg2

class search_modules:
    def __init__(self):
        self.db = dbAPI()
        self.re_module = retrieval_modules(self.db)

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

    def _judge_and (self,query:str):
        pattern = re.compile(r'.*[Aa][Nn][Dd].*')
        return pattern.match(query)

    def _and_search(self,query_word_list:list) -> list:
        map = {}
        for word in query_word_list:
            indexs = self.db.queryWordWithoutPos(word)
            if indexs is None:
                return []
            for index in indexs:
                if index not in map:
                    map[index] = 1
                else:
                    map[index] += 1
        res_list = []
        for doc in map.keys():
            if map[doc] == len(query_word_list):
                res_list.append(doc)
        return res_list

    def _filter_result(self,search_res:list,docs:list):
        hashset = set(docs)
        new_res = []
        for res in search_res:
            if res[0] in hashset:
                new_res.append(res)
        return new_res

    def search(self,query:str):
        query_word_list = self.re_module.processing_str(query)
        res_BM25 =  self.re_module.cal_BM25(query_word_list)
        if self._judge_and(query):
            print("and search")
            docs = self._and_search(query_word_list)
            return self._filter_result(res_BM25, docs)
        else:
            print("normal search")
            return res_BM25


class dbAPI:
    def __init__(self):
        # initialize the database connection
        print("dbAPI inited")
        self.URL = "postgres://mnfzbtbqqtwxmw:c45b5f08434d82163f69cf2577024e48b7a36851b7dbac1a184b6d8fcf77cd1f@ec2-34-247-118-233.eu-west-1.compute.amazonaws.com:5432/d1hvpuu2kapqvu"
        self.con = psycopg2.connect(self.URL, sslmode='require')

    def queryWordWithoutPos(self, word):
        '''
        Given a word, from INVERTED INDEX: querying and returning list of docIDs.

        '''
        cur = self.con.cursor()
        cur.execute(f'SELECT * from productioninvertednew i where i.token_name = \'{word}\'')
        result = cur.fetchone()
        if result != None:
            d = {}
            for i in result[3].split('\n'):
                z = i.split(':')
                d[int(z[0])] = list(map(int, z[1].split(',')))

            # res = []
            # for i in d:
            #     # print(i)
            #     for x in range(len(d[i])):
            #         # print(i)
            #         res.append(i)

            return [*d]
        else:
            return None
            
    def queryDocIDs(self, doclist):
        cur = self.con.cursor()
        string_t = [str(int) for int in doclist]
        id_list = "(" + ",".join(string_t) + ")"
        print("QUERYING..")
        print("SELECT * from productionraw i where i.\"DocID\" in " + id_list)
        cur.execute(f"SELECT * from productionraw i where i.\"DocID\" in {id_list}")
        result = cur.fetchall()
        return result

    # 新加的两个方法
    def queryWord(self, word):
        '''
        Given a word, from INVERTED INDEX: querying and returning list of docIDs.

        '''
        print('query word')
        cur = self.con.cursor()
        cur.execute(f'SELECT * from productioninvertednew i where i.token_name = \'{word}\'')
        result = cur.fetchone()
        return result

    def queryDocNum(self):
        cur = self.con.cursor()
        cur.execute(f'SELECT COUNT(*) from productionraw')
        result = cur.fetchone()
        return result[0]

# 重写搜索模块
class retrieval_modules:
    def __init__(self, db):
        self.db = db
        self.memory_index = {}
        self.total_doc_numbers = db.queryDocNum()
        self.word_num_list = []
        # 假设有200000篇文章 每篇文章的长度为50
        for i in range(900000):
            self.word_num_list.append(50)

    # 将从数据库中inverted_index表中获得的数据加入到memory中
    def _add_to_memory(self, token_name: str, index: str):
        index_list = index.split("\n")
        self.memory_index[token_name] = {}
        for i in index_list:
            doc_pos = i.split(":")
            doc_id = doc_pos[0]
            pos = doc_pos[1]
            self.memory_index[token_name][int(doc_id)] = len(pos.split(","))

    def processing_str(self,query:str) -> list:
        query_word_list = []
        processed_str = search_modules.preprocessing(search_modules, query,True)
        for res_now in processed_str.split(" "):
            if res_now not in self.memory_index:
                query_res = self.db.queryWord(res_now)
                if query_res is not None:
                    self._add_to_memory(query_res[1], query_res[3])
            # 这里还需要LRU处理内存 防止内存泄漏
            query_word_list.append(res_now)
        return query_word_list

    # total_doc_numbers 文档总数
    def cal_TFIDF(self, query_word_list: list) -> list:
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
    def cal_BM25(self, query_word_list:list, avg_word_num: float=500,
                 para_k1: float = 1, para_b: float = 0.75) -> list:
        words_num_in_docs = self.word_num_list
        res_map = {}
        for word in query_word_list:
            if word in self.memory_index:
                cur_doc_map = self.memory_index[word]
                DF = len(cur_doc_map)
                IDF = math.log(len(words_num_in_docs) / DF, 10)
                for doc in cur_doc_map.keys():
                    TF = cur_doc_map[doc]
                    UP = (para_k1 + 1) * TF
                    # print(">>> DOC length is " + str(doc))
                    DOWN = TF + para_k1 * ((1 - para_b) + para_b * (words_num_in_docs[doc] / avg_word_num))
                    score = UP / DOWN * IDF
                    if doc not in res_map:
                        res_map[doc] = score
                    else:
                        res_map[doc] += score
        sorted_list = sorted(list(res_map.items()), key=lambda x: x[1], reverse=True)
        return sorted_list

if __name__ == "__main__":
    #时刻在内存中保存一个search_modules的对象，以后的搜索都用这个对象搜索
    se = search_modules()
    while (True):
        uinput = input("\n请输入想要查询的句子\n")
        print('res : ',se.search(query=uinput)[:30])

