import pygame
import os.path


set_win = {"WIDTH" : 800,
           "HEIGHT" : 500,
           "FPS" : 60}
abs_path = os.path.abspath(__file__ + "/..") + "\\image\\"


bg_tennis_image = pygame.transform.scale(pygame.image.load(abs_path + "bg_tennis.png"), (800, 700))
