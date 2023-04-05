import random

from dino_runner.components.obstacles.obstacle import Obstacle

from dino_runner.utils.constants import SCREEN_WIDTH

from dino_runner.utils.constants import BIRD

class Bird(Obstacle):
    def __init__(self, image):
        self.image = image
        self.type = 0
        super().__init__(self.image, self.type)
        self.rect.x = SCREEN_WIDTH
        coordinates = [250, 450, 390]
        self.rect.y = random.choice(coordinates)
        self.fly_index = 0
        
            
    def draw(self, screen):
        if self.fly_index >= 10:
            self.fly_index = 0
        self.image = BIRD[0] if self.fly_index < 5 else BIRD[1]
        screen.blit(self.image,self.rect)
        self.fly_index += 1    