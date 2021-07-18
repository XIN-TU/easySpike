import pandas as pd
import json


def csv2json(filename, start=0, end=0):

    data = pd.read_csv(filename, names=[
                       'id', 'title', 'content', 'time', 'comments', 'serving', 'Extra', 'calories', 'img_link'])

    # print(data.head(1))

    data.dropna(inplace=True)
    new = data['content'].str.split("\r\n\r\n", n=2, expand=True)
    data['title'] = new[0]
    data['ingredients'] = new[1]
    data['instructions'] = new[2]
    # print(new.shape)

    data.drop(columns=['content'], inplace=True)

    result = data.to_json(orient='records')
    parsed = json.loads(result)

    # print(len(parsed))

    for i in parsed[start:end]:

        if i['title'] == 'None':
            parsed.remove(i)
  
    # print(len(parsed))

    fp = open('output', 'w')
    for i in parsed[start:end]:
        fp.writelines(str(i) + '\n\n')
    fp.close()
    return parsed[start:end]


def csv2json(data, start=0, end=0):

    # data = pd.read_csv(filename, names=[
    #                    'id', 'title', 'content', 'time', 'comments', 'serving', 'Extra', 'calories', 'img_link'])

    # print(data.head(1))

    data.dropna(inplace=True)
    new = data['content'].str.split("\r\n\r\n", n=2, expand=True)
    data['title'] = new[0]
    data['ingredients'] = new[1]
    data['instructions'] = new[2]
    # print(new.shape)

    data.drop(columns=['content'], inplace=True)

    result = data.to_json(orient='records')
    parsed = json.loads(result)

    # print(len(parsed))

    for i in parsed[start:end]:

        if i['title'] == 'None':
            parsed.remove(i)
  
    # print(len(parsed))

    fp = open('output', 'w')
    for i in parsed[start:end]:
        fp.writelines(str(i) + '\n\n')
    fp.close()
    return parsed[start:end]



if __name__ == "__main__":
    print("testing csv-2-json")
    csv2json('sample.csv', 5, 10)
