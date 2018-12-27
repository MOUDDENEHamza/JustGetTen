import pygame

from bases import get_random_board, display
from merge import get_adjacent_tiles, modification, gravity
from possibles import get_max_board_value

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PURPLE = (139, 39, 117)
BROWN = (108, 68, 62)
PINK = (219, 128, 199)
VERDE = (31, 89, 6)
ORANGE = (223, 136, 19)
BLACK = (0, 0, 0)

WIDTH = 800
HEIGHT = 600

TILE_ZONE_TOP = 50
TILE_SIDE = 70

" write with white color on rectangle"


def text_objects(text, font):
    textSurface = font.render(text, True, WHITE)
    return textSurface, textSurface.get_rect()


"write with black color"


def overwrite_text(text, font):
    textSurface = font.render(text, True, BLACK)
    return textSurface, textSurface.get_rect()


def put_text_rect(font_size, text, x, y, screen):
    object_text = pygame.font.Font('freesansbold.ttf', font_size)
    object_surface, object_rect = text_objects(text, object_text)
    object_rect.center = (x, y)
    screen.blit(object_surface, object_rect)
    return object_rect


"draw rectangle"


def overwrite_text_rect(font_size, text, x, y, screen):
    pygame.draw.rect(screen, BLACK, (x - 50, y - 20, 100, 40))


def replace_text(font_size, text, x, y, screen):
    overwrite_text_rect(font_size, text, x, y, screen)
    put_text_rect(font_size, text, x, y, screen)


"create our board"


def put_tile(text, x, y, tile_side, screen):
    forground = (5, 5, 5)

    color = None
    if text == 1: color = GREEN
    if text == 2: color = BLUE
    if text == 3: color = ORANGE
    if text == 4: color = RED
    if text == 5: color = VERDE
    if text == 6: color = PURPLE
    if text == 7: color = PINK
    if text == 8: color = YELLOW
    if text == 9: color = BROWN

    tile = pygame.draw.rect(screen, color, (y, x, tile_side, tile_side))
    font = pygame.font.Font(None, 50)
    text = font.render(str(text), 0, forground)
    screen.blit(text, (y - 20 + (tile_side / 2), x - 20 + (tile_side / 2)))
    return tile


"display of game"


def refresh_screen(screen, board):
    screen.fill(BLACK)

    put_text_rect(20, 'Final Score', 650, 50, screen)

    put_text_rect(20, str(get_max_board_value(board)), 650, 100, screen)

    put_text_rect(20, 'Elapsed time', 650, 380, screen)

    play_again_rect = put_text_rect(20, 'Play Again', 650, 200, screen)
    quit_rect = put_text_rect(20, 'Quit', 650, 300, screen)

    tiles = []
    for i in range(len(board)):
        tmp = []
        for j in range(len(board)):
            tile = put_tile(board[i][j], TILE_ZONE_TOP + (TILE_SIDE * i), TILE_ZONE_TOP + (TILE_SIDE * j), TILE_SIDE,
                            screen)

    return tiles


"add a effet on the cells adjacents"


def hover_tiles(screen, adj_tiles):
    for tile in adj_tiles:
        x = TILE_ZONE_TOP + tile[0] * TILE_SIDE
        y = TILE_ZONE_TOP + tile[1] * TILE_SIDE

        pygame.draw.rect(screen, BLACK, pygame.Rect(y, x, TILE_SIDE, TILE_SIDE), 2)


"start"


def start_new_game(level):
    proba = (0.1, 0.2, 0.3)

    board = get_random_board(n=level, proba=proba)
    tiles = []
    hovered = []
    selected = None

    display(board)
    print('level ', level)
    pygame.init()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("JUST GET TEN")

    clock = pygame.time.Clock()

    font_name = pygame.font.match_font('arial')

    put_text_rect(20, 'Final Score', 650, 50, screen)
    score_val_rec = put_text_rect(20, str(get_max_board_value(board)), 650, 100, screen)

    put_text_rect(20, 'Elapsed time', 650, 380, screen)

    play_again_rect = put_text_rect(20, 'Play Again', 650, 200, screen)
    quit_rect = put_text_rect(20, 'Quit', 650, 300, screen)

    tile_zone_top = 50
    tile_side = 70

    for i in range(len(board)):
        tmp = []
        for j in range(len(board)):
            tile = put_tile(board[i][j], tile_zone_top + (tile_side * i), tile_zone_top + (tile_side * j), tile_side,
                            screen)
            tmp.append(tile)

        tiles.append(tmp)

    game_over = False
    start_new = False
    win = False
    time_elapsed = False
    start_ticks = pygame.time.get_ticks()  # starter tick
    warning = False

    while not game_over:

        sec = (pygame.time.get_ticks() - start_ticks) / 1000

        replace_text(20, str(sec), 650, 420, screen)

        if sec >= 25:

            if warning == False:
                pygame.mixer.music.load('ui/tic-tac.mp3')
                pygame.mixer.music.play(0)
                warning = True

        if sec > 30:  # if more than 10 seconds close the game
            game_over = True
            time_elapsed = True

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                game_over = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos

                if play_again_rect.collidepoint(pygame.mouse.get_pos()):
                    game_over = True
                    start_new = True

                if quit_rect.collidepoint(pygame.mouse.get_pos()):
                    game_over = True

                if x > tile_zone_top and x < (level * tile_side) + tile_zone_top:
                    if y > tile_zone_top and y < (level * tile_side) + tile_zone_top:

                        tiles = refresh_screen(screen, board)

                        _y_index = (x - tile_zone_top) // tile_side
                        _x_index = (y - tile_zone_top) // tile_side
                        "get adjacents cells"
                        if selected != None and selected != []:
                            print('merge attempt ..')

                            adjs = get_adjacent_tiles(board, [], _x_index, _y_index)

                            print(selected, adjs)
                            "fusion of cells"
                            if selected in adjs:
                                print('in ajds ?')
                                modification(board, _x_index, _y_index)
                                gravity(board, proba=proba)

                                start_ticks = pygame.time.get_ticks()  # starter tick
                                "if you win"
                                if get_max_board_value(board) == 10:
                                    game_over = True
                                    win = True

                                tiles = refresh_screen(screen, board)
                                selected = []


                            else:

                                print('new selection')

                                tiles = refresh_screen(screen, board)

                                adjacents = get_adjacent_tiles(board, [], _x_index, _y_index)

                                hover_tiles(screen, adjacents)

                                selected = [_x_index, _y_index]

                        else:

                            print('new selection')

                            tiles = refresh_screen(screen, board)

                            adjacents = get_adjacent_tiles(board, [], _x_index, _y_index)

                            hover_tiles(screen, adjacents)

                            selected = [_x_index, _y_index]

        pygame.display.update()
        clock.tick(60)

    if start_new:
        start_new_game(level)
    "if you win we add a sound victory"
    if win:
        # play sound


        pygame.mixer.music.load('ui/win.mp3')
        pygame.mixer.music.play(0)

        start_new_game(level)

    pygame.quit()


def save_game_state():
    pass


def load_game_state():
    pass


"the function display the menu in excution"


def game_ui_init():
    pygame.init()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("JUST GET TEN")

    clock = pygame.time.Clock()

    font_name = pygame.font.match_font('arial')

    hard = put_text_rect(20, '1 - New Game (hard) 4 x 4', 350, 150, screen)
    medium = put_text_rect(20, '2 - New Game (medium) 5 x 5', 350, 200, screen)
    easy = put_text_rect(20, '3 - New Game (easy) 6 x 6', 350, 250, screen)
    load = put_text_rect(20, '4 - Load saved game', 350, 300, screen)

    choosed = False
    new_game = False
    load_game = False
    level = 5

    while not choosed:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                choosed = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos

                if hard.collidepoint(pygame.mouse.get_pos()):
                    new_game = True
                    level = 4
                    load_game = False
                    choosed = True

                if medium.collidepoint(pygame.mouse.get_pos()):
                    new_game = True
                    level = 5
                    load_game = False
                    choosed = True

                if easy.collidepoint(pygame.mouse.get_pos()):
                    new_game = True
                    level = 6
                    load_game = False
                    choosed = True

                if load.collidepoint(pygame.mouse.get_pos()):
                    load_game = True
                    new_game = False
                    choosed = True

        pygame.display.update()
        clock.tick(60)
    pygame.quit()

    if new_game:
        start_new_game(level)

    if load_game:
        load_game_state()

    quit()


game_ui_init()
