# -*- coding: utf-8 -*-

import urllib.request, json

filename_in = "test.csv"
filename_out = "test.txt"

def loadText():
    file = open(filename_in, 'r', encoding='utf-8')
    lines = file.readlines()
    for line in lines:
        print(analyze(line.replace("\n", "")))
        saveText(analyze(line.replace("\n", ""))["result"])
    file.close()

def saveText(str):
    file = open(filename_out, 'a', encoding='utf-8')
    file.writelines("\n"+str)
    file.close()

def analyze(str):
    url = "https://nattoh.xyz/mecab/api/1.0/extraction"
    #url = "https://nattoh.xyz/mecab/api/1.0/analyze"
    method = "POST"
    headers = {"Content-Type" : "application/json"}

    obj = {"key" : "hoge", "text" : str}
    json_data = json.dumps(obj).encode("utf-8")

    request = urllib.request.Request(url, data=json_data, method=method, headers=headers)
    with urllib.request.urlopen(request) as response:
        response_body = response.read().decode("utf-8")
        return json.loads(response_body)

if __name__ == '__main__':
    print(analyze("あいうえおかきくけこさしすせそ"))
