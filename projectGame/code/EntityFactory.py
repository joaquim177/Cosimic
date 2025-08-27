


from code.Background import Background


class EntityFactory():
   @staticmethod
   def  getEntity(entity_name:str, position= (0,0)):
        match entity_name:
            case 'level1':
               list_bg = []
               for i in range(2):
                   list_bg.append(Background(f'level1bg{i}', position=(0,0)))
               return list_bg