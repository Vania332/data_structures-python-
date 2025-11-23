class Node:
    def __init__(self, val: int, next=None):
         self.val = val
         self.next = next
         
class LinkedList:
    def __init__(self, root):
        self.root = root
    
    def append(self, val: int):
        tmp = self.root
        while tmp.next:
            tmp = tmp.next
        tmp.next = Node(val=val)
        
    def output(self):
        tmp = self.root
        while tmp:
            print(tmp.val, end=" ")
            tmp = tmp.next
            
    def search(self, val: int) -> bool:
        tmp = self.root
        while tmp:
            if tmp.val == val:
                return True
            tmp = tmp.next
        return False
    
    def pop(self):
        tmp = self.root
        if tmp.next.next:
            while tmp.next.next:
                tmp = tmp.next
            tmp.next = None  
    
    def reverse(self):
        prev = None
        current = self.root
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.root = prev

root = Node(10)
ll = LinkedList(root=root)
ll.append(13)
ll.append(30)

ll.output()

ll.reverse()
print("\n")
ll.output()