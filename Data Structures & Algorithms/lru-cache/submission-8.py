class Node :
        def __init__(self,key,value):
            self.key = key
            self.val = value
            self.prev = None
            self.next = None

class LRUCache:

    
    
    def __init__(self, capacity: int):

        self.capacity = capacity
        self.nodes_map = {}
        
        self.head = Node(-1,-1)
        self.tail = Node(-1,-1)
        
        self.head.next = self.tail
        self.tail.prev = self.head
       


    def appendleft(self,target_node):
        
        print("Appending left -" ,target_node.val)
        target_node.prev = self.head
        target_node.next = self.head.next
        
        self.head.next.prev = target_node
        self.head.next = target_node
        
        
    
    def remove(self,target_node):

        print("Removing -" ,target_node.val)
        
        next_node =   target_node.next
        prev_node =   target_node.prev
        
        next_node.prev = prev_node
        prev_node.next = next_node

    
    def get(self, key: int) -> int:

        if key in self.nodes_map :
            
            node = self.nodes_map[key]
            print("Get - ", node.val)
            self.remove(node)
            self.appendleft(node)
            print(node.val)
            return node.val
        
        else :
            print("Get - Not Found")
            return -1    

           
        
    def put(self, key: int, value: int) -> None:

       
        if key in self.nodes_map :
                node = self.nodes_map[key]
                self.remove(node)
                node.val = value
                print("Update Exist")
                self.appendleft(node)
        
        elif len(self.nodes_map) < self.capacity :

            print(self.nodes_map)
            node = Node(key,value)
            self.appendleft(node)
            self.nodes_map[key] = node
            print("New", node.val)
        
        else :
            
            del self.nodes_map[self.tail.prev.key] 
            self.remove(self.tail.prev)
            node = Node(key,value)
            print("Pop and add")
            self.appendleft(node)
            self.nodes_map[key] = node
                

    
       
    '''
        # Not an efficient solution
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
    '''



        


        
