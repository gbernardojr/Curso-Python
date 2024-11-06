import pygame
import random

# Configurações iniciais
pygame.init()

# Dimensões da tela
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
GRID_SIZE = 20

# Cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
PINK = (255, 105, 180)
ORANGE = (255, 165, 0)

# Classe do Pac-Man
class PacMan:
    def __init__(self):
        self.x = SCREEN_WIDTH // 2 // GRID_SIZE
        self.y = SCREEN_HEIGHT // 2 // GRID_SIZE
        self.direction = 'RIGHT'

    def move(self):
        if self.direction == 'UP':
            self.y -= 1
        elif self.direction == 'DOWN':
            self.y += 1
        elif self.direction == 'LEFT':
            self.x -= 1
        elif self.direction == 'RIGHT':
            self.x += 1

        # Mantém Pac-Man dentro da tela
        self.x %= SCREEN_WIDTH // GRID_SIZE
        self.y %= SCREEN_HEIGHT // GRID_SIZE

    def draw(self, screen):
        pygame.draw.circle(screen, YELLOW, (self.x * GRID_SIZE + GRID_SIZE // 2, self.y * GRID_SIZE + GRID_SIZE // 2), GRID_SIZE // 2)

# Classe do Fantasma
class Ghost:
    def __init__(self, start_x, start_y, strategy):
        self.x = start_x
        self.y = start_y
        self.strategy = strategy
        self.color = strategy['color']
        self.speed = 0.5  # Velocidade do fantasma

    def move(self, pacman):
        if self.strategy['name'] == 'Blinky':
            # Segue diretamente o Pac-Man
            self.move_towards(pacman)

        elif self.strategy['name'] == 'Pinky':
            # Move para onde o Pac-Man vai
            future_x = pacman.x + (1 if pacman.direction == 'RIGHT' else -1 if pacman.direction == 'LEFT' else 0)
            future_y = pacman.y + (1 if pacman.direction == 'DOWN' else -1 if pacman.direction == 'UP' else 0)
            self.move_towards(PacManPosition(future_x % (SCREEN_WIDTH // GRID_SIZE), future_y % (SCREEN_HEIGHT // GRID_SIZE)))

        elif self.strategy['name'] == 'Inky':
            # Move aleatoriamente e na direção do Pac-Man
            if random.random() < 0.5:
                self.move_random()
            else:
                self.move_towards(pacman)

        elif self.strategy['name'] == 'Clyde':
            # Segue o Pac-Man, mas a uma distância mínima
            distance = abs(self.x - pacman.x) + abs(self.y - pacman.y)
            if distance > 5:
                self.move_towards(pacman)
            else:
                # Muda de direção aleatoriamente se estiver perto
                self.move_random()

        # Mantém o fantasma dentro da tela
        self.x %= SCREEN_WIDTH // GRID_SIZE
        self.y %= SCREEN_HEIGHT // GRID_SIZE

    def move_towards(self, target):
        # Move o fantasma em direção ao alvo
        if abs(self.x - target.x) > self.speed:
            self.x += self.speed if self.x < target.x else -self.speed
        if abs(self.y - target.y) > self.speed:
            self.y += self.speed if self.y < target.y else -self.speed

    def move_random(self):
        # Move aleatoriamente em uma direção
        direction = random.choice(['UP', 'DOWN', 'LEFT', 'RIGHT'])
        if direction == 'UP':
            self.y -= self.speed
        elif direction == 'DOWN':
            self.y += self.speed
        elif direction == 'LEFT':
            self.x -= self.speed
        elif direction == 'RIGHT':
            self.x += self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x * GRID_SIZE, self.y * GRID_SIZE, GRID_SIZE, GRID_SIZE))

# Classe auxiliar para representar a posição do Pac-Man
class PacManPosition:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Função principal do jogo
def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Pac-Man com Estratégias de Fantasmas')

    clock = pygame.time.Clock()

    pacman = PacMan()
    # Definindo estratégias para cada fantasma
    strategies = [
        {'name': 'Blinky', 'color': RED},
        {'name': 'Pinky', 'color': PINK},
        {'name': 'Inky', 'color': BLUE},
        {'name': 'Clyde', 'color': ORANGE},
    ]
    
    ghosts = []
    # Posicionar fantasmas aleatoriamente, garantindo que eles não fiquem na mesma posição
    positions = set()
    for strategy in strategies:
        while True:
            start_x = random.randint(0, SCREEN_WIDTH // GRID_SIZE - 1)
            start_y = random.randint(0, SCREEN_HEIGHT // GRID_SIZE - 1)
            if (start_x, start_y) not in positions:
                positions.add((start_x, start_y))
                ghosts.append(Ghost(start_x, start_y, strategy))
                break

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    pacman.direction = 'UP'
                elif event.key == pygame.K_DOWN:
                    pacman.direction = 'DOWN'
                elif event.key == pygame.K_LEFT:
                    pacman.direction = 'LEFT'
                elif event.key == pygame.K_RIGHT:
                    pacman.direction = 'RIGHT'

        pacman.move()

        for ghost in ghosts:
            ghost.move(pacman)

        screen.fill(BLACK)

        pacman.draw(screen)
        for ghost in ghosts:
            ghost.draw(screen)

        # Verifica se Pac-Man colidiu com um fantasma
        for ghost in ghosts:
            if (pacman.x, pacman.y) == (ghost.x, ghost.y):
                print("Game Over! Você foi pego por um fantasma.")
                running = False

        pygame.display.flip()
        clock.tick(10)

    pygame.quit()

if __name__ == '__main__':
    main()
