import sys
import pygame

# 初始化
pygame.init()
# 建立 window 視窗，size = 800x600
window_surface = pygame.display.set_mode((800,600))
# 設定標題為 Hello World
pygame.display.set_caption('Hello World')
# 清除畫面並填滿背景色
window_surface.fill((255, 255, 255))
# 事件迴圈監聽事件，進行事件處理
while True:
    # 迭代整個事件迴圈，若有符合事件則對應處理
    for event in pygame.event.get():
        # 當使用者結束視窗，程式也結束
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
