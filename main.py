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
    player1 = Board(start_game["LEFT_PLAYER"][0], start_game["LEFT_PLAYER"][1], start_game["LEFT_PLAYER"][2], start_game["LEFT_PLAYER"][3], None, 5)
    player2 = Board(start_game["RIGHT_PLAYER"][0],start_game["RIGHT_PLAYER"][1] , start_game["RIGHT_PLAYER"][2] , start_game["RIGHT_PLAYER"][3], None, 5)
    ball = Ball(350, 250, 20, (255, 0, 0), None, choice([-5, 5]))
    button_list.append(pygame.Rect(set_win["WIDTH"] // 2 - set_button["WIDTH"] // 2, 
                                   set_win["HEIGHT"] // 2 - set_button["HEIGHT"] - 55, set_button["WIDTH"], set_button["HEIGHT"]))
    button_list.append(pygame.Rect(set_win["WIDTH"] // 2 - set_button["WIDTH"] // 2, 
                                   set_win["HEIGHT"] // 2 - set_button["HEIGHT"] + 75, set_button["WIDTH"], set_button["HEIGHT"]))
    button_list.append(pygame.font.Font(None, 40))
    button_list.append(pygame.font.Font(None, 40))
    while game:
        window.blit(bg_tennis_image, (0,0))
        pygame.draw.rect(window, (255,0,0), player1)
        pygame.draw.rect(window, (0, 0, 255), player2)
        pygame.draw.circle(window, ball.COLOR, (ball.X, ball.Y), ball.RADIUS)
        player1.move()
        player2.move()
        
        win_lose_score(window, ball, player1, player2)
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
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos
                if button_list[0].collidepoint(x, y):
                    start(ball, player1, player2)
                elif button_list[1].collidepoint(x, y):
                    game = False        
        clock.tick(60)
        pygame.display.flip()

run()
