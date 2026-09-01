class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.storage_list = []

        

    def get(self, key: int) -> int:

        for item in self.storage_list :
            k,v = item
            if k == key :
                self.storage_list.remove(item)
                self.storage_list.insert(0,(key,v))
                return v
        
        return -1     
        
    def put(self, key: int, value: int) -> None:

        for item in self.storage_list :
            k,v = item
            if k == key :
                self.storage_list.remove(item)
                self.storage_list.insert(0,(key,value))
                return
        
        if len(self.storage_list) >=  self.capacity :
            self.storage_list.pop()
        
        self.storage_list.insert(0,(key,value))
       




        


        
