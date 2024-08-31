import pygame
import sys

pygame.init()

start_screen_image = pygame.image.load('Tic (1).png')
grid_image = pygame.image.load('Tic.png')


pygame.mixer.music.load('clock.mp3')  
pygame.mixer.music.set_volume(0.5)  


screen_size = start_screen_image.get_size()
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Tic-Tac-Toe")

x_image = pygame.image.load('x_mark.png')
o_image = pygame.image.load('o_mark.png')

hex_size = (60, 60)
x_image = pygame.transform.scale(x_image, hex_size)
o_image = pygame.transform.scale(o_image, hex_size)

musicon_image = pygame.image.load('musicon.png')
musicoff_image = pygame.image.load('musicoff.png')
musicon_image = pygame.transform.scale(musicon_image, hex_size)
musicoff_image = pygame.transform.scale(musicoff_image, hex_size)


slider_rect = pygame.Rect(110, screen_size[1] - 20, 100, 10)  
knob_rect = pygame.Rect(110, screen_size[1] - 25, 10, 20)  
is_dragging = False  
volume_level = 0.5  

# Define button areas
start_button_rect = pygame.Rect(145, 230, 70, 160)  
guide_button_rect = pygame.Rect(145, 340, 70, 230)  
music_button_rect = pygame.Rect(10, screen_size[1] - 70, 100, 40)  


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GRAY = (200, 200, 200)

# Game variables
current_player = "X"
board = [""] * 9  # Empty board for 9 positions
player_names = ["Player 1", "Player 2"]
player_scores = [0, 0]  # Player 1 and Player 2 scores
tie_score = 0  # Tie score
game_winner = None
music_on = True  # Music state

pygame.mixer.music.play(-1)  


hex_centers = [
    (313, 213), (400, 260), (490, 213),  # Top row
    (313, 313), (400, 360), (490, 313),  # Middle row
    (313, 413), (400, 460), (490, 413)   # Bottom row
]

# Function to draw X or O mark on the grid
def draw_mark(center, player):
    if player == "X":
        mark_image = x_image
    else:
        mark_image = o_image
    mark_rect = mark_image.get_rect(center=center)
    screen.blit(mark_image, mark_rect)

# Function to check if there's a winner
def check_win(board):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] != "":
            return board[condition[0]], condition  # Return both winner and winning positions
    return None, []

# Function to check if the board is full
def is_board_full(board):
    return all(mark != "" for mark in board)

# Function to reset the board
def reset_board():
    global board
    board = [""] * 9

# Function to make the winning mark bounce once
def bounce_winning_marks(positions, player):
    for i in range(-5, 6):  # Move up and down once
        screen.blit(grid_image, (0, 0))  # Redraw the grid
        for index, mark in enumerate(board):
            if mark:
                center = hex_centers[index]
                if index in positions:  # Bounce winning marks
                    draw_mark((center[0], center[1] + i), player)
                else:
                    draw_mark(center, mark)
        pygame.display.flip()
        pygame.time.wait(30)

# Function to handle the Tic-Tac-Toe game logic
def tic_tac_toe_game():
    global current_player, player_scores, tie_score, game_winner
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                # Check for music button click
                if music_button_rect.collidepoint(mouse_pos):
                    toggle_music()  # Toggle music on/off
                # Check for hex click
                for index, center in enumerate(hex_centers):
                    if board[index] == "" and (mouse_pos[0] - center[0]) ** 2 + (mouse_pos[1] - center[1]) ** 2 < 5000:
                        board[index] = current_player
                        draw_mark(center, current_player)
                        winner, win_positions = check_win(board)
                        if winner:
                            if winner == "X":
                                player_scores[0] += 1
                            else:
                                player_scores[1] += 1
                            bounce_winning_marks(win_positions, winner)  # Bounce winning marks once
                            if player_scores[0] == 3 or player_scores[1] == 3:
                                game_winner = winner
                                running = False
                            else:
                                reset_board()
                        elif is_board_full(board):
                            tie_score += 1
                            reset_board()
                        current_player = "O" if current_player == "X" else "X"
                        break

        screen.blit(grid_image, (0, 0))

        # Draw the scoreboard
        font = pygame.font.Font(None, 36)
        score_text = f"{player_names[0]} - {player_scores[0]}  |  TIE - {tie_score}  |  {player_names[1]} - {player_scores[1]}"
        score_surface = font.render(score_text, True, BLACK)
        screen.blit(score_surface, (screen_size[0]//2 - score_surface.get_width()//2, 20))

        # Draw music toggle button
        draw_music_button()

        for index, mark in enumerate(board):
            if mark:
                draw_mark(hex_centers[index], mark)

        pygame.display.flip()

    # Display the final winner
    font = pygame.font.Font(None, 72)
    winner_text = f"{player_names[0] if game_winner == 'X' else player_names[1]} wins the game!"
    winner_surface = font.render(winner_text, True, BLACK)
    screen.blit(winner_surface, (screen_size[0]//2 - winner_surface.get_width()//2, screen_size[1]//2 - winner_surface.get_height()//2))
    pygame.display.flip()
    pygame.time.wait(3000)

# Function to display name input pop-up for both players
def name_input_popups():
    global player_names
    font = pygame.font.Font(None, 36)
    
    # Input boxes for both players
    input_box_1 = pygame.Rect(10, 10, 200, 50)  # Upper left
    input_box_2 = pygame.Rect(screen_size[0] - 210, 10, 200, 50)  # Upper right
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color_1, color_2 = color_inactive, color_inactive
    active_1, active_2 = False, False
    text_1, text_2 = '', ''
    done_1, done_2 = False, False

    while not (done_1 and done_2):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Check if the user clicked on the input boxes
                if input_box_1.collidepoint(event.pos):
                    active_1 = True
                    active_2 = False
                elif input_box_2.collidepoint(event.pos):
                    active_2 = True
                    active_1 = False
                else:
                    active_1 = False
                    active_2 = False
                # Change the current color of the input boxes
                color_1 = color_active if active_1 else color_inactive
                color_2 = color_active if active_2 else color_inactive
            elif event.type == pygame.KEYDOWN:
                if active_1:
                    if event.key == pygame.K_RETURN:
                        player_names[0] = text_1
                        done_1 = True
                    elif event.key == pygame.K_BACKSPACE:
                        text_1 = text_1[:-1]
                    else:
                        text_1 += event.unicode
                elif active_2:
                    if event.key == pygame.K_RETURN:
                        player_names[1] = text_2
                        done_2 = True
                    elif event.key == pygame.K_BACKSPACE:
                        text_2 = text_2[:-1]
                    else:
                        text_2 += event.unicode

        screen.blit(grid_image, (0, 0))  # Redraw grid behind input boxes
        pygame.draw.rect(screen, color_1, input_box_1, 2)
        text_surface_1 = font.render(text_1, True, color_1)
        screen.blit(text_surface_1, (input_box_1.x+5, input_box_1.y+5))
        
        # Draw input box for player 2
        pygame.draw.rect(screen, color_2, input_box_2, 2)
        text_surface_2 = font.render(text_2, True, color_2)
        screen.blit(text_surface_2, (input_box_2.x+5, input_box_2.y+5))
        
        pygame.display.flip()

# Function to display the guide
def display_guide():
    guide_rect = pygame.Rect(200, 100, 500, 400)
    close_button_rect = pygame.Rect(guide_rect.x + guide_rect.width - 30, guide_rect.y, 20, 20)
    showing_guide = True

    while showing_guide:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if close_button_rect.collidepoint(event.pos):
                    showing_guide = False

        # Draw guide rectangle
        pygame.draw.rect(screen, WHITE, guide_rect)
        pygame.draw.rect(screen, RED, close_button_rect)

        # Draw "X" on close button
        font = pygame.font.Font(None, 36)
        close_text = font.render('X', True, WHITE)
        screen.blit(close_text, (close_button_rect.x + 5, close_button_rect.y))

        # Draw guide text
        guide_font = pygame.font.Font(None, 28)
        guide_text = ["Guide:", "1. Click on a hex to place your mark.", "2. Marks are either X or O.", "3. First to align 3 marks wins!"]
        for i, line in enumerate(guide_text):
            text_surface = guide_font.render(line, True, BLACK)
            screen.blit(text_surface, (guide_rect.x + 20, guide_rect.y + 40 + i * 30))

        pygame.display.flip()

# Function to toggle music on or off
def toggle_music():
    global music_on
    if music_on:
        pygame.mixer.music.pause()
    else:
        pygame.mixer.music.play(-1)  # Start the music from the beginning
    music_on = not music_on

# Function to draw the music button
def draw_music_button():
    music_button_image = musicon_image if music_on else musicoff_image
    screen.blit(music_button_image, music_button_rect)




def draw_volume_slider():
    # Draw slider bar
    pygame.draw.rect(screen, GRAY, slider_rect)
    # Draw knob
    pygame.draw.rect(screen, RED, knob_rect)

# Function to handle volume slider movement
def handle_volume_slider(mouse_pos):
    global is_dragging, volume_level
    if is_dragging:
        # Constrain the knob movement within the slider
        new_x = max(slider_rect.x, min(mouse_pos[0], slider_rect.x + slider_rect.width - knob_rect.width))
        knob_rect.x = new_x
        # Calculate volume based on knob position
        volume_level = (knob_rect.x - slider_rect.x) / (slider_rect.width - knob_rect.width)
        pygame.mixer.music.set_volume(volume_level)

# Update the start interface function to include volume adjustment
def start_interface():
    global is_dragging

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if start_button_rect.collidepoint(event.pos):
                    # Show the game grid first, then input names
                    screen.blit(grid_image, (0, 0))
                    pygame.display.flip()
                    name_input_popups()
                    tic_tac_toe_game()
                elif guide_button_rect.collidepoint(event.pos):
                    display_guide()
                elif music_button_rect.collidepoint(event.pos):
                    toggle_music()  # Toggle music on/off
                elif knob_rect.collidepoint(event.pos):
                    is_dragging = True  # Start dragging the knob
            elif event.type == pygame.MOUSEBUTTONUP:
                is_dragging = False  # Stop dragging the knob
            elif event.type == pygame.MOUSEMOTION and is_dragging:
                handle_volume_slider(event.pos)  # Adjust volume based on knob movement

        screen.blit(start_screen_image, (0, 0))
        draw_music_button()
        draw_volume_slider()  # Draw volume slider
        pygame.display.flip()

# Run the start interface
start_interface()
