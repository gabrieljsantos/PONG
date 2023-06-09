# functions.py
from setup import *
from pygame.locals import *
import random

def draw_score():
    global score_a
    global score_b
    global score_value_color

    fonte = pygame.font.get_default_font()

    size_fonte = 100  # Tamanho fixo da fonte para exibir a pontuação

    # Renderizar o valor da pontuação do jogador A
    fontesys = pygame.font.SysFont(fonte, size_fonte)  # Criar uma fonte com o tipo de fonte padrão e tamanho especificado
    score_o = fontesys.render(str(score_a), 1, score_value_color)  # Renderizar o valor da pontuação do jogador A
    largura_texto, altura_texto = score_o.get_size()  # Obter as dimensões do texto renderizado
    rect_texto = score_o.get_rect(centerx=((size_tela_x / 2) - 100), centery=50)  # Criar um retângulo para posicionar o texto centralizado
    tela.blit(score_o, rect_texto)  # Desenhar o valor da pontuação do jogador A na tela

    # Renderizar o valor da pontuação do jogador B
    fontesys = pygame.font.SysFont(fonte, size_fonte)  # Criar uma fonte com o tipo de fonte padrão e tamanho especificado
    score_x = fontesys.render(str(score_b), 1, score_value_color)  # Renderizar o valor da pontuação do jogador B
    largura_texto, altura_texto = score_x.get_size()  # Obter as dimensões do texto renderizado
    rect_texto = score_x.get_rect(centerx=((size_tela_x / 2) + 100), centery=50)  # Criar um retângulo para posicionar o texto centralizado
    tela.blit(score_x, rect_texto)  # Desenhar o valor da pontuação do jogador B na tela
    """
    Essa função renderiza a pontuação dos jogadores A e B na tela do jogo.
    Ela usa a fonte padrão do Pygame com um tamanho fixo de 100 para exibir a pontuação.
    O valor da pontuação é convertido em uma string e renderizado na tela.
    Em seguida, um retângulo é criado para posicionar o texto centralizado horizontalmente, e o texto é desenhado na tela utilizando o retângulo como referência.
    Isso é feito separadamente para os jogadores A e B, usando as variáveis score_a e score_b, respectivamente.
    O loop continua até que a variável i atinja a altura total da tela.
    """

def straight_speed():
    global ball_color
    global ball_speed_x
    global ball_speed_y

    # Desenhar uma linha reta com base na velocidade da bola
    pygame.draw.line(tela, ball_color, (ball_pos_x, ball_pos_y), ((ball_pos_x + (10 * ball_speed_x)), (ball_pos_y + (10 * ball_speed_y))))

    """
    Essa função desenha uma linha reta na tela com base na velocidade da bola.
    Ela usa as variáveis ball_color para determinar a cor da linha, ball_speed_x para a velocidade da bola no eixo x e ball_speed_y para a velocidade da bola no eixo y. A 
    linha é desenhada usando a função pygame.draw.line, especificando as coordenadas de início e fim da linha.As coordenadas de início são definidas pelas variáveis ball_pos_x 
    e ball_pos_y, e as coordenadas de fim são calculadas adicionando um valor proporcional à velocidade da bola em cada eixo.
    """

def draw_line_division():
    global size_tela_y
    global size_tela_x
    global size_strokes_division_x
    global n_strokes
    global spacing_percentage
    global color_line_division

    # Calcular o espaçamento entre as linhas de divisão
    spacing = (size_tela_y * spacing_percentage) / n_strokes

    # Calcular a altura das linhas de divisão
    size_strokes_division_y = (size_tela_y - (size_tela_y * spacing_percentage)) / n_strokes

    # Calcular a posição x das linhas de divisão
    line_pos_x = (size_tela_x / 2) - (size_strokes_division_x / 2)

    # Desenhar as linhas de divisão
    i = 0
    while i < size_tela_y:
        i += spacing / 2
        pygame.draw.rect(tela, color_line_division, (int(line_pos_x), int(i), size_strokes_division_x, size_strokes_division_y))
        i += size_strokes_division_y + (spacing / 2)
    """
    Essa função desenha as linhas de divisão na tela. Ela utiliza várias variáveis globais, como `size_tela_y` e `size_tela_x` para obter as dimensões da tela, `size_strokes_division_x` para determinar a largura das linhas de divisão, `n_strokes` para determinar o número de pontos nas linhas de divisão, `spacing_percentage` para determinar o espaçamento entre os pontos, e `color_line_division` para determinar a cor das linhas de divisão.
    O espaçamento entre as linhas de divisão é calculado com base na altura da tela e na porcentagem de espaçamento desejada. A altura das linhas de divisão é calculada subtraindo a porcentagem de espaçamento da altura total da tela e dividindo pelo número de pontos nas linhas de divisão.
    A posição x das linhas de divisão é calculada para que elas fiquem centralizadas na tela.
    Em seguida, um loop é executado para desenhar as linhas de divisão. O loop incrementa a variável `i` pelo espaçamento desejado e desenha um retângulo na posição especificada usando a função `pygame.draw.rect`. O retângulo tem a cor definida por `color_line_division` e possui a largura e altura determinadas pelas variáveis `size_strokes_division_x` e `size_strokes_division_y`, respectivamente.
    O loop continua até que a variável `i` atinja a altura total da tela."""

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

    # Verificar qual jogador ganhou e atualizar a pontuação
    if ganhador == "a":
        score_a += 1
        # Escolher uma velocidade aleatória para a bola e definir a direção para a direita
        ball_speed_x, ball_speed_y = random.choice(ball_speed_start)
        ball_speed_x = abs(ball_speed_x)
    elif ganhador == "b":
        score_b += 1
        # Escolher uma velocidade aleatória para a bola e definir a direção para a esquerda
        ball_speed_x, ball_speed_y = random.choice(ball_speed_start)
        ball_speed_x = -abs(ball_speed_x)

    # Reposicionar a bola no centro da tela
    ball_pos_x = size_tela_x / 2
    ball_pos_y = size_tela_y / 2
    """
    Essa função é chamada quando um jogador ganha um ponto. Ela recebe como argumento o identificador do jogador vencedor (ganhador). A função utiliza várias variáveis globais, como score_a e score_b para atualizar a pontuação dos jogadores, ball_speed_x e ball_speed_y para definir a velocidade da bola, ball_pos_x e ball_pos_y para reposicionar a bola no centro da tela, size_tela_x e size_tela_y para obter as dimensões da tela, e ball_speed_start_x para escolher uma velocidade inicial aleatória para a bola.
    Se o jogador "a" vencer, a pontuação de "score_a" é incrementada em 1, e uma velocidade aleatória é escolhida para a bola, com a direção definida para a direita.
    Se o jogador "b" vencer, a pontuação de "score_b" é incrementada em 1, e uma velocidade aleatória é escolhida para a bola, com a direção definida para a esquerda.
    Em seguida, a posição da bola é atualizada para o centro da tela.
    """

def update_ball_position(delta_time):
    global ball_pos_x
    global ball_pos_y
    global ball_speed_x
    global ball_speed_y
    global raio
    global racket_size_x
    global racket_size_y
    global racket_pos_a_y
    global racket_pos_b_y
    global score_a
    global score_b
    global racket_vel_a
    global racket_vel_b
    global delta_ball_speed
    
    global lost_ball_speed_x, lost_ball_speed_y

    # Salvar a velocidade anterior da bola para verificar se houve alteração na velocidade
    lost_ball_speed_x, lost_ball_speed_y = ball_speed_x, ball_speed_y

    # Verificar se a bola atingiu a parte superior ou inferior da tela e inverter a direção
    if (ball_pos_y + raio) >= size_tela_y or (ball_pos_y - raio) <= 0:
        ball_speed_y = ball_speed_y * -1

    # Verificar colisão com a raquete do jogador A (esquerda)
    if ((ball_pos_x - raio) <= (0 + racket_size_x)) and (ball_speed_x < 0) and (ball_pos_y > racket_pos_a_y) and (ball_pos_y < (racket_pos_a_y + racket_size_y)):
        ball_speed_x = ball_speed_x * -1
        ball_speed_y = ball_speed_y + (3 * racket_vel_a)
    elif ball_pos_x < 0:
        # Se a bola ultrapassar a borda esquerda da tela, o jogador B vence
        win("b")

    # Verificar colisão com a raquete do jogador B (direita)
    if (ball_pos_x) < (0 + racket_size_x) and (ball_pos_y > racket_pos_a_y) and (ball_pos_y < (racket_pos_a_y + racket_size_y)):
        ball_speed_y = (ball_speed_y * (-1)) + racket_vel_a
        if (ball_speed_y) > 0:
            ball_pos_y = (racket_pos_a_y + racket_size_y) + 1
        if (ball_speed_y) < 0:
            ball_pos_y = racket_pos_a_y - 1

    # Verificar colisão com a raquete do jogador B (direita)
    if ((ball_pos_x + raio) >= (size_tela_x - racket_size_x)) and (ball_speed_x > 0) and (ball_pos_y > racket_pos_b_y) and (ball_pos_y < (racket_pos_b_y + racket_size_y)):
        ball_speed_x = ball_speed_x * -1
        ball_speed_y = ball_speed_y + (3 * racket_vel_b)
    elif ball_pos_x > size_tela_x:
        # Se a bola ultrapassar a borda direita da tela, o jogador A vence
        win("a")

    # Verificar colisão com a raquete do jogador B (direita)
    if (ball_pos_x) > (size_tela_x - racket_size_x) and (ball_pos_y > racket_pos_b_y) and (ball_pos_y < (racket_pos_b_y + racket_size_y)):
        ball_speed_y = (ball_speed_y * (-1)) + racket_vel_b
        if (ball_speed_y) > 0:
            ball_pos_y = (racket_pos_b_y + racket_size_y) + 1
        if (ball_speed_y) < 0:
            ball_pos_y = racket_pos_b_y - 1

    # Atualizar a posição da bola com base na velocidade e no tempo
    ball_pos_x = ball_pos_x + (ball_speed_x * delta_time)
    ball_pos_y = ball_pos_y + (ball_speed_y * delta_time)

    # Desenhar a bola na tela
    pygame.draw.circle(tela, ball_color, (int(ball_pos_x), int(ball_pos_y)), raio)

    # Verificar se houve alteração na velocidade da bola
    if (ball_speed_x != lost_ball_speed_x) or (ball_speed_y != lost_ball_speed_y):
        delta_ball_speed = True
    else:
        delta_ball_speed = False
    """
    Essa função é responsável por atualizar a posição da bola no jogo. Ela recebe como argumento delta_time, que representa a diferença de tempo entre os quadros do jogo.
    A função utiliza várias variáveis globais, como ball_pos_x e ball_pos_y para a posição da bola, ball_speed_x e ball_speed_y para a velocidade da bola, raio para o raio da bola, racket_size_x e racket_size_y para o tamanho das raquetes dos jogadores, racket_pos_a_y e racket_pos_b_y para a posição vertical das raquetes dos jogadores A e B, score_a e score_b para as pontuações dos jogadores, racket_vel_a e racket_vel_b para as velocidades das raquetes dos jogadores A e B, delta_ball_speed para verificar se houve alteração na velocidade da bola, lost_ball_speed_x e lost_ball_speed_y para armazenar a velocidade anterior da bola.
    A função realiza várias verificações e atualizações para o movimento da bola e colisões com as raquetes dos jogadores A e B. Ela também verifica se a bola ultrapassou as bordas da tela e chama a função win para atualizar a pontuação e reposicionar a bola no centro quando um jogador marca um ponto.
    Por fim, a função desenha a bola na posição atualizada na tela e verifica se houve alteração na velocidade da bola, atualizando a variável delta_ball_speed de acordo.
    """

def move_racket_a():
    # Obter o estado das teclas pressionadas
    keys = pygame.key.get_pressed()
    
    # Variáveis globais utilizadas na função
    global racket_pos_a_y
    global ball_pos_y
    global racket_vel_a
    global racket_acel_a
    global racket_vel_max_a
    global racket_size_y
    global decay_rate
    
    # Verificar se a tecla "g" está pressionada para mover a raquete para cima
    if keys[K_g]:
        racket_vel_a += racket_acel_a * (-1)
    
    # Verificar se a tecla "b" está pressionada para mover a raquete para baixo
    elif keys[K_b]:
        racket_vel_a += racket_acel_a * (1)
    
    # Caso nenhuma tecla esteja pressionada, aplicar uma taxa de decaimento à velocidade da raquete
    else:
        racket_vel_a = racket_vel_a - (racket_vel_a * decay_rate)
    
    # Limitar a velocidade máxima da raquete A
    if racket_vel_a > racket_vel_max_a:
        racket_vel_a = racket_vel_max_a
    if racket_vel_a < -racket_vel_max_a:
        racket_vel_a = -racket_vel_max_a
    
    # Limitar o movimento da raquete A dentro da tela
    if ((racket_pos_a_y + racket_size_y) >= size_tela_y and racket_vel_a > 0) or (racket_pos_a_y <= 0 and racket_vel_a < 0):
        racket_vel_a = 0
    
    # Atualizar a posição vertical da raquete A
    racket_pos_a_y += racket_vel_a
    """
    Essa função controla o movimento da raquete do jogador A com base nas teclas pressionadas.
    A função começa obtendo o estado das teclas pressionadas usando pygame.key.get_pressed(). Em seguida, ela verifica se a tecla "g" está pressionada para mover a raquete para cima, ou se a tecla "b" está pressionada para mover a raquete para baixo. Caso nenhuma tecla esteja pressionada, é aplicada uma taxa de decaimento à velocidade da raquete.
    Em seguida, a função limita a velocidade máxima da raquete A para evitar movimentos muito rápidos. Também é verificado se o movimento da raquete ultrapassa os limites da tela, e nesse caso, a velocidade é ajustada para zero.
    Por fim, a função atualiza a posição vertical da raquete A com base na velocidade atual.'
    """

def move_racket_b():
    # Variáveis globais utilizadas na função
    global racket_pos_b_y
    global ball_pos_y
    global racket_vel_b
    global racket_acel_b
    global racket_vel_max_b
    global racket_size_y
    global decay_rate
    global ball_speed_x
    global ball_speed_y
    global collision_prediction_fluctuation, fluctuation_of_collision_prediction_fluctuation
    global collision_y

    # Verificar se houve mudança na velocidade da bola
    if delta_ball_speed == True:
        # Calcular a posição prevista de colisão vertical da bola com a raquete B
        b = collision_prediction_fluctuation + random.randint(-fluctuation_of_collision_prediction_fluctuation, fluctuation_of_collision_prediction_fluctuation)
        collision_y = ((((size_tela_x - ball_pos_x) / ball_speed_x) * ball_speed_y) + ball_pos_y) + random.randint(-abs(b), abs(b))

    # Desenhar um círculo na posição prevista de colisão vertical
    ## pygame.draw.circle(tela, ball_color, (size_tela_x, int(collision_y)), raio/5)

    # Verificar a direção do movimento da bola e ajustar a velocidade da raquete B em consequência
    if ball_speed_x > 0 or ball_pos_x > (size_tela_x / 2):
        if racket_pos_b_y > collision_y:
            racket_vel_b -= racket_acel_b
        elif racket_pos_b_y + racket_size_y < collision_y:
            racket_vel_b += racket_acel_b
        else:
            racket_vel_b = racket_vel_b - (racket_vel_b * decay_rate)
    else:
        racket_vel_b = racket_vel_b - (racket_vel_b * decay_rate / 100)
    
    # Limitar a velocidade máxima da raquete B
    if racket_vel_b > racket_vel_max_b:
        racket_vel_b = racket_vel_max_b
    if racket_vel_b < -racket_vel_max_b:
        racket_vel_b = -racket_vel_max_b
    
    # Limitar o movimento da raquete B dentro da tela
    if ((racket_pos_b_y + racket_size_y) >= size_tela_y and racket_vel_b > 0) or (racket_pos_b_y <= 0 and racket_vel_b < 0):
        racket_vel_b = 0
    
    # Atualizar a posição vertical da raquete B
    racket_pos_b_y += racket_vel_b

    """
    Essa função controla o movimento da raquete do jogador B com base na posição prevista de colisão vertical da bola com a raquete.
    A função começa definindo as variáveis globais utilizadas na função. Em seguida, ela verifica se houve mudança na velocidade da bola. Se houver, é calculada a posição prevista de colisão vertical da bola com a raquete B, levando em consideração uma flutuação aleatória. Um círculo é desenhado nessa posição prevista de colisão para fins de visualização.
    Depois, a função verifica a direção do movimento da bola e ajusta a velocidade da raquete B de acordo. Se a bola estiver se movendo para
    """    

## Aqui estão as funções draw_racket_a e draw_racket_b:

def draw_racket_a():
    global racket_size_x
    global racket_size_y
    global racket_color_a
    global racket_pos_a_x
    global racket_pos_a_y
    
    # Desenhar a raquete do jogador A na tela
    pygame.draw.rect(tela, racket_color_a, (racket_pos_a_x, racket_pos_a_y, racket_size_x, racket_size_y))

def draw_racket_b():
    global racket_size_x
    global racket_size_y
    global racket_color_b
    global racket_pos_b_x
    global racket_pos_b_y
    
    # Desenhar a raquete do jogador B na tela
    pygame.draw.rect(tela, racket_color_b, (racket_pos_b_x, racket_pos_b_y, racket_size_x, racket_size_y))
"""
Essas funções são responsáveis por desenhar as raquetes dos jogadores A e B na tela.
A função draw_racket_a desenha a raquete do jogador A na posição especificada pelas variáveis racket_pos_a_x e racket_pos_a_y. O tamanho da raquete é determinado pelas variáveis racket_size_x e racket_size_y, e a cor é definida pela variável racket_color_a.
A função draw_racket_b é semelhante, mas desenha a raquete do jogador B na posição especificada pelas variáveis racket_pos_b_x e racket_pos_b_y. O tamanho e a cor da raquete são definidos pelas variáveis racket_size_x, racket_size_y e racket_color_b, respectivamente.
Ambas as funções utilizam a função pygame.draw.rect para desenhar um retângulo na tela com as dimensões e a cor especificadas. O retângulo representa a raquete do jogador correspondente.
"""