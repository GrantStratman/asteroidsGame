from pygame.math import Vector2
from pygame.transform import rotozoom

from utils import load_sprite , wrap_position, get_random_velocity

#create a constant vector 
UP = Vector2(0, -1)
#Create a game object
class GameObject:
    def __init__(self, position, sprite, velocity):
        self.position = Vector2(position)
        self.sprite = sprite
        self.radius = sprite.get_width() / 2
        self.velocity = Vector2(velocity)

    def draw(self, surface):
        blit_position = self.position - Vector2(self.radius)
        surface.blit(self.sprite, blit_position)

    def move(self, surface):
        self.position = wrap_position(self.position + self.velocity, surface)
#check if two objects have collided
    def collides_with(self, other_obj):
        distance = self.position.distance_to(other_obj.position)
        return distance < self.radius + other_obj.radius





class Spaceship(GameObject):
    #variable for how fast you can rotate the ship
    MANEUVERABILITY = 3
    ACCELERATION = 0.25
    BULLET_SPEED = 3
    #This is the constructor for the spaceship, it take in the position and the create bullet callback to SpaceRocks
    def __init__(self, position, create_bullet_callback):
        self.create_bullet_callback = create_bullet_callback
        # Make a copy of the original UP vector
        self.direction = Vector2(UP)

        super().__init__(position, load_sprite("spaceship"), Vector2(0))
#change the rotation either clockwise or counterclockwise
    def rotate(self, clockwise=True):
        sign = 1 if clockwise else -1
        angle = self.MANEUVERABILITY * sign
        self.direction.rotate_ip(angle)

    def draw(self, surface):
        angle = self.direction.angle_to(UP)
        rotated_surface = rotozoom(self.sprite, angle, 1.0)
        rotated_surface_size = Vector2(rotated_surface.get_size())
        blit_position = self.position - rotated_surface_size * 0.5
        surface.blit(rotated_surface, blit_position)


    def accelerate(self):
        self.velocity + self.direction * self.ACCELERATION
    
    #Create a method called shoot that will create a bullet and add it to the list of bullets
    def shoot(self):
        #Calculate the velocity of the bullet
        bullet_velocity = self.direction * self.BULLET_SPEED + self.velocity
        #Create a bullet object
        bullet = Bullet(self.position, bullet_velocity)

        #Call the create bullet callback to add the bullet to the list of bullets
        self.create_bullet_callback(bullet)



class Asteroid(GameObject):
    def __init__(self, position):
        super().__init__(position, load_sprite("asteroid"), get_random_velocity(1,3))


class Bullet(GameObject):
    #Intialize using the game object constructor but add velocity as a parameter becasue the bullets will move
    def __init__(self,position,velocity):
        super().__init__(position, pygame.draw.circle(30),velocity )




