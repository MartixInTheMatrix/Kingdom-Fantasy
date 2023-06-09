import pygame 
import objects.entity as entity

        



class Player(entity.Entity):
    """Heritated from Entity Object but with special functions"""
    def __init__(self, coords, screen, tilemap, FRICTION, SCREEN_WIDTH, SCREEN_HEIGHT, chat, isMeyer, level):
        super().__init__(self, entity.EntityType["PLAYER"],
                         "",
                         coords, screen, tilemap, FRICTION, SCREEN_WIDTH, SCREEN_HEIGHT, [""], isMeyer, level)
        self.speed = 8
        self.level = level
        
    def render(self, skin=pygame.image.load("./resources/animations/player/idle/idle00.png")):
        self.image = pygame.transform.scale(skin, (self.size, self.size))
        self.screen.blit(self.image, (self.SCREEN_WIDTH//2 - (self.size//2), self.SCREEN_HEIGHT//2 - (self.size//2))) # joueur toujours au millieu de l'écran, c'est le bg qui bouge
   
    def tick(self, delta_time):
        # Entity general movement physics
        
        # v += a * f * dt
        self.velocity = [v + a * f * delta_time for v, a, f in zip(self.velocity, self.accel, self.friction)]

        self.check_borders(delta_time)
        self.check_collision(delta_time)
    
        # d = v * dt
        self.x += self.velocity[0] * delta_time * self.speed
        self.y += self.velocity[1] * delta_time * self.speed

        # v -= min(|v * f * dt|, |v|)
        self.velocity = [v - min(v * f * delta_time, v, key = abs) for v, f in zip(self.velocity, self.friction)]
        
        
        
        
    def attack(self, e):
        e.hurt(1)
        if e.hp == 0:
            self.level.entities.remove(e)
            self.level.counter += 1

    def hurt(self, damage):
        self.hp -= damage
        self.level.hp -= damage
  

