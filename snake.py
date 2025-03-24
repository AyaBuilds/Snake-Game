import pygame
import random
import time

# Initialisation de Pygame
pygame.init()

# Paramètres de la fenêtre
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20  # Taille des cases du jeu
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game 🐍")

# Couleurs
BEIGE = (245, 245, 220)  # Couleur beige
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)  # Couleur noire
WHITE = (255, 255, 255)

# Police de texte par défaut
font = pygame.font.Font(None, 36)  # Utilisation de la police par défaut

# Fonction pour afficher le texte
def display_text(text, color, y_offset=0):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 + y_offset))
    screen.blit(text_surface, text_rect)

# Initialisation du serpent
snake = [(100, 100), (90, 100), (80, 100)]  # Positions initiales du serpent
snake_dir = (CELL_SIZE, 0)  # Direction initiale (vers la droite)

# Fonction pour générer une nouvelle pomme, en évitant qu'elle apparaisse sur le serpent
def spawn_food():
    while True:
        x = random.randint(0, (WIDTH // CELL_SIZE) - 1) * CELL_SIZE
        y = random.randint(0, (HEIGHT // CELL_SIZE) - 1) * CELL_SIZE
        if (x, y) not in snake:  # Vérifie que la pomme ne soit pas sur le serpent
            return x, y

food = spawn_food()

# Jeu en cours ?
running = True
clock = pygame.time.Clock()

# Affichage du message de bienvenue pendant 3 secondes
screen.fill(BEIGE)  # Fond beige
display_text("Bienvenue dans le Jeu Snake par AyaBuilds", BLACK, -50)
display_text("Appuyez sur une touche pour commencer", BLACK, 50)
pygame.display.flip()

# Attendre que l'utilisateur appuie sur une touche pour commencer
waiting_for_key = True
while waiting_for_key:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            waiting_for_key = False
        elif event.type == pygame.KEYDOWN:
            # Une touche est pressée, commence le jeu
            waiting_for_key = False
            screen.fill(BEIGE)  # Efface le texte et fond
            pygame.display.flip()  # Rafraîchit l'écran

            # Petite pause avant de commencer le jeu
            time.sleep(0.5)

# Boucle de jeu
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_dir != (0, CELL_SIZE):
                snake_dir = (0, -CELL_SIZE)
            elif event.key == pygame.K_DOWN and snake_dir != (0, -CELL_SIZE):
                snake_dir = (0, CELL_SIZE)
            elif event.key == pygame.K_LEFT and snake_dir != (CELL_SIZE, 0):
                snake_dir = (-CELL_SIZE, 0)
            elif event.key == pygame.K_RIGHT and snake_dir != (-CELL_SIZE, 0):
                snake_dir = (CELL_SIZE, 0)

    # Déplacement du serpent
    new_head = (snake[0][0] + snake_dir[0], snake[0][1] + snake_dir[1])
    snake.insert(0, new_head)

    # Vérification des collisions avec la pomme
    if new_head == food:
        food = spawn_food()  # Génère une nouvelle pomme
    else:
        snake.pop()  # Retirer la dernière partie du serpent si on n'a pas mangé la pomme

    # Vérification des collisions avec les bords ou le corps du serpent
    if (
        new_head[0] < 0 or new_head[0] >= WIDTH or
        new_head[1] < 0 or new_head[1] >= HEIGHT or
        new_head in snake[1:]
    ):
        running = False

    # Dessin du serpent
    screen.fill(BEIGE)  # Fond de l'écran
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (segment[0], segment[1], CELL_SIZE, CELL_SIZE))

    # Dessin de la pomme
    pygame.draw.rect(screen, RED, (food[0], food[1], CELL_SIZE, CELL_SIZE))

    pygame.display.flip()

    # Réduire la vitesse du jeu
    clock.tick(10)  # Vitesse du jeu (plus petit = plus lent)

pygame.quit()


