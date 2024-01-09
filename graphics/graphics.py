import pygame
import sys


class GraphicsEngine:

    def __init__(self):
        pygame.init()
        info_object = pygame.display.Info()
        self.screen_width = 600 # Lățimea ferestrei
        self.screen_height = 400 # Înălțimea ferestrei
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Labyrinth Game")

        self.cell_size = min(self.screen_width // 20, self.screen_height // 15)  # Calculăm dimensiunea celulei
        self.game_width = self.screen_width // self.cell_size  # Calculăm lățimea labirintului
        self.game_height = self.screen_height // self.cell_size  # Calculăm înălțimea labirintului

        self.player_pos = [0, 0]  # Poziția inițială a jucătorului

    def handle_movement(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.move_player(-1, 0)
            elif event.key == pygame.K_RIGHT:
                self.move_player(1, 0)
            elif event.key == pygame.K_UP:
                self.move_player(0, -1)
            elif event.key == pygame.K_DOWN:
                self.move_player(0, 1)

    def move_player(self, dx, dy):
        final_x, final_y = self.game.find_final_position()
        new_x = self.player_pos[0] + dx
        new_y = self.player_pos[1] + dy

        # Verificăm coliziunile cu zidurile folosind dimensiunile labirintului
        if 0 <= new_x < self.game_width and 0 <= new_y < self.game_height:
            # Verificăm dacă celula este liberă (1 reprezintă un zid, 0 reprezintă un spațiu liber)
            if self.game.labirint[new_y][new_x] != 1:
                self.player_pos = [new_x, new_y]

                #Verificare dacă jucătorul a ajuns la poziția finală
                if (new_x, new_y) == (final_x, final_y):
                    self.is_game_over = True

    def draw_labirint(self):
        for y in range(self.game_height):
            for x in range(self.game_width):
                if (x, y) == (0, 0):  # Poziția pentru căsuța de start
                    pygame.draw.rect(
                        self.screen, self.game.start_color,
                        (x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size)
                    )
                elif (x, y) == (self.game_width - 1, self.game_height - 1):  # Poziția pentru căsuța finală
                    pygame.draw.rect(
                        self.screen, self.game.finish_color,
                        (x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size)
                    )
                elif self.game.labirint[y][x] == 1:
                    pygame.draw.rect(
                        self.screen, (0, 0, 0),
                        (x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size)
                    )
                elif (x, y) == tuple(self.player_pos):  # Poziția pentru jucător
                    pygame.draw.rect(
                        self.screen, (255, 165, 0),
                        (x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size)
                    )

        # pygame.draw.rect(
        #     self.screen, (255, 165, 0),
        #     (self.player_pos[0] * self.cell_size, self.player_pos[1] * self.cell_size, self.cell_size, self.cell_size)
        # )

    def update_screen(self):
        self.screen.fill((255, 255, 255))  # Umple ecranul cu alb
        self.draw_labirint()

        if self.is_game_over:
            self.draw_end_menu()
        pygame.display.flip()

    def draw_end_menu(self):
        # Desenează fundalul pentru meniu
        pygame.draw.rect(self.screen, (200, 200, 200), (100, 100, 400, 200))

        # Desenează textul pentru întrebare
        font = pygame.font.Font(None, 36)
        text = font.render("Would you like to play again?", True, (0, 0, 0))
        self.screen.blit(text, (150, 130))

        # Desenează butoanele pentru da și nu
        pygame.draw.rect(self.screen, (178, 26, 39), (150, 170, 100, 50))  # Butonul Da
        pygame.draw.rect(self.screen, (0, 100, 0), (350, 170, 100, 50))  # Butonul Nu

        # Text pentru butoane
        # Obține dimensiunea ecranului și obiectul de tip font
        screen_rect = self.screen.get_rect()
        font = pygame.font.Font(None, 36)

        # Creează textele pentru butoane
        text_da = font.render("YES", True, (255, 255, 255))
        text_nu = font.render("NO", True, (255, 255, 255))

        # Obține dreptunghiurile pentru textele butoanelor
        text_da_rect = text_da.get_rect()
        text_nu_rect = text_nu.get_rect()

        # Centrare text "YES" și "NO" în mijlocul ecranului pentru axa x
        text_da_rect.centerx = screen_rect.centerx - 100  # Centrul pentru butonul "YES"
        text_nu_rect.centerx = screen_rect.centerx + 100  # Centrul pentru butonul "NO"

        # Setează coordonatele pentru axa y
        text_da_rect.y = 180
        text_nu_rect.y = 180

        # Desenează textele butoanelor pe ecran la noile poziții calculate
        self.screen.blit(text_da, text_da_rect)
        self.screen.blit(text_nu, text_nu_rect)

    def run_game(self, game):

        self.game = game
        self.is_game_over = False

        while True:
            self.update_screen()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                    self.handle_movement(event)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    if self.is_game_over:
                        if 150 <= mouse_x <= 250 and 170 <= mouse_y <= 220:  # Verificare pentru butonul "Da"
                            # Logica pentru acțiunea atunci când este apăsat butonul "Da"
                            self.game.reset_labirint()  # Generare labirint nou
                            self.is_game_over = False  # Resetare starea jocului
                            self.player_pos = [0, 0]  # Resetează poziția jucătorului
                        elif 350 <= mouse_x <= 450 and 170 <= mouse_y <= 220:  # Verificare pentru butonul "Nu"
                            # Logica pentru acțiunea atunci când este apăsat butonul "Nu"
                            sys.exit()  # Sau orice altceva dorești să faci atunci când utilizatorul apasă "Nu"
            self.update_screen()  # Actualizează ecranul

