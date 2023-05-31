# 爬取README.md到'One-Readmes/'

import requests        #导入requests包
import json
from shutil import copyfile
import time
import datetime
import os
from sys import argv
token, bg, ed = [int(it) for it in argv[1:]]

crepos = {}
with open('Chosen-repos.txt', 'r') as ipfile:
    i = 0
    for repo in ipfile:
        if repo != '\n':
            # p = repo.find('github.com/')
            crepos[repo[:-1]] = i
        i += 1
repos = []
with open('One-Chosen-repos.txt', 'r') as ipfile:
    for repo in ipfile:
        if repo != '\n':
            # p = repo.find('github.com/')
            repos.append(repo[:-1])
i = 0
with open('Ghtokens.txt', 'r') as ipfile:
    tokens = ipfile.readlines()
headers = {
    "Authorization" : 'token ' + tokens[token][:-1]
}
key_dict = {'per_page' : 100}
for i in range(bg, ed):
    repo = repos[i]
    if os.path.exists('One-Readmes/' + str(i)):
        continue
    if repo in crepos.keys():
        ex = crepos[repo]
        if os.path.exists('Readmes/' + str(ex)):
            copyfile('Readmes/' + str(ex), 'One-Readmes/' + str(i))
            print(i, ex)
            continue
    url = 'https://api.github.com/repos/' + repo + '/contents/README.md'
    try:
        strhtml = requests.get(url, params=key_dict, headers=headers).text
    except:
        print('Error:', repo)
        continue
    try:
        strhtml_json = json.loads(strhtml)
    except:
        print('Error:', repo)
        continue
    if isinstance(strhtml_json, list):
        strhtml_json = strhtml_json[0]
    if 'message' in strhtml_json.keys():
        if strhtml_json["message"] in {"Not Found", "Repository access blocked"}:
            print(repo)
            continue
        elif strhtml_json["message"].startswith("API rate limit exceeded"):
            while 'message' in strhtml_json.keys() and strhtml_json["message"].startswith("API rate limit exceeded"):
                now_time = datetime.datetime.now()
                print(i, now_time.strftime('%H:%M:%S'))
                time.sleep(300)
                strhtml = requests.get(url, params=key_dict, headers=headers).text
                try:
                    strhtml_json = json.loads(strhtml)
                except:
                    print('Error:', repo)
                    continue
        else:
            print(strhtml)
            continue
    if 'download_url' in strhtml_json.keys():
        url = strhtml_json['download_url']
    else:
        print('Error:', repo)
        print(strhtml)
        continue
    try:
        strhtml = requests.get(url, params=key_dict, headers=headers).text
    except:
        print(repo)
        continue
    with open('One-Readmes/' + str(i), 'w') as opfile:
        opfile.write(strhtml)
        