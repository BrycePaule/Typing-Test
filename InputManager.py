import pygame

class InputManager():

    """
    Handles all player inputs.
    """

    def __init__(self, game):
        self.game = game


    def handle_events(self):
        """ Event handler. """

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game.stop_game()
                    pygame.quit()

                elif 97 <= event.key <= 122:
                    self.game.blurb.current_word_typed += pygame.key.name(event.key)
                    self.game.keyboard.add_key_press(event.key)

                    if not self.game.running:
                        self.game.start_game()

                elif event.key == pygame.K_SPACE:
                    self.game.blurb.results.append([self.game.blurb.current_word, self.game.blurb.current_word_typed])
                    self.game.blurb.mark_and_shift()
                    self.game.blurb.current_word_typed = ''

                    if not self.game.running:
                        self.game.start_game()

                elif event.key == pygame.K_BACKSPACE:
                    self.game.blurb.current_word_typed = self.game.blurb.current_word_typed[:-1]
                    self.game.blurb.backspace_recolour()