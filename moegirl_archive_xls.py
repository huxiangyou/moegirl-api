"""
Python 3.8.0
对列出的页面进行存档
初次运行大约耗时5分钟 在已有存档上覆盖大约耗时1分钟

Jan 7, 2020
Jan 15, 2020
Jan 19, 2020
Hu Xiangyou
"""
print(__file__.rsplit("\\",1)[1])
print(__doc__)
import requests
from urllib import parse
import time
import openpyxl
import os
import second2days
import socket

filepath="PAGELIST.xlsx"
fold="archive/"
fileData="!.txt"

url="https://zh.moegirl.org/api.php"

params1={'action':'query','format':'json','prop':'info|redirects','curtimestamp':1,'indexpageids':1,'rdlimit':500,'inprop':'talkid','pageids':''}
params={'action':'query','format':'json','prop':'revisions','curtimestamp':1,'indexpageids':1,'rvprop':'content|ids','pageids':''}

Workbook:type=openpyxl.workbook.workbook.Workbook
Worksheet:type=openpyxl.worksheet.worksheet.Worksheet
Cell:type=openpyxl.cell.cell.Cell

b:Workbook=openpyxl.load_workbook(filepath)
sMain:Worksheet=b.worksheets[0]
sTemp:Worksheet=b.worksheets[1]
sCate:Worksheet=b.worksheets[2]
sheets:Worksheet=b.worksheets

n_all=0
n_new=0
n_overridden=0

f=open(fold+fileData,'r',encoding='UTF-8')
reviddict=eval(f.read())
f.close()

pageidlist:list=[]
for sheet in sheets:
	pageidlist+=[c.value for c in list(sheet.columns)[1]]

def devide(l:list,n:int)->list:
	for i in range(0,len(l),n):
		yield l[i:i+n]

def isResponceOK(json:dict)->bool:
	if 'batchcomplete' in json:
		return True
	else:
		print("Responce is not complete.")
		return False

def pageEdited(json:dict,pageid:int,oldrevid:int)->bool:
	lastrevid=json['query']['pages'][str(pageid)]['lastrevid']
	if oldrevid!=lastrevid:
		return True
	else:
		return False

def saveData():
	f=open(fold+fileData,'w',encoding='UTF-8')
	f.write(str(reviddict))
	f.close()

def saveContent(pageid:str):
	global n_new,n_overridden
	while True:
		try:
			a=requests.get(url,params={**params,**{'pageids':pageid}},timeout=(10,30))
		except:
			print(".",end="")
			continue
		else:
			break
	json:dict=a.json()
	if not isResponceOK(json):
		raise
	if 'revisions' in json['query']['pages'][str(pageid)]:
		content=json['query']['pages'][str(pageid)]['revisions'][0]['*']
		title=json['query']['pages'][str(pageid)]['title']
		revid=json['query']['pages'][str(pageid)]['revisions'][0]['revid']
		title_in_file=title.replace("/","／").replace(":","：").replace("\\","＼").replace("*","＊").replace("?","？").replace("\"","＂").replace("<","＜").replace(">","＞").replace("|","｜")
		if title!=reviddict[pageid][1]:
			print("[提示][移]","\t[Moved]",reviddict[pageid][1],"->",title,"\t[Note] Please delete the old archive file.")
		if os.path.isfile(fold+title_in_file+".txt"):
			if pageid in reviddict and reviddict[pageid][0]==revid and reviddict[pageid][1]==title:
				print("[—]\t","\t[PID]",pageid,"\t[RID]",revid,"\t[Title]",title)
				pass
			else:
				f=open(fold+title_in_file+".txt",'w',encoding='UTF-8')
				f.write(content)
				f.close()
				reviddict[pageid]=[revid,title]
				print("[存][覆盖]","\t[PID]",pageid,"\t[RID]",revid,"\t[Title]",title)
				n_overridden+=1
		else:
			f=open(fold+title_in_file+".txt",'w',encoding='UTF-8')
			f.write(content)
			f.close()
			reviddict[pageid]=[revid,title]
			print("[存][新]","\t[PID]",pageid,"\t[RID]",revid,"\t[Title]",title)
			n_new+=1

input("Enter to start.")
start_time=time.time()
print("started at",time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(start_time)))

for pageidlist_d in devide(pageidlist,50):
	l_param:str="|".join(str(i) for i in pageidlist_d)
	while True:
		try:
			a=requests.get(url,params={**params1,**{'pageids':l_param}},timeout=(10,30))
		except:
			print(".",end="")
			continue
		else:
			break
	json:dict=a.json()
	for pageid in pageidlist_d:
		if pageid in reviddict:
			if pageEdited(json,pageid,reviddict[pageid]):
				saveContent(pageid)
		else:
			saveContent(pageid)
		n_all+=1
reviddict['info']="萌娘百科LoveLive!系列页面存档"
reviddict['time']=json['curtimestamp']
reviddict['by']=socket.getfqdn(socket.gethostname())

saveData()

print()
end_time=time.time()
print("ended   at",time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(end_time)))
print(second2days.main(end_time-start_time),"spent.")

print(n_all,"pages checked.")
print(n_new,"were newly saved.",n_overridden,"were overridden.")

input("Done.")