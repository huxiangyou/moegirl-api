"""
Python 3.8.0
列出所有与文件相同的文件
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

url="https://common.moegirl.org/api.php"

params={'action':'query','format':'json','prop':'duplicatefiles','curtimestamp':1,'indexpageids':1,'dflimit':'max'}
n_all=0
n_same_pair=0

def devide(l:list,n:int)->list:
	for i in range(0,len(l),n):
		yield l[i:i+n]

file="imagelist.xlsx"

Workbook:type=openpyxl.workbook.workbook.Workbook
Worksheet:type=openpyxl.worksheet.worksheet.Worksheet
Cell:type=openpyxl.cell.cell.Cell

bi:Workbook=openpyxl.load_workbook(file)

imageidlist=[]
imagetitlelist=[]
for sheet in bi.worksheets:
	imageidlist+=[c.value for c in list(sheet.columns)[1]]
	imagetitlelist+=[c.value for c in list(sheet.columns)[2]]

input("Enter to start.")
start_time=time.time()
print("started at",time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(start_time)))

for imageidlist_d in devide(imageidlist,50):
	l_param:str="|".join(str(i) for i in imageidlist_d)
	while True:
		try:
			a=requests.get(url,params={**params,**{'pageids':l_param}},timeout=(10,30))
		except:
			print(".",end="")
			continue
		else:
			break
	json:dict=a.json()
	for image in json['query']['pages']:
		imageJson=json['query']['pages'][image]
		imageid=imageJson['pageid']
		imagetitle=imageJson['title']
		n_all+=1
		if 'duplicatefiles' in imageJson:
			n_same_pair+=1
			print("[图][同]","\t[File]",imageid,"\t",imagetitle)
			for sameimage in imageJson['duplicatefiles']:
				sameimagetitle="File:"+sameimage['name'].replace("_"," ")
				if sameimagetitle not in imagetitlelist:
					imagetitlelist.append(sameimagetitle)
					print("\t\t\t\t\t[Same][新]",sameimagetitle)
				else:
					print("\t\t\t\t\t[Same]",sameimagetitle)
		else:
			#print("[图][-]","\t[File]",imageid,"\t",imagetitle)
			pass

print()
end_time=time.time()
print("ended   at",time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(end_time)))
print(second2days.main(end_time-start_time),"spent.")

print(n_same_pair,"files have their same files found.")

input("Done.")