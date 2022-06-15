class EntitiesComparator:
    
    def compare(entity1,entity2):
        if entity1.is_dynamic():
            return 1
        if entity2.is_dynamic():
            return -1
        return 0

        
        