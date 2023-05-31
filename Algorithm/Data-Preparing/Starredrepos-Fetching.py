import requests        #导入requests包
import json
import sys
import time
users = []
with open('Stargazers.txt', 'r') as ipfile:
    for user in ipfile:
        if user != '\n':
            users.append(user[:-1])
headers = {
    "Authorization" : "token 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"
}
key_dict = {'per_page' : 100}
s = set()
for i in range(10000):
    user = users[i]
    url = 'https://api.github.com/users/' + user + '/starred'
    j = 1
    repos = []
    while True:
        key_dict['page'] = j
        strhtml = requests.get(url, params=key_dict, headers=headers).text
        strhtml_json = json.loads(strhtml)
        if strhtml[0] == '{':
            if strhtml_json["message"] in {"Not Found", "Repository access blocked"}:
                print(user)
                break
            elif strhtml_json["message"].startswith("API rate limit exceeded"):
                while strhtml[0] == '{' and strhtml_json["message"].startswith("API rate limit exceeded"):
                    time.sleep(300)
                    strhtml = requests.get(url, params=key_dict, headers=headers).text
                    strhtml_json = json.loads(strhtml)
            elif strhtml_json["message"].startswith("In order to keep"):
                print(user)
                break
            else:
                print(strhtml)
                sys.exit(0)
        for repo in strhtml_json:
            repos.append(repo['full_name'])
        if len(strhtml_json) < 100:
            break
        j += 1
    with open('Starred-Repos/' + str(i), 'w') as opfile:
        for repo in repos:
            opfile.write(repo + '\n')
    
