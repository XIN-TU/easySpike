# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 18:33:44 2021

@author: 70473
"""
# import packages
import re
from stemming.porter2 import stem
from collections import defaultdict
import collections
import numpy as np
import pandas as pd

class Tfidf_search:
    
    def preprocessing(self,data,tag=False):
    #     For tokenisation, you can simply split on every non-letter character, or you can have special treatment for some cases (such as - or '). Please explain in your report your selections and why you did so.
        token_ls = re.split(r"[^\w]",data)
        lower_tkls = [i.lower() for i in token_ls]
        if not tag:
            stem_ls = [stem(i) for i in lower_tkls]
        else:
    #     For stopping Please use the stop words list mentioned above.
            with open("englishST.txt") as f:
                stop_words = f.readlines()
            stop_words_ls = [i.strip() for i in stop_words]
            rmst_ls =[i for i in lower_tkls if i not in stop_words_ls]
    #     for stemming, you do NOT need to write your own stemmer. Use any available package for Porter stemmer. 
            stem_ls = [stem(i) for i in rmst_ls]
        return " ".join(stem_ls)
    
        # read data collections and generate the positional inverted index
    def inverted_index_generation(self,filepath):
        data = pd.read_csv(filepath)
        data.drop("Unnamed: 0",axis = 1,inplace =True)
        data["id"] = data.index + 1
        new = data['content'].str.split("\r\n\r\n", n=2, expand=True)
        data['ingredients'] = new[1]
        data['instructions'] = new[2]
        term_s_dic = defaultdict(list)
        all_set = set(data["id"].values)
        self.db = data
        for sample in data.values:
        #     print(sample[1])
            title_ls = self.preprocessing(sample[0],True).split()
            content_ls = self.preprocessing(sample[1],True).split()
            all_text_ls = title_ls+content_ls
        #     print(all_text_ls)
            for pos,i in enumerate(all_text_ls):
                term_s_dic[i].append((sample[8],pos+1))
        return term_s_dic,all_set
    
    def remove_posi_index(self,posi_inverted_index):
        inverted_index_dictionary = defaultdict(set)
        for key,value in posi_inverted_index.items():
            inverted_index_dictionary[key] = [i[0] for i in value]
        return inverted_index_dictionary

    def search(self,inverted_index_dictionary,formula_ls):
        document_ls = []
        for word in formula_ls:
            index = inverted_index_dictionary[self.preprocessing(word,True)]
    #         print(index)
            document_ls.append(set(index))
        term_index_ls = set()
        for i in document_ls:
            term_index_ls = term_index_ls | i
        return term_index_ls
    
    def return_rank(self,posi_inverted_index,all_set,query):
        term_s_dic = self.remove_posi_index(posi_inverted_index)
        N = len(all_set)
        results = []
        formula_ls = self.preprocessing(query,True).split()
        for docid in self.search(term_s_dic,formula_ls):
            tf_idf = 0
            for token in formula_ls:
                if collections.Counter(term_s_dic[token])[docid] !=0:
                    tf_idf += (1+np.log10(collections.Counter(term_s_dic[token])[docid])) * np.log10(N/len(set(term_s_dic[token])))
            results.append((docid,tf_idf))
        score_ls = sorted(results,key = lambda x:x[1],reverse = True)
        id_list = [i[0] for i in score_ls]
        # print(score_ls)
        return id_list
    
if __name__ == "__main__":
    new_search = Tfidf_search()    
    posi_inverted_index,all_set =new_search.inverted_index_generation("test_data.csv")
    posi_inverted_index = dict(sorted(posi_inverted_index.items(),key = lambda item:item[0]))
    query = input("please input the search receipe with critical words:\n")
    id_rank_list = new_search.return_rank(posi_inverted_index,all_set,query)
    