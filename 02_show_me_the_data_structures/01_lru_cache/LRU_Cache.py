from nodes import nodes as nd

class LRU_Cache(object):
    def __init__(self, capacity):
        # Initialize class variables
        self.capacity = capacity #capacity
        self.map = dict() #HashMap
        self.head = None
        self.tail = None
    
    def __repr__(self):
        if self.map is None:
            return 'None'
        return str(self.map) 

    def get(self, key):
        """
        Retrieve item from provided key. Return -1 if nonexistent.
        """
        dnode = self.map.get(key) #dobleNode
        head = self.map.get(self.head)
        if dnode is not None: 
            # validar si no es cabezera, si no que el anterior apunte al nodo siguiente
            if dnode.next is not None:
                self.map[dnode.next].previous = dnode.previous
            # Eliminar entre los nodos 
            if dnode.previous is not None:
                self.map[dnode.previous].next = dnode.next
            else:
                self.tail = dnode.next
            if head is not None:
                head.next = key
            dnode.previous = self.head
            dnode.next = None
            self.head = key
            return dnode
        else:
            return -1

    def set(self, key, value):
        """
        Set the value if the key is not present in the cache. If the cache 
        is at capacity remove the oldest item.
        """ 
        # primero evaluar si el cache tiene un tama;o
        if self.capacity != 0:
            
            # Evaluar si no esta lleno, si no eliminar
            if len(self.map)+1 > self.capacity:
                tail_aux = self.map[self.tail]
                del self.map[self.tail]
                self.tail = tail_aux.next
                
            head = self.map.get(self.head)
            dnode = nd(value)
            # Evaluar si el cache esta vacio
            if head is None:
                self.head = key
                self.tail = key
            else:
                dnode.previous = self.head
                head.next = key
            self.map[key] = dnode
            self.head = key
        else:
            print("Error: size cache == 0")
        print(self.map)

if __name__ == "__main__": ##TEST
    
    our_cache = LRU_Cache(5)
    
    our_cache.set(1, 1);
    our_cache.set(2, 2);
    our_cache.set(3, 3);
    our_cache.set(4, 4);
    
    
    print(our_cache.get(1))       # returns 1
    print(our_cache.get(2))       # returns 2
    print(our_cache.get(9))      # returns -1 because 9 is not present in the cache
    
    our_cache.set(5, 5) 
    our_cache.set(6, 6)
    
    print(our_cache.get(3))      # returns -1 because the cache reached it's 
                                 #capacity and 3 was the least recently used entry