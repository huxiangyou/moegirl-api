"""
Python 3.8.0
列出页面及分类中包含的所有图片
大约耗时40分钟

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
file="./imagelist.txt"

url="https://zh.moegirl.org/api.php"

params={'action':'query','format':'json','prop':'images','curtimestamp':1,'indexpageids':1,'imlimit':500,'pageids':''}

Workbook:type=openpyxl.workbook.workbook.Workbook
Worksheet:type=openpyxl.worksheet.worksheet.Worksheet
Cell:type=openpyxl.cell.cell.Cell

b:Workbook=openpyxl.load_workbook(filepath)
sMain:Worksheet=b.worksheets[0]
sTemp:Worksheet=b.worksheets[1]
sCate:Worksheet=b.worksheets[2]
sheets:Worksheet=b.worksheets

n_all=0
image_new=0

def isResponceOK(json:dict)->bool:
	if 'batchcomplete' in json:
		return True
	else:
		print("Responce is not complete.")
		return False

def isResponceContinue(json:dict)->bool:
	if 'continue' in json:
		return json['continue']['cmcontinue']
	else:
		return False

pageidlist:list=[]
for sheet in sheets:
	pageidlist+=[c.value for c in list(sheet.columns)[1]]
imagelist=[]
f=open(file,'r',encoding='UTF-8')
imagelist+=f.read().splitlines()
f.close()

categorytitlelist=[
'Category:LoveLive!系列',
'Category:LoveLive!',
'Category:LoveLive!音乐专辑封面',
'Category:LoveLive!音乐专辑假封面',
'Category:LoveLive!中角色',
'Category:东条希',
'Category:高坂绢穗',
'Category:高坂穗乃果',
'Category:高坂穗乃果的父亲',
'Category:高坂雪穗',
'Category:美佳',
'Category:南日和子',
'Category:南小鸟',
'Category:女性歌手(LoveLive!)',
'Category:绮罗翼',
'Category:山田博子',
'Category:矢泽虎太郎',
'Category:矢泽妮可',
'Category:矢泽笑美',
'Category:矢泽心',
'Category:矢泽心爱',
'Category:统堂英玲奈',
'Category:文香',
'Category:西木野瑞妃',
'Category:西木野真姬',
'Category:小泉花阳',
'Category:星空凛',
'Category:秀子',
'Category:绚濑绘里',
'Category:绚濑亚里沙',
'Category:优木杏树',
'Category:园田海未',
'Category:LoveLive!虹咲学园学园偶像同好会',
'Category:LoveLive!虹咲学园学园偶像同好会音乐专辑封面',
'Category:LoveLive!虹咲学园学园偶像同好会音乐专辑假封面',
'Category:LoveLive!虹咲学园学园偶像同好会中角色',
'Category:艾玛·维尔德',
'Category:朝香果林',
'Category:宫下爱',
'Category:近江彼方',
'Category:上原步梦',
'Category:天王寺璃奈',
'Category:樱坂雫',
'Category:优木雪菜',
'Category:中须霞',
'Category:LoveLive!Sunshine!!',
'Category:LoveLive!Sunshine!!音乐专辑封面',
'Category:LoveLive!Sunshine!!音乐专辑假封面',
'Category:LoveLive!Sunshine!!中角色',
'Category:渡边曜',
'Category:渡边月',
'Category:高海美渡',
'Category:高海千歌',
'Category:高海志满',
'Category:国木田花丸',
'Category:黑泽黛雅',
'Category:黑泽露比',
'Category:津岛善子',
'Category:鹿角理亚',
'Category:鹿角圣良',
'Category:千歌的母亲',
'Category:松浦果南',
'Category:小原鞠莉',
'Category:樱内梨子',
'Category:LoveLive!学园偶像祭',
'Category:LoveLive!虹咲学园学园偶像同好会音乐专辑假封面',
'Category:LoveLive!Sunshine!!音乐专辑假封面',
'Category:LoveLive!学园偶像祭中角色',
'Category:艾玛·维尔德',
'Category:白濑小雪',
'Category:白木凪',
'Category:坂卷千鹤子',
'Category:兵藤小百合',
'Category:多多良瑠羽',
'Category:逢泽游宇',
'Category:福原命',
'Category:高天原睦月',
'Category:宫下香',
'Category:鬼崎晶',
'Category:黑崎隼',
'Category:黑羽咲良',
'Category:黑羽咲夜',
'Category:吉川瑞希',
'Category:结城纱菜',
'Category:近江彼方',
'Category:近江遥',
'Category:九条圣来',
'Category:菊池朱美',
'Category:克里斯蒂娜(LoveLive!)',
'Category:拉克夏达',
'Category:兰花(LoveLive!)',
'Category:蕾贝卡(LoveLive!)',
'Category:蕾欧',
'Category:绫小路姬乃',
'Category:玛利亚(LoveLive!)',
'Category:门田剑',
'Category:鸟居步美',
'Category:齐木风',
'Category:森岛奈奈香',
'Category:山内奈奈子',
'Category:杉崎亚矢',
'Category:设乐风海',
'Category:神谷理华',
'Category:深山聪子',
'Category:藤城悠弓',
'Category:笹原京子',
'Category:田中幸子',
'Category:桐原优香',
'Category:西村文绘',
'Category:下园咲',
'Category:相川凉',
'Category:篠宫明瑠',
'Category:须田伊瑠香',
'Category:伊莎贝拉(LoveLive!)',
'Category:一之濑茉莉花',
'Category:樱坂雫',
'Category:永山南',
'Category:御堂优理',
'Category:月岛结架',
'Category:早乙女紫',
'Category:珍妮佛',
'Category:支仓笠音',
'Category:志贺仁美',
'Category:紫藤美咲',
'Category:佐伯丽音',
'Category:LoveLive!音乐专辑假封面',
'Category:LoveLive!学园偶像祭ALL STARS',
'Category:深井冰配音版LoveLive',
'Category:趴趴玩偶LoveLive!',
'Category:LoveLive!学园偶像祭~课后活动~',
'Category:LoveLive! School Hamedol Project',
]

categorytitlelist_2=[
]

input("Enter to start.")
start_time=time.time()
print("started at",time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(start_time)))

for pageid in pageidlist:
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
		break
	if 'images' in json['query']['pages'][str(pageid)]:
		for imageJson in json['query']['pages'][str(pageid)]['images']:
			imagetitle=imageJson['title'] if 'title' in imageJson else ""
			if imagetitle not in imagelist:
				imagelist.append(imagetitle)
				print("[图][使用]","\t[From]",json['query']['pages'][str(pageid)]['title'],"\t[File]",imagetitle)
				# f=open(file,'a+',encoding='UTF-8')
				# f.write(str(imagetitle)+"\n")
				# f.close()
				image_new+=1
			else:
				#print("-","\t[From]",json['query']['pages'][str(pageid)]['title'],"\t[File]",imagetitle)
				pass

url="https://common.moegirl.org/api.php"

params={'action':'query','format':'json','list':'categorymembers','cmlimit':500,'cmnamespace':'6'}

for categorytitle in categorytitlelist+categorytitlelist_2:
	cmcontinue=''
	while True:
		while True:
			try:
				if cmcontinue:
					a=requests.get(url,params={**params,**{'cmtitle':categorytitle,'cmcontinue':cmcontinue}},timeout=(10,30))
				else:
					a=requests.get(url,params={**params,**{'cmtitle':categorytitle}},timeout=(10,30))
			except:
				print(".",end="")
				continue
			else:
				break
		json:dict=a.json()
		for imageJson in json['query']['categorymembers']:
			imagetitle=imageJson['title'] if 'title' in imageJson else ""
			if imagetitle not in imagelist:
				imagelist.append(imagetitle)
				print("[图][分类]","\t[Cate]",categorytitle,"\t[File]",imagetitle)
				# f=open(file,'a+',encoding='UTF-8')
				# f.write(str(imagetitle)+"\n")
				# f.close()
				image_new+=1
			else:
				#print("-","\t[Cate]",categorytitle,\t[File]",imagetitle)
				pass
		cmcontinue=isResponceContinue(json)
		if not cmcontinue:
			break

print()
end_time=time.time()
print("ended   at",time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(end_time)))
print(second2days.main(end_time-start_time),"spent.")

print(image_new,"images found.")

input("Done.")