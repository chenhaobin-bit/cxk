fangjian = {
    "门厅" : {
        "name":"门厅",
        "juqing":"你身处古堡的阴暗⻔厅。头顶⼀盏布满蜘蛛⽹的吊灯微微摇晃，投下忽明忽暗的光芒。空⽓中弥漫着潮湿的霉味，脚下是冰冷的⼤理⽯地⾯。北⾯是⼀扇沉重的橡⽊⻔，⻔上雕刻着狰狞的怪兽头像，东⾯则是⼀条通向⿊暗深处的⾛廊。",
        "lu": {"北":"大厅", "东": "走廊"},
        "wupin" : [{'name': '门厅地毯下的纸条','juqing': "⼀张陈旧的纸条，似乎是从某本书⻚上撕下来的，上⾯潦草地写着 ‘光芒指引⽅向’。" }],
    },
    "大厅" : {
        "name":"大厅",
        "juqing":"你推开橡⽊⻔，进⼊了古堡的宏伟的⼤厅。尽管岁⽉流逝，依稀可⻅昔⽇的辉煌。⼀个巨⼤的⽔晶吊灯（虽然已经缺了⼏盏灯泡）仍然悬挂在⾼耸的天花板上。彩⾊玻璃窗阻挡了外界的光线，使得⼤厅内光线昏暗。南⾯是你进来的⻔厅，⻄⾯是⼀扇装饰华丽的⽊⻔，通往图书馆，东⾯则是⼀道拱形⽯⻔，通向餐厅。",
        "lu": {"南":"门厅", "西": "图书馆","东": "餐厅"},
        "wupin" : [{'name': '壁炉拔火棍','juqing': "⼀根沉重的铁制拨⽕棍，顶端装饰着狮⼦头。" }],
    },
    "走廊" : {
        "name":"走廊",
        "juqing":"你沿着昏暗的⾛廊前⾏，脚踩在吱吱作响的⽊地板上。墙壁上挂着褪⾊的家族画像，画像中的⼈物表情模糊不清，仿佛在注视着你。⾛廊尽头似乎传来微弱的滴⽔声。⻄⾯是⻔厅。",
        "lu": {"西":"门厅"},
        "wupin" : [{'name': '生锈的铁钥匙','juqing': "⼀把锈迹斑斑的铁钥匙，看起来年代久远，也许能打开古堡的某扇门。" }],
    },
    "图书馆" : {
        "name":"图书馆",
        "juqing":"你推开装饰华丽的⽊⻔，⾛进了布满灰尘的图书馆。⾼耸的书架⼀直延伸到天花板，上⾯堆满了布满灰尘的书籍。空⽓中弥漫着浓重的旧书和⽪⾰的味道，令⼈昏昏欲睡。阳光透过⾼窗洒进来，照亮了书架上零星散落的⾦箔。东⾯是通往⼤厅的⽊⻔。",
        "lu": {"东":"大厅"},
        "wupin" : [{'name': '一本皮面精装的古书','juqing': "⼀本⽪⾯精装的古书，书⻚已经泛⻩，封⾯上⽤难以辨认的⽂字写着书名。翻开书⻚，⾥⾯似乎是关于古堡历史的记载。" }],
    },
    "餐厅" : {
        "name":"餐厅",
        "juqing":"你穿过拱形⽯⻔，来到了宽敞的餐厅。⻓⻓的橡⽊餐桌上布满了厚厚的灰尘，锈迹斑斑的银质餐具散落在桌⾯上，仿佛⼀场盛宴突然中断。墙壁上挂着巨⼤的狩猎场景油画，画布已经开始剥落。⻄⾯是通往⼤厅的拱形⽯⻔，北⾯是⼀扇破旧的⽊⻔，通向厨房。",
        "lu": {"西":"大厅", "北": "厨房"},
        "wupin" : [{'name': '餐桌上的银色烛台','juqing': "⼀个精致的银⾊烛台，上⾯镶嵌着⼀些宝⽯，但⼤部分已经脱落。" }],
    },    
    "厨房" : {
        "name":"厨房",
        "juqing":"“你推开破旧的⽊⻔，进⼊了阴冷潮湿的厨房。腐烂的⽓味扑⿐⽽来，令⼈作呕。⽣锈的厨具散落在各处，巨⼤的壁炉已经冰冷，炉膛⾥堆满了⿊⾊的灰烬。南⾯是餐厅。地板中央，你注意到⼀块不寻常的⽊板，似乎可以移动，也许是⼀个隐蔽的活板⻔，通往地下。",
        "lu": {"南":"餐厅", "下": "隐藏出口"},
        "wupin" : [{'name': '壁炉旁的⽕柴','juqing': "⼀盒潮湿的⽕柴，看起来还能⽤，也许可以点燃什么。" },
                   {'name': '水桶', 'description': '一个破旧的木水桶，里面积满了浑浊的雨水。'},
                   ],
    },

}

'''帮助指令'''
def get_help():
    print("可用指令：")
    print("help: 显示帮助信息")
    print("look: 查看当前房间的详细描述")
    print("go【方向】: 向指定方向移动 ")
    print("take[物品名称]: 拾取房间内物品")
    print("inventory: 查看背包中物品")
    print("quit: 退出游戏")


'''当前房间'''
def get_look(wuzi):
    print(f"{wuzi['name']}")
    print(wuzi["juqing"])
    if wuzi["wupin"]:
        print("房间里有:")
        for dongxi in wuzi["wupin"]:
            print(f"{dongxi['name']}:{dongxi['juqing']}")
    else:
        print("房间里没有明显的物品")
    print("可通往的方向:")
    for fangxiang,mingcheng in wuzi["lu"].items():
        print(f"{fangxiang} -> {mingcheng}")

    '''移动指令'''
def get_go(fx,wuzi):
    for fangxiang,xinwu in fangjian[wuzi]["lu"].items():
        if xinwu == fx:
            print(f"你进入了{xinwu}")
            return xinwu
        elif fangxiang == "下" and fx =="down":
            return "down"
    print("那边没有路")
    return wuzi
    
def get_take(mingcheng,wuzi,beibao):
    wupin1 = fangjian[wuzi]["wupin"]
    for i in wupin1:
        if i["name"] == mingcheng:
            print(f"你拿起了{i['name']}")
            beibao.append(i)
            wupin1.remove(i)
            return
    print("这里什么都没有孩子")

def get_inventory(beibao):
    if not beibao:
        print("你的背包是空的")
    else:
        print("你的背包里有：")
        for i in beibao:
            print(f"{i['name']}")


    
def main():
    chushi = "门厅"
    beibao1 = []
    get_look(fangjian[chushi])
    cxk = True
    while cxk:
        control = input("")
        if control == "help":
            get_help()
        elif control == "look":
            get_look(fangjian[chushi])
        elif control.startswith("go "):
            jjboy = control[3:].strip()
            xinwu = get_go(jjboy,chushi)
            chushi = xinwu
            if xinwu == "down":
                print("你逃出了古堡！")
                return None
            else:
                get_look(fangjian[chushi])
        elif control.startswith("take "):
            wupin = control[5:].strip()
            get_take(wupin,chushi,beibao1)
        elif control == "inventory":
            get_inventory(beibao1)
        elif control == "quit":
            cxk = False
        else:
            print("无效的指令！！！")

main()