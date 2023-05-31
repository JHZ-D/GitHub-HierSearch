# 每个仓库随机选取stargazer
import random
usercode = {}
suer = set()
with open('Stargazers.txt', 'r') as ipfile:
    i = 0
    for line in ipfile:
        usercode[line] = i
        i += 1
        suer.add(line)
s = set()
p = []
ausers = []
j = i
for i in range(2274, 2281):
    with open('Github-First-Stargazers/' + str(i), 'r') as ipfile:
        for user in ipfile:
            if user not in suer:
                suer.add(user)
                ausers.append(user)
                usercode[user] = j
                j += 1
with open('Stargazers.txt', 'a') as opfile:
    for user in ausers:
        opfile.write(user)
for i in range(2274, 2281):
    with open('Github-First-Stargazers/' + str(i), 'r') as ipfile:
        # users = ipfile.readlines()
        # l = len(users)
        # m = []
        # n = 0
        # fl = 0
        # while True:
        #     if l < 2:
        #         break

        #     x1 = random.randint(0, l - 1)
        #     ex = users[x1]
        #     if usercode[ex] not in s:
        #         s.add(usercode[ex])
        #         m.append(ex)
        #         n += 1
        #         if n == 2:
        #             break
        #     else:
        #         fl += 1
        #     if fl >= l:
        #         break
        # if n < 2:
        #     for j in range(l):
        #         ex = users[j]
        #         if usercode[ex] not in s:
        #             s.add(usercode[ex])
        #             m.append(ex)
        #             n += 1
        #             if n == 2:
        #                 break
        # if n < 2:
        #     print(i)
        # p.append(m)
        users = ipfile.readlines()
        l = len(users)
        m = []
        n = 0
        fl = 0
        while True:
            if l < 1:
                break

            x1 = random.randint(0, l - 1)
            ex = users[x1]
            if usercode[ex] not in s:
                s.add(usercode[ex])
                m.append(ex)
                break
            else:
                fl += 1
            if fl >= l:
                break
        if n < 1:
            for j in range(l):
                ex = users[j]
                if usercode[ex] not in s:
                    s.add(usercode[ex])
                    m.append(ex)
                    break
        if n < 1:
            print(i)
        p.append(m)
    with open('Chosen-Stargazers/' + str(i), 'w') as opfile:
        for u in m:
            opfile.write(u)