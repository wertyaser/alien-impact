import pygame
import sys
import random

# Initialize Pygame
pygame.init()
pygame.mixer.init()

# Load bullet sound
bullet_sound = pygame.mixer.Sound("./bullet.wav")

# Load background music
pygame.mixer.music.load("./bg.wav")

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Player
player_size = 50
player_speed = 7
player_lives = 3
points = 0

# Initialize the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Alien Impact")

# Load images
player_image = pygame.image.load("./player.png")  # Replace with the actual path to your plane image
player_image = pygame.transform.scale(player_image, (player_size, player_size))

logo_image = pygame.image.load("./title.png")  # Replace with the actual path to your logo image
logo_image = pygame.transform.scale(logo_image, (400, 200))  # Adjust the size of the logo as needed

# Game loop
clock = pygame.time.Clock()

def show_menu():
    font = pygame.font.Font(None, 36)

    play_button = font.render("Play", True, WHITE)
    how_to_play_button = font.render("How to Play", True, WHITE)
    about_button = font.render("About", True, WHITE)
    exit_button = font.render("Exit", True, WHITE)

    while True:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if 300 <= x <= 500 and 200 <= y <= 250:
                    return "play"
                elif 300 <= x <= 500 and 300 <= y <= 350:
                    return "how_to_play"
                elif 300 <= x <= 500 and 400 <= y <= 450:
                    return "about"
                elif 300 <= x <= 500 and 500 <= y <= 550:
                    pygame.quit()
                    sys.exit()

        # Display title
        screen.blit(logo_image, (200, 10))

        pygame.draw.rect(screen, (0, 128, 255), (300, 200, 200, 50))
        pygame.draw.rect(screen, (0, 128, 255), (300, 300, 200, 50))
        pygame.draw.rect(screen, (0, 128, 255), (300, 400, 200, 50))
        pygame.draw.rect(screen, (0, 128, 255), (300, 500, 200, 50))

        screen.blit(play_button, (350, 210))
        screen.blit(how_to_play_button, (350, 310))
        screen.blit(about_button, (350, 410))
        screen.blit(exit_button, (350, 510))

        pygame.display.flip()


def show_how_to_play():
    font_title = pygame.font.Font(None, 36)
    font_content = pygame.font.Font(None, 24)

    how_to_play_title = font_title.render("How to Play Alien Impact", True, WHITE)

    # Render each line separately to ensure line breaks
    line1 = font_content.render("1. Use 'A' and 'D' keys to move your spaceship left and right.", True, WHITE)
    line2 = font_content.render("2. Press the 'Space' key to shoot and destroy incoming alien ships.", True, WHITE)
    line3 = font_content.render("3. Avoid enemy fire to prevent losing lives.", True, WHITE)
    line4 = font_content.render("4. Survive as long as possible to score points and set new records!", True, WHITE)
    line5 = font_content.render("Press 'Esc' to return to the main menu.", True, WHITE)

    while True:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return "menu"

        screen.blit(how_to_play_title, (50, 50))
        screen.blit(line1, (50, 100))
        screen.blit(line2, (50, 130))
        screen.blit(line3, (50, 160))
        screen.blit(line4, (50, 190))
        screen.blit(line5, (50, 220))

        pygame.display.flip()


def show_about():
    font_title = pygame.font.Font(None, 36)
    font_content = pygame.font.Font(None, 24)

    about_title = font_title.render("About Alien Impact", True, WHITE)

    # Render each line separately to ensure line breaks
    line1 = font_content.render("Alien Impact is an arcade-style game inspired by classic space invaders.", True, WHITE)
    line2 = font_content.render("Players navigate a spaceship, aiming to survive waves of enemy alien attacks.", True,
                                WHITE)
    line3 = font_content.render("Enjoy the thrill of this retro-style space adventure and test your skills!", True,
                                WHITE)
    line4 = font_content.render("Press 'Esc' to return to the main menu.", True, WHITE)

    while True:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return "menu"

        screen.blit(about_title, (50, 50))
        screen.blit(line1, (50, 100))
        screen.blit(line2, (50, 130))
        screen.blit(line3, (50, 160))
        screen.blit(line4, (50, 190))

        pygame.display.flip()


def game():
    global player_lives, points
    player_x = WIDTH // 2
    player_y = HEIGHT - player_size - 10

    enemy_size = 50
    enemy_speed = 1
    enemies = []

    bullet_speed = 7
    bullets = []

    # Start playing background music
    pygame.mixer.music.play(-1)

    speed_up_timer = pygame.time.get_ticks()  # Initialize the timer
    speed_up_interval = 10000  # Speed up every 10 seconds (in milliseconds)

    # Load enemy image
    enemy_image = pygame.image.load("./enemy.png")  # Replace with the actual path to your enemy image
    enemy_image = pygame.transform.scale(enemy_image, (enemy_size, enemy_size))

    def draw_player(x, y):
        screen.blit(player_image, (x, y))

    def draw_enemy(x, y):
        screen.blit(enemy_image, (x, y))

    def draw_bullet(x, y):
        pygame.draw.rect(screen, WHITE, (x, y, 5, 10))

    last_point_time = pygame.time.get_ticks()

    while True:
        current_time = pygame.time.get_ticks()

        # Add points every 3 seconds
        if current_time - last_point_time >= 3000:
            points += 5
            last_point_time = current_time

        # Speed up enemies every 10 seconds
        if current_time - speed_up_timer >= speed_up_interval:
            enemy_speed += 1  # Increase enemy speed
            speed_up_timer = current_time  # Reset the timer

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    player_x -= player_speed
                elif event.key == pygame.K_d:
                    player_x += player_speed
                elif event.key == pygame.K_SPACE:
                    bullet_sound.play()
                    bullets.append([player_x + player_size // 2 - 2, player_y - 10])

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            player_x -= player_speed
        if keys[pygame.K_d]:
            player_x += player_speed

        screen.fill((0, 0, 0))

        # Display points
        font = pygame.font.Font(None, 36)
        points_text = font.render(f"Points: {points}", True, WHITE)
        screen.blit(points_text, (10, 10))

        # Move and draw bullets
        for bullet in bullets:
            bullet[1] -= bullet_speed
            draw_bullet(bullet[0], bullet[1])

        # Move and draw enemies
        for enemy in enemies:
            enemy[1] += enemy_speed
            draw_enemy(enemy[0], enemy[1])

            # Check for collisions with player
            if (
                    player_x < enemy[0] < player_x + player_size or
                    player_x < enemy[0] + enemy_size < player_x + player_size
            ) and (
                    player_y < enemy[1] < player_y + player_size or
                    player_y < enemy[1] + enemy_size < player_y + player_size
            ):
                player_lives -= 1
                enemies.remove(enemy)

        # Check for collisions with bullets
        for bullet in bullets[:]:
            for enemy in enemies[:]:
                if (
                        enemy[0] < bullet[0] < enemy[0] + enemy_size and
                        enemy[1] < bullet[1] < enemy[1] + enemy_size
                ):
                    bullets.remove(bullet)
                    enemies.remove(enemy)

        # Draw the player
        draw_player(player_x, player_y)

        # Draw remaining lives
        font = pygame.font.Font(None, 36)
        lives_text = font.render(f"Lives: {player_lives}", True, WHITE)
        screen.blit(lives_text, (10, 50))

        # Check for game over
        if player_lives <= 0:
            return "game_over"

        # Spawn new enemies
        if pygame.time.get_ticks() % 100 == 0:
            enemy_x = random.randint(0, WIDTH - enemy_size)
            enemy_y = -enemy_size
            enemies.append([enemy_x, enemy_y])

        pygame.display.flip()
        clock.tick(FPS)


def game_over():
    global player_lives, points
    font = pygame.font.Font(None, 72)
    game_over_text = font.render("Game Over", True, RED)
    retry_button = font.render("Retry", True, WHITE)
    menu_button = font.render("Main Menu", True, WHITE)

    while True:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if 300 <= x <= 500 and 200 <= y <= 250:
                    player_lives = 3  # Reset lives
                    points = 0 # Reset points
                    return "retry"
                elif 300 <= x <= 500 and 300 <= y <= 350:
                    return "menu"

        screen.blit(game_over_text, (200, 100))
        screen.blit(retry_button, (350, 210))
        screen.blit(menu_button, (350, 310))

        pygame.display.flip()

def main():
    pygame.mixer.music.play(-1)

    while True:
        choice = show_menu()

        if choice == "play":
            # player_lives = 3
            result = game()
            if result == "game_over":
                choice = game_over()

                if choice == "retry":
                    continue
                elif choice == "menu":
                    continue

        elif choice == "how_to_play":
            choice = show_how_to_play()  

            if choice == "menu":
                continue

        elif choice == "about":
            choice = show_about()

            if choice == "menu":
                continue



if __name__ == "__main__":
    main()
