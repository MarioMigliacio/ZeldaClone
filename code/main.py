import pygame
from settings import *
from level import Level

#from debug import debug

class Game:
    def __init__(self):
        
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption(GAME_NAME)
        self.level = Level()
    
    def run(self):
        running = True
        
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    running = False
            
            self.screen.fill('black')
            self.level.run()
                
            pygame.display.update()
            self.clock.tick(FPS)
        
        pygame.quit()

if __name__ == '__main__':
    game = Game()
    game.run()