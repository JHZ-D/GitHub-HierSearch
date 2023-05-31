import requests        #导入requests包
import json
import sys
import time
repos = []
with open('DirGitUnif.txt', 'r') as ipfile:
    for repo in ipfile:
        if repo != '\n':
            p = repo.find('github.com/')
            repos.append(repo[p + 11:-1])
i = 0
headers = {
    "Authorization" : "token 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"
}
key_dict = {'per_page' : 100}
for i in range(2280, 2281):
    repo = repos[i]
# for repo in repos:
    # if i < 1:
    #     i += 1
    #     continue
    url = 'https://api.github.com/repos/' + repo + '/stargazers'
    users = []
    for j in range(1, 40001):
        key_dict['page'] = j
        strhtml = requests.get(url, params=key_dict, headers=headers).text
        strhtml_json = json.loads(strhtml)
        if strhtml[0] == '{':
            if strhtml_json["message"] in {"Not Found", "Repository access blocked"}:
                print(repo)
                break
            elif strhtml_json["message"].startswith("API rate limit exceeded"):
                while strhtml[0] == '{' and strhtml_json["message"].startswith("API rate limit exceeded"):
                    time.sleep(300)
                    strhtml = requests.get(url, params=key_dict, headers=headers).text
                    strhtml_json = json.loads(strhtml)
            else:
                print(strhtml)
                sys.exit(0)
        for user in strhtml_json:
            users.append(user['login'])
        if len(strhtml_json) < 100:
            break
    with open('Github-First-Stargazers/' + str(i), 'w') as opfile:
        for user in users:
            opfile.write(user + '\n')
    # i += 1
        