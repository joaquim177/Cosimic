

from code.Enimy import Enimy
from code.Entity import Entity
from code.PlayerShot import PlayerShot


class EntityMediator:

    @staticmethod
    def __verify_collision_windom(ent: Entity):
        if isinstance(ent, Enimy):
           if(ent.rect.right <= 230):
               ent.health = 0
               return True
           else:
               return False
        if isinstance(ent, PlayerShot):
           if(ent.rect.left <= 720):
               ent.health = 0
               return True
           else:
               return False
    @staticmethod      
    def verify_health(entity_list: list[Entity]):
        for ent in entity_list[:]:                    # usa [:] para iterar em cópia
           if isinstance(ent, Enimy) and ent.health <= 0: 
               entity_list.remove(ent)

    

    @staticmethod
    def verify_collision(entity_list: list[Entity], level=None):
        for ent in entity_list[:]:      
            if isinstance(ent, Enimy) and ent.rect.left <= 0:
                print("ola")
                ent.health = 0
                if level:
                    level.lives -= 1
                    print(f"💔 perdeu uma vida, vidas restantes: {level.lives}")
                            
            if isinstance(ent, PlayerShot):
                for other in entity_list[:]:
                    if isinstance(other, Enimy) and ent.rect.colliderect(other.rect):
                        other.health = 0              # mata o inimigo
                        ent.health = 0                # mata o tiro
                        print("💥 inimigo atingido!")