# Jogo Pong em Python

Este é um projeto que implementa o clássico jogo Pong utilizando a biblioteca Pygame em Python. O jogo consiste em rebater uma bola entre dois jogadores, um jogador controlado pelo usuário e outro controlado pelo computador, com o objetivo de marcar pontos.

## Funcionalidades implementadas

O jogo Pong implementado neste projeto possui as seguintes funcionalidades:

- Movimento das barras: O jogador pode controlar a sua barra para rebater a bola usando as teclas `G` e `B`, enquanto a barra controlada pelo computador se move automaticamente.
- Pontuação: O jogo mantém o registro da pontuação do jogador e do computador, que é exibida na tela durante o jogo.
- Reinício da partida: Após cada ponto marcado, a bola retorna ao centro e o jogo continua. O primeiro jogador a atingir a pontuação máxima vence a partida.
- Velocidade da bola: A bola se move em trajetórias curvas com velocidades aleatórias, adicionando um elemento de desafio ao jogo.

## Como executar o jogo

1. Certifique-se de ter o Python instalado em sua máquina.
2. Instale a biblioteca Pygame executando o seguinte comando no terminal:
   ```
   pip install pygame
   ```
3. Baixe os arquivos do projeto e navegue até o diretório onde estão localizados.
4. Execute o arquivo `pong.py` para iniciar o jogo.
5. Use as teclas `G` e `B` para controlar a barra do jogador e rebater a bola.
6. Acompanhe a pontuação na tela e jogue até que um dos jogadores alcance a pontuação máxima.

## Funções

O jogo Pong faz uso de várias funções implementadas no arquivo `functions.py`. Aqui estão algumas das principais funções utilizadas:

- `update_ball_position(delta_time)`: Atualiza a posição da bola com base nas colisões. Essa função é responsável pelo movimento da bola no jogo.
- `draw_racket_a()`, `draw_racket_b()`: Desenha as barras dos jogadores A e B na tela.
- `move_racket_a()`, `move_racket_b()`: Controla o movimento das barras dos jogadores A e B com base nas teclas pressionadas pelos jogadores.
- `draw_line_division()`: Desenha a linha de divisão no meio da tela para separar os campos dos jogadores.
- `draw_score()`: Exibe a pontuação dos jogadores na tela.

## Limitações

O jogo Pong implementado possui algumas limitações a serem consideradas:
- Bug 1 - A bolinha entra dentro da raquete se a mesma e atigida nos lados, e como consequancia é rebatida.
- Bug 2 - Ás vezes a bolinha é telestransportada para a outra extremidade da raquete se a  mesma é atingina nos cantos.
- Apenas um modo de jogo: O jogo implementa apenas o modo de jogo jogador vs computador. Não há suporte para jogadores adicionais ou jogabilidade online.
- Interface gráfica simples: A interface gráfica do jogo é minimalista, com elementos básicos desenhados na tela. Não há animações sofisticadas ou efeitos visuais avançados.
- Dificuldade fixa do computador: O computador controla a barra com uma dificuldade fixa, o que significa que não há opções para ajustar o nível de dificuldade do oponente controlado


## Oque pode ser feito com o projeto?
- Edite, melhore, corrija os bugs, faça oque achar melhor!
- Entre em contato comigo pelo instagram gabriel_j.santos_ ou pelo link:
[![Instagram](https://img.shields.io/badge/Instagram-Follow%20Me-%23E4405F?logo=instagram)](https://instagram.com/gabriel_j.santos_?igshid=NTc4MTIwNjQ2YQ==)