from html import entities


class Square:
    def __init__(self):
        self.entities = set()

    def get_entities(self):
        return self.entities

    def put(self, new_entity):
        if self.eaten_by_existing_entities(new_entity):
            return False        
        entities_to_remove=self.eat_existing_entities(new_entity)
        entities_to_remove.clear()

        self.entities.add(new_entity)
        return True

    def eaten_by_existing_entities(self, new_entity):
        for entity in self.entities:
            if new_entity.is_eatable_by(entity):
                entity.eat(new_entity)
                return True
        return False

    def eat_existing_entities(self, new_entity): 
        entities_to_remove=set()       
        for entity in self.entities:
            if entity.is_eatable_by(new_entity):                
                new_entity.eat(entity)
                entities_to_remove.add(entity)
            return entities_to_remove
        

    def delete_entity(self, entity):
        self.entities.remove(entity)

    def is_empty(self):
        return len(self.entities) == 0

    def __str__(self):
        if self.is_empty():
            return "[]"
        else:
            return str(self.entities)
