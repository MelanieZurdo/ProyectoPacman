

class Square:
    def __init__(self):
        self.entity = None

    def put(self, entity):
        self.entity = entity
        return self.entity

    def is_empty(self):
        return self.entity == None

    def __str__(self):
        if self.is_empty():
            return "[]"
        else:
            return str(self.entity)
