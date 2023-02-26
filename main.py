import pygame
from game_object import *
from data import *
from random import choice

pygame.init()


window = pygame.display.set_mode((set_win["WIDTH"], set_win["HEIGHT"]))
pygame.display.set_caption("Ping-Pong")

def run():
    game = True
    clock = pygame.time.Clock()
    player1 = Board(50, 250, 20, 100, None, 5)
    player2 = Board(750, 250, 20 , 100, None, 5)
    ball = Ball(350, 250, 20, (255, 0, 0), None, choice([-5, 5]))



    while game:
        window.blit(bg_tennis_image, (0,0))
        pygame.draw.rect(window, (255,0,0), player1)
        pygame.draw.rect(window, (0, 0, 255), player2)
        pygame.draw.circle(window, ball.COLOR, (ball.X, ball.Y), ball.RADIUS)
        player1.move()
        player2.move()
        print(ball.SPEED)
        if ball.DIRECTION:
            ball.move(player1)
        else:
            ball.move(player2)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    player1.MOVE["UP"] = True
                if event.key == pygame.K_s:
                    player1.MOVE["DOWN"] = True
                if event.key == pygame.K_UP:
                    player2.MOVE["UP"] = True
                if event.key == pygame.K_DOWN:
                    player2.MOVE["DOWN"] = True
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    player1.MOVE["UP"] = False
                if event.key == pygame.K_s:
                    player1.MOVE["DOWN"] = False
                if event.key == pygame.K_UP:
                    player2.MOVE["UP"] = False
                if event.key == pygame.K_DOWN:
                    player2.MOVE["DOWN"] = False

        
        clock.tick(60)
        pygame.display.flip()

run()
