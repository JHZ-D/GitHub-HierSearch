# -*- coding: utf-8 -*-

# from scripts import tabledef
# from scripts import forms
# from scripts import helpers
from flask import Flask, redirect, url_for, render_template, request, session
from flask_cors import CORS
import json
import sys
import os
import re
import copy

app = Flask(__name__)
CORS(app, supports_credentials=True)
app.secret_key = os.urandom(12)  # Generic key for dev purposes only
with open('common/wholegraphtreerepo.json', 'r') as f:
    wholegraphtree = json.load(f)
with open('common/pageinfo.json', 'r') as f:
    pageinfo = json.load(f)
with open('common/topic_desc.json', 'r') as f:
    topic_desc = json.load(f)
with open('common/Repos-Info.json', 'r') as f:
    repos_info = json.load(f)
with open('common/topicnumdesc.json', 'r') as f:
    topicnumdesc = json.load(f)
with open('common/cateinfoonlygithub.json', 'r') as f:
    cateinfoonlygithub = json.load(f)
with open('common/topicdict.json', 'r') as f:
    topicdict = json.load(f)
with open('common/wholedict.json', 'r') as f:
    wholedict = json.load(f)
with open('common/repoclus.json', 'r') as f:
    repoclus = json.load(f)
with open('common/clurepos.json', 'r') as f:
    clusrepos = json.load(f)
with open('common/ReposforSearch.json', 'r') as f:
    reposforsearch = json.load(f)
with open('common/topicrepo.json', 'r') as f:
    topicrepo = json.load(f)

# Heroku
#from flask_heroku import Heroku
#heroku = Heroku(app)

@app.after_request
def af_request(resp):     
    """
    #请求钩子，在所有的请求发生后执行，加入headers。
    :param resp:
    :return:
    """
    # resp = make_response(resp)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['Access-Control-Allow-Methods'] = 'GET,POST'
    resp.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
    return resp


# ======== Routing =========================================================== #
# @app.route('/', methods=['GET', 'POST'])


# -------- Login ------------------------------------------------------------- #
# def login():
#     if not session.get('logged_in'):
#         form = forms.LoginForm(request.form)
#         if request.method == 'POST':
#             username = request.form['username'].lower()
#             password = request.form['password']
#             if form.validate():
#                 if helpers.credentials_valid(username, password):
#                     session['logged_in'] = True
#                     session['username'] = username
#                     return json.dumps({'status': 'Login successful'})
#                 return json.dumps({'status': 'Invalid user/pass'})
#             return json.dumps({'status': 'Both fields required'})
#         return render_template('login.html', form=form)
#     user = helpers.get_user()
#     return render_template('home.html', user=user)


# @app.route("/logout")
# def logout():
#     session['logged_in'] = False
#     return redirect(url_for('login'))


# -------- Signup ---------------------------------------------------------- #
# @app.route('/signup', methods=['GET', 'POST'])
# def signup():
#     if not session.get('logged_in'):
#         form = forms.LoginForm(request.form)
#         if request.method == 'POST':
#             username = request.form['username'].lower()
#             password = helpers.hash_password(request.form['password'])
#             email = request.form['email']
#             if form.validate():
#                 if not helpers.username_taken(username):
#                     helpers.add_user(username, password, email)
#                     session['logged_in'] = True
#                     session['username'] = username
#                     return json.dumps({'status': 'Signup successful'})
#                 return json.dumps({'status': 'Username taken'})
#             return json.dumps({'status': 'User/Pass required'})
#         return render_template('login.html', form=form)
#     return redirect(url_for('login'))


# -------- Settings ---------------------------------------------------------- #
# @app.route('/settings', methods=['GET', 'POST'])
# def settings():
#     if session.get('logged_in'):
#         if request.method == 'POST':
#             password = request.form['password']
#             if password != "":
#                 password = helpers.hash_password(password)
#             email = request.form['email']
#             helpers.change_user(password=password, email=email)
#             return json.dumps({'status': 'Saved'})
#         user = helpers.get_user()
#         return render_template('settings.html', user=user)
#     return redirect(url_for('login'))

cut = set()
def dfsknowgraph(tree, id, repos, depth = -1):
    newtree = copy.deepcopy(tree)
    cut.add(tree['id'])
    if depth == 0:
        for child in tree['children']:
            if child['id'].startswith('rp'):
                if child['id'] in repos:
                    newtree['children'].remove(child)
            else:
                newtree['children'].remove(child)
        newtree['children'] = newtree['children'][:5]
        return newtree
    
    if depth == 1:
        cnt = 0
        newtree['children'] = []
        newrepos = copy.deepcopy(repos)
        for child in tree['children']:
            if child['id'].startswith('rp') and not child['id'] in repos:
                newtree['children'].append(child)
                cnt += 1
                newrepos.append(child['id'])
                if cnt == 5:
                    break
        for child in tree['children']:
            if not child['id'].startswith('rp'):
                newtree['children'].append(dfsknowgraph(child, child['id'], newrepos, 0))
        return newtree
    
    if depth == 2:
        cnt = 0
        newtree['children'] = []
        newrepos = []
        for child in tree['children']:
            if child['id'].startswith('rp'):
                newtree['children'].append(child)
                cnt += 1
                newrepos.append(child['id'])
                if cnt == 5:
                    break
        for child in tree['children']:
            if not child['id'].startswith('rp'):
                newtree['children'].append(dfsknowgraph(child, child['id'], newrepos, 0))
        return newtree

    if tree['id'] == id:
        cnt = 0
        newtree['children'] = []
        newrepos = []
        for child in tree['children']:
            if child['id'].startswith('rp'):
                newtree['children'].append(child)
                cnt += 1
                newrepos.append(child['id'])
                if cnt == 5:
                    break
        for child in tree['children']:
            if not child['id'].startswith('rp'):
                newtree['children'].append(dfsknowgraph(child, child['id'], newrepos, 1))
        return newtree
    if not 'children' in tree:
        return None
    for child in tree['children']:
        if child['id'] in cut:
            continue
        if (child['id'].startswith('tp') or child['id'].startswith('ts')) and (id.startswith('pg') or id[0].isdigit()):
            continue
        if child['id'].startswith('pg') and id[0].isdigit():
            continue
        if child['id'] == id:
            newtree['children'] = [dfsknowgraph(child, child['id'], [], 2)]
            return newtree
        else:
            dfsre = dfsknowgraph(child, id, [], -1)
            if dfsre != None:
                print(tree['id'])
                return dfsre
    return None

def getGraph(id, parentid):
    curitem = wholedict[id]
    curnode = {'id':id, 'label':curitem['label'], 'group':curitem['group'], 'children':[], 'cur': 1}
    reposet = set()
    if curitem['children']:
        if not curitem['children'][0].startswith('rp'):
            for child in curitem['children']:
                if child.startswith('rp'):
                    continue
                childitem = wholedict[child]
                childnode = {'id':child, 'label':childitem['label'], 'group':childitem['group'], 'children':[], 'parent':id}
                if not childitem['children']:
                    curnode['children'].append(childnode)
                    continue
                if childitem['children'][0].startswith('rp'):
                    for cchild in childitem['children']:
                        if not cchild in reposet:
                            reposet.add(cchild)
                            childnode['children'].append({'id':cchild, 'label':repos_info[cchild[2:]]['full_name'], 'group':4, 'parent':child})
                else:
                    for cchild in childitem['children'][:5]:
                        if cchild.startswith('rp'):
                            continue
                        cchilditem = wholedict[cchild]
                        cchildnode = {'id':cchild, 'label':cchilditem['label'], 'group':cchilditem['group'], 'children':[], 'parent':child}
                        if not cchilditem['children']:
                            childnode['children'].append(cchildnode)
                            continue
                        if cchilditem['children'][0].startswith('rp'):
                            cchildnode['children'] += [{'id':ccchild, 'label':repos_info[ccchild[2:]]['full_name'], 'group':4, 'parent':cchild} for ccchild in cchilditem['children'] if not ccchild in reposet]
                            reposet |= set([c['id'] for c in cchildnode['children']])
                        childnode['children'].append(cchildnode)
                curnode['children'].append(childnode)
        else:
            for child in curitem['children']:
                if not child in reposet:
                    reposet.add(child)
                    curnode['children'].append({'id':child, 'label':repos_info[child[2:]]['full_name'], 'group':4, 'parent':id})
    if id == '0':
        curnode['parent'] = None
        return curnode
    parents = curitem['parent']
    if not parentid:
        parentid = parents[0]
    parentnode = wholedict[parentid]
    graph = {'id':parentid, 'label':parentnode['label'], 'group':parentnode['group'], 'parent':None}
    curnode['parent'] = parentid
    graph['children'] = [curnode]
    return graph

def getRepoGraph(repo):
    clus = repoclus[repo[2:]]
    graph = {'id':repo, 'label':repos_info[repo[2:]]['full_name'], 'group':4, 'parent':None, 'children':[]}
    for clu in clus:
        graph['children'].append({'id':'tp'+str(clu), 'label':topicdict['tp'+str(clu)], 'group':2, 'parent':None})
    return graph

@app.route('/getKnowp', methods=['GET'])
def getKnowp():
    # print(request.args)
    nodeid = request.args.get('text')
    parentid = None
    if 'parent' in request.args:
        parentid = request.args.get('parent')
    desc = ''
    url = ''
    wikibaseurl = 'https://en.wikipedia.org/wiki/'
    topicbaseurl = 'https://github.com/topics/'
    repobaseurl = 'https://github.com/'
    print('base!')
    graph = {}
    cut.clear()
    if nodeid.startswith('rp'):
        desc = repos_info[nodeid[2:]]['description']
        url = repobaseurl + repos_info[nodeid[2:]]['full_name']
        graph = getRepoGraph(nodeid)
    else:
        # graph = dfsknowgraph(wholegraphtree, nodeid, [])
        graph = getGraph(nodeid, parentid)
        if nodeid.startswith('pg'):
            desc = pageinfo[nodeid[2:]]['desc']
            url = wikibaseurl + pageinfo[nodeid[2:]]['name']
        elif nodeid.startswith('tp'):
            if nodeid in topicnumdesc:
                desc = topicnumdesc[nodeid]
            url = topicbaseurl + topicdict[nodeid]
        elif nodeid.startswith('ts'):
            if nodeid[2:] in topic_desc:
                desc = topic_desc[nodeid[2:]]
            url = topicbaseurl + nodeid[2:]
        else:
            if 'mainpage' in cateinfoonlygithub[nodeid]:
                try:
                    desc = pageinfo[str(cateinfoonlygithub[nodeid]['mainpage'])]['desc']
                except:
                    desc = ''
            url = wikibaseurl + 'Category:' + cateinfoonlygithub[nodeid]['name']

    return json.dumps({'graph': graph, 'description': desc, 'url': url})

def dfsRepos(tree):
    if tree.startswith('tp') and tree[2:] in clusrepos:
        return set(clusrepos[tree[2:]])
    if tree.startswith('ts'):
        if tree[2:] in topicrepo:
            return set(topicrepo[tree[2:]])
        return set()
    repos = set()
    for child in wholedict[tree]['children']:
        if not child.startswith('rp'):
            repos |= dfsRepos(child)
    return repos

def MatchingRepos(keywords, repos):  # 输入为列表
    # keywords is a list of keywords
    # repos is a list of repos
    # return a list of repos that match the keywords
    # if no repos match the keywords, return an empty list
    # if no keywords are given, return the original list of repos
    if len(keywords) == 0:
        return repos
    keywords = re.split("[^a-zA-Z]", keywords)
    keywords = set([keyword.lower() for keyword in keywords if keyword != ''])
    matchingRepos = []
    m = 0
    for info in repos:
        if keywords.issubset(set(info['content'])):
            matchingRepos.append(info)
        # for keyword in keywords:
        #     if not (keyword in reponame or keyword in description):
        #         m = 1
        #         break
        # if m == 0:
        #     matchingRepos.append(info)
    # sort matchingRepos by number of stars
    matchingRepos.sort(key=lambda x: x['stargazers_count'], reverse=True)
    return matchingRepos

@app.route('/repo', methods=['GET'])
def getRepo():
    # print(request.args)
    searchText = request.args.get('text')
    cateid = request.args.get('cate')
    if cateid != '0':
        repos = list(dfsRepos(cateid))
    if searchText == '':
        repos.sort(key=lambda x:repos_info[x]['stargazers_count'], reverse=True)
        showRepos = [{'id':repo, 'reponame':repos_info[repo]['full_name'], 'description':repos_info[repo]['description']} for repo in repos]
        return json.dumps({'repos': showRepos[:50]})
    if cateid == 0:
        searchRepos = [dict(reposforsearch[k], id=k) for k in reposforsearch]
    else:
        searchRepos = [dict(reposforsearch[k], id=k) for k in repos]
    showRepos = MatchingRepos(searchText, searchRepos)
    showRepos = [{'id':repo['id'], 'reponame':repo['full_name'], 'description':repo['description']} for repo in showRepos]
    return json.dumps({'repos': showRepos[:100]})


# ======== Main ============================================================== #
if __name__ == "__main__":
    app.run(debug=True, use_reloader=True, host="0.0.0.0")