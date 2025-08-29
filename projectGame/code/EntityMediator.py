

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
        for ent in entity_list:
            if isinstance(ent, Enimy) and ent.health <= 0:
                 entity_list.remove(ent)
            

    

    @staticmethod
    def verify_collision(entity_list:list[Entity]):
        for i in range(len(entity_list)):
            test_entity = entity_list[i]
            test = EntityMediator.__verify_collision_windom(test_entity)
            if test:
                print('- 1 life')