"""
Python 3.8.0
登录并编辑指定页面

Mar 8, 2020
Hu Xiangyou

注意：运行此程序前请先测试通过
"""

import requests

url="https://zh.moegirl.org/api.php"
USERNAME=YOUR_USERNAME
PASSWORD=YOUR_PASSWORD

if __name__=='__main__':
	session=requests.Session()

def login(username=USERNAME,password=PASSWORD):
	"""登录"""
	ja=session.get(url,params={'action':'query','format':'json','meta':'tokens','type':'login'},timeout=(10,30)).json()
	logintoken=ja['query']['tokens']['logintoken']
	jb=session.post(url,data={'action':'clientlogin','format':'json','logintoken':logintoken,'username':username,'password':password,'loginreturnurl':'https://zh.moegirl.org/index.php'},timeout=(10,30)).json()
	return jb['clientlogin']['status']=='PASS'

def edit(pageid=185503,text="<noinclude><!-- 请勿删除此行 -->{{沙盒顶部}}<!-- 请勿删除此行 --></noinclude>\n测试通过[[Special:ApiSandbox|API]]编辑—~~~~",summary="// 使用[[Special:ApiSandbox|API]]编辑",minor=1):
	"""将页面内容更改为指定内容"""
	ja=session.get(url,params={'action':'query','format':'json','meta':'tokens','type':'csrf'},timeout=(10,30)).json()
	csrftoken=ja['query']['tokens']['csrftoken']
	jb=session.post(url,data={'action':'edit','format':'json','token':csrftoken,'pageid':pageid,'text':text,'summary':summary,'minor':minor,'nocreate':1},timeout=(10,30)).json()
	return jb['edit']['result']=='Success'

def append(pageid=185503,appendtext="\n测试通过[[Special:ApiSandbox|API]]编辑—~~~~",summary="// 使用[[Special:ApiSandbox|API]]编辑",minor=1):
	"""在页面后追加指定内容"""
	ja=session.get(url,params={'action':'query','format':'json','meta':'tokens','type':'csrf'},timeout=(10,30)).json()
	csrftoken=ja['query']['tokens']['csrftoken']
	jb=session.post(url,data={'action':'edit','format':'json','token':csrftoken,'pageid':pageid,'appendtext':appendtext,'summary':summary,'minor':minor,'nocreate':1},timeout=(10,30)).json()
	return jb['edit']['result']=='Success'

def replace(pageid=185503,old="1",new="2",summary="替换 {old} → {new} // 使用[[Special:ApiSandbox|API]]编辑",minor=1):
	"""替换页面中的内容"""
	ja=requests.get(url,params={'action':'query','format':'json','prop':'revisions','curtimestamp':1,'indexpageids':1,'rvprop':'content|ids|timestamp','pageids':pageid},timeout=(10,30)).json()
	jp=ja['query']['pages'][str(pageid)]['revisions'][0]
	basetimestamp=jp['timestamp']
	starttimestamp=ja['curtimestamp']
	content=jp['*']
	if old and old in content:
		content_new=content.replace(old,new)
		jb=session.get(url,params={'action':'query','format':'json','meta':'tokens','type':'csrf'},timeout=(10,30)).json()
		csrftoken=jb['query']['tokens']['csrftoken']
		jc=session.post(url,data={'action':'edit','format':'json','token':csrftoken,'pageid':pageid,'text':content_new,'summary':summary.format(old=old,new=new),'minor':minor,'nocreate':1,'basetimestamp':basetimestamp,'starttimestamp':starttimestamp},timeout=(10,30)).json()
		return jc['edit']['result']=='Success'
	else:
		return None
