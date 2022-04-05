class Square:
    def __init__(self):
        self.entity = None
        self.create_square()
    
    def create_square(self):
        self.square=list()        

    def put(self, entity):  
        self.entity=entity      
        self.square.append(self.entity)

    def delete(self):
        self.entity = None

    def is_empty(self):
        return self.entity == None

    def get_entity(self,index):        
        for i in range(0,len(self.square)):
            if i==index:
                return self.square[i]

    def __str__(self):
        if self.is_empty():
            return "[ ]"
        else:
            return ",".join(map(str, self.square)) 
