import pygame

from models import Spaceship, Asteroid



from utils import get_random_position, load_sprite




class SpaceRocks:
    #Constant variable for the min distance a asteroid can spawn
    MINDISTANCE = 250
    def __init__(self):
        self._init_pygame()
        self.screen = pygame.display.set_mode((800, 600))
        self.background = load_sprite("space", False)
        self.clock = pygame.time.Clock()
        self.asteroids = []
        self.spaceship = Spaceship((400, 300))


        for i in range(6):
            while True:
                position = get_random_position(self.screen)
                if(position.distance_to(self.spaceship.position) > self.MINDISTANCE):
                    break

            self.asteroids.append(Asteroid(position))

    def main_loop(self):
        while True:
            self._handle_input()
            self._process_game_logic()
            self._draw()

    def _init_pygame(self):
        pygame.init()
        pygame.display.set_caption("Space Rocks")

    def _handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (
                event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
            ):
                quit()
        
        #Have python recognize key presses
        is_key_pressed = pygame.key.get_pressed()

        if self.spaceship:
            if is_key_pressed[pygame.K_RIGHT]:
                self.spaceship.rotate(clockwise=True)
            elif is_key_pressed[pygame.K_LEFT]:
                self.spaceship.rotate(clockwise=False)
            if is_key_pressed[pygame.K_UP]:
                self.spaceship.accelerate()

    #Get the game objects
    def get_game_objects(self):
        game_objects = [*self.asteroids]

        if self.spaceship:
            game_objects.append(self.spacesihp)
        
            return game_objects
    


    def _process_game_logic(self):
        for game_object in self.get_game_objects():
            game_object.move(self.screen)

        if self.spaceship:
            for asteroid in self.asteroid:
                if asteroid.collides_with(self.spaceship):
                    self.spaceship = None
                    break
        
    

    
    


    def _draw(self):
        self.screen.blit(self.background, (0, 0))
        

        for game_object in self.get_game_objects():
            game_object.draw(self.screen)

        pygame.display.flip()
        self.clock.tick(60)


