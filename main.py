import pygame
import Bottom #Bottom.py
import Ball
pygame.init()

screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("打磚塊遊戲")
#初始化底版
bottom = Bottom.Bottom(400,550,100,30)

#初始化球
ball = Ball.Ball(bottom)

white = (255,255,255)
screen.fill(white)
pygame.display.update()
mouse_x = 0
gameRun = True
while gameRun:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameRun = False
        if event.type == pygame.MOUSEMOTION:
            #滑鼠移動事件
            #pygame.mouse.get_pos()取得當前滑鼠座標
            #回傳 (x, y)
            mouse_x = pygame.mouse.get_pos()[0]
            bottom.move(mouse_x - bottom.w/2)
            ball.move(mouse_x)
        if event.type == pygame.MOUSEBUTTONDOWN:
            ball.status = 1 #從wait -> run
    ball.move(mouse_x) #為了每一幀的移動
    screen.fill(white)
    #畫底版
    pygame.draw.rect(screen,
                     (255,0,0),
                     [bottom.x,
                      bottom.y,
                      bottom.w,
                      bottom.h],
                     0)
    pygame.draw.circle(screen,
                       (255,0,255),
                       [ball.x,
                        ball.y],
                       ball.r,
                       0)
    pygame.display.update()
pygame.quit()
