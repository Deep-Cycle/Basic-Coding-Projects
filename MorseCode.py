
import pygame
import random




# variables
unit = 60
WIDTH = 560
HEIGHT = 720
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0,0,255)

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Morse Code")

clock = pygame.time.Clock()
start_time = pygame.time.get_ticks()
reset = True
running = True

mode = 'letter'
font_name = pygame.font.match_font('arial')

rect = pygame.Rect(40,40,480,320)
button_rect = pygame.Rect(180,410,200,200)
image1 = pygame.image.load("morse_code_1.jpg")
image1 = pygame.transform.scale(image1,(400,400))
image1.set_colorkey((255,255,255))
image2 = pygame.image.load("morse_code_2.jpg")
image2 = pygame.transform.scale(image2,(400,400))
image2.set_colorkey((255,255,255))

pygame.mixer.music.load('morse_code_sound.wav')


my_final_input = []
the_final_input = ''
word = []
morse_code = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..'
}
morse_code_reversed = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F',
    '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L',
    '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R',
    '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
    '-.--': 'Y', '--..': 'Z'
}
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
           "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]



def dot_dash(time):
    dot_or_dash = ''
    if time > 0.5*unit and time < 2.5*unit:
        dot_or_dash = '.'
    if time > 2.5*unit and 3.5*unit:
        dot_or_dash = '-'
    return dot_or_dash

def check(val1, val2):
    if val1 == val2:
        return True
    else:
        return False

def draw_text(surf, text, size, x, y, color=WHITE):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.centerx = x
    text_rect.top = y
    surf.blit(text_surface, text_rect)







while True:
    if reset:
        screen.fill(WHITE)
        pygame.draw.rect(screen, BLACK, rect)
        screen.blit(image1, (80, 300))
        draw_text(screen, 'Click Mouse To Reset, Move Mouse to Check your answer', 16, WIDTH / 2, HEIGHT / 1.05, BLACK)
        answer = False
        inactive = False
        start_play = True
        my_dotordash = ''
        my_final_input = []
        the_checking_input = ''
        reset = False

    if start_play == True:
        question_letter = random.choice(letters)
        draw_text(screen,'Question: '+question_letter, 64, WIDTH/2, HEIGHT/5,)
        start_play = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                start_time = pygame.time.get_ticks()
                pygame.draw.rect(screen, WHITE, button_rect)
                pygame.mixer.music.play()
                screen.blit(image2, (80, 300))
                inactive = True

        elif event.type == pygame.KEYUP:
            screen.blit(image1, (80, 300))
            pygame.mixer.music.stop()
            if event.key == pygame.K_SPACE:
                end_time = pygame.time.get_ticks()
                duration = (end_time - start_time)
                my_dotordash = dot_dash(duration)

            if my_dotordash != '':
                my_final_input.append(my_dotordash)
        elif event.type == pygame.MOUSEBUTTONUP:
            reset = True

        if inactive:
            elapsed_time = pygame.time.get_ticks() - start_time

            if elapsed_time > 7*unit:
                the_checking_input = ''.join(my_final_input)

                if the_checking_input != '':
                    if mode == 'word':
                        word.append(the_checking_input)

                    if mode == 'letter':
                        my_letter = morse_code_reversed.get(the_checking_input, None)
                        if my_letter is not None:
                            answer = check(question_letter, my_letter)
                            if answer:
                                pygame.draw.rect(screen, GREEN, rect)
                                draw_text(screen, 'Click Mouse To Reset, Move Mouse to Check your answer', 16,
                                          WIDTH / 2, HEIGHT / 1.05, BLACK)
                                draw_text(screen, 'Correct', 32, WIDTH/2, HEIGHT/5)
                                draw_text(screen, 'Question: ' + question_letter, 32, WIDTH / 2, HEIGHT / 3.5)
                                inactive = False

                            else:
                                pygame.draw.rect(screen, RED, rect)
                                draw_text(screen, 'Click Mouse To Reset, Move Mouse to Check your answer', 16,
                                          WIDTH / 2, HEIGHT / 1.05, BLACK)
                                draw_text(screen, 'Incorrect, your answer is: ' + my_letter, 32, WIDTH/2, HEIGHT/5)
                                draw_text(screen, 'Question: ' + question_letter, 32, WIDTH / 2, HEIGHT / 3.5)
                                inactive = False

                        else:
                            pygame.draw.rect(screen, RED, rect)
                            draw_text(screen, 'Click Mouse To Reset, Move Mouse to Check your answer', 16, WIDTH / 2,
                                      HEIGHT / 1.05, BLACK)
                            draw_text(screen, 'Incorrect, your answer is: ' + the_checking_input, 32, WIDTH / 2, HEIGHT / 5)
                            draw_text(screen, 'Question: ' + question_letter, 32, WIDTH / 2, HEIGHT / 3.5)
                            inactive = False


    pygame.display.update()
    clock.tick(240)




