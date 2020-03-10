"""
Python 3.8.0
列出所有链入到收录的链接的却没有被收录的页面
大约耗时15分钟

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

filepath="PAGELIST.xlsx"

url="https://zh.moegirl.org/api.php"

params={'action':'query','format':'json','prop':'linkshere','curtimestamp':1,'indexpageids':1,'lhlimit':500,'lhshow':'!redirect','lhprop':'pageid|title','lhnamespace':'*'}

Workbook:type=openpyxl.workbook.workbook.Workbook
Worksheet:type=openpyxl.worksheet.worksheet.Worksheet
Cell:type=openpyxl.cell.cell.Cell

b:Workbook=openpyxl.load_workbook(filepath)
sMain:Worksheet=b.worksheets[0]
sTemp:Worksheet=b.worksheets[1]
sCate:Worksheet=b.worksheets[2]
sheets:Worksheet=b.worksheets

n_all=0
link_new=0

def isResponceContinue(json:dict)->bool:
	if 'batchcomplete' in json:
		return json['batchcomplete']
	elif 'continue' in json:
		return json['continue']['lhcontinue']
	else:
		print("[!!] Responce is not complete.")
		return True

pagetitlelist:list=[]
for sheet in sheets:
	pagetitlelist+=[c.value for c in list(sheet.columns)[3]]
	for c in list(sheet.columns)[5]:
		if c.value:
			pagetitlelist+=list(eval(c.value))

pagetitlelinkedfromlist:list=pagetitlelist.copy()

input("Enter to start.")
start_time=time.time()
print("started at",time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(start_time)))

for pagetitle in pagetitlelist:
	lhcontinue=''
	while True:
		while True:
			try:
				if lhcontinue:
					a=requests.get(url,params={**params,**{'titles':pagetitle,'lhcontinue':lhcontinue}},timeout=(10,30))
				else:
					a=requests.get(url,params={**params,**{'titles':pagetitle}},timeout=(10,30))
			except:
				print(".",end="")
				continue
			else:
				break
		json:dict=a.json()
		pageid=int(json['query']['pageids'][0])
		title=json['query']['pages'][str(pageid)]['title']
		if 'linkshere' in json['query']['pages'][str(pageid)]:
			for linkJson in json['query']['pages'][str(pageid)]['linkshere']:
				linktitle=linkJson['title'] if 'title' in linkJson else ""
				linkid=linkJson['pageid'] if 'pageid' in linkJson else ""
				if linktitle not in pagetitlelinkedfromlist:
					pagetitlelinkedfromlist.append(linktitle)
					print("[链][外]","\t[Linked]",pageid,"\t",title,"\t[From]",linkid,"\t",linktitle,sep="")
					link_new+=1
				else:
					#print("[链][内]","\t[LinkedID]",pageid,"\t[Linked]",title,"\t[From]",linktitle,sep="")
					pass
		lhcontinue=isResponceContinue(json)
		if not lhcontinue:
			break


print()
end_time=time.time()
print("ended   at",time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(end_time)))
print(second2days.main(end_time-start_time),"spent.")

print(link_new,"links found.")

input("Done.")