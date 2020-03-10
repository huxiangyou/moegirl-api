"""
Python 3.8.0
找到所有对指定页面在指定时间内做出过贡献的用户及其贡献数

Jan 7, 2020
Jan 15, 2020
Jan 26, 2020
Mar 5, 2020
Hu Xiangyou
"""
print(__file__.rsplit("\\",1)[1])
print(__doc__)
import requests
import time
import os
import second2days

filepath="PAGELIST.txt"

url="https://zh.moegirl.org/api.php"

rvduration=None#30*86400
rvendtime=time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime(time.time()-rvduration)) if rvduration else '2013-07-08T00:00:00Z'

params={'action':'query','format':'json','prop':'revisions','rvprop':'user','rvlimit':'max','curtimestamp':1,'indexpageids':1,'rvend':rvendtime}

print("Find Contibutions after",rvendtime)

f=open(filepath,'r',encoding='UTF-8')
pagelistfile=f.read().splitlines()
f.close()
pageidlist=[]
for pageline in pagelistfile:
	if pageline.split("\t")[0] in ('[M___]','[T___]','[C___]'):
		pageidlist.append(int(pageline.split("\t")[1]))

n_all=0
users_revisions={}
users_pages={}

def devide(l:list,n:int)->list:
	for i in range(0,len(l),n):
		yield l[i:i+n]

def isResponceOK(json:dict)->bool:
	if 'batchcomplete' in json:
		return True
	else:
		print("Responce is not complete.")
		return False

def isResponceContinue(json:dict)->bool:
	if 'continue' in json:
		return json['continue']['rvcontinue']
	else:
		return False

input("Enter to start.")
start_time=time.time()
print("started at",time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(start_time)))

for pageid in pageidlist:
	rvcontinue=''
	revnum_this=0
	while True:
		while True:
			try:
				if rvcontinue:
					a=requests.get(url,params={**params,**{'pageids':pageid,'rvcontinue':rvcontinue}},timeout=(10,30))
				else:
					a=requests.get(url,params={**params,**{'pageids':pageid}},timeout=(10,30))
				json:dict=a.json()
			except:
				print(".",end="")
				continue
			else:
				break
		title=json['query']['pages'][str(pageid)]['title']
		revisions=json['query']['pages'][str(pageid)]['revisions'] if 'revisions' in json['query']['pages'][str(pageid)] else []
		revnum_this+=len(revisions)
		for r in revisions:
			if r["user"] in users_revisions:
				users_revisions[r["user"]]+=1
				if pageid not in users_pages[r["user"]]:
					users_pages[r["user"]].append(pageid)
			else:
				users_revisions[r["user"]]=1
				users_pages[r["user"]]=[pageid]
		n_all+=1
		rvcontinue=isResponceContinue(json)
		if not rvcontinue:
			print("[编]","\t[PID]",pageid,"\t[Revs]",revnum_this,"\t[Title]",title)
			break

print()
end_time=time.time()
print("ended   at",time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(end_time)))
print(second2days.main(end_time-start_time),"spent.")

users_morethan5={}
for u in sorted(users_revisions.items(),key=lambda x:x[1],reverse=True):
	if u[1]>=0:
		users_morethan5[u[0]]=(users_revisions[u[0]],len(users_pages[u[0]]))

print(n_all,"pages checked.")
print(len(users_revisions),"contributors found.",sum(users_revisions.values()),"revisions found.")
print("Revs","Pages","Username",sep="\t")
for u in users_morethan5:
	print(users_morethan5[u][0],users_morethan5[u][1],u,sep="\t")

input("Done.")
