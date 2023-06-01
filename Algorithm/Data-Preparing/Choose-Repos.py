# 从75w仓库中挑出超过150star的仓库

import json
repos = []


with open('One-Chosen-repos.txt', 'r') as ipfile:
    for repo in ipfile:
        repos.append(repo[:-1])
whos = '['
for i in range(6):
    with open('Gitrepo-Info/' + str(i) + '.txt', 'r') as ipfile:
        s = ipfile.read()
        whos += s
whos = whos[:-2] + ']'
repoinfo = json.loads(whos)
stars = []  
with open('Repos-morethan-150.txt', 'w') as opfile:
    for repo in repoinfo:
        if 'stargazers_count' in repo.keys() and repo['stargazers_count'] >= 150:
            opfile.write(repo['full_name'] + '\n')
