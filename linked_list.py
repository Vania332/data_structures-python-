
class LinkedList:
    class __Node:
        def __init__(self, val: int, next=None):
            self.val = val
            self.next = next
            
        def __repr__(self):
            return f"value: {self.val}"
            
    def __init__(self):
        self.__head = None
        self.__tail = None
    
    
        
    def add_first(self, val: int):
        new_node =  self.__Node(val=val)
        if self.__is_empty():
            self.__initialize(new_node)
        else:
            new_node.next = self.__head
            self.__head = new_node

    def add_last(self, val: int):
        new_node = self.__Node(val=val)
        if self.__is_empty():
            self.__initialize(new_node)
        else:
            self.__tail.next = new_node
            self.__tail = new_node
    
    def remove_first(self):
        if self.__is_empty():
            raise ValueError("Cannot remove an element from en empty list")
        
        removed_value = self.__head.val 
        
        if self.__has_one_node():
            self.__reset()
        else:
            next = self.__head.next
            self.__head = None
            self.__head = next
        
        return removed_value
    
    def remove_last(self):
        if self.__is_empty():
            raise ValueError("Cannot remove an element from en empty list")
        
        removed_value = self.__tail.val
        
        if self.__has_one_node():
            self.__reset()
        else:
            prev = self.__get_node_before_last()
            prev.next = None
            self.__tail = prev
        
        return removed_value
    
    def remove(self, value):
        if self.__is_empty():
            raise ValueError("Cannot remove an element from en empty list")
        
        if self.__head.val == value:
            self.remove_first()
            return
        
        if self.__tail.val == value:
            self.remove_last()
            return 
        
        current = self.__head
        prev = self.__head
        
        while current.next:
            if current.val == value:
                prev.next = current.next
                current.next = None
                return
            
            prev = current
            current = current.next
        
        raise ValueError("Value not found in the list")
    
    
    
    
    def __get_node_before_last(self):
        if self.__is_empty() or self.__has_one_node():
            return None
        
        current = self.__head
        while current.next != self.__tail:
            current = current.next
            
        return current
        
    def __has_one_node(self):
        return self.__head == self.__tail
    
    def __reset(self):
        self.__head = self.__tail = None    
        
    def __is_empty(self):
        return self.__head is None

    def __initialize(self, node):
        self.__tail = self.__head = node
        
    
    