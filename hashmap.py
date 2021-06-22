class HashMap:
    def __init__(self):
        self.size = 2
        self.hash_map  = [None]*self.size
        self.vals = [None]*self.size
        self.next_free = 0

    def add(self, key, val):
        if self.next_free >= self.size:
            print("Something went wrong")
            return

        index = hash(key) % (self.size-1)

        node = Node(key=key, val=val)
        # La place est libre !
        if self.hash_map[index] == None:
            self.vals[self.next_free] = node
            self.hash_map[index] = self.next_free
            self.next_free += 1
        else: # Pas de place pour toi
            self.vals[self.hash_map[index]].add_to_end(node)
        


    def retrieve(self, key):
        index_ix = hash(key) % (self.size-1)
        
        val_index = self.hash_map[index_ix]
        if val_index == None:
            return
        node = self.vals[val_index]
        while node != None:
            if node.key == key:
                return node.val
            node = node.next


class Node:
    def __init__(self, val, key):
        self.next = None
        self.val = val
        self.key = key

    def set_next(self, node):
        self.next = node

    def add(self, val):
        node = Node(val)
        node.next = self.next
        self.set_next(node)

    def add_to_end(self,node):
        current = self
        while current.next != None:
            current = current.next
        current.set_next(node)

    def delete(self, step):
        current_node = self
        for _ in range(step-1):
            current_node = current_node.next
        new_node = current_node.next.next
        current_node.next = new_node

    def find_mid(self):
        fleche1 = self
        fleche2 = self

        while fleche2 is not None:
            fleche2 = fleche2.next.next
            fleche1 = fleche1.next 
    
    def print(self):
        print(self.val, end=" ")
        if self.next:
            self.next.print()    



hash_map = HashMap()
hash_map.add("D", "d")
hash_map.add("C", "c")
hash_map.add("A", "a")
hash_map.add("B", "b")
print(hash_map.retrieve("A"))
print(hash_map.retrieve("B"))
print(hash_map.retrieve("C"))
print(hash_map.retrieve("E"))