#--coding:utf-8--
import pygame,sys
import pygame.freetype  # 绘制文字的增强库
import io
# 初始化

pygame.init()
# 1.窗体设置
size=width,height=1000,700 # 通过函数传递参数 设置固定的窗口大小
screen=pygame.display.set_mode(size)    # 创建窗口
# 2.背景图片的设置
BLACK=0,0,0 # 通过函数传递参数 设置窗口背景颜色
screen.fill(BLACK)  # 设置窗口背景颜色
background=pygame.image.load("corsairBACKGROUND.jpg")   # 载入图片
screen.blit(background,(0,0))
   # 把图片background放到（0,0）的位置
# 3.窗体标题栏的设置
# 4.矩形框的设置
'''
r1POS=0,50,500,100  # r1rect矩形框的左上角坐标x,y,矩形框的宽度，高度
r1WIDTH=0   # 矩形的边框宽度。0表示填充矩形
r1rect=pygame.draw.rect(screen,GREEN,r1POS,r1WIDTH)
'''
# 5.文字的设置
BLACK=0,0,0
WHITE=255,255,255
GREEN=95,171,84
micFONT=pygame.freetype.Font('C://Windows//Fonts//simhei.ttf',18)  # 字体路径，字体大小
# 6. 读文件
file_dialog=io.open("dialog.txt",encoding='utf-8')
option1=io.open("option1.txt",encoding='utf-8')
option2=io.open("option2.txt",encoding='utf-8')
option3=io.open("option3.txt",encoding='utf-8')
#text类
class Text():
    #role为指定的角色的名称，这里我用的是int类型，后面可直接改为角色名即string类型，poition为角色显示的位置，0为左边，1为中间，2为右边
    #filename是打开的文件的名称，因为可能有对话的文件和旁白什么的
    def __init__(self,role,position,filename):
        choicePOS = [70, 531] #对话出现的位置
        self.role = role
        self.position = role
        src = 'lh0'
        role=src+str(role)+".png" #角色图片的相对路径
        role_pic=pygame.image.load(role) #加载图片
        diag = pygame.image.load("diag_board.jpg")
        if position==0:
            role_position=0
        elif position==1:
            role_position = 400
        elif position == 2:
            role_position = 700
        screen.blit(role_pic, (role_position, 0)) #显示角色图片
        screen.blit(diag, (40, 500)) #显示对话
        while True:
            content = filename.readline() #按行读取文本内容
            content = content.strip('\n') #去掉换行符号
            if content == "##": #当读到##时停止
                print(content)
                break
            wordRect1 = micFONT.render_to(screen, choicePOS, content, fgcolor=BLACK, size=30) #输出读到的内容
            choicePOS[1]=choicePOS[1]+30




#事件处理
#此结构要换！！！否则一次只能读取一个事件，很难后续操作
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT: # 用户按下了结束键
            sys.exit()
        elif event.type==pygame.MOUSEBUTTONDOWN:
            text = Text(1, 0,file_dialog)
        # 说明：用户输入A/B/C选择选项
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_a :
                print("A choice")
                text = Text(2, 1,option1)
            elif event.key==pygame.K_b:
                print("B choice")
                text = Text(3, 2,option2)
            elif event.key==pygame.K_c:
                print("C choise")
                text = Text(4, 2,option3)
        elif event.type==pygame.MOUSEMOTION:    # 设计时用鼠标获得当前位置，定位用
            print("[MOUSEMOTION]:",event.pos,event.rel,event.buttons)
        elif event.type==pygame.MOUSEBUTTONUP:  # 设计时用鼠标获得当前位置，定位用
            print("[MOUSEBUTTONUP]:",event.pos,event.button)
        elif event.type==pygame.MOUSEBUTTONDOWN:    # 设计时用鼠标获得当前位置，定位用
            print("[MOUSEBUTTONDOWN]:",event.pos,event.button)
    pygame.display.update() # 显示图片
