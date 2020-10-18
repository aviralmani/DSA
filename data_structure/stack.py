# stack using linklist:

class newElement():
    def __init__(self, data = None):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None

    def addFirst(self, data):
        new_element = newElement(data)
        if self.head:
            new_element.next = self.head
            self.head = new_element
        else:
            self.head = new_element

    def deletefirst(self):
        if self.head:
            deleted_element = self.head
            self.head = self.head.next
            deleted_element.next = None
            return deleted_element
        else:
            return None
class stack():
    def __init__(self,top=None):
        self.ll = LinkedList()

    def pop(self):
        deleted_element = self.ll.deletefirst()
        return deleted_element

    def push(self, data):
        self.ll.addFirst(data)


# s1 = stack()
# s1.push(1)
# s1.push(2)
# s1.push(3)
# s1.push(4)
# print(s1.pop().data)
# print(s1.pop().data)
# print(s1.pop().data)
# print(s1.pop().data)
# print(s1.pop())
