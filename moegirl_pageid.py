"""
Python 3.8.0
对列出的页面的大小求和

Jan 7, 2020
Jan 15, 2020
Jan 26, 2020
Hu Xiangyou
"""
print(__file__.rsplit("\\",1)[1])
print(__doc__)
import requests
import time
import os
import second2days

url="https://zh.moegirl.org/api.php"

params={'action':'query','format':'json','prop':'info','curtimestamp':1,'indexpageids':1}

inputtitlelist="""星空凛
小泉花阳
西木野真姬
南小鸟
园田海未
矢泽妮可
LoveLive!
Aji人
那就是我们的奇迹
樱坂雫
逢泽游宇
黑羽咲良
东条希
宫下香
设乐风海
结城纱菜
菊池朱美
NicoNicoNi
高坂穗乃果
绚濑绘里
深井冰配音版LoveLive
告白日和！
Blueberry Train
Mermaid festa vol.2 ~Passionate~
乙女式恋爱塾
Cutie Panther
Diamond Princess的忧郁
Someday of my life
恋爱的信号Rin rin rin!
我开始做魔法使了！
孤独的Heaven
Love marginal
Sweet&sweet holiday
Pure girls project
UNBALANCED LOVE
不知道的Love 教给我吧Love
来自微热的Mystery
我们的LIVE 与你的LIFE
Snow halation
Baby maybe 恋爱的按钮
夏色笑颜1,2,Jump!
Mermaid festa vol.1
满怀“love”接近中！
Music S.T.A.R.T!!
所以说请加油吧
夏天，请不要结束。
Love Novels
Soldier game
LOVELESS WORLD
After school NAVIGATORS
Listen to my heart!!
LoveLive!学园偶像祭
Oh,Love&Peace!
Wonderful Rush
前进Tomorrow
玻璃花园
WILD STARS
Beat in Angel
欲于辉夜之城起舞
寻常悲伤的尽头
好狡猾哟Magnetic today
Daring!!
勇气的Reason
Anemone heart
LoveLive!学园偶像天国
纯爱镜头
START:DASH!!
软绵绵的哦！
跳绳
可爱妮可的女子之道
LONELIEST BABY
梦想之门
爱不是太阳吗？
你不再是孤单一人了哦
Paradise Live
宝物(LoveLive!)
ENDLESS PARADE
No brand girls
Love wing bell
转转凛MIRACLE
Storm in Lover
SENTIMENTAL StepS
明明只是你！
Shangri-La Shower
永远Friends
小夜啼鸟恋诗
友情No Change
秋日彼端的遥远天空
Spica Terrible
我们是未来之花
如今的我们
一定能听见青春
从今以后的Someday
Wonder zone
Private Wars
无论何时一直
COLORFUL VOICE
Dancing stars on me!
Happy maker!
KiRa-KiRa Sensation!
Shocking Party
向幸福前行的SMILING!
你着欢喜我喜欢着你
如果从那时一定
LoveLive!学园偶像祭/主要角色
两个人的Happiness
我喜欢你你喜欢我吗？
冬天给予的预感
Trouble Busters
Silent tonight
然后是最后一页
CheerDay CheerGirl!
想看见同一颗星
Dreamin' Go! Go!!
为了保护我们心爱的ooo……成为偶像！
正因为是太无情
成为如此忧美的日子
没有梦想的梦想不是梦想
革命吗？神明大人！
迄今为止的LoveLive!
M是μ’sic的M
Super LOVE=Super LIVE!
支仓笠音
琴梨
LoveLive!Sunshine!!
高海千歌
LoveLive!/投票
想在MUSEUM做什么？
最坏又最好的PARADISO
乙姬心恋宫殿
出道风云
LoveLive!学园偶像祭/UR
LoveLive!学园偶像祭/SR
LoveLive!学园偶像祭/R
Angelic Angel
Hello,细数繁星
SUNNY DAY SONG
HEARTBEAT(LoveLive!)
黑泽黛雅
渡边曜
津岛善子
樱内梨子
松浦果南
我们是合而为一的光芒
Future style
南日和子
黑泽露比
国木田花丸
小原鞠莉
矢泽笑美
LoveLive!事件年表
LoveLive!/音乐列表
孤独的回廊
LoveLive!学园偶像祭/课题
LoveLive!学园偶像祭/称号
LoveLive!学园偶像祭/活动历史数据
羽毛知道了？
闪光Resolution
I'll smile for yours
秘密与花园
在这里等待
梦ONCE AGAIN
NEURON, NEURON!!
矢泽心
LoveLive!学园偶像祭/背景
矢泽心爱
LoveLive!学园偶像祭/星空凛卡牌
As Time Goes By
抢镜脸
你的心灵是否光芒闪耀？
爱上你万岁！
女性歌手(LoveLive!)
学园偶像(LoveLive!)
LoveLive!Sunshine!!/事件年表
Step! ZERO to ONE
LoveLive!/希绘里Radio Garden
Aqours HEROES
LoveLive!/TV动画作品
浦之星女子学院
HEART to HEART
正因为是暴风雨中的爱恋
LoveLive!/μ's Go Go! LoveLive! 2015 ~Dream Sensation!~
NO EXIT ORION
LoveLive!学园偶像电影
LoveLive!/LoveLi部 广播课外活动
LoveLive!/LoveLi部 Nico生课外活动
LoveLive!/新田Fight Club
WAO-WAO Powerful day!
LoveLive!/Tokyo MX特番泄露事件
LoveLive!/μ's 3rd Anniversary LoveLive!
从今以后
想成为回忆以上的存在
LoveLive!/μ's NEXT LoveLive! 2014 ~ENDLESS PARADE~
春情Romantic
绮罗翼
统堂英玲奈
优木杏树
LoveLive!/μ's First LoveLive!
LoveLive!/μ's New Year LoveLive! 2013
秀子
文香
美佳
A-RISE
高坂雪穗
绚濑亚里沙
矢泽虎太郎
高坂绢穗
西木野瑞妃
山田博子
深山聪子
笹原京子
山内奈奈子
鸟居步美
LoveLive!/μ's Final LoveLive!
错觉CROSSROADS
PSYCHIC FIRE
Printemps
LoveLive!/希果百宝箱
我们的LIVE 与你的LIFE(单曲)
MOMENT RING
Snow halation(单曲)
Love marginal(单曲)
Diamond Princess的忧郁(单曲)
不知道的Love 教给我吧Love(单曲)
夏色笑颜1,2,Jump!(单曲)
海色少女令人着迷
小鸟Lovin' you
淡淡的穗乃果色！
满怀“love”接近中！(单曲)
LoveLive! Solo Live! collection Memorial BOX I
Mermaid festa vol.2 ~Passionate~(单曲)
乙女式恋爱塾(单曲)
告白日和！(单曲)
Soldier game(单曲)
Wonderful Rush(单曲)
我们活在当下(单曲)
Μ's Best Album Best Live! collection
LoveLiv部 广播课外活动 妮凛花 主题曲DJCD
一定能听见青春(单曲)
前进Tomorrow START:DASH!!
从今以后的Someday Wonder zone
No brand girls START:DASH!!
Notes of School idol days
从微热到Mystery(单曲)
Cutie Panther(单曲)
Pure girls project(单曲)
Music S.T.A.R.T!!(单曲)
宝物 Paradise Live
LoveLive! Solo Live! collection Memorial BOX II
那就是我们的奇迹(单曲)
无论何时一直(单曲)
梦想之门(单曲)
Love wing bell Dancing stars on me!
KiRa-KiRa Sensation! Happy maker!
Notes of School idol days ~Glory~
Shangri-La Shower(单曲)
永远Friends(单曲)
秋日彼端的遥远天空(单曲)
冬天给予的预感(单曲)
M是μ’sic的M(单曲)
Μ's Best Album Best Live! Collection II
Angelic Angel Hello,细数繁星
SUNNY DAY SONG HEARTBEAT
我们是合而为一的光芒 Future style
Notes of School Idol Days ~Curtain Call~
HEART to HEART!(单曲)
WAO-WAO Powerful day!(单曲)
想成为回忆以上的存在(单曲)
错觉CROSSROADS(单曲)
再会了再见！
MOMENT RING(单曲)
天使们的福音
BiBi
LoveLive!/翻唱
Lily white
高天原睦月
须田伊瑠香
近江遥
西村文绘
蕾贝卡(LoveLive!)
紫藤美咲
永山南
桐原优香
一之濑茉莉花
克里斯蒂娜(LoveLive!)
兵藤小百合
吉川瑞希
御堂优理
月岛结架
杉崎亚矢
LoveLive!/应援
九条圣来
黑羽咲夜
田中幸子
篠宫明瑠
藤城悠弓
神谷理华
近江彼方
佐伯丽音
鬼崎晶
福原命
志贺仁美
坂卷千鹤子
森岛奈奈香
下园咲
多多良瑠羽
白木凪
黑崎隼
门田剑
齐木风
绫小路姬乃
白濑小雪
相川凉
兰花(LoveLive!)
拉克夏达
伊莎贝拉(LoveLive!)
艾玛·维尔德
珍妮佛
玛利亚(LoveLive!)
蕾欧
早乙女紫
想在AQUARIUM恋爱
等待我的恋爱之歌
哪怕是望尘莫及的繁星
LL神教
Endless Love 来自过去的礼物
Endless Love 妹妹哈啦咻
Endless Love 珍惜彼此的相遇
我和希相处的一天
夜空是否全然知晓？
元气全开DAY!DAY!DAY!
Endless Love 友情No Change
元气全开DAY!DAY!DAY!(单曲)
LoveLive!/广播剧列表
让我俘虏你的心PLEASE!!
悸动分类学
CYaRon!
LoveEcho中翻组
Guilty Night, Guilty Kiss!
Strawberry Trapper
AZALEA
Guilty Kiss
如果奇迹有颜色，那一定是橙色
青空Jumping Heart
下定决心Hand in Hand
LoveLive!学园偶像祭/往期版本
你的心灵是否光芒闪耀？(单曲)
LoveLive!学园偶像祭/投票/国服
LoveLive!学园偶像祭/投票/主页
LoveLive!学园偶像祭/投票
与其诉说梦想，不如高歌梦想
最喜欢的话就没问题！
Humming Friend
想用梦照亮夜空
LoveLiver
鹿角理亚
Sunshine熠熠生辉之歌
SELF CONTROL!!
不成熟的DREAMER
因为要在Pops heart间舞蹈
鹿角圣良
天空与心灵皆能雨过天晴
思念合而为一吧
让我俘虏你的心PLEASE!!(单曲)
Strawberry Trapper(单曲)
MIRAI TICKET
LoveLive!Sunshine!!/Aqours First LoveLive!～Step! ZERO to ONE～
无法停止的Jingle Bell
Waku-Waku-Week!
无法停止的Jingle Bell(单曲)
圣日的祈祷
LoveLive!Sunshine!!/TV动画作品
Daydream Warrior
Sailing to the Sunshine
G弦上的灰姑娘
Thrilling One-way
想在AQUARIUM恋爱(单曲)
国立音乃木坂学院
P.S.的另一侧
LONELY TUNING
Guilty Eyes Fever
追赶太阳吧！
LoveLive!Sunshine!!/Aqours 2nd LoveLive! HAPPY PARTY TRAIN TOUR
HAPPY PARTY TRAIN
青空Jumping Heart(单曲)
与其诉说梦想，不如高歌梦想(单曲)
下定决心Hand in Hand／最喜欢的话就没问题！
想用梦照亮夜空／不成熟的DREAMER
思念合而为一吧／MIRAI TICKET
HAPPY PARTY TRAIN(单曲)
想谈少女以上的恋爱
SKY JOURNEY
LoveLive!学园偶像祭/活动列表
LoveLive!学园偶像祭/第一次 Challenge Festival
LoveLive!学园偶像祭/第一次 Medley Festival
LoveLive!学园偶像祭/第一次 Score Match
LoveLive!学园偶像祭/Sweet Holiday 小鸟的点心
LoveLive!学园偶像祭/第二次 Medley Festival
LoveLive!学园偶像祭/第一次 散步拉力赛
LoveLive!学园偶像祭/第二次 Challenge Festival
LoveLive!学园偶像祭/第三次 Medley Festival
LoveLive!学园偶像祭/第二次 Score Match
LoveLive!学园偶像祭/第四次 Medley Festival
LoveLive!学园偶像祭/第五次 Medley Festival
LoveLive!学园偶像祭/第六次 Medley Festival
LoveLive!学园偶像祭/第七次 Medley Festival
LoveLive!学园偶像祭/第八次 Medley Festival
LoveLive!学园偶像祭/第九次 Medley Festival
LoveLive!学园偶像祭/第三次 Score Match
LoveLive!学园偶像祭/第十次 Medley Festival
LoveLive!学园偶像祭/第三次 Challenge Festival
LoveLive!学园偶像祭/第十一次 Medley Festival
LoveLive!学园偶像祭/第十二次 Medley Festival
LoveLive!学园偶像祭/第四次 Score Match
LoveLive!学园偶像祭/怀抱明月 Love*Heart
LoveLive!学园偶像祭/理想中的我
LoveLive!学园偶像祭/第五次 Score Match
LoveLive!学园偶像祭/无瑕的少女心
LoveLive!学园偶像祭/忧郁的公主
LoveLive!学园偶像祭/第一次的Happy tune
LoveLive!学园偶像祭/闪耀吧 Can I do!
LoveLive!学园偶像祭/第九次 Challenge Festival
LoveLive!学园偶像祭/We are NAVIGATORS!
LoveLive!学园偶像祭/第二十五次 Score Match
LoveLive!学园偶像祭/第二十七次 Score Match
LoveLive!学园偶像祭/第二十六次 Score Match
LoveLive!学园偶像祭/猎物…就是你!
LoveLive!学园偶像祭/纯真宣言!
LoveLive!学园偶像祭/我的心摇摆不定
LoveLive!学园偶像祭/快点…看向我这边!
LoveLive!学园偶像祭/爱是海市蜃楼
LoveLive!学园偶像祭/亲口说出I love you
LoveLive!学园偶像祭/第六次 Score Match
LoveLive!学园偶像祭/第七次 Score Match
LoveLive!学园偶像祭/为什么肚肚会饿呢?
LoveLive!学园偶像祭/第八次 Score Match
LoveLive!学园偶像祭/第一次的活动好辛苦!?
LoveLive!学园偶像祭/第九次 Score Match
LoveLive!学园偶像祭/我们之间的秘密。
LoveLive!学园偶像祭/第十次 Score Match
LoveLive!学园偶像祭/μ's 泳装大赛。
LoveLive!学园偶像祭/第十一次 Score Match
LoveLive!学园偶像祭/音乃木阪七大不可思议。
LoveLive!学园偶像祭/第十二次 Score Match
LoveLive!学园偶像祭/青梅竹马的2人。
LoveLive!学园偶像祭/第十三次 Score Match
LoveLive!学园偶像祭/和凛一夜的误会。
LoveLive!学园偶像祭/第十四次 Score Match
LoveLive!学园偶像祭/小希的心灵生活。
LoveLive!学园偶像祭/妮可的秘密测定♡
LoveLive!学园偶像祭/第十五次 Score Match
我在海岸大街等着你哦
LoveLive!学园偶像祭/夜空似乎知晓一切
LoveLive!学园偶像祭/第二十八次 Score Match
LoveLive!学园偶像祭/那是恋之诗
LoveLive!学园偶像祭/第十六次 Score Match
LoveLive!学园偶像祭/好想凝视着你的每一天
LoveLive!学园偶像祭/第二十九次 Score Match
LoveLive!学园偶像祭/第十七次 Score Match
LoveLive!学园偶像祭/竭尽全力的欢笑吧
LoveLive!学园偶像祭/SMILING!
LoveLive!学园偶像祭/第十八次 Score Match
LoveLive!学园偶像祭/第十九次 Score Match
LoveLive!学园偶像祭/第二十次 Score Match
LoveLive!学园偶像祭/今日的闪耀预感
LoveLive!学园偶像祭/Loving you!
LoveLive!学园偶像祭/Magnetic today!!
LoveLive!学园偶像祭/非常非常MIRACLE
LoveLive!学园偶像祭/喜欢喜欢软绵绵
LoveLive!学园偶像祭/研究必要
LoveLive!学园偶像祭/不灭热情
LoveLive!学园偶像祭/第二十一次 Score Match
LoveLive!学园偶像祭/第二十二次 Score Match
LoveLive!学园偶像祭/第二十三次 Score Match
LoveLive!学园偶像祭/第二十四次 Score Match
LoveLive!学园偶像祭/第三十次 Score Match
LoveLive!学园偶像祭/第十三次 Medley Festival
LoveLive!学园偶像祭/第十四次 Medley Festival
LoveLive!学园偶像祭/第四次 Challenge Festival
LoveLive!学园偶像祭/第五次 Challenge Festival
LoveLive!学园偶像祭/第十五次 Medley Festival
LoveLive!学园偶像祭/第十六次 Medley Festival
LoveLive!学园偶像祭/第六次 Challenge Festival
LoveLive!学园偶像祭/第七次 Challenge Festival
LoveLive!学园偶像祭/第八次 Challenge Festival
LoveLive!学园偶像祭/礼包详情
不久将来的Happy End
LoveLive!学园偶像祭/第三十一次 Score Match
LoveLive!学园偶像祭/对视的两人
不久将来的Happy End(单曲)
GALAXY HidE and SeeK
INNOCENT BIRD
脆弱易碎
Aqours CLUB CD SET
GALAXY HidE and SeeK(单曲)
Shadow gate to love
LoveLive!学园偶像祭/投票/国际服
LoveLive!学园偶像祭/投票/日服
LoveLive!学园偶像祭/第十七次 Medley Festival
LoveLive!学园偶像祭/别离开我 You are my love
Landing action Yeah!!
天王寺璃奈
宫下爱
朝香果林
上原步梦
优木雪菜
中须霞
LoveLive!学园偶像祭/第三十二次 Score Match
脆弱易碎(单曲)
LoveLive!学园偶像祭/请给我幸福的结局
LoveLive!学园偶像祭/第一次 友情大合战
LoveLive!学园偶像祭/像梦一般的One night
向夏天的门 Never end ver.
盛夏为谁所拥有？
夏天结束的雨声
家乡之爱满满夏日时光
LoveLive!学园偶像祭/第三十三次 Score Match
SUMMER VACATION
Saint Snow
LoveLive!学园偶像祭~课后活动~
樱之雨(同人社团)
LoveLive!学园偶像祭/第十次 Challenge Festival
LoveLive!学园偶像祭/第二次 散步拉力赛
LoveLive!学园偶像祭/往期版本更新记录
LoveLive!学园偶像祭/第十八次 Medley Festival
LoveLive!学园偶像祭ALL STARS
LoveLive!虹咲学园学园偶像同好会
LoveLive!学园偶像祭/Calling you!
你逢田姐当然会oo呀
未来的我们早已知晓
环游在你眼瞳中的冒险
LoveLive!学园偶像祭/第十一次 Challenge Festival
勇气在哪？在你的内心！
"MY LIST" to you!
MY舞 TONIGHT
LoveLive!学园偶像祭/努力的人是最棒的
未来的我们早已知晓(单曲)
LoveLive!学园偶像祭/可以恋爱哦
CRASH MIND
MIRACLE WAVE
One More Sunshine Story
LoveLive!学园偶像祭/第二次 友情大合战
勇气在哪？在你的内心！(单曲)
DROPOUT
MY舞 TONIGHT／MIRACLE WAVE
Awaken the power
LoveLive!学园偶像祭/第三十四次 Score Match
大家晚安！
LoveLive!学园偶像祭/第三次 散步拉力赛
Awaken the power(单曲)
WATER BLUE NEW WORLD
WONDERFUL STORIES
LoveLive!Sunshine!!学园偶像电影~彩虹彼端~
LoveLive!学园偶像祭/第三次 友情大合战
In this unstable world
Pianoforte Monologue
WATER BLUE NEW WORLD／WONDERFUL STORIES
LoveLive!学园偶像祭/雪花大会
Journey to the Sunshine
LoveLive!学园偶像祭/第十二次 Challenge Festival
Beginner's Sailing
LoveLive!学园偶像祭/第四次 友情大合战
LoveLive!Sunshine!!/Aqours 3rd LoveLive! Tour ～WONDERFUL STORIES～
LoveLive!学园偶像祭/第三十五次 Score Match
RED GEM WINK
WHITE FIRST LOVE
LoveLive!学园偶像祭/第四次 散步拉力赛
LoveLive!学园偶像祭/第五次 友情大合战
New winding road
是鱼还是果南？
LoveLive!学园偶像祭/相同的心情
趴趴玩偶LoveLive!
LoveLive!Sunshine!!/Saint Snow PRESENTS LoveLive!Sunshine!! HAKODATE UNIT CARNIVAL
LoveLive!学园偶像祭/第十三次 Challenge Festival
趴趴玩偶LoveLive!/关卡报酬一览
奇迹闪耀
樱花再见
毕业了呢
Guilty!? Farewell party
LoveLive!学园偶像祭/第六次 友情大合战
Hop Step Wai!
LoveLive!学园偶像祭/第十四次 Challenge Festival
Aqours CLUB CD SET 2018
LoveLive!Sunshine!!/Aqours 4th LoveLive! ～Sailing to the Sunshine～
LoveLive!学园偶像祭/第五次 散步拉力赛
趴趴玩偶LoveLive!/趴趴一览
LoveLive!学园偶像祭/第七次 友情大合战
LoveLive!Sunshine!!/Aqours World Love Live! in LA ~Beyond the Pacific~
Thank you, FRIENDS!!
No.10
Thank you, FRIENDS!!(单曲)
LoveLive!Sunshine!!/应援
LoveLive!学园偶像祭/Guilty Eyes 堕入情网
趴趴玩偶LoveLive!/称号
LoveLive! Solo Live! collection Memorial BOX III
大家一起Score Match 历次活动与曲池
LoveLive!学园偶像祭/第十五次 Challenge Festival
向着梦想的一步
Diamond(LoveLive!)
你理想的女主角
LoveLive!学园偶像祭/LoveLive!学园偶像祭发展历史
LoveLive!学园偶像祭/游戏机制
LoveLive!学园偶像祭/活动介绍
LoveLive!学园偶像祭/歌曲列表
LoveLive!学园偶像祭/外部链接及参考资料
LoveLive!学园偶像祭/第八次 友情大合战
Starlight(LoveLive!)
特别Going!!
想去沉睡的森林啊
LoveLive!学园偶像祭/第三十六次 Score Match
CHASE!
Evergreen(LoveLive!)
Doki Pipo Emotion
TOKIMEKI Runners
LoveLive!学园偶像祭/有种预感我们将再见面呢
TOKIMEKI Runners(专辑)
LoveLive!学园偶像祭/第六次 散步拉力赛
LoveLive!学园偶像祭/第三十七次 Score Match
起始之路
不可能预测Driving!
Marine Border Parasol
LoveLive!学园偶像祭/第九次 友情大合战
LoveLive!系列
LoveLive!学园偶像祭/第七次 散步拉力赛
LoveLive!学园偶像祭/第十六次 Challenge Festival
LoveLive!学园偶像祭/我想通过这首歌来帮助你
Hop? Stop? Nonstop!
Next SPARKLING!!
我们奔跑而来的道路…
LoveLive!学园偶像祭/第三十八次 Score Match
Believe again／Brightest Melody／Over The Next Rainbow
逃离迷途莫比乌斯环
LoveLive!Sunshine!!/Infobox
Brightest Melody
Believe again
Over The Next Rainbow
LoveLive!学园偶像祭/第八次 散步拉力赛
我们奔跑而来的道路…／Next SPARKLING!!
LoveLive!Sunshine!!/偶像活动杂项
逃离迷途莫比乌斯环／Hop? Stop? Nonstop!
LoveLive!学园偶像祭/第十次 友情大合战
高海美渡
渡边月
LoveLive!学园偶像祭/第十九次 Medley Festival
Thank you, FRIENDS!! SOLO CONCERT
LoveLive!学园偶像祭/第十七次 Challenge Festival
Sailing to the Rainbow
LoveLive!Sunshine!!/Aqours 5th LoveLive! ～Next SPARKLING!!～
LoveLive!Sunshine!!/Aqours World LoveLive! ASIA TOUR 2019
LoveLive!学园偶像祭/第十一次 友情大合战
LoveLive!学园偶像祭/第九次 散步拉力赛
高坂穗乃果的父亲
LoveLive!学园偶像祭/第三十九次 Score Match
高海志满
LoveLive!学园偶像祭/第二十次 Medley Festival
千歌的母亲
LoveLive!Sunshine!!/Aqours World LoveLive! in LA ～BRAND NEW WAVE～
LoveLive!学园偶像祭/卒業バイバイ
Jump up HIGH!!
Aqours CLUB CD SET 2019
LoveLive!学园偶像祭/第十八次 Challenge Festival
梨子的母亲
LoveLive!系列/9th Anniversary LOVE LIVE! FEST
LoveLive!学园偶像祭/第十次 散步拉力赛
I-n-g, I TRY!!
LoveLive!学园偶像祭/第十二次 友情大合战
LoveLive!学园偶像祭/第二十一次 Medley Festival
冒险Type A, B, C!!
未体验HORIZON(单曲)
LoveLive!学园偶像祭/SIFID
LoveLive!学园偶像祭/第四十次 Score Match
未体验HORIZON
LoveLive!学园偶像祭/きっと誰もが通る道ですね
Deep Resonance
Dance with Minotaurus
LoveLive!虹咲学园学园偶像同好会/虹咲学园学园偶像同好会 First Live “with You”
Love U my friends(专辑)
Love U my friends
开花宣言
Wonderland(LoveLive!)
Audrey
Wish(LoveLive!)
友 & 爱
My Own Fairy-Tale
MELODY(LoveLive!)
声音连接起来吧
Tele-telepathy
KOKORO Magic “A to Z”
LoveLive!学园偶像祭/第十九次 Challenge Festival
学园偶像祭系列感谢祭
学园偶像祭系列感谢祭/2016
学园偶像祭系列感谢祭/2017
学园偶像祭系列感谢祭/2019
学园偶像祭系列感谢祭/2018
学园偶像祭系列感谢祭/2015
KOKORO Magic “A to Z”(单曲)
LoveLive!学园偶像祭/響く共鳴、つながるセカイ
LoveLive!学园偶像祭ALL STARS/游戏机制
LoveLive!学园偶像祭/第二十二次 Medley Festival
LoveLive!Sunshine!!/UNIT LIVE ADVENTURE 2020
LoveLive!学园偶像祭ALL STARS/秘密のパーティー！
LoveLive!学园偶像祭ALL STARS/外部链接及参考资料
Wake up, Challenger!!
New Romantic Sailors
LoveLive!学园偶像祭/キミは最高のPartner
LoveLive!学园偶像祭ALL STARS/活动介绍与列表
LoveLive!学园偶像祭ALL STARS/和装モデルはお任せあれ！
Braveheart Coaster
LoveLive!学园偶像祭ALL STARS/"你"
LoveLive!学园偶像祭/第十一次 散步拉力赛
LoveLive!学园偶像祭ALL STARS/下町巡り珍道中
LoveLive!系列/All Night Nippon GOLD
LoveLive!虹咲学园学园偶像同好会/虹咲学园午休放送室
Amazing Travel DNA
LoveLive!学园偶像祭/第十三次 友情大合战
Love Pulsar
Phantom Rocket Adventure
New Romantic Sailors(单曲)
CHANGELESS
孤独Teleport
Braveheart Coaster(单曲)
LoveLive!学园偶像祭/第四十一次 Score Match
空中恋爱论
迷宫世界
Amazing Travel DNA(单曲)
Μ's Memorial CD-BOX「Complete BEST BOX」
LoveLive!虹咲学园学园偶像同好会/应援
SUPER NOVA
Love Triangle
Dream Land！Dream World！
Cheer for you!!
Sing & Smile!!
Beautiful Moonlight
SUPER NOVA(单曲)
Dream Land！Dream World！(单曲)
Sing & Smile!!(单曲)
DiverDiva
A·ZU·NA
QU4RTZ
LoveLive!学园偶像祭/第二十次 Challenge Festival
虹咲学园
秋叶原记者(LoveLive!)
LoveLive!虹咲学园学园偶像同好会/AbemaTV Ultra Games印象女孩决定战
LoveLive!虹咲学园学园偶像同好会/事件年表
LoveLive!学园偶像祭/第十四次 友情大合战
三船栞子
LoveLive!学园偶像祭ALL STARS/歌曲列表
A song for You! You? You!!
LoveLive!学园偶像祭/第二十三次 Medley Festival
LoveLive!虹咲学园学园偶像同好会/TV动画作品
LoveLive!学园偶像祭/第二十一次 Challenge Festival
LoveLive!学园偶像祭ALL STARS/剧情列表
A song for You! You? You!!(单曲)
なってしまった!
LoveLive!学园偶像祭/第四十二次 Score Match
LoveLive!虹咲学园学园偶像同好会/虹咲学园早安放送室
Category:LoveLive!
Category:LoveLive! 学园偶像祭
Category:LoveLive!Sunshine!!
Category:LoveLive!音乐
Category:LoveLive!题材同人作品
Category:LoveLive!音乐专辑
Category:LoveLive!音乐单曲
Category:LoveLive!Sunshine!!音乐
Category:LoveLive!音乐唱片
Category:Endless Love系列
Category:Lily white音乐单曲
Category:Saint Snow歌曲
Category:LoveLive!虹咲学园学园偶像同好会音乐
Category:LoveLive!系列
Category:LoveLive!虹咲学园学园偶像同好会
Category:BiBi音乐单曲
Category:Printemps音乐单曲
Category:LoveLive!学园偶像祭ALL STARS
Category:LoveLive!系列音乐
Category:LoveLive!虹咲学园学园偶像同好会音乐唱片
Category:LoveLive!虹咲学园学园偶像同好会音乐单曲
Category:LoveLive!虹咲学园学园偶像同好会音乐专辑
Category:DiverDiva音乐单曲
Category:A·ZU·NA音乐单曲
Category:QU4RTZ音乐单曲
Category:DiverDiva歌曲
Category:A·ZU·NA歌曲
Category:QU4RTZ歌曲
Category:LoveLive!Sunshine!!音乐唱片
Category:LoveLive!Sunshine!!音乐单曲
Category:虹咲学园学园偶像同好会歌曲
Category:LoveLive!Sunshine!!音乐专辑
Category:AZALEA音乐单曲
Category:Guilty Kiss音乐单曲
Category:CYaRon!音乐单曲
Category:Aqours歌曲
Category:CYaRon!歌曲
Category:AZALEA歌曲
Category:Guilty Kiss歌曲
Category:Μ's歌曲
Category:Printemps歌曲
Category:Lily white歌曲
Category:BiBi歌曲
Category:Saint Aqours Snow歌曲
Category:A-RISE歌曲
Category talk:萌百Loveliver
Category talk:Lily white音乐单曲
Talk:Aji人
Talk:矢泽妮可
Talk:NicoNicoNi
Talk:Diamond Princess的忧郁
Talk:我开始做魔法使了！
Talk:小泉花阳
Talk:LoveLive!
Talk:M是μ’sic的M
Talk:LoveLive!学园偶像祭
Talk:高海千歌
Talk:LoveLive!Sunshine!!
Talk:樱内梨子
Talk:抢镜脸
Talk:LoveLive!/Tokyo MX特番泄露事件
Talk:我们的LIVE 与你的LIFE
Talk:我们是合而为一的光芒
Talk:Diamond Princess的忧郁(单曲)
Talk:LL神教
Talk:MOMENT RING
Talk:我和希相处的一天
Talk:夜空是否全然知晓？
Talk:元气全开DAY!DAY!DAY!
Talk:LoveEcho中翻组
Talk:想在AQUARIUM恋爱
Talk:黑泽露比
Talk:HEARTBEAT(LoveLive!)
Talk:渡边曜
Talk:不成熟的DREAMER
Talk:如今的我们
Talk:START:DASH!!
Talk:LoveLive!学园偶像祭/投票/台服
Talk:LoveLive!学园偶像祭/第一次的Happy tune
Talk:爱不是太阳吗？
Talk:Private Wars
Talk:LoveLive!学园偶像祭/第八次 Challenge Festival
Talk:SUNNY DAY SONG
Talk:趴趴玩偶LoveLive!
Talk:LoveLive!学园偶像祭/第二次 散步拉力赛
Talk:LoveLive!虹咲学园学园偶像同好会
Talk:园田海未
Talk:LoveLive!系列
Talk:想看见同一颗星
Talk:天王寺璃奈
Talk:微笑小香香
Talk:Mermaid festavol.1
Talk:我们活在当下
Talk:第一次的Happy tune
Talk:爱不是太阳么
Talk:ダイヤモンドプリンセスの憂鬱
Talk:钻石公主的忧郁
Talk:钻石公主的忧郁(专辑)
Talk:LoveLive!School idol festival PERFECT Dream Project
Talk:夜空全都知道吗？
Talk:Diamond Princess的忧郁(专辑)
Talk:M是μ'sic的M
Talk:魔法使初次见面!
Talk:LoveLive!/2015
Talk:LoveLive!/201601
LoveLive
Love Arrow Shoot
Minalinsky
凛喵
南ことり
南琴梨
矢泽にこ
矢泽仁子
矢泽妮歌
矢泽日香
LoveLive！
Love Live!
Lovelive
Lovelive!
ラブライブ
ラブライブ!
ラブライブ School idol project
垃圾人
明星學生妹
爱与演唱会！
Osaka Shizuku
それは僕たちの奇跡
好好的一个人
宫下可可
我们的奇迹
日香日香日
樱坂しずく
樱阪雫
这就是我们的奇迹
黒羽咲良
KKE
NiconicoNi
Niconiconi
Niconiconi～
妮可妮可妮
妮可笑眯眯
微笑小香香
果果
深井冰版lovelive！
绚濑絵里
2.5次元LoveLive!
ぶる～べりぃ♡とれいん
ぶる～べりぃ♥とれいん
告白日和
告白日和!
告白日和、です！
深井冰配音版LoveLive!
深井冰配音版lovelive
蓝莓 列车
蓝莓火车
Mermaid festa vol.2 ~passionate~
ダイヤモンドプリンセスの憂鬱
乙女式れんあい塾
人鱼狂欢节 vol.2 ~激情版~
凛凛凛个鳖
恋のシグナルRin rin rin!
恋爱的信号Rin rin rin
恋爱的信号 Rin rin rin
恋爱的信号 Rin rin rin!
钻石公主的忧郁
まほうつかいはじめました！
不知道的Love 告诉我吧Love
孤独なHeaven
孤独天堂
孤独的天堂
我开始做魔法使了
我开始做魔法使了!
知らないLove*教えてLove
请教我如何面对未到的爱情
魔法使初次见面!
ぼららら
不知道的Love*教给我吧Love
僕らのLIVE 君とのLIFE
微热mystery
微热的Mystery
微熱からMystery
我们的Live与你的Life
我们的live 你的life
知らないLove＊教えてLove
雪色光晕
Baby maybe 恋のボタン
Baby maybe恋爱的button
Baby maybe恋爱的按钮
Baby maybe恋爱的纽扣
Mermaid festavol.1
Snow Halation
もぎゅっと“love”で接近中！
人鱼狂欢节 vol. 1
夏色えがおで1,2,Jump!
满怀爱意接近中!
あのねがんばれ
あのねがんばれ!
もぎゅっと“love”で接近中!
我·说·啊·请·你·加·油
我·说·啊·请·你·加·油!
我说啊请你加油
满怀love接近中
满怀“love”接近中!
满怀爱意接近中
满怀爱意接近你
After school NAVIGATOR
LoveLive! 学园偶像祭
Loveless world
ラブノベルス
士兵游戏
夏、終わらないで。
夏天,请不要结束
夏天请不要结束
夏日,不会终结
夏日勿终
SIF
Wonderful rush
ススメ→トゥモロウ
前进→Tomorrow
学园偶像祭
想在輝夜之城起舞
我给你三张KKE
硝子の花園
继续前进→Tomorrow
輝夜の城で踊りたい
ありふれた悲しみの果て
ずるいよMagnetic today
不夜城之舞
买袜子go go
勇気のReason
学园偶像天国
欲于辉夜城起舞
满溢悲伤的尽头
磁力花园
辉夜城
LoveLive! 学园偶像天国
Puwapuwa-o!
なわとび
ぷわぷわーお!
ぷわぷわーお！
妮可不理
純愛レンズ
软绵绵的-哦!
软绵绵的哦
黑丝的大叔
にこぷり♡女子道
にこぷり♥女子道
にこぷり女子道
ユメノトビラ
梦想大门
爱不是太阳么
爱不是太阳么?
爱不是太阳吗
通向梦想之门
通往梦想的大门
くるりんMIRACLE
もうひとりじゃないよ
タカラモノズ
一心一教
团团凛MIRACLE
宝物(LoveLive!学园偶像祭)
爱は太阳じゃない？
爱不像太阳吗?
爱如阳光
爱如阳光?
キミのくせに
キミのくせに!
キミのくせに！
你怎么可能会有女朋友嘛
分明就是你!
明明只是你
明明只是你!
永遠フレンズ
转一圈出奇迹
风暴花园
Nightingale Love Song
ナイチンゲールラブソング
友情ノーチェンジ
友情不变
永远friends
秋のあなたの空遠く
秋之彼端路遥远
秋天的你远离天空
秋日的你远在天边
秋日的你逐渐远去
きっと青春が聞こえる
これからのSomeday
スピカテリブル
一定能听见青春的乐章
僕らは今のなかで
我们是未来的花朵
我们活在当下
未来的某一天
珍珠星的距离
私たちは未来の花
どんなときもずっと
ふたりハピネス
もしもからきっと
るてしキスキしてる
シアワセ行きのSMILING!
向幸福前行的SMILING
如果将来一定
学园偶像祭主要角色
学院偶像祭主要角色
王大粽
そして最後のページには
冬がくれた予感
冬天带给我的预感
同じ星が见たい
喜欢吗喜欢吗？
好きですが好きですか?
好きですが好きですか？
开心二人组
想见到同样的繁星
我喜欢你你喜欢我吗
だってだって噫無情
为了保护我们心爱的○○○……成为偶像！
可是可是噫无情
成为如此优美的日子
斯くも憂美な日となりて
无梦之梦不是梦
梦なき梦は梦じゃない
正因为是噫无情
革命ですね？神様！
革命吗?神明大人!
LLSS
LoveLive！Sunshine!!
M是μ'sic的M
これまでのLoveLive!
これまでのラブライブ！
ミはμ'sicのミ
ミはμ’sicのミ
爱与演唱会！阳光！！
迄今为止的lovelive
革命ですね?神様!
Lovelive! Sunshine!!
Lovelivesunshine
MUSEUMでどうしたい？
ラブライブ！サンシャイン！！
乙姫心で恋宫殿
乙姫心で恋宮殿
想在MUSEUM做什么
最低で最高のPARADISO
棕色羊驼
白色羊驼
?←HEARTBEAT
Hello,数星星
Hello,星を数えて
ハテナハートビート
僕たちはひとつの光
僕光
南小鸟的母亲
我们是一束光
黑澤ダイヤ
黒澤ダイヤ
LoveLive!音乐列表
Lovelive!事件年表
Lovelive!音乐列表
コドクの回廊
南太太
妮可的母亲
小鸟的母亲
矢泽妮可的母亲
黑澤ルビィ
黒澤ルビィ
NEURON,NEURON!!
ここで待ってるよ
夢☆ONCE AGAIN
大头抢镜
矢泽可可亚
矢泽可可罗
秘密と花園
羽は知ってしまったの
羽は知ってしまったの？
羽毛知道了
你的心灵是否光芒闪耀
君のこころは輝いてるかい？
喜欢你万岁!
愛してるばんざーい!
愛してるばんざーい！
爱上你万岁
爱上你万岁!
爱你万岁
爱你万岁!
爱你万岁!(PIANO MIX)
Aqours
Aqours☆HEROES
Go Go Lovelive 2015 Dream Sensation
HEART to HEART!
LoveLive! μ's Go→Go! LoveLive! 2015 〜Dream Sensation!〜
RADIO animelo mix LoveLive!~希绘里 Radio Garden~
RADIO animelo mix LoveLive 希绘里 Radio Garden
Step！ZERO to ONE
女性歌手(LoveLive!剧场版)
嵐のなかの恋だから
LoveLive!/剧场版动画
LoveLive! NEXT LoveLive! 2014 ENDLESS PARADE
LoveLive! The School idol Movie
LoveLive! μ's 3rd Anniversary LoveLive!
LoveLive部 Nico生课外活动
LoveLive部 Nico生课外活动~鸟果海~ & LoveLive部 Nico生课外活动~鸟果真姬~
Loveli Radio NicoRinPana
NEXT LoveLive 2014 ENDLESS PARADE
Nico生LoveLive! 新田 Fight Club
思い出以上になりたくて
Μ's →NEXT LoveLive! 2014 〜ENDLESS PARADE〜
優木あんじゅ
希果百宝箱
春情ロマンティック
真姬的母亲
穗乃果的母亲
綺羅ツバサ
西木野真姬的母亲
錯覚CROSSROADS
高坂穗乃果的母亲
Diamond Princess的忧郁(专辑)
Love marginal(专辑)
Moment ring
Snow halation(专辑)
不知道的Love 教给我吧Love(专辑)
夏色笑颜1,2,Jump!(专辑)
我们的LIVE 与你的LIFE(专辑)
海色少女に魅せられて
钻石公主的忧郁(专辑)
钻石公主的忧郁(单曲)
Memorial BOX I Solo Live! collection
Mermaid festa vol.2 ~Passionate~(专辑)
ことりLovin' you
ことりLovin' you(专辑)
ほんのり穗乃果色！
小鸟Lovin' you(专辑)
海色少女令人着迷(专辑)
淡淡的穗乃果色(专辑)
淡淡的穗乃果色！(专辑)
满怀“love”接近中!(专辑)
Soldier game(专辑)
Wonderful Rush(专辑)
一定能听见青春的乐章(专辑)
告白日和！(专辑)
如今的我们(专辑)
如今的我们(单曲)
少女式恋爱塾(专辑)
少女式恋爱塾(单曲)
我们活在当下(专辑)
这是，告白日和！(专辑)
Cutie Panther(专辑)
Memorial BOX II Solo Live! collection
Music S.T.A.R.T!!(专辑)
Pure girls project(专辑)
一定能听见青春(专辑)
从微热到Mystery(专辑)
无论何时一直(专辑)
梦想之门(专辑)
这就是我们的奇迹(专辑)
那就是我们的奇迹(专辑)
M是μ'sic的M(专辑)
M是μ'sic的M(单曲)
Shangri-La Shower(专辑)
Μ's Best Album Best Live! collection II
冬天给予的预感(专辑)
永远Friends(专辑)
秋之彼端路遥远(专辑)
秋之彼端路遥远(单曲)
秋天的你的遥远天空(专辑)
秋日彼端的遥远天空(专辑)
Angelic Angel Hello,数星星
HEART to HEART!(专辑)
SUNNY DAY SONG ?←HEARTBEAT
WAO-WAO Powerful day!(专辑)
さようならへさよなら
再会了再见
再会了再见!
想成为回忆以上的存在(专辑)
錯覚CROSSROADS(专辑)
错觉CROSSROADS(专辑)
Bibi
Lily white(LoveLive!)
LoveLive!翻唱
MOMENT RING(专辑)
さようならへさよなら!
一之濑茉莉香
克里斯蒂娜(LoveLive!学园偶像祭)
天使们的福音(专辑)
夜空はなんでも知ってるの？
夜空全都知道吗？
届かない星だとしても
待ってて愛のうた
恋になりたいAQUARIUM
恋になりたい AQUARIUM
恋欲水族馆
想在水族馆恋爱
等着爱的歌
艾玛·薇蒂
CYaRon
Endless Love 从未改变的友情
LoveLive!广播剧列表
ときめき分類学
トリコリコPLEASE!!
元气全开DAY!DAY!DAY!(专辑)
元気全开 DAY! DAY! DAY!
元気全開DAY! DAY! DAY!
心跳分类学
让我俘虏你的心PLEASE
CYaRon！
ダイスキだったらダイジョウブ！
ハミングフレンド
ユメ語るよりユメ歌おう
一生一念
从诉说梦想到歌唱梦想
你的心灵是否光芒闪耀(专辑)
你的心灵是否光芒闪耀？(专辑)
最喜欢的话就没问题
決めたよHand in Hand
Humming friend
LLer
Pops heartで踊るんだもん！
サンシャインぴっかぴか音頭
夢で夜空を照らしたい
想いよひとつになれ
拉拉人
未熟DREAMER
空も心も晴れるから
让我俘虏你的心PLEASE(专辑)
LoveLive!Sunshine!!/TV动画化作品
Strawberry Trapper(专辑)
ジングルベルがとまらない
不会停止的Jingle Bell
停不下来的Jingle Bell
停不下来的Jingle Bell(专辑)
圣日之祈祷
无法停止的Jingle Bell(专辑)
聖なる日の祈り
让我俘虏你的心PLEASE!!(专辑)
G線上のシンデレラ
Lovelive!Sunshine!!/动画化作品
Sailing to the Sunshine(专辑)
Thrilling one way
Μ's
Μ’s
想在AQUARIUM恋爱(专辑)
想在水族馆恋爱(专辑)
想在水族馆恋爱(单曲)
User:萌萌汤圆/Lovelive!Sunshine!!/动画化作品
HAPPY PARTY TRAIN(专辑)
LoveLive!学园偶像祭活动列表
LoveLive日服活动列表
P.S.の向こう側
下定决心Hand in Hand／最喜欢的话就没问题
与其诉说梦想，不如高歌梦想(专辑)
太陽を追いかけろ！
少女以上の恋がしたい
青空Jumping Heart(专辑)
音乃木坂学院
LoveLive! 学园偶像祭活动列表
Sweet Holiday 小鸟的点心
第1回 Challenge Festival
第1回 Medley Festival
第1回 Score Match
第2回 Medley Festival
第一次 Challenge Festival
第一次 Medley Festival
第一次 Score Match
第二次 Medley Festival
LoveLive!学园偶像祭/第一次 散步拉力活动
LoveLive!学园偶像祭/第一次 散步拉力赛活动
LoveLive!学园偶像祭/第一次 校园漫步关卡战
第1回 おさんぽラリー
第1回 散步拉力赛
第一次 散步拉力活动
第三次 Medley Festival
第二次 Challenge Festival
第二次 Score Match
第四次 Medley Festival
第七次 Medley Festival
第三次 Challenge Festival
第三次 Score Match
第九次 Medley Festival
第五次 Medley Festival
第八次 Medley Festival
第六次 Medley Festival
第十一次 Medley Festival
第十二次 Medley Festival
第十次 Medley Festival
忧郁的公主
怀抱明月 Love*Heart
我在海边等着你哦
无瑕的少女心
海岸通りで待ってるよ
理想中的我
第一次的Happy tune
第五次 Score Match
第四次 Score Match
闪耀吧 Can I do!
LoveLive!学园偶像祭/LoveLive!学园偶像祭礼包详情
LoveLive!学园偶像祭/不灭的热情
LoveLive!学园偶像祭/相互凝视的二人
LoveLive!学园偶像祭/相互对视的二人
LoveLive!学园偶像祭礼包详情
在不久的将来的Happy end
第四次 Challenge Festival
近未来Happy End
近未来Happy end
近未来ハッピーエンド
Aqours CLUB CD SET(专辑)
GALAXY HidE and SeeK(专辑)
Landing action Yeah!!(专辑)
コワレヤスキ
不久将来的Happy End(专辑)
别离开我 You are My Love
已无法分离 You are My Love
易碎之恋
易碎的爱
近未来Happy End(专辑)
LoveLive!学园偶像祭/如梦似幻的One night
LoveLive!学园偶像祭/已无法分离 You are My Love
LoveLive!学园偶像祭/第一次 好友MATCH
LoveLive!学园偶像祭/请给我一个Happy end
LoveLive!学园偶像祭/请给我一个快乐的结局
コワレヤスキ(专辑)
中須かすみ
優木せつ菜
易碎之恋(专辑)
脆弱易碎(专辑)
SUMMER VACATION(专辑)
地元愛♡満タン☆サマーライフ
夏の終わりの雨音が
夏への扉 Never end ver.
家乡之爱♡满满☆夏日时光
故乡爱 满载的 夏日生活
故乡爱♡满载的☆夏日生活
盛夏为谁所拥有?
盛夏是谁的东西?
真夏は誰のモノ？
LLAS
LoveLive!School Idol Festival Perfect Dream Project
LoveLive!学园偶像祭/第二次 散步拉力活动
LoveLive!学园偶像祭/第二次 散步拉力赛活动
LoveLive!虹之咲学园校园偶像同好会
Love Live! Nijigasaki High School Idol Club
PDP
Sifas
樱花雨
虹咲学园学园偶像同好会
LoveLive!School idol festival PERFECT Dream Project
LoveLive!学园偶像祭/努力的人最棒
MY舞☆TONIGHT
“MY LIST” to you!
你逢田姐当然会OO呀
勇气在哪?在你的内心!
勇気はどこに？君の胸に！
君の瞳を巡る冒険
未来の僕らは知ってるよ
未来の僕らは知ってるよ(专辑)
DROPOUT!?
LoveLive!学园偶像祭/恋爱也无妨喔
LoveLive!学园偶像祭/第二次 好友MATCH
MY舞☆TONIGHT／MIRACLE WAVE
おやすみなさん！
勇气在哪?在你的内心!(专辑)
勇気はどこに？君の胸に！(专辑)
大家晚安!
晚安大家!
未来的我们早已知晓(专辑)
Awaken the power(专辑)
Beginner’s Sailing
Journey to the Sunshine(专辑)
LoveLive!Sunshine!!/剧场版动画
LoveLive!Sunshine!! The School Idol Movie Over the Rainbow
LoveLive!学园偶像祭/おこりんぼ大会
LoveLive!学园偶像祭/第三次 好友MATCH
LoveLive!学园偶像祭/第三次 散步拉力
LoveLive!学园偶像祭/第四次 好友MATCH
爱与演唱会!阳光!!学园偶像电影:彩虹彼端
LoveLive!学园偶像祭/おんなじキモチなの
LoveLive!学园偶像祭/第五次 好友MATCH
Puchiguru
Puchiguru LoveLive!
SAKANAKANANDAKA?
さかなかなんだか？
ぷちぐるラブライブ！
是鱼吗，还是什么？
是鱼还是什么？
趴趴玩偶LoveLive
Aqours World Love Live! in LA ~Beyond the Pacific~
Hop Step Wai!(专辑)
Hop Step Whee!
キセキヒカル
サクラバイバイ
ホップ ステップ ワーイ！
卒業ですね
奇迹生辉
樱花Bye-Bye
樱花bye-bye
LoveLive!学园偶像祭/Guilty Eyesで 恋に落ちて
LoveLive!学园偶像祭/LoveLive!学园偶像祭游戏机制
LoveLive!学园偶像祭游戏机制
Memorial BOX III Solo Live! collection
Thank you, FRIENDS!!(专辑)
あなたの理想のヒロイン
みんなでスコアマッチ 历次活动与曲池
ダイアモンド
夢への一歩
Doki Pipo☆Emotion
LoveLive!学园偶像祭/LoveLive!学园偶像祭外部链接及参考资料
LoveLive!学园偶像祭/LoveLive!学园偶像祭歌曲列表
LoveLive!学园偶像祭/LoveLive!学园偶像祭活动介绍
LoveLive!学园偶像祭外部链接及参考资料
LoveLive!学园偶像祭歌曲列表
LoveLive!学园偶像祭活动介绍
めっちゃGoing!!
ドキピポ☆エモーション
眠れる森に行きたいな
LoveLive!学园偶像祭/また会える気がするからさ
LoveLive!学园偶像祭/助けてあげたい この歌で
Sailing to the Rainbow(专辑)
ハジマリロード
予測不可能Driving!
僕らの走ってきた道は…
僕らの走ってきた道は…／Next SPARKLING!!
开始的Road
逃走迷走メビウスループ
逃走迷走メビウスループ／Hop? Stop? Nonstop!
Jump up HIGH!!(专辑)
LoveLive!School idol festival PERFECT Dream Project/Love Live! Nijigasaki High School Idol Club First Live “with You”
LoveLive!School idol festival PERFECT Dream Project/虹咲学园学园偶像同好会 First Live “with You”
LoveLive! Fes
LoveLive!系列/LoveLive! Fest
☆Wonderland☆
冒険Type A, B, C!!
未体験HORIZON
未体验HORIZON(专辑)
KOKORO Magic "A to Z"
LoveLive!学园偶像祭/学园偶像祭感谢祭
SIF感谢祭
Teletelepathy
☆ワンダーランド☆
オードリー
テレテレパシー
友&愛
声繋ごうよ
学园偶像祭感谢祭
LoveLive!学园偶像祭/学园偶像祭感谢祭/学园偶像祭感谢祭2016
LoveLive!学园偶像祭/学园偶像祭感谢祭/学园偶像祭感谢祭2017
LoveLive!学园偶像祭/学园偶像祭感谢祭/学园偶像祭感谢祭2019
SIF感谢祭2016
SIF感谢祭2017
SIF感谢祭2019
学园偶像祭感谢祭2016
学园偶像祭感谢祭2017
学园偶像祭感谢祭2018
学园偶像祭感谢祭2019
Braveheart Coaster(专辑)
KOKORO Magic “A to Z”(专辑)
LoveLive!学园偶像祭/学园偶像祭感谢祭/学园偶像祭感谢祭2015
LoveLive!学园偶像祭/学园偶像祭感谢祭/学园偶像祭感谢祭2018
New Romantic Sailors(专辑)
SIF感谢祭2015
SIF感谢祭2018
コドク·テレポート
孤独teleport
学园偶像祭感谢祭2015
A ZU NA
Amazing Travel DNA(专辑)
Dream Land!Dream World!
Dream Land! Dream World!
Dream Land！Dream World！(专辑)
SUPER NOVA(专辑)
Sing & Smile!!(专辑)
Μ's Memorial CD-BOX “Complete BEST BOX”
Μ'ｓ Memorial CD-BOX「Complete BEST BOX」
メイズセカイ
AZUNA
なってしまった！
三船刊子
萌娘百科:页面存废/LoveLiveSongGai2/SIF
Template:Llsiftop
Template:Llhead
Template:LoveLive!收录曲目
Template:LoveLive!
Template:LoveLiveSongGai
Template:用户 LLer
Template:Lltop
Template:LoveLive!跨媒体展开
Template:Muse成员对她的称呼
Template:Muse成员对她的称呼/doc
Template:LoveLiveSunshine
Template:LoveLive!角色列表
Template:Llsstop
Template:LoveLive人物信息
Template:LoveLive人物信息/doc
Template:LLSIF属性
Template:LLSIF属性/doc
Template:LoveLiveSIF台词
Template:LoveLiveSIF台词/doc
Template:LoveLive!收录曲目/动画第一季
Template:LoveLive!收录曲目/动画第二季
Template:LoveLive!收录曲目/剧场版
Template:LoveLive!收录曲目/单曲
Template:LoveLive!收录曲目/迷你小队单曲
Template:LoveLive!收录曲目/其他歌曲
Template:LoveLive!收录曲目/独唱
Template:LoveLive!收录曲目/doc
Template:LoveLiveSongGai/doc
Template:LoveLiveSongGai/SIF
Template:LoveLiveSongGai/SIF/doc
Template:LoveLive!Sunshine!!曲目
Template:Llsshead
Template:LoveLive!/角色表述
Template:LoveLive!/角色表述/doc
Template:LoveLive!/系列音乐列表
Template:LoveLive!Sunshine!!跨媒体展开
Template:Editnotices/Page/LoveLive!Sunshine!!
Template:LoveLiveSongGai/SIFAC
Template:LoveLiveSongGai/SIFAC/doc
Template:LoveLive!SchoolIdolProject
Template:LoveLive卡片信息
Template:LoveLive卡片信息/doc
Template:LoveLive!学园偶像祭:导航
Template:Puchigurutop
Template:LoveLive!虹咲学园学园偶像同好会
Template:LoveLive!Sunshine!!曲目/单曲
Template:LoveLive!Sunshine!!曲目/迷你小队单曲
Template:LoveLive!Sunshine!!曲目/动画第一季
Template:LoveLive!Sunshine!!曲目/动画第二季
Template:LoveLive!Sunshine!!曲目/其他歌曲
Template:LoveLive!Sunshine!!曲目/剧场版
Template:Llseriestop
Template:LoveLive!学园偶像祭ALL STARS:导航
Template:Llnijigakutop
Template:LoveLive!虹咲学园学园偶像同好会曲目
Template:LoveLive!学园偶像祭系列
Template:LoveLive!/角色颜色
Template:用户 拉邦结派
Template:LoveLive!/角色颜色/doc
Template:LoveLiveSongGai/SIFAS
Template:LoveLiveSongGai/SIFAS/doc
Template talk:LoveLive!
Template talk:LoveLive!收录曲目
Template talk:LoveLive!NS!
Template talk:LoveLive!角色列表
Template talk:LoveLive人物信息
Template talk:LoveLiveSongGai
Template talk:LoveLiveSunshine
Template talk:LoveLiveSongGai/SIF
Template talk:LoveLive!SchoolIdolProject
Template talk:LoveLive卡片信息
Template talk:LoveLive!/角色颜色
Template talk:LoveLive!学园偶像祭
Template talk:LoveLiveSchoolIdolProject!
Template talk:LoveLive!Sunshine!!
Template:LoveLive!学园偶像祭
Template:用户 LL
Template:LLSIFCARD
Template:LoveLive!学园偶像祭/doc
Template:LoveLive!曲目
Template:LoveLiveSchoolIdolProject!
Template:LoveLive!Sunshine!!
Template:LoveLive学园偶像祭:导航
Template:LoveLive!School idol festival PERFECT Dream Project
Template:LoveLive!系列
Template:用户 拉帮结派
Template:LoveLiveSongGai3/SIFAC
User:Hamon002/LL系列歌曲中翻计划
User:妹空酱/Lovelive音乐
User:BlackHerrey/Test
User:BlackHerrey/Sandbox
User:Zyzsdy/Sandbox
User:东山奈央/LoveLive!收录曲目
User:可爱的琉璃月/ll音乐
User:可爱的琉璃月/ll演唱会
User:可爱的琉璃月/sif难度变动
User:可爱的琉璃月/沙盒存档
User:Eddie32/FinalLive
User:Eddie32/LoveLiveForever!
User:Bili hei/个人沙盒2
User:Zyzsdy/LLSS色卡
User:Bili hei/LoveLive staff转推
User:Aqours萌娘/君のこころは輝いてるかい
User:Zyzsdy/LLSS资源
User:Hanamarumaru/HAPPY PARTY TRAIN
User:あるゆな/Sandbox
User:胡祥又/想在AQUARIUM恋爱应援
User:田中琴叶/我对某些LLer的一点看法
User:HoshinoSaika/Sandbox
User:HoshinoSaika/Sandbox1
User:HoshinoSaika/LLsong
User:HoshinoSaika/Sandbox3
User:HoshinoSaika/Sandbox5
User:Bbbbbbbbba/Love Novels（Lyrica Live）
User:Lsrxzz000/Sandbox
User:Nzh21/Sandbox/1
User:TBB000623/Lovelive学园偶像祭国服礼包
User:胡祥又/萌娘百科LoveLive!系列编辑部
User:Sanry/List"""

attr=""

pagetitlelist=inputtitlelist.splitlines()

n_all=0

def devide(l:list,n:int)->list:
	for i in range(0,len(l),n):
		yield l[i:i+n]

def isResponceOK(json:dict)->bool:
	if 'batchcomplete' in json:
		return True
	else:
		print("Responce is not complete.")
		return False

deletedpages=set()

input("Enter to start.")
start_time=time.time()
print("started at",time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(start_time)))

for pagetitlelist_d in devide(pagetitlelist,10):
	l_param:str="|".join(str(i) for i in pagetitlelist_d)
	titleset=set()
	while True:
		try:
			a=requests.get(url,params={**params,**{'titles':l_param}},timeout=(10,30))
		except:
			print(".",end="")
			continue
		else:
			json:dict=a.json()
			break
	if not isResponceOK(json):
		break
	for pageid in json['query']['pageids']:
		if 'missing' in json['query']['pages'][pageid]:
			pass
		else:
			title=json['query']['pages'][pageid]['title']
			print(attr,pageid,title,sep="\t")
			n_all+=1
			titleset.add(title)
	deletedpages.update(set(pagetitlelist_d)-titleset)

print()
end_time=time.time()
print("ended   at",time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(end_time)))
print(second2days.main(end_time-start_time),"spent.")
print(n_all,"/",len(pagetitlelist))
if len(pagetitlelist)>n_all:
	print("deleted:",deletedpages)

input("Done.")
