import pygame
import sys
from settings import *
from level import Level
from camera import CameraGroup
from button import Button
from pause import *
from npc import Dialogue, Execution, NPC

class Interface:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.button_sfx = pygame.mixer.Sound("images/music/button_sfx.mp3")
        self.font = pygame.font.Font('freesansbold.ttf', FONT_SIZE)
        self.music_sfx = pygame.mixer.Sound("images/music/music_background.mp3")
        self.vol = 0.1
        self.music_sfx.play(loops=-1)
        self.music_sfx.set_volume(self.vol)

    def main_menu(self):
        # Load images
        startstatic_img = pygame.image.load('images/button/start_static.png')
        starthover_img = pygame.image.load('images/button/start_hover.png')
        quitstatic_img = pygame.image.load('images/button/quit_static.png')
        quithover_img = pygame.image.load('images/button/quit_hover.png')
        optionhover_img = pygame.image.load('images/button/opt_hover.png')
        optionstatic_img = pygame.image.load('images/button/opt_static.png')

        background_image = pygame.image.load('images/background/mane_background1.jpg')
        background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

        title_img = pygame.image.load('images/title.png')
        title_img = pygame.transform.scale(title_img, (600, 350))

        image_rect = startstatic_img.get_rect()
        image_x = (WIDTH - image_rect.width) // 2

        start_button = Button(image_x, 400, startstatic_img, starthover_img, (200, 100))
        quit_button = Button(image_x, 500, quitstatic_img, quithover_img, (200, 100))
        option_button = Button(10, 10, optionstatic_img, optionhover_img, (75, 75))

        while True:
            self.screen.blit(background_image, (0, 0))
            self.screen.blit(title_img, (400, 80))

            if start_button.draw(self.screen):
                self.button_sfx.play()
                self.music_sfx.set_volume(0)
                return "start"

            if quit_button.draw(self.screen):
                self.button_sfx.play()
                return "quit"

            if option_button.draw(self.screen):
                self.button_sfx.play()
                return "option"

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()

    def option(self):
        # Load images
        volup_static = pygame.image.load('images/button/vol_up.png')
        volup_hover = pygame.image.load('images/button/vol_up-hover.png')
        voldown_static = pygame.image.load('images/button/vol_down-static.png')
        voldown_hover = pygame.image.load('images/button/vol_down-hover.png')
        volmute_static = pygame.image.load('images/button/vol_mute-static.png')
        volmute_hover = pygame.image.load('images/button/vol_mute-hover.png')
        back_static = pygame.image.load('images/button/back_static.png')
        back_hover = pygame.image.load('images/button/back_hover.png')

        background_image = pygame.image.load('images/background/mane_background1.jpg')
        background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

        vol_up_button = Button(425, 200, volup_static, volup_hover, (200, 100))
        vol_down_button = Button(625, 200, voldown_static, voldown_hover, (200, 100))
        vol_mute_button = Button(425, 300, volmute_static, volmute_hover, (408, 100))
        back_button = Button(5, 640, back_static, back_hover, (150, 80))

        while True:
            self.screen.fill('grey')
            self.screen.blit(background_image, (0, 0))

            if vol_up_button.draw(self.screen):
                self.button_sfx.play()
                self.adjust_volume(0.1)

            if vol_down_button.draw(self.screen):
                self.button_sfx.play()
                self.adjust_volume(-0.1)

            if vol_mute_button.draw(self.screen):
                self.button_sfx.play()
                self.music_sfx.set_volume(0)

            if back_button.draw(self.screen):
                self.button_sfx.play()
                return "back"  # name option back button as back 

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()

    def story_info(self):
        # Define messages with multiple layers
        messages = [
            [
                {"text": "In the fog-drenched streets of Arcadia, a series of grisly murder shatters",
                 "color": WHITE,
                 "position": (25, 250)},
                {"text": "the tranquility of its residents.",
                 "color": WHITE,
                 "position": (400, 300)},
            ],
            [
                {"text": "Its’s 7am in the morning and you discovered the victim’s body laying",
                 "color": WHITE,
                 "position": (60, 250)},
                {"text": "in the village of Arcadia and the blood was still damped which means",
                 "color": WHITE,
                 "position": (70, 300)},
                {"text": "the killing happened not long ago",
                 "color": WHITE,
                 "position": (380, 350)}
            ],
            [
                {"text": "You, as a seasoned detective, are tasked with unraveling the mystery",
                 "color": WHITE,
                 "position": (70, 250)},
                {"text": "behind these brutal killings. Come on detective,",
                 "color": WHITE,
                 "position": (260, 300)},
                {"text": "let’s not waste any time and find the murderer before it’s too late!",
                 "color": WHITE,
                 "position": (100, 350)}
            ]
        ]

        # Load the new background image
        new_background_image = pygame.image.load('images/background/background2.jpg')
        new_background_image = pygame.transform.scale(new_background_image, (WIDTH, HEIGHT))

        # Main loop
        active_message = 0
        layer_counter = 0
        speed = 10  # Adjust the speed of typewriter effect
        scroll_speed = 1  # Adjust the speed of background scrolling
        background_x = 0  # Initialize background_x

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN and active_message < len(messages) - 1:
                        active_message += 1
                        layer_counter = 0  # Reset the layer counter when changing message
                    elif event.key == pygame.K_RETURN and active_message == len(messages) - 1 and layer_counter >= speed * len(messages[active_message][-1]["text"]):
                        return "start_game"  # Signal to start the game

            # Scroll the background
            background_x -= scroll_speed
            if background_x <= -WIDTH:  # Reset background position to create endless scrolling effect
                background_x = 0

            # Clear the screen
            self.screen.fill(BLACK)

            # Display the new background
            self.screen.blit(new_background_image, (background_x, 0))
            if background_x < 0:
                self.screen.blit(new_background_image, (background_x + WIDTH, 0))

            # Display messages for the active layer
            for i, layer in enumerate(messages[active_message]):
                text = layer["text"]
                color = layer["color"]
                position = layer["position"]

                if layer_counter < speed * len(text):
                    layer_counter += 1

                text_surface = self.font.render(text[0:layer_counter // speed], True, color)
                text_rect = text_surface.get_rect(topleft=position)

                # Create a semi-transparent box behind the text
                box_rect = pygame.Rect(text_rect.x - 10, text_rect.y - 5, text_rect.width + 20, text_rect.height + 10)
                pygame.draw.rect(self.screen, (0, 0, 0, 100), box_rect)  # 100 is the alpha value for transparency

                # Blit text surface onto the screen
                self.screen.blit(text_surface, text_rect)

            pygame.display.flip()

    def adjust_volume(self, vol_change):
        self.vol += vol_change
        self.vol = max(0.0, min(1.0, self.vol))
        self.music_sfx.set_volume(self.vol)


class Game:
    def __init__(self):
        # General setup
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
        pygame.display.set_caption('Mystery Case')
        self.clock = pygame.time.Clock()

        # Bring the page here
        self.level = Level()
        self.camera_group = CameraGroup()
        self.interface = Interface()
        self.dialogue = Dialogue()
        self.execution = Execution()

        # Main menu setup
        self.main_menu = self.interface.main_menu()
        self.music_sfx = pygame.mixer.Sound("images/music/music_background.mp3")
        self.button_sfx = pygame.mixer.Sound("images/music/button_sfx.mp3")
        self.spawn_sfx = pygame.mixer.Sound("sfx/Voicy_Undertale Spawn.mp3")  # spawn sound
        self.vol = 0.1
        self.music_sfx.play(loops=-1)
        self.music_sfx.set_volume(self.vol)

        # Congratulations message surface
        self.congratulations_surface = pygame.Surface((WIDTH, HEIGHT))
        self.congratulations_image = pygame.image.load('images/background/background.jpg')
        self.congratulations_image = pygame.transform.scale(self.congratulations_image, (WIDTH, HEIGHT))
        self.congratulations_surface.blit(self.congratulations_image, (0, 0))
        self.congratulations_text = self.interface.font.render("Congratulations! You Win!", True, WHITE)
        self.congratulations_rect = self.congratulations_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))

        # Game over message surface
        self.game_over_surface = pygame.Surface((WIDTH, HEIGHT))
        self.game_over_image = pygame.image.load('images/background/background.jpg')
        self.game_over_image = pygame.transform.scale(self.game_over_image, (WIDTH, HEIGHT))
        self.game_over_surface.blit(self.game_over_image, (0, 0))
        self.game_over_text = self.interface.font.render("Game Over! You Lose!", True, WHITE)
        self.game_over_rect = self.game_over_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))

        # Play again button
        play_again_button_static = pygame.image.load('images/button/play_again.png')
        play_again_button_hover = pygame.image.load('images/button/play_again_hover.png')
        button_x = (WIDTH - play_again_button_static.get_width()) // 2 - 50
        self.game_over_button = Button(button_x, HEIGHT * 0.7, play_again_button_static, play_again_button_hover,
                                       (200, 100))

    def run_game(self, background_x):
        pause = False

        # Play spawn sound effect
        self.spawn_sfx.play()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                elif event.type == pygame.KEYDOWN:
                    if all(count > 0 for count in NPC.interaction_counts.values()):
                        if event.key == pygame.K_a:
                            self.display_congratulations()
                        elif event.key in (pygame.K_b, pygame.K_c, pygame.K_d):
                            self.display_game_over()
                            return "game_over"

                    if event.key == pygame.K_ESCAPE:
                        pause = not pause

            if pause:
                self.screen.blit(pause_surface, (0, 0))
                if vol_up_button.draw(self.screen):
                    self.button_sfx.play()
                    self.adjust_volume(0.1)

                if vol_down_button.draw(self.screen):
                    self.button_sfx.play()
                    self.adjust_volume(-0.1)

                if vol_mute_button.draw(self.screen):
                    self.button_sfx.play()
                    self.music_sfx.set_volume(0)
            else:
                self.screen.fill('#2D99E2')
                self.level.run()
                self.camera_group.update()

            pygame.display.update()
            self.clock.tick(FPS)

    def display_congratulations(self):
        self.screen.blit(self.congratulations_surface, (0, 0))
        self.screen.blit(self.congratulations_text, self.congratulations_rect)
        pygame.display.flip()
        pygame.time.delay(2000)
        pygame.quit()
        sys.exit()

    def display_game_over(self):
        while True:
            self.screen.blit(self.game_over_surface, (0, 0))
            self.screen.blit(self.game_over_text, self.game_over_rect)
            if self.game_over_button.draw(self.screen):
                self.button_sfx.play()
                return "play_again"
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

    def adjust_volume(self, vol_change):
        self.vol += vol_change
        self.vol = max(0.0, min(1.0, self.vol))
        self.music_sfx.set_volume(self.vol)

    def run_menu(self):
        while True:
            if self.main_menu == "start":
                action = self.interface.story_info()
                if action == "start_game":
                    result = self.run_game(background_x=0)  # Pass the required argument
                    if result == "play_again":
                        continue  # Restart the game loop
                    elif result == "game_over":
                        self.display_game_over()
                        break  # Exit the loop if the player chooses not to play again
            elif self.main_menu == "quit":
                pygame.quit()
                sys.exit()

            elif self.main_menu == "option":
                option_action = self.interface.option()
                if option_action == "back":
                    self.main_menu = self.interface.main_menu()


if __name__ == '__main__':
    game = Game()
    game.run_menu()
