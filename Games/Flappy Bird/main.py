import pygame, sys, random, math, os

def draw_floor(w):
    screen.blit(floor_surface, (floor_x_pos, round(h*0.88)))
    screen.blit(floor_surface, (floor_x_pos + w, round(h*0.88)))

def create_pipe():
    # random_pipe_pos = random.choice(pipe_height)
    random_pipe_pos = random.randrange(400, 800, 100)
    bottom_pipe = pipe_surface.get_rect(midtop = (700, random_pipe_pos))
    top_pipe = pipe_surface.get_rect(midbottom = (700, random_pipe_pos - 300))
    return bottom_pipe, top_pipe

def move_pipes(pipes):
    for pipe in pipes:
        pipe.centerx -= 4
    return pipes

def delete_pipes(pipes):
    if pipes and pipes[0].centerx < 0:
        pipes.pop(0)
    return pipes

def draw_pipe(pipes):
    for pipe in pipes:
        if pipe.bottom >= h:
            screen.blit(pipe_surface, pipe)
        else:
            flip_pipe = pygame.transform.flip(pipe_surface, False, True)
            screen.blit(flip_pipe, pipe)

def check_collision(pipes):
    for pipe in pipes:
        if bird_rect.colliderect(pipe):
            death_sound.play()
            return False
    if bird_rect.top <= -100 or bird_rect.bottom >= round(h*0.88):
        death_sound.play()
        return False
    return True

def rotate_bird(bird):
    new_bird = pygame.transform.rotozoom(bird, -bird_movement*2.5, 1)
    return new_bird

def bird_animation():
    new_bird = bird_frames[bird_index]
    new_bird_rect = new_bird.get_rect(center = (100, bird_rect.centery))
    return new_bird, new_bird_rect

def increase_score(pipes):
    global score
    for pipe in pipes:
        if pipe.centerx == 96:
            score += 0.5
            score_sound.play()

def score_display(game_state):
    if game_state == 'main_game':
        score_surface = game_font.render(str(math.floor(score)), True, (255, 255, 255))
        score_rect = score_surface.get_rect(center = (288, 100))
        screen.blit(score_surface, score_rect)
    if game_state == 'game_over':
        score_surface = game_font.render(f'Score: {math.floor(score)}', True, (255, 255, 255))
        score_rect = score_surface.get_rect(center = (288, 100))
        screen.blit(score_surface, score_rect)

        highest_score_surface = game_font.render(f'Highest Score: {math.floor(highest_score)}', True, (255, 255, 255))
        highest_score_rect = highest_score_surface.get_rect(center = (288, 850))
        screen.blit(highest_score_surface, highest_score_rect)

# Main
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
pygame.mixer.pre_init(frequency = 44100, size = 16, channels = 1, buffer = 512)
pygame.init()
screen = pygame.display.set_mode((576, 1024))
clock = pygame.time.Clock()
game_font = pygame.font.Font(os.path.join(__location__, 'FlappyBird_Python-master/04B_19.ttf'), 40)

# Game variables
gravity = 0.2
bird_movement = 0
game_active = False
score = 0
highest_score = 0

w, h = pygame.display.get_surface().get_size()
bg_surface = pygame.image.load(os.path.join(__location__, 'assets/background-day.png')).convert()
bg_surface = pygame.transform.scale(bg_surface, (w, h))

floor_surface = pygame.image.load(os.path.join(__location__, 'assets/base.png')).convert()
floor_surface = pygame.transform.scale2x(floor_surface)
w_floor = floor_surface.get_width()
floor_x_pos = 0

bird_downflap = pygame.transform.scale2x(pygame.image.load(os.path.join(__location__, 'assets/bluebird-downflap.png')).convert_alpha())
bird_midflap = pygame.transform.scale2x(pygame.image.load(os.path.join(__location__, 'assets/bluebird-midflap.png')).convert_alpha())
bird_upflap = pygame.transform.scale2x(pygame.image.load(os.path.join(__location__, 'assets/bluebird-upflap.png')).convert_alpha())
bird_frames = [bird_downflap, bird_midflap, bird_upflap]
bird_index = 0
bird_surface = bird_frames[bird_index]
bird_rect = bird_surface.get_rect(center = (100, round(round(h*0.88)/2)))
BIRDFLAP = pygame.USEREVENT + 1
pygame.time.set_timer(BIRDFLAP, 200)
"""
bird_surface = pygame.image.load('assets/bluebird-midflap.png').convert_alpha()
bird_surface = pygame.transform.scale2x(bird_surface)
bird_rect = bird_surface.get_rect(center = (100, round(round(h*0.88)/2)))
"""

pipe_surface = pygame.image.load(os.path.join(__location__, 'assets/pipe-green.png')).convert()
pipe_surface = pygame.transform.scale2x(pipe_surface)
pipe_list = []
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, 1200)
pipe_height = [400, 600, 800]

game_over_surface = pygame.transform.scale2x(pygame.image.load(os.path.join(__location__, 'assets/message.png')).convert_alpha())
game_over_rect = game_over_surface.get_rect(center = (288, 500))

flap_sound = pygame.mixer.Sound(os.path.join(__location__, 'sound/sfx_wing.wav'))
death_sound = pygame.mixer.Sound(os.path.join(__location__, 'sound/sfx_die.wav'))
score_sound = pygame.mixer.Sound(os.path.join(__location__, 'sound/sfx_point.wav'))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_active:
                bird_movement = -8
                flap_sound.play()
            if event.key == pygame.K_SPACE and game_active == False:
                game_active = True
                pipe_list.clear()
                bird_rect.center = (100, 512)
                bird_movement = 0
                score = 0

        if event.type == SPAWNPIPE:
            pipe_list.extend(create_pipe())

        if event.type == BIRDFLAP:
            if bird_index == 2:
                bird_index = 0
            else:
                bird_index += 1
            bird_surface, bird_rect = bird_animation()

    #Background
    screen.blit(bg_surface, (0, 0))
    
    if game_active:
        #Bird
        bird_movement += gravity
        rotated_bird = rotate_bird(bird_surface)
        bird_rect.centery += bird_movement
        screen.blit(rotated_bird, bird_rect)

        #Pipes
        pipe_list = move_pipes(pipe_list)
        pipe_list = delete_pipes(pipe_list)
        draw_pipe(pipe_list)

        game_active = check_collision(pipe_list)

        #Score
        increase_score(pipe_list)
        score_display('main_game')
    else:
        if score > highest_score:
            highest_score = score
        screen.blit(game_over_surface, game_over_rect)
        score_display('game_over')

    #Floor
    draw_floor(w_floor)
    floor_x_pos -= 1
    if floor_x_pos == - w_floor:
        floor_x_pos = 0

    pygame.display.update()
    clock.tick(120)     # FPS
