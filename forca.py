import pygame
import random

# Inicializando Pygame
pygame.init()

# Inicializando o mixer para o som de fundo
pygame.mixer.init()

# Definindo as dimensões da tela
WIDTH, HEIGHT = 900, 700  # Aumentando a altura e largura da janela
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jogo da Forca")

# Definindo as cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Fonte
LETTER_FONT = pygame.font.SysFont('comicsans', 30)  # Diminuiu a fonte
WORD_FONT = pygame.font.SysFont('comicsans', 50)    # Diminuiu a fonte
TITLE_FONT = pygame.font.SysFont('comicsans', 70)

# Palavras para o jogo
words = ["PYTHON", "COMPUTADOR", "JOGO", "DESENVOLVIMENTO", "HANGMAN"]

# Carregando o som de fundo
pygame.mixer.music.load("som_de_fundo.mp3")  # Substitua com o caminho do seu arquivo de som
pygame.mixer.music.play(-1)  # -1 faz com que o som toque em loop

# Função para desenhar o enforcado
def draw_hangman(errors):
    if errors >= 1:
        pygame.draw.line(win, BLACK, (100, 500), (300, 500), 5)  # Base
    if errors >= 2:
        pygame.draw.line(win, BLACK, (200, 500), (200, 150), 5)  # Poste
    if errors >= 3:
        pygame.draw.line(win, BLACK, (200, 150), (350, 150), 5)  # Braço superior
    if errors >= 4:
        pygame.draw.line(win, BLACK, (350, 150), (350, 200), 5)  # Cordão
    if errors >= 5:
        pygame.draw.circle(win, BLACK, (350, 250), 50, 5)  # Cabeça
    if errors >= 6:
        pygame.draw.line(win, BLACK, (350, 300), (350, 400), 5)  # Corpo
    if errors >= 7:
        pygame.draw.line(win, BLACK, (350, 350), (300, 400), 5)  # Braço esquerdo
    if errors >= 8:
        pygame.draw.line(win, BLACK, (350, 350), (400, 400), 5)  # Braço direito
    if errors >= 9:
        pygame.draw.line(win, BLACK, (350, 400), (300, 450), 5)  # Perna esquerda
    if errors >= 10:
        pygame.draw.line(win, BLACK, (350, 400), (400, 450), 5)  # Perna direita

# Função para desenhar o botão de reiniciar
def draw_button():
    pygame.draw.rect(win, GREEN, (WIDTH//2 - 100, HEIGHT - 100, 200, 50))
    text = LETTER_FONT.render("Reiniciar", 1, BLACK)
    win.blit(text, (WIDTH//2 - text.get_width()//2, HEIGHT - 90))

# Função para verificar clique no botão
def button_clicked(pos):
    x, y = pos
    return WIDTH//2 - 100 <= x <= WIDTH//2 + 100 and HEIGHT - 100 <= y <= HEIGHT - 50

# Função para desenhar o jogo (palavra, letras, e o enforcado)
def draw(word, guessed, errors):
    win.fill(WHITE)
    text = TITLE_FONT.render("Jogo da Forca", 1, BLACK)
    win.blit(text, (WIDTH//2 - text.get_width()//2, 20))

    # Desenhar a palavra
    display_word = ""
    for letter in word:
        if letter in guessed:
            display_word += letter + " "
        else:
            display_word += "_ "
    text = WORD_FONT.render(display_word, 1, BLACK)
    win.blit(text, (400, 350))  # Movemos a palavra para abaixo do enforcado

    # Desenhar as letras erradas
    text = LETTER_FONT.render("Letras erradas: " + " ".join(guessed), 1, RED)
    win.blit(text, (10, 550))  # Movemos as letras erradas para mais embaixo

    # Área para anúncios do Google
    ad_text = LETTER_FONT.render("Anúncios do Google aqui", 1, BLACK)  # Exemplo de texto de anúncio
    win.blit(ad_text, (WIDTH//2 - ad_text.get_width()//2, 600))  # Centralizando abaixo das letras erradas

    # Desenhar o enforcado
    draw_hangman(errors)

    pygame.display.update()

# Função principal do jogo
def main():
    word = random.choice(words).upper()
    guessed = []
    errors = 0
    game_over = False

    # Loop do jogo
    FPS = 60
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN and not game_over:
                if event.key >= pygame.K_a and event.key <= pygame.K_z:
                    letter = chr(event.key).upper()
                    if letter not in guessed:
                        guessed.append(letter)
                        if letter not in word:
                            errors += 1

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if game_over and button_clicked(pos):
                    # Reiniciar o jogo
                    word = random.choice(words).upper()
                    guessed = []
                    errors = 0
                    game_over = False

        draw(word, guessed, errors)

        # Verificar se o jogador venceu ou perdeu
        if errors == 10 or all(letter in guessed for letter in word):
            game_over = True
            win.fill(WHITE)

            if errors == 10:
                text = WORD_FONT.render("Você perdeu!", 1, RED)
            else:
                text = WORD_FONT.render("Você venceu!", 1, BLACK)

            win.blit(text, (WIDTH//2 - text.get_width()//2, HEIGHT//2 - text.get_height()//2))
            draw_button()
            pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
