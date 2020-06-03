'''
打飞机项目
显示背景

'''

import pygame

if __name__ =='__main__':

    screen = pygame.display.set_mode((480,890),0,32)

    bgImageFile='./sucai/background.png'

    background=pygame.image.load(bgImageFile).convert()

'''
1.显示背景
    screen.blit(background,(0,0))
    pygame.display.update()

'''
while True:
    screen.blit(background,(0,0))
    pygame.display.update()

