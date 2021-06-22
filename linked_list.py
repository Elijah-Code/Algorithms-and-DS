class Node:
    def __init__(self, val=None):
        self.next = None
        self.val = val

    def set_next(self, node):
        self.next = node

    def add(self, val):
        node = Node(val)
        node.next = self.next
        self.set_next(node)

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

l = [3,1,123,51,671,714,5123,51,2]


head = Node(l[0])
current_node = head
for elem in l[1:]:
    node = Node(elem)
    current_node.set_next(node)
    current_node = node

head.print()
        