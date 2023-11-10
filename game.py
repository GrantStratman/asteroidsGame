import pygame

from models import Spaceship, Asteroid



from utils import get_random_position, load_sprite




class SpaceRocks:
    #Constant variable for the min distance a asteroid can spawn
    MINDISTANCE = 250
    def __init__(self):
        self._init_pygame()
        self.screen = pygame.display.set_mode((800, 600))
        
        self.clock = pygame.time.Clock()
        #Use Lists to keep track of both the asteroids and the bullets 
        self.asteroids = []
        self.bullets = []
        self.spaceship = Spaceship((400, 300), self.bullets.append)


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
            elif (
                #Genterates a bullet when the space bar is pressed
                self.spaceship
                and event.type == pygame.KEYDOWN
                and event.key == pygame.K_SPACE
            ):
                self.spaceship.shoot()
        #Have python recognize key presses: by using the built in fuction is_key_pressed we can check if certain keys have been pressed then preform an action        is_key_pressed = pygame.key.get_pressed()
        
        if self.spaceship:
            if is_key_pressed[pygame.K_RIGHT]:
                self.spaceship.rotate(clockwise=True)
            elif is_key_pressed[pygame.K_LEFT]:
                self.spaceship.rotate(clockwise=False)
            if is_key_pressed[pygame.K_UP]:
                self.spaceship.accelerate()

    #Get the game objects
    def get_game_objects(self):
        game_objects = [*self.asteroids, *self.bullets]
        #this prevents the game from return in an empty spaceship once it has been destroyed
        if self.spaceship:
            game_objects.append(self.spacesihp)
        
            return game_objects
    


    def _process_game_logic(self):
        for game_object in self.get_game_objects():
            game_object.move(self.screen)
        
        #Uses the built in collides_with method to check if any of the asteroids collides with the spaceship
        if self.spaceship:
            for asteroid in self.asteroid:
                if asteroid.collides_with(self.spaceship):
                    self.spaceship = None
                    break
        
        #Use a nested for loop to check if a asteroid collides wit the bullet. the funciton, "collides_with" will return true if the objects connect 
        for bullet in self.bullets[:]:
            for asteroid in self.asteroids[:]:
                if asteroid.collides_with(bullet):
                    #remove the asteroid from the list of asteroids
                    self.asteroids.remove(asteroid)
                    #remove the bullet from the list of bullets
                    self.bullets.remove(bullet)
                    break
        #check if bullets leave the screen
        #Make a copy of the bullets list using : so we don't get an error from removing items while iterating
        for bullet in self.bullets[:]:
            #use .collidepoint to see if the asteroid collided with the edge of the screen
            if not self.screen.get_rect().collidepoint(bullet.position):
                self.bullets.remove(bullet)
                

    
    


    def _draw(self):
        self.screen.blit(self.background, (0, 0))
        

        for game_object in self.get_game_objects():
            game_object.draw(self.screen)

        pygame.display.flip()
        self.clock.tick(60)


