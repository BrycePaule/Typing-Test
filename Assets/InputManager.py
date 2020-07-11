import pygame

class InputManager():

    def __init__(self, blurb):
        self.blurb = blurb


    def update(self):
        pass


    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()

                elif event.key == pygame.K_SPACE:
                    self.blurb.keystrokes += ' '

                elif event.key == pygame.K_BACKSPACE:
                    self.blurb.keystrokes = self.blurb.keystrokes[:-1]
                    self.blurb.backspace_recolour()

                elif 97 <= event.key <= 122:
                    self.blurb.keystrokes += pygame.key.name(event.key)
                    # print(self.blurb.keystrokes)

                # print(pygame.key.name(event.key))
                # print(event.key)