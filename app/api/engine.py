# do whatever you need to import; be aware to update pipfile and pipfile.lock accordingly. 
"""
 ________  ________  _______    ______  
|        \|        \|       \  /      \ 
 \$$$$$$$$ \$$$$$$$$| $$$$$$$\|  $$$$$$\
   | $$      | $$   | $$  | $$| $$___\$$
   | $$      | $$   | $$  | $$ \$$    \ 
   | $$      | $$   | $$  | $$ _\$$$$$$\
   | $$      | $$   | $$__/ $$|  \__| $$
   | $$      | $$   | $$    $$ \$$    $$
    \$$       \$$    \$$$$$$$   \$$$$$$ 

"""
from .func import *
from .algorithm import *
# from .newalgorithm import *
from .algo2 import *

def is_vegan(s):
    try:
        str_ls = s.split()
        # print(str_ls)
        # print(s)
        list_string = ["rib","chop","sausage","ham","beef","lamb","pork"]
        string_set = set(str_ls)
        if any([word in string_set for word in list_string]):
            return False
        else:
            return True
    except:
        return False

def is_gluten(s):
    try:
        str_ls = s.split()
        list_string = ["wheat", "barley","rye","Barley","flakes","flour","pearl","Breading","bread","stuffing","Bulgur","Durum","Farro","Graham"]
        string_set = set(str_ls)
        if any([word in string_set for word in list_string]):
            return False
        else:
            return True
    except:
        return False

def is_time(string):
    str_ls_digit = []
    for i in string.split():
        if i.isdigit():
            str_ls_digit.append(int(i))
    if("hour" in string.split() or "hours" in string.split() or len(str_ls_digit)>1):
        return False
    elif str_ls_digit[0]<=30:
        return True
    else:
        return False

def check_cal(string):
    str_ls_digit = []
    for i in string.split():
        if i.isdigit():
            str_ls_digit.append(int(i))
    if len(str_ls_digit) == 0:
        return False
    elif str_ls_digit[0] <= 500:
        return True
    else:
        return False


def engine_init(keywords: str, paras: list) -> list:
    """
    This is the entry for TTDS retrival engine. 
    Implementation is from here. 

    Args:
        keywords (string): a string which is being inputted into the searchbox as keyword.
        paras (list): some special parameters for advanced search. 
    """
    print(">>> ENGINE START! <<<")
    

    '''
    ##### Codes below are really primitive response. Please replace all of them!
        Engine v1: valid search input: index step  [seperated by space]
        e.g., 1 2 returns item 1,2; 2 3 returns 2,3,4
        # Note because some entries are EMPTY, it could return fewer entries. 

    '''
    # init database 
    db = dbAPI()


    ### this is the algorithm v1
    # word_num_list = []
    
    # for i in range(2400000):
    #     word_num_list.append(50)
    # re_mo = retrieval_modules(db)

    # res = re_mo.cal_BM25(keywords, word_num_list, 50)

    ### algorithm v2:
    se = search_modules()
    ret_raw = se.search(query=keywords)[:200]
    id_list = []
    for i in ret_raw:
        id_list.append(i[0])
    print(id_list)

    res_raw = db.queryDocIDs(id_list)
    print("===================================")
    # print(len(list))
    columns = ["index","title","content","time","comments","serving","No_want_to_try","calories","img_link","url_link","ingredients","instructions","id"]

    data_ls = pd.DataFrame(res_raw,columns = columns)
    data_result = data_ls[['title', 'content', 'time', 'comments', 'serving', 'No_want_to_try',
        'calories', 'img_link', 'id', 'ingredients', 'instructions']]
    print(id_list)
    data_result.index = data_result["id"]
    data_result = data_result.loc[id_list]
    # data_result.to_pickle('result.pkl')
    data_result = data_result[data_result['content'].map(len) < 10000]
    print("-----------")
    print(data_result.shape)
    # retrieval_result = pd.DataFrame(data_ls,columns=['title', 'content', 'time', 'comments', 'serving', 'No_want_to_try',
    #    'calories', 'img_link', 'id', 'ingredients', 'instructions'])

    # print(original_db["id"].isin(id_rank_list))
    # result_df = retrieval_result

    print(paras)
    if 'Quick & Easy' in paras:
        print("Quick and easy selected")
        data_result = data_result[data_result["time"].apply(lambda x: is_time(x))]
        
    if 'Calories<500k' in paras:
        print("calories < 500k selected")
        data_result = data_result[data_result["calories"].apply(lambda x: check_cal(x))]

    if 'Gluten free' in paras:
        print("Gluten free selected")
        data_result = data_result[data_result["content"].apply(lambda x:is_gluten(x))]
    if 'Vegetarian' in paras:
        print("eat veg")
        data_result = data_result[data_result["content"].apply(lambda x:is_vegan(x))]
        
    result = data_result.to_json(orient='records')
    parsed = json.loads(result)         


    '''
    #####
    '''

    fp = open('output', 'w')
    for i in parsed:
        fp.writelines(str(i) + '\n\n')
    fp.close()

    return parsed