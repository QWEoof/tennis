import pygame
import os.path


set_win = {"WIDTH" : 800,
           "HEIGHT" : 500,
           "FPS" : 60}
set_ball = {"RADIUS" : 20,
            "SPEED" : 8}
set_board = {"HEIGHT" : 250}

start_game = {"LEFT_PLAYER" : (15, set_win["HEIGHT"] // 2 - set_board["HEIGHT"] // 2, 20, set_board["HEIGHT"]),
              "RIGHT_PLAYER" : (set_win["WIDTH"] - 20 - 15, set_win["HEIGHT"] // 2 - set_board["HEIGHT"] // 2, 20, 250),
              "BALL" : {
                    "LEFT_PLAYER" : (set_win["WIDTH"] // 2, set_win["HEIGHT"]//2),
                    "RIGHT_PLAYER" : (set_win["WIDTH"] // 2, set_win["HEIGHT"]//2)
              }}
set_button = {"WIDTH" : 200,
              "HEIGHT" : 75,}
button_list = list()
abs_path = os.path.abspath(__file__ + "/..") + "\\image\\"


bg_tennis_image = pygame.transform.scale(pygame.image.load(abs_path + "bg_tennis.png"), (800, 700))
