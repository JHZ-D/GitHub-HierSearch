from selenium import webdriver
from queue import Queue
from bs4 import BeautifulSoup
import time
import os
import random
preurl = 'https://en.wikipedia.org/wiki/'
driver = webdriver.Chrome()

with open('Pageleaf-crawled.txt', 'r') as crawled:
    stpage = int(crawled.read())
L = {}
with open('Pageleaf-encode.txt', 'r', encoding='utf-8') as encodes:
    for page in encodes:
        if page == '':
            continue
        PNum = int(page[: page.find(' ')])
        PName = page[page.find(' ') + 1:-1]
        L[PNum] = PName
leafps = []
with open('filter-files/remainpages.txt', 'r') as ipfile:
    for line in ipfile:
        leafps.append(int(line))
# for fps in leafps:
#     if fps >= stpage:
#         break
for p in leafps:
    if p < stpage:
        continue
    crwurl = preurl + L[p]
    while True:
        try:
            driver.get(crwurl)
        except:
            time.sleep(60)
        else:
            break
    html_page = driver.page_source
    with open('Wiki-Pageleaves/' + str(p), 'w', encoding='utf-8') as cf:
        cf.write(html_page)
    soup = BeautifulSoup(html_page,'lxml')
    ifb = soup.find('table', class_='infobox vevent')
    ghlink = ''
    if ifb != None:
        lines = ifb.find_all('th')
        for line in lines:
            if line.get_text() == 'Repository':
                ns = line.next_sibling
                nsa = ns.find('a')
                # print(nsa)
                if nsa and 'href' in nsa.attrs.keys():
                    ghlink = nsa['href']
                break
    nodes = soup.find_all('a')
    links = []
    for node in nodes:
        link = node.get('href')
        if link and link.find('github.com') != -1:
            links.append(link)
    with open('Github-Links/' + str(p), 'w', encoding='utf-8') as cf:
        cf.write(ghlink + '\n\n')
        for link in links:
            cf.write(link + '\n')
    with open('Pageleaf-crawled.txt', 'w') as wf:
        wf.write(str(p + 1))
    tm = random.uniform(1, 3)
    time.sleep(tm)