# 爬取仓库信息：'full_name', 'description', 'fork', 'language', 'stargazers_count', 'topics'到'Gitrepo-Info/'文件夹中

import requests        #导入requests包
import json
from shutil import copyfile
import time
import datetime
import os
import sys
import copy
from sys import argv
token, bg, ed, fn = [int(it) for it in argv[1:]]

with open('Ghtokens.txt', 'r') as ipfile:
    tokens = ipfile.readlines()
headers = {
    "Authorization" : 'token ' + tokens[token][:-1]
}
key_dict = {'per_page' : 100}
repos = []
with open('One-Chosen-repos.txt', 'r') as ipfile:
    for repo in ipfile:
        if repo != '\n':
            # p = repo.find('github.com/')
            repos.append(repo[:-1])    
wrrepos = []
for i in range(bg, ed):
    repo = repos[i]
    url = 'https://api.github.com/repos/' + repo
    
    try:
        strhtml = requests.get(url, params=key_dict, headers=headers).text
    except:
        print('28 Error:', repo)
        continue
    try:
        strhtml_json = json.loads(strhtml)
    except:
        print('33 Error:', repo)
        continue
    if isinstance(strhtml_json, list):
        print('37', repo, strhtml)
        continue
    if 'message' in strhtml_json.keys():
        if strhtml_json["message"] in {"Not Found", "Repository access blocked", 'This repository is empty.'}:
            print('41 Error:', repo)
        elif strhtml_json["message"].startswith("API rate limit exceeded"):
            while isinstance(strhtml_json, dict) and 'message' in strhtml_json.keys() and strhtml_json["message"].startswith("API rate limit exceeded"):
                now_time = datetime.datetime.now()
                print(i, now_time.strftime('%H:%M:%S'))
                time.sleep(300)
                strhtml = requests.get(url, params=key_dict, headers=headers).text
                try:
                    strhtml_json = json.loads(strhtml)
                except:
                    print('50 Error:', repo)
                    continue
        else:
            print('55', repo, strhtml)
            continue
    repodict = {}
    # repodict['id'] = i
    # repodict['full_name'] = strhtml_json['full_name']
    repodict = {key: value for key, value in strhtml_json.items() if key in ['full_name', 'description', 'fork', 'language', 'stargazers_count', 'topics']}
    repodict['id'] = i
    wrrepos.append(copy.deepcopy(repodict))
    if i % 20 == 0:
        with open('Gitrepo-Info/' + str(fn) + '.txt', 'a') as opfile:
            for repo in wrrepos:
                strhtml = json.dumps(repo, indent=1)
                opfile.write(strhtml + ',\n')
            wrrepos = []
with open('Gitrepo-Info/' + str(fn) + '.txt', 'a') as opfile:
    for repo in wrrepos:
        strhtml = json.dumps(repo, indent=1)
        opfile.write(strhtml + ',\n')
    wrrepos = []