#setup.py

#Imports:
from math import *
import pygame
import random

#Variáveis relacionadas à tela:
size_tela_x = 720  # largura da tela
size_tela_y = 576  # altura da tela

#Variáveis relacionadas à bola:
raio = 12  # raio da bola
ball_pos_x = size_tela_x/2  # posição x inicial da bola
ball_pos_y = size_tela_x/2  # posição y inicial da bola
ball_speed_start = [
    (24 + 3*sqrt(2), 14),
    (24 + 3*sqrt(2), -14),
    (-19, -6*sqrt(3)),
    (-19, 6*sqrt(3)),
    (27, 0)
]  # velocidades iniciais da bola
ball_speed_x , ball_speed_y = random.choice(ball_speed_start) #Velocidades atuais da bola
ball_color = (255, 255, 255)  # cor da bola
lost_ball_speed_x, lost_ball_speed_y = 0, 0  # velocidade perdida da bola
delta_ball_speed = False  # indicador de mudança na velocidade da bola


#Variáveis relacionadas às raquetes:
racket_size_x = 10  # largura da raquete
racket_size_y = 50  # altura da raquete
racket_color_a = (255, 255, 255)  # cor da raquete A
racket_color_b = (255, 255, 255)  # cor da raquete B
racket_pos_a_x = 0  # posição x da raquete A
racket_pos_a_y = size_tela_y / 2  # posição y inicial da raquete A
racket_pos_b_x = size_tela_x - racket_size_x  # posição x da raquete B
racket_pos_b_y = (size_tela_y / 2) - (racket_size_y / 2)  # posição y inicial da raquete B
racket_vel_b = 0  # velocidade atual da raquete B
racket_vel_a = 0  # velocidade atual da raquete A
racket_acel_a = 0.01  # aceleração da raquete A
racket_acel_b = 0.01  # aceleração da raquete B
racket_vel_max_a = 6  # velocidade máxima da raquete A
racket_vel_max_b = 6  # velocidade máxima da raquete B
decay_rate = 0.1  # taxa de decaimento da velocidade da raquete
collision_y = 0  # posição y da colisão da raquete

#Variáveis relacionadas à pontuação:
score_a = 0  # pontuação do jogador A
score_b = 0  # pontuação do jogador B
score_value_color = (255, 255, 255)  # cor do valor da pontuação

#Variáveis relacionadas às linhas de divisão:
size_strokes_division_x = 5  # largura das linhas de divisão
n_strokes = 20  # número de pontos nas linhas de divisão
spacing_percentage = 0.2  # espaçamento entre os pontos nas linhas de divisão
color_line_division = (255, 255, 255)  # cor das linhas de divisão


#Outras variáveis:
background_color = (10, 10, 10)  # cor de fundo da tela
collision_prediction_fluctuation = 35  # flutuação de previsão de colisão
fluctuation_of_collision_prediction_fluctuation = 40  # flutuação da flutuação de previsão de colisão

#Inicialização do Pygame:
pygame.init()  # inicializar o Pygame
tela = pygame.display.set_mode((size_tela_x, size_tela_y))  # criar a tela
pygame.display.set_caption("PONG")  # definir o título da janela do jogo
