import random
#导入random库
import pygame
# 导入pygame库
from pygame.locals import *
# 导入一些常用的函数和常量
from sys import exit
# 向sys模块借一个exit函数用来退出程序

BLUE = (0, 0, 255, 255)
GRAY = (88, 87, 86, 255)
WHITE = (255, 255, 255, 255)
BLACK = (0, 0, 0, 0)
#定义颜色

WIDTH  = 600
HEIGHT = 600
GRID_WIDTH = 20
#设置窗口的宽和高以及网格宽

SCREEN = []
#图形的人种分布


def draw_background(surf):

    #画出边框
    rect_lines = [
        ((GRID_WIDTH, GRID_WIDTH), (GRID_WIDTH, HEIGHT - GRID_WIDTH)),
        ((GRID_WIDTH, GRID_WIDTH), (WIDTH - GRID_WIDTH, GRID_WIDTH)),
        ((GRID_WIDTH, HEIGHT - GRID_WIDTH),
         (WIDTH - GRID_WIDTH, HEIGHT - GRID_WIDTH)),
        ((WIDTH - GRID_WIDTH, GRID_WIDTH),
         (WIDTH - GRID_WIDTH, HEIGHT - GRID_WIDTH)),
    ]
    for line in rect_lines:
        pygame.draw.line(surf, BLACK, line[0], line[1], 2)

    # 画出中间的网格线
    for i in range(int(WIDTH / GRID_WIDTH) - 3):
        pygame.draw.line(surf, BLACK,
                         (GRID_WIDTH * (2 + i), GRID_WIDTH),
                         (GRID_WIDTH * (2 + i), HEIGHT - GRID_WIDTH))
        pygame.draw.line(surf, BLACK,
                         (GRID_WIDTH, GRID_WIDTH * (2 + i)),
                         (HEIGHT - GRID_WIDTH, GRID_WIDTH * (2 + i)))

#更新背景
def update_background(surf , rec):
    #填充颜色
    for i in range(int(len(rec))):
        for j in range(len(rec[i])):
            if(rec[i][j] == 4):
                pygame.draw.rect(surf, GRAY, ((GRID_WIDTH * (1 + i), GRID_WIDTH * (1 + j)), (GRID_WIDTH, GRID_WIDTH)))
            elif(rec[i][j] == 0.05):
                pygame.draw.rect(surf, BLUE, ((GRID_WIDTH * (1 + i), GRID_WIDTH * (1 + j)), (GRID_WIDTH, GRID_WIDTH)))
            else:
                pygame.draw.rect(surf, WHITE, ((GRID_WIDTH * (1 + i), GRID_WIDTH * (1 + j)), (GRID_WIDTH, GRID_WIDTH)))
    # 画网格
    draw_background(surf)

#初始化人种分布
def init_rec(rec):
    rec = [[4 if random.random() > 0.777 else 0.05 if random.random() < 0.222 else 1 for i in range
    (int(WIDTH / GRID_WIDTH) - 2)] for j in range(int(HEIGHT / GRID_WIDTH) - 2)]
    return rec

#更新人群居住
def update_rec(rec):
    #循环遍历
    a = 0
    count = 0
    #计数器和是否搬迁
    for i in range(int(len(rec))):
        for j in range(len(rec[i])):
            if(i == 0 and j == 0 and rec[i][j] != 1):
                if(rec[i][j + 1] != rec[i][j] or rec[i + 1][j] != rec[i][j] or rec[i + 1][j + 1] != rec[i][j]):
                    a = 1
            elif(i == 0 and j == (len(rec[i])- 1) and rec[i][j] != 1):
                if (rec[i][j - 1] != rec[i][j] or rec[i + 1][j] != rec[i][j] or rec[i + 1][j - 1] != rec[i][j]):
                    a = 1
            elif(i == (len(rec) - 1) and j == 0 and rec[i][j] != 1):
                if (rec[i - 1][j] != rec[i][j] or rec[i][j + 1] != rec[i][j] or rec[i - 1][j + 1] != rec[i][j]):
                    a = 1
            elif(i == (len(rec) - 1) and j ==(len(rec[i]) - 1) and rec[i][j] != 1):
                if (rec[i - 1][j] != rec[i][j] or rec[i][j - 1] != rec[i][j] or rec[i - 1][j - 1] != rec[i][j]):
                    a = 1
            #四个角上的点
            elif(i == 0 and rec[i][j] != 1):
                if(rec[i][j] == 0.05):
                    if (rec[i][j - 1] * rec[i][j + 1] * rec[i + 1][j - 1] * rec[i + 1][j] * rec[i + 1][j + 1] > 0.002):
                        a = 1
                else:
                    if(rec[i][j - 1] + rec[i][j + 1] + rec[i + 1][j - 1] + rec[i + 1][j] + rec[i + 1][j + 1] < 12):
                        a=1
            elif (i == (len(rec) - 1) and rec[i][j] != 1):
                if (rec[i][j] == 0.05):
                    if (rec[i][j - 1] * rec[i][j + 1] * rec[i - 1][j - 1] * rec[i - 1][j] * rec[i - 1][j + 1] > 0.002):
                        a = 1
                else:
                    if (rec[i][j - 1] + rec[i][j + 1] + rec[i - 1][j - 1] + rec[i - 1][j] + rec[i - 1][j + 1] < 12):
                        a = 1
            elif (j == 0 and rec[i][j] != 1):
                if (rec[i][j] == 0.05):
                    if (rec[i - 1][j] * rec[i + 1][j] * rec[i - 1][j + 1] * rec[i][j + 1] * rec[i + 1][j + 1] > 0.002):
                        a = 1
                else:
                    if (rec[i - 1][j] + rec[i + 1][j] + rec[i - 1][j + 1] + rec[i][j + 1] + rec[i + 1][j + 1] < 12):
                        a = 1
            elif (j == (len(rec[i]) - 1) and rec[i][j] != 1):
                if (rec[i][j] == 0.05):
                    if (rec[i - 1][j] * rec[i + 1][j] * rec[i - 1][j - 1] * rec[i][j - 1] * rec[i + 1][j - 1] > 0.002):
                        a = 1
                else:
                    if (rec[i - 1][j] + rec[i + 1][j] + rec[i - 1][j - 1] + rec[i][j - 1] + rec[i + 1][j - 1] < 12):
                        a = 1
            #四边上的点
            elif(rec[i][j] != 1):
                if(rec[i - 1][j - 1] / rec[i][j] == 1):
                    count = count + 1
                if(rec[i - 1][j] / rec[i][j] == 1):
                    count = count + 1
                if (rec[i - 1][j + 1] / rec[i][j] == 1):
                    count = count + 1
                if (rec[i][j - 1] / rec[i][j] == 1):
                    count = count + 1
                if (rec[i][j + 1] / rec[i][j] == 1):
                    count = count + 1
                if (rec[i + 1][j - 1] / rec[i][j] == 1):
                    count = count + 1
                if (rec[i + 1][j] / rec[i][j] == 1):
                    count = count + 1
                if (rec[i + 1][j + 1] / rec[i][j] == 1):
                    count = count + 1
            if(count < 3):
                a = 1
            #中间的点
            if(a == 1):
                #随机在无人地找家
                while True:
                    new_home = random.randint(0, len(rec)*len(rec[i]) - 1)
                    if (rec[int(new_home / len(rec))][new_home % len(rec[i])] == 1):
                        rec[int(new_home / len(rec))][new_home % len(rec[i])] = rec[i][j]
                        break
                rec[i][j] = 1
                #reccove[i][j] =0
                a = 0
                count =0
            #搬迁
            else:
                a = 0
                count = 0
            #不搬迁

    return rec
    #返回更新后的人群


pygame.init()
# 初始化pygame,为使用硬件做准备

screen = pygame.display.set_mode((WIDTH, HEIGHT))
# 创建了一个窗口
pygame.display.set_caption("Human-Life")
# 设置窗口标题

SCREEN = init_rec(SCREEN)
#初始化人群

while True:
    # 主循环

    # 设置屏幕间隔
    pygame.time.wait(1500)

    screen.fill(WHITE)
    #将背景设置成白色
    draw_background(screen)
    # 画出网格

    for event in pygame.event.get():
        if event.type == QUIT:
            # 接收到退出事件后退出程序
            exit()

    SCREEN = update_rec(SCREEN)

    update_background(screen, SCREEN)
    #实现背景的绘画

    pygame.display.update()
    # 刷新一下画面
