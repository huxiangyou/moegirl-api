"""
Python 3.8.0
检查是否属于指定分类却没有被收录的页面
大约耗时2分钟

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
import second2days

filepath="PAGELIST.xlsx"

url="https://zh.moegirl.org/api.php"

params={'action':'query','format':'json','list':'categorymembers','cmlimit':500,'cmnamespace':'0|10|14'}

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

def isResponceOK(json:dict)->bool:
	if 'batchcomplete' in json:
		return True
	else:
		print("Responce is not complete.")
		return False

pageidlist:list=[]
for sheet in sheets:
	pageidlist+=[int(c.value) for c in list(sheet.columns)[1]]

categorytitlelist=[c.value for c in list(sheets[2].columns)[3]]

input("Enter to start.")
start_time=time.time()
print("started at",time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(start_time)))
for categorytitle in categorytitlelist:
	while True:
		try:
			a=requests.get(url,params={**params,**{'cmtitle':categorytitle}},timeout=(10,30))
		except:
			print(".",end="")
			continue
		else:
			break
	json:dict=a.json()
	if not isResponceOK(json):
		break
	for pageJson in json['query']['categorymembers']:
		pageid=int(pageJson['pageid'] if 'pageid' in pageJson else "")
		title=pageJson['title'] if 'title' in pageJson else ""
		if pageid not in pageidlist:
			print("[类]","\t[Cat]",categorytitle,"\t[PID]",pageid,"\t[Title]",title)
			pageidlist.append(pageid)
			n_new+=1
		else:
			#print("-","\t[Cat]",categorytitle,"\t[PID]",pageid,"\t[Title]",title)
			pass


print()
end_time=time.time()
print("ended   at",time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(end_time)))
print(second2days.main(end_time-start_time),"spent.")

print(n_new,"newly found.")

input("Done.")