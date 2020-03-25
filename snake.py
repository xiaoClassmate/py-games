#---sys 系統相關的參數以及函式，python標準函式庫 
import pygame,sys,time,random 
from pygame.locals import *

#---定義顏色(R,G,B)
redColor = pygame.Color(255,0,0)
blackColor = pygame.Color(0,0,0)
whiteColor = pygame.Color(255,255,255)

#---定義遊戲結束
def gameOver():
    pygame.quit()
    sys.exit()

#---定義主函數及各種初始化
def main():
    pygame.init() # 遊戲初始化
    fpsClock = pygame.time.Clock() # 控制幀數率，每個循環多久時間運行一次
    playSurface = pygame.display.set_mode((640,480)) # 創建窗口，即顯示(width, height)    
    pygame.display.set_caption('貪食蛇')
    snakePosition = [80,100] # snake 起始位置
    snakeBody = [[80,100],[100,100],[120,100]] # snake 大小，每個方塊 20x20
    targetPosition = [300,300] # 目標起始位置
    targetFlag = 1 # 判斷目標是否被吃掉
    direction = 'right' # 起始方向
    changeDirection = direction # 設定後來要變更的方向
    
    #---檢查鍵盤事件
    while True:
        for event in pygame.event.get(): # event.get() 處理所有事件
            if event.type == QUIT: # 如果我什麼也沒按，
                pygame.quit() # ---| 貪食蛇自然會走到邊界，
                sys.exit()    # ---| 然後 Game Over ~

            #---判斷鍵盤事件
            elif event.type == KEYDOWN: # 有什麼鍵被我按下了
                if event.key == K_RIGHT: # 假設我按的鍵是右邊
                    changeDirection = 'right'# 那就讓方向變成右邊，下面以此類推
                if event.key == K_LEFT:
                    changeDirection = 'left'
                if event.key == K_UP:
                    changeDirection = 'up'
                if event.key == K_DOWN:
                    changeDirection = 'down'
                if event.key == K_ESCAPE: # 假設 ESC 被按下
                    pygame.event.post(pygame.event.Event(QUIT)) # event.post() 添加名為 QUIT 事件

        #---判斷是否為反方向
        if changeDirection == 'right' and not direction == 'left':
            direction = changeDirection
        if changeDirection == 'left' and not direction == 'right':
            direction = changeDirection
        if changeDirection == 'up' and not direction == 'down':
            direction = changeDirection
        if changeDirection == 'down' and not direction == 'up':
            direction = changeDirection

        #---移動，[0] 為 x 軸 ; [1] 為 y 軸
        if direction == 'right':
            snakePosition[0] += 20
        if direction == 'left':
            snakePosition[0] -= 20
        if direction == 'up':
            snakePosition[1] -= 20
        if direction == 'down':
            snakePosition[1] += 20

        #---增加長度
        snakeBody.insert(0,list(snakePosition))

        #---判斷重疊
        if snakePosition[0] == targetPosition[0] and snakePosition[1] == targetPosition[1]:
            targetFlag = 0 # 蛇與目標重疊，表示被吃掉
        else:
            snakeBody.pop()

        #---隨機生成
        if targetFlag == 0:
            x = random.randrange(1,32)
            y = random.randrange(1,24)
            targetPosition = [int(x*20),int(y*20)]
            targetFlag = 1

        #---繪製邊界
        playSurface.fill(blackColour)
        for position in snakeBody:
        # 繪製幾何圖形 pygame.draw.rect(畫布, 顏色, [x坐標, y坐標, 寬度, 高度])
            pygame.draw.rect(playSurface,whiteColour,Rect(position[0],position[1],20,20))
            pygame.draw.rect(playSurface,redColour,Rect(targetPosition[0], targetPosition[1],20,20))

        #---刷新顯示
        pygame.display.flip()

        #---超越邊界
        if snakePosition[0] > 620 or snakePosition[0] < 0:
            gameOver(playSurface)
        if snakePosition[1] > 460 or snakePosition[1] < 0:
            for snakeBody in snakeBody[1:]:
                if snakePosition[0] == snakeBody[0] and snakePosition[1] == snakeBody[1]:
                    gameOver(playSurface)

        #---遊戲速度                
        fpsClock.tick(10)

#---啟動遊戲
if __name__ == '__main__':
    main()