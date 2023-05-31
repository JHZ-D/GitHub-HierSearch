from selenium import webdriver
from queue import Queue
from bs4 import BeautifulSoup
import time
import os
import random
preurl = 'https://en.wikipedia.org/wiki/'
driver = webdriver.Chrome()

K = {}
KV = {}
LV = {}
with open('Page-encode.txt', 'r', encoding='utf-8') as encodes:
    for page in encodes:
        if page == '':
            continue
        PNum = int(page[: page.find(' ')])
        PName = page[page.find(' ') + 1:-1]
        K[PNum] = PName
        KV[PName] = PNum
with open('Pageleaf-encode.txt', 'r', encoding='utf-8') as encodes:
    for page in encodes:
        if page == '':
            continue
        PNum = int(page[: page.find(' ')])
        PName = page[page.find(' ') + 1:-1]
        LV[PName] = PNum
Edgeset = set()
with open('Page-edges.txt', 'r') as edges:
    for edge in edges:
        Edgeset.add(edge)
Edgeleafset = set()
with open('Pageleaf-edges.txt', 'r') as edges:
    for edge in edges:
        Edgeleafset.add(edge)

cq = Queue()
MN = len(K)
MP = len(LV)
with open('Page-crawling.txt', 'r') as crfile:
    for page in crfile:
        if page == '':
            continue
        cq.put(int(page))

while not cq.empty():
    dealing = cq.get()
    crwurl = preurl + K[dealing]
    driver.get(crwurl)
    html_page = driver.page_source
    with open('Wiki-Categories/' + str(dealing), 'w', encoding='utf-8') as cf:
        cf.write(html_page)
    soup = BeautifulSoup(html_page,'lxml')
    links = soup.find_all('div', class_='CategoryTreeItem')
    for link in links:
        np = link.a['title']
        if np in KV.keys():
            s = str(dealing) + ' ' + str(KV[np]) + '\n'
            if s not in Edgeset:
                with open('Page-edges.txt', 'a') as edgefile:
                    edgefile.write(s)
            continue
        KV[np] = MN
        K[MN] = np
        cq.put(MN)
        with open('Page-encode.txt', 'a', encoding='utf-8') as encodes:
            encodes.write(str(MN) + ' ' + np + '\n')
        with open('Page-crawling.txt', 'a') as crfile:
            crfile.write(str(MN) + '\n')
        with open('Page-edges.txt', 'a') as edgefile:
            edgefile.write(str(dealing) + ' ' + str(MN) + '\n')
        MN += 1
    soup = BeautifulSoup(html_page,'lxml')
    pagestop = soup.find('div', id='mw-pages')
    if pagestop != None:
        links = pagestop.find_all('li')
        for link in links:
            np = link.a['title']
            if np in LV.keys():
                s = str(dealing) + ' ' + str(LV[np]) + '\n'
                if s not in Edgeleafset:
                    with open('Pageleaf-edges.txt', 'a') as edgefile:
                        edgefile.write(s)
                continue
            LV[np] = MP
            with open('Pageleaf-encode.txt', 'a', encoding='utf-8') as encodes:
                encodes.write(str(MP) + ' ' + np + '\n')
            with open('Pageleaf-edges.txt', 'a') as edgefile:
                edgefile.write(str(dealing) + ' ' + str(MP) + '\n')
            MP += 1
    
    with open('Page-crawling.txt', 'r') as crfile:
        with open('Page-crawling1.txt', 'w') as nf:
            i = 0
            for line in crfile:
                if i > 0:
                    nf.write(line)
                i += 1
    while True:
        try:
            os.remove('Page-crawling.txt')
        except PermissionError:
            time.sleep(1)
        else:
            break
    os.rename('Page-crawling1.txt', 'Page-crawling.txt')
    tm = random.uniform(1, 3)
    time.sleep(tm)
    # pagesobj = soup.find('span', id_='Pages_in_category')
    # print(pagesobj)



# with open('test.txt', 'w', encoding='utf-8') as wrfile:
#     wrfile.write(html_page)