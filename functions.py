from setup import *
from pygame.locals import *
import random


def draw_score(): ## Desenhar a janela de Score
    global score_a
    global score_b
    global score_value_color

    fonte=pygame.font.get_default_font()
    ## definindo tamanho da fonte em função do valor de win_n_
    """if score_a >= 1000:
        size_fonte = 55
    elif score_a >= 100:
        size_fonte = 75
    elif score_a >= 10:
        size_fonte = 100
    else:
        size_fonte = 150"""
    size_fonte = 100
    fontesys=pygame.font.SysFont(fonte, size_fonte)
    score_o = fontesys.render(str(score_a) , 1, (score_value_color)) 
    largura_texto, altura_texto = score_o.get_size() # Obtenha as dimensões do texto
    rect_texto = score_o.get_rect(centerx=((size_tela_x/2)-100), centery=50)# Crie um objeto Rect para centralizar o texto na posição
    tela.blit(score_o,rect_texto)

    ## definindo tamanho da fonte em função do valor de win_n_
    """if score_b >= 1000:
        size_fonte = 55
    elif score_b >= 100:
        size_fonte = 75
    elif score_b >= 10:
        size_fonte = 100
    else:
        size_fonte = 150"""
    
    fontesys=pygame.font.SysFont(fonte, size_fonte)
    score_x = fontesys.render(str(score_b) , 1, (score_value_color)) 
    largura_texto, altura_texto = score_x.get_size() # Obtenha as dimensões do texto
    rect_texto = score_x.get_rect(centerx=((size_tela_x/2)+100), centery=50)# Crie um objeto Rect para centralizar o texto na posição
    tela.blit(score_x,rect_texto)

def straight_speed():

    global ball_color
    global ball_speed_x
    global ball_speed_y
    pygame.draw.line(tela, ball_color, (ball_pos_x, ball_pos_y), ((ball_pos_x+(10*ball_speed_x)), (ball_pos_y+(10*ball_speed_y))))

def draw_line_division():
    global size_tela_y
    global size_tela_x
    global size_strokes_division_x
    global n_strokes
    global spacing_percentage
    global color_line_division
    spacing = (size_tela_y*spacing_percentage)/n_strokes 
    size_strokes_division_y = (size_tela_y - (size_tela_y * spacing_percentage)) / n_strokes
    line_pos_x=(size_tela_x/2)-(size_strokes_division_x/2)

    i=0
    while i < size_tela_y:
        i += spacing/2
        pygame.draw.rect(tela, color_line_division, (int(line_pos_x), int(i), size_strokes_division_x, size_strokes_division_y))
        i += size_strokes_division_y+(spacing/2)

def win(ganhador):
    global score_a
    global score_b
    global ball_speed_x
    global ball_speed_y
    global ball_pos_x
    global ball_pos_y
    global size_tela_x
    global size_tela_y
    global ball_speed_start_x

    if ganhador == "a":
        score_a += 1
        ball_speed_x , ball_speed_y = random.choice(ball_speed_start)
        ball_speed_x = abs(ball_speed_x)
    if ganhador == "b":
        score_b += 1
        ball_speed_x , ball_speed_y = random.choice(ball_speed_start)
        ball_speed_x = - abs(ball_speed_x)

    ball_pos_x = size_tela_x/2
    ball_pos_y = size_tela_y/2


def update_ball_position(delta_time):
    global ball_pos_x
    global ball_pos_y
    global ball_speed_x
    global ball_speed_y
    global raio
    global paddles_size_x
    global paddles_size_y
    global paddles_pos_a_y
    global paddles_pos_b_y
    global score_a
    global score_b
    global paddles_vel_a
    global paddles_vel_b
    global delta_ball_speed
    
    global lost_ball_speed_x, lost_ball_speed_y

    lost_ball_speed_x, lost_ball_speed_y = ball_speed_x , ball_speed_y

    if (ball_pos_y+raio) >= size_tela_y or (ball_pos_y-raio) <= 0:
        ball_speed_y = ball_speed_y * -1

    if ((ball_pos_x-raio) <= (0+paddles_size_x)) and (ball_speed_x < 0) and (ball_pos_y > paddles_pos_a_y) and (ball_pos_y < (paddles_pos_a_y + paddles_size_y)):
        ball_speed_x = ball_speed_x * -1
        ball_speed_y = ball_speed_y + (3*paddles_vel_a)
    elif ball_pos_x < 0:
        win("b")
        
    if (ball_pos_x) < (0+paddles_size_x) and (ball_pos_y >(paddles_pos_a_y)) and (ball_pos_y < (paddles_pos_a_y+paddles_size_y)):
        ball_speed_y = (ball_speed_y*(-1)) + paddles_vel_a
        if (ball_speed_y) > 0:
            ball_pos_y = (paddles_pos_a_y+paddles_size_y)+ 1 
        if (ball_speed_y) < 0:
            ball_pos_y = (paddles_pos_a_y)- 1 
    """if (ball_pos_y > (paddles_pos_a_y+paddles_size_y)) and (ball_pos_y < (paddles_pos_a_y+paddles_size_y+raio)) and (ball_pos_x > (paddles_pos_a_x+paddles_size_x)) and (ball_pos_x < (paddles_pos_a_x+paddles_size_x+raio)):
        if ball_speed_x == 0 or ball_speed_y == 0:
            n = ball_speed_x
            ball_speed_x = -ball_speed_y
            ball_speed_y = n
        else:
            ball_speed_x*=-1
            ball_speed_y*=-1
        if ball_speed_x != 0:
            ball_pos_x+=(ball_speed_x/abs(ball_speed_x))
        if ball_speed_y != 0:
            ball_pos_y+=(ball_speed_y/abs(ball_speed_y))"""

    if ((ball_pos_x+raio) >= (size_tela_x-paddles_size_x)) and (ball_speed_x > 0) and (ball_pos_y > paddles_pos_b_y) and (ball_pos_y < (paddles_pos_b_y + paddles_size_y)):
        ball_speed_x = ball_speed_x * -1
        ball_speed_y = ball_speed_y + (3*paddles_vel_b)
    elif ball_pos_x > size_tela_x:
        win("a")
        
    if (ball_pos_x) > (size_tela_x-paddles_size_x) and (ball_pos_y >(paddles_pos_b_y)) and (ball_pos_y < (paddles_pos_b_y+paddles_size_y)):
        ball_speed_y = (ball_speed_y*(-1)) + paddles_vel_b
        if (ball_speed_y) > 0:
            ball_pos_y = (paddles_pos_b_y+paddles_size_y)+ 1 
        if (ball_speed_y) < 0:
            ball_pos_y = (paddles_pos_b_y)- 1
    

    ball_pos_x = ball_pos_x + (ball_speed_x * delta_time)
    ball_pos_y = ball_pos_y + (ball_speed_y * delta_time)

    pygame.draw.circle(tela, ball_color, (int(ball_pos_x), int(ball_pos_y)), raio)

    if (ball_speed_x != lost_ball_speed_x) or (ball_speed_y != lost_ball_speed_y):
        delta_ball_speed = True
    else:
        delta_ball_speed = False

def move_paddles_a():
    keys = pygame.key.get_pressed()
    global paddles_pos_a_y
    global ball_pos_y
    global paddles_vel_a
    global paddles_acel_a
    global paddles_vel_max_a
    global paddles_size_y
    global decay_rate
    if keys[K_g]:
        paddles_vel_a += paddles_acel_a * (-1)
    elif keys[K_b]:
        paddles_vel_a += paddles_acel_a * (1)
    else:
        paddles_vel_a = paddles_vel_a - (paddles_vel_a * decay_rate)
    if paddles_vel_a > paddles_vel_max_a:
        paddles_vel_a = paddles_vel_max_a
    if paddles_vel_a < -paddles_vel_max_a:
        paddles_vel_a = -paddles_vel_max_a

    if ((paddles_pos_a_y + paddles_size_y) >= size_tela_y and paddles_vel_a > 0) or (paddles_pos_a_y <= 0 and paddles_vel_a < 0):
        paddles_vel_a = 0

    paddles_pos_a_y += paddles_vel_a

def move_paddles_b():
    global paddles_pos_b_y
    global ball_pos_y
    global paddles_vel_b
    global paddles_acel_b
    global paddles_vel_max_b
    global paddles_size_y
    global decay_rate
    global ball_speed_x
    global ball_speed_y
    global collision_prediction_fluctuation, fluctuation_of_collision_prediction_fluctuation
    global collision_y

    if  delta_ball_speed == True:
        b = collision_prediction_fluctuation + random.randint(-fluctuation_of_collision_prediction_fluctuation, fluctuation_of_collision_prediction_fluctuation)
        collision_y = ((((size_tela_x-ball_pos_x)/ball_speed_x) * ball_speed_y) + ball_pos_y) + random.randint(-abs(b), abs(b))

    pygame.draw.circle(tela, ball_color, (size_tela_x, int(collision_y)), raio/5)
    
    if ball_speed_x > 0 or ball_pos_x > (size_tela_x/2):
        if (paddles_pos_b_y > collision_y):
            paddles_vel_b -= paddles_acel_b
        elif (paddles_pos_b_y+paddles_size_y < collision_y):
            paddles_vel_b += paddles_acel_b
        else:
            paddles_vel_b = paddles_vel_b - (paddles_vel_b * decay_rate)
    else:
        paddles_vel_b = paddles_vel_b - (paddles_vel_b * decay_rate/100)
    """if ball_speed_x > 0:
        if (paddles_vel_b > 0 and direction_move_b < 0) or (paddles_vel_b < 0 and direction_move_b > 0):
            paddles_vel_b += paddles_acel_b * 2 * direction_move_b
        else:    
            paddles_vel_b += paddles_acel_b * direction_move_b
    else:
        paddles_vel_b = paddles_vel_b - (paddles_vel_b * decay_rate)"""

    if paddles_vel_b > paddles_vel_max_b:
        paddles_vel_b = paddles_vel_max_b
    if paddles_vel_b < -paddles_vel_max_b:
        paddles_vel_b = -paddles_vel_max_b

    if ((paddles_pos_b_y + paddles_size_y) >= size_tela_y and paddles_vel_b > 0) or (paddles_pos_b_y <= 0 and paddles_vel_b < 0):
        paddles_vel_b = 0

    paddles_pos_b_y += paddles_vel_b
    
def draw_paddles_a():
    global paddles_size_x
    global paddles_size_y
    global paddles_color_a
    global paddles_pos_a_x
    global paddles_pos_a_y
    pygame.draw.rect(tela, paddles_color_a, (paddles_pos_a_x, paddles_pos_a_y, paddles_size_x, paddles_size_y))

def draw_paddles_b():
    global paddles_size_x
    global paddles_size_y
    global paddles_color_b
    global paddles_pos_b_x
    global paddles_pos_b_y
    pygame.draw.rect(tela, paddles_color_b, (paddles_pos_b_x, paddles_pos_b_y, paddles_size_x, paddles_size_y))

