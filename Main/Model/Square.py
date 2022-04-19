class Square:
    def __init__(self):
        self.entities = set()
        self.entity_to_remove = None

    def get_entities(self):
        return self.entities 
        
    def get_entity(self):
        for entity in self.entities:
            return entity 

    def put_entitie_in_square(self, static_entity):
        self.entities.add(static_entity)

    def put(self, new_entity):
        if self.eaten_by_existing_entities(new_entity):
            return False
        self.eat_existing_entities(new_entity)
        self.remove_eatable_entity()
        self.entities.add(new_entity)
        return True
    

    def eaten_by_existing_entities(self, new_entity):
        for entity in self.entities:
            if new_entity.is_eatable_by(entity):
                entity.eat(new_entity)
                return True
        return False

    def eat_existing_entities(self, new_entity):
        for entity in self.entities:
            if entity.is_eatable_by(new_entity):
                self.entity_to_remove = entity
                new_entity.eat(entity)

    def remove_eatable_entity(self):
        self.remove(self.entity_to_remove)

    def remove(self, entity):
        self.entities.remove(entity)

    def is_empty(self):
        return len(self.entities) == 0

    def __str__(self):
        if self.is_empty():
            return "[]"
        else:
            return str(str(self.entities))
