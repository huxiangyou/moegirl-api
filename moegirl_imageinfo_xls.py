"""
Python 3.8.0
列出图片的信息
大约耗时10分钟

Jan 19, 2020
Hu Xiangyou
"""
print(__file__.rsplit("\\",1)[1])
print(__doc__)
import requests
from urllib import parse
import time
import openpyxl
import second2days

filepath="imagelist.xlsx"

url="https://common.moegirl.org/api.php"

params={'action':'query','format':'json','prop':'imageinfo','curtimestamp':1,'indexpageids':1,'iiprop':'timestamp|size|mime','iilimit':500}

Workbook:type=openpyxl.workbook.workbook.Workbook
Worksheet:type=openpyxl.worksheet.worksheet.Worksheet
Cell:type=openpyxl.cell.cell.Cell

b:Workbook=openpyxl.load_workbook(filepath)
sMain:Worksheet=b.worksheets[0]
sheets:Worksheet=b.worksheets

n_all={}
n_delete=0
size_all={}

def devide(l:list,n:int)->list:
	for i in range(0,len(l),n):
		yield l[i:i+n]

def isResponceOK(json:dict)->bool:
	if 'batchcomplete' in json:
		return True
	else:
		print("Responce is not complete.")
		return False

pageidlist:list=[]
pagetitlelist:list=[]
for sheet in sheets:
	clist=list(sheet.columns)[1]
	ctlist=list(sheet.columns)[2]
	for ci in range(len(clist)):
		if clist[ci].value:
			pageidlist.append(clist[ci].value)
		else:
			pagetitlelist.append(ctlist[ci].value)

input("Enter to start.")
start_time=time.time()
print("started at",time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(start_time)))

for pageidlist_d in devide(pageidlist,50):
	l_param:str="|".join(str(i) for i in pageidlist_d)
	while True:
		try:
			a=requests.get(url,params={**params,**{'pageids':l_param}},timeout=(10,30))
		except:
			print(".",end="")
			continue
		else:
			break
	json:dict=a.json()
	if not isResponceOK(json):
		raise
	for pageid in json['query']['pageids']:
		pageJson=json['query']['pages'][str(pageid)]
		title=pageJson['title'] if 'title' in pageJson else ""
		if 'imageinfo' in json['query']['pages'][str(pageid)]:
			mime=pageJson['imageinfo'][0]['mime'] if 'mime' in pageJson['imageinfo'][0] else ""
			size=pageJson['imageinfo'][0]['size'] if 'size' in pageJson['imageinfo'][0] else 0
			print("[文件]","\t[FID]",pageid,"\t[Size]",str(size)+"\t[Title]",title)
			if mime in n_all:
				n_all[mime]+=1
				size_all[mime]+=size
			else:
				n_all[mime]=1
				size_all[mime]=size
		else:
			print("[Ｘ]","\t[FID]",pageid,"\t\t[Title]",title)
			n_delete+=1

for pagetitlelist_d in devide(pagetitlelist,10):
	l_param:str="|".join(str(i) for i in pagetitlelist_d)
	while True:
		try:
			a=requests.get(url,params={**params,**{'titles':l_param}},timeout=(10,30))
		except:
			print(".",end="")
			continue
		else:
			break
	json:dict=a.json()
	if not isResponceOK(json):
		raise
	for pageid in json['query']['pageids']:
		pageJson=json['query']['pages'][str(pageid)]
		title=pageJson['title'] if 'title' in pageJson else ""
		if 'imageinfo' in json['query']['pages'][str(pageid)]:
			mime=pageJson['imageinfo'][0]['mime'] if 'mime' in pageJson['imageinfo'][0] else ""
			size=pageJson['imageinfo'][0]['size'] if 'size' in pageJson['imageinfo'][0] else 0
			print("[文件]","\t[FID]",pageid,"\t[Size]",str(size)+"\t[Title]",title)
			if mime in n_all:
				n_all[mime]+=1
				size_all[mime]+=size
			else:
				n_all[mime]=1
				size_all[mime]=size
		else:
			print("[Ｘ]","\t[FID]",pageid,"\t\t[Title]",title)
			n_delete+=1


print()
end_time=time.time()
print("ended   at",time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(end_time)))
print(second2days.main(end_time-start_time),"spent.")

print(sum(n_all.values()),"files checked.")
print(n_delete,"files not found.")
print(sum(size_all.values()),"Bytes in total.")
for mime in n_all:
	print("[MIME]",mime,"\t[Pages]",n_all[mime],"\t[Size]",size_all[mime])

input("Done.")