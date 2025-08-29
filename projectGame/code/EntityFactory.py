
import random
from code.Background import Background
from code.Enimy import Enimy
from code.Player import Player
from code.const import WIN_HEIGHT


class EntityFactory():
   @staticmethod
   def  getEntity(entity_name:str, position= (0,0)):
        match entity_name:
            case 'level1':
               list_bg = [
               Background(f'level1bg{i}', position=(20, 100) if i == 1 else (0, 0))
               for i in range(2)
               ]
               return list_bg
            case 'player':
                return Player('player', (50,50))
            case 'cometa':
                return Enimy('cometa', (720, random.randint(60,200)))