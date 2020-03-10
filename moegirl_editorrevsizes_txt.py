"""
Python 3.8.0
找到所有对指定页面在指定时间内做出过贡献的用户及其贡献数及贡献字节数

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
rvstarttime=time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime(time.time()-rvduration)) if rvduration else '2013-07-01T00:00:00Z'

params={'action':'query','format':'json','prop':'revisions','rvprop':'user|size','rvlimit':'max','curtimestamp':1,'indexpageids':1,'rvstart':rvstarttime,'rvdir':'newer'}

print("Find Contibutions after",rvstarttime)

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
users_sizes={}

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
	size_last=0
	revnum_page=0
	editors_page=[]
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
		revnum_page+=len(revisions)
		for r in revisions:
			user_r=r["user"]
			size_added=r["size"]-size_last
			if user_r in users_revisions:
				users_revisions[user_r]+=1
				if user_r not in editors_page:
					editors_page.append(user_r)
					users_pages[user_r]+=1
				users_sizes[user_r]+=size_added
			else:
				users_revisions[user_r]=1
				users_pages[user_r]=1
				users_sizes[user_r]=size_added
				editors_page.append(user_r)
			size_last=r["size"]
		n_all+=1
		rvcontinue=isResponceContinue(json)
		if rvcontinue:
			print("[编]","\t[PID]",pageid,"\t[Revs]",revnum_page,"\t[Ctrbtrs]",len(editors_page),"\t[Size]",size_last,"\t[Title]",title,end="\t\r")
		else:
			print("[编]","\t[PID]",pageid,"\t[Revs]",revnum_page,"\t[Ctrbtrs]",len(editors_page),"\t[Size]",size_last,"\t[Title]",title)
			break

print()
end_time=time.time()
print("ended   at",time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(end_time)))
print(second2days.main(end_time-start_time),"spent.")

users_morethan5={}
for u in sorted(users_revisions.items(),key=lambda x:x[1],reverse=True):
	if u[1]>=0:
		users_morethan5[u[0]]=(users_revisions[u[0]],users_pages[u[0]],users_sizes[u[0]])

print(n_all,"pages checked.")
print(len(users_revisions),"contributors found.",sum(users_revisions.values()),"revisions found.")
print("[Revs]","[Pages]","[Size]","[Username]",sep="\t")
for u in users_morethan5:
	print(users_morethan5[u][0],users_morethan5[u][1],users_morethan5[u][2],u,sep="\t")

input("Done.")
