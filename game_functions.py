import sys
from time import sleep
import pygame
from bullet import Bullet
from alien import Alien


def check_events(ai_settings, screen, ship, bullets, aliens, stats, play_button, sb):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():  # NOTE: Our event loop, watch key events.
        if event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, aliens, bullets, stats)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, play_button, ship, aliens, bullets, mouse_x, mouse_y, sb)


def start_game(ai_settings, screen, ship, aliens, bullets, stats):
    """Start game."""
    # Start up sound
    pygame.mixer.init()
    sound = pygame.mixer.Sound('sounds/361261__japanyoshithegamer__8-bit-spaceship-startup.wav')
    sound.play()
    sleep(2)  # Delay movement of the aliens
    
    # Reset game settings whenever a new game starts
    ai_settings.initialize_dynamic_settings()

    # Hide mouse cursor when game starts
    pygame.mouse.set_visible(False)

    # Reset game stats
    stats.reset_stats()

    stats.game_active = True

    # Empty list of aliens and bullets
    aliens.empty()
    bullets.empty()

    # Create new fleet and center ship
    create_fleet(ai_settings, screen, ship, aliens)
    ship.center_ship()

def check_play_button(ai_settings, screen, stats, play_button, ship, aliens, bullets, mouse_x, mouse_y, sb):
    """Start a new game when the player clicks Play."""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)

    if button_clicked and not stats.game_active:
        ai_settings.initialize_dynamic_settings()
        # Reset the score and level images
        sb.prep_images()
        stats.write_score()
        start_game(ai_settings, screen, ship, aliens, bullets, stats)

def check_keydown_events(event, ai_settings, screen, ship, aliens, bullets, stats):
    """Respond to keypresses."""
    if event.key == pygame.K_q:
        # NOTE: Exit the running process for our game, ie quit the game.
        stats.write_score()
        sys.exit()
    elif event.key == pygame.K_p:
        # start game on key press of p
        start_game(ai_settings, screen, ship, aliens, bullets, stats)
    elif event.key == pygame.K_RIGHT:
        # Move the ship rect to the right.
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        # Move the ship rect to the left.
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    # TODO: Add pause event if game_active && press p


def fire_bullet(ai_settings, screen, ship, bullets):
    """Fire bullet if limit not reached yet."""

    if len(bullets) < ai_settings.bullets_allowed:
        # Sound
        pygame.mixer.init()
        sound = pygame.mixer.Sound('sounds/126423__cabeeno-rossley__shoot-laser.wav')
        sound.play()

        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def update_bullets(ai_settings, screen, ship, aliens, bullets, stats, sb):
    """Update position of bullets and get rid of old bullets."""
    # Check for any bullets that have hit aliens. If so, remove bullet-alien.
    check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets, stats, sb)

    bullets.update()  # Change position of existing bullets

    for bullet in bullets.copy():  # Remove old bullets
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def check_high_score(stats, sb):
    """Check to see if there's a new high score."""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()

def check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets, stats, sb):
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    # Update score
    if collisions:
        for aliens in collisions.values():
            # Sound
            pygame.mixer.init()
            sound = pygame.mixer.Sound('sounds/222575__coby12388__bombhit01.wav')
            sound.play()

            stats.score += ai_settings.alien_points * len(aliens)
            sb.prep_score()
            check_high_score(stats, sb)

    if len(aliens) == 0:
        # Destroy esisting bullets, create new fleet.
        bullets.empty()
        ai_settings.increase_speed()
        start_new_level(stats, sb)
        create_fleet(ai_settings, screen, ship, aliens)

def start_new_level(stats, sb):
    """Start a new game level."""
    # Sound
    pygame.mixer.init()
    sound = pygame.mixer.Sound('sounds/126422__cabeeno-rossley__level-up.wav')
    sound.play()
    
    # Increase the player's level if they can destroy the fleet
    stats.level += 1
    # Re-draw the level image
    sb.prep_level()
    
    sleep(2)

def check_keyup_events(event, ship):
    """Respond to key releases."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def update_screen(ai_settings, screen, ship, aliens, bullets, stats, play_button, sb):
    # Redraw screen each pass of the loop and fill bg.
    screen.fill(ai_settings.bg_color)
    # Draw each bullet in bullets set
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    # Draw ship
    ship.blitme()
    # Draws each element in a group
    aliens.draw(screen)
    # Draw score
    sb.prep_images()
    sb.show_score()
    # Draw play button only if game hasn't started
    if not stats.game_active:
        play_button.draw_button()
    # Make the most recently drawn screen visible.
    pygame.display.flip()


def get_number_aliens_x(ai_settings, alien_width):
    """Determine the number of aliens that fit in a row."""
    available_space_x = ai_settings.screen_width - (2 * alien_width)
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """Create an alien and add to group."""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def get_number_rows(ai_settings, ship_height, alien_height):
    """Determine the number of rows of aliens that fit on the screen."""
    available_space_y = (ai_settings.screen_height - (3 * alien_height - ship_height))
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def create_fleet(ai_settings, screen, ship, aliens):
    """Create a full fleet of aliens."""

    # Create an alien and place it in the row.
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

    # Create the fleet of aliens
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)


def update_aliens(ai_settings, stats, screen, ship, aliens, bullets, sb):
    """Update the positions of all aliens in the fleet."""
    # Check if any aliens are beyond screen edges, if so change direction
    check_fleet_edges(ai_settings, aliens)
    check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets, sb)
    aliens.update()

    # Look for alien-ship collisions

    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, ship, aliens, bullets, sb)
        check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets, sb)

def check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets, sb):
    """Check if any aliens have reached bottom of screen."""
    screen_rect = screen.get_rect()

    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # Treat this the same as if ship got hit
            ship_hit(ai_settings, stats, screen, ship, aliens, bullets, sb)
            break


def check_fleet_edges(ai_settings, aliens):
    """Respond appropriately if any aliens have reached an edge."""
    for alien in aliens.sprites():
        # If alien sprite is past the edge of the screen:
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def change_fleet_direction(ai_settings, aliens):
    """Drop the entire fleet and change the fleet's direction."""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed

    ai_settings.fleet_direction *= -1


def ship_hit(ai_settings, stats, screen, ship, aliens, bullets, sb):
    """Respond to ship being hit."""
    # Sound
    pygame.mixer.init()
    sound = pygame.mixer.Sound('sounds/382310__myfox14__game-over-arcade.wav')
    sound.play()

    # Decrement ships_left by 1
    if stats.ships_left > 0:
        stats.ships_left -= 1
        sleep(0.5)
    
    # Update scoreboard
    sb.prep_ships()

    if stats.ships_left < 1:
        stats.game_active = False
        pygame.mouse.set_visible(True)
        stats.write_score()
        print('game over')
        # TODO: Change message at end to 'game over'
    else:
        # Empty the list of aliens and bullets
        aliens.empty()
        bullets.empty()

        # Create new fleet and center ship
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

        # Dramatic pause
        sleep(0.5)
