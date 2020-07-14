import pygame

class InputManager():

    def __init__(self, game):
        self.game = game


    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game.stop_game()
                    pygame.quit()

                elif 97 <= event.key <= 122:
                    self.game.blurb.keystrokes += pygame.key.name(event.key)
                    self.game.keyboard.add_key_press(event.key)
                    if not self.game.running:
                        self.game.start_game()

                elif event.key == pygame.K_SPACE:
                    self.game.blurb.keystrokes += ' '
                    if not self.game.running:
                        self.game.start_game()

                elif event.key == pygame.K_BACKSPACE:
                    self.game.blurb.keystrokes = self.game.blurb.keystrokes[:-1]
                    self.game.blurb.backspace_recolour()