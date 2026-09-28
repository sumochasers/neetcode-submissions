class Node :
    def __init__(self, key, value):
        self.freq = 1
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
       

class DoublyLinkedList :
    
    def __init__(self):
        self.size = 0
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def append(self, node):
        prev_node = self.tail.prev
        
        prev_node.next = node
        node.prev = prev_node
        
        node.next = self.tail
        self.tail.prev = node
        
        self.size += 1
    
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1
    
    def remove_first(self) -> int :
        if self.is_empty() :
            return 
        key = self.head.next.key
        self.remove(self.head.next)
        return key
    
    def is_empty(self):
        return self.size == 0


class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.node_by_key : dict[int, Node]= {}
        self.list_by_freq : dict[int, DoublyLinkedList] = {}
        self.minimum = None

    def size(self) -> int : 
        return len(self.node_by_key)

    def update(self, value, node) -> None:
        
        freq = node.freq
        next_freq = freq + 1
        node.freq = next_freq
        node.value = value

        old_list = self.list_by_freq[freq]
        old_list.remove(node)
        
        if old_list.is_empty():
            del self.list_by_freq[freq]
            # definitely +1 exisit cos current freq is incremented to that
            if freq == self.minimum :
                self.minimum += 1

        if next_freq not in self.list_by_freq :
            self.list_by_freq[next_freq] = DoublyLinkedList()

        new_list = self.list_by_freq[next_freq]
        new_list.append(node)
        

    def get(self, key: int) -> int:
        if key not in self.node_by_key :
            return -1
        
        # update the freq list and return 
        node = self.node_by_key[key]
        self.update(node.value, node)
    
        return node.value
         
    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        if key in self.node_by_key :
            node = self.node_by_key[key]
            self.update(value, node)
            return
        
        if self.size() >= self.capacity :
            
            old_list = self.list_by_freq[self.minimum]
            del_key = old_list.remove_first()

            del self.node_by_key[del_key]
            
            if old_list.size == 0 :
                del self.list_by_freq[self.minimum]
            
        node = Node(key, value)
        
        if 1 not in self.list_by_freq :
            self.list_by_freq[1] = DoublyLinkedList()
        
        node_list = self.list_by_freq[1]
        node_list.append(node)

        self.node_by_key[key] = node
        self.minimum = 1
        




        
           

        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)