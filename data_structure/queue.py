class element():
    def __init__(self, data= None):
        self.data = data;
        self.next = None;

class linklist():
    def __init__(self):
        self.head = None;

    def addlast(self, data):
        new_element = element(data);
        if self.head:
            current_element = self.head;
            while current_element.next != None:
                current_element = current_element.next;
            current_element.next = new_element;
        else:
            self.head = new_element;

    def deleteFirst(self):
        if self.head:
            deleted_element = self.head
            self.head = self.head.next
            deleted_element.next = None
            return deleted_element
        else:
            return None

class queue():
    def __init__(self):
        self.q1 = linklist();

    def push(self, data):
        self.q1.addlast(data);

    def pop(self):
       return self.q1.deleteFirst();


q = queue()
q.push(1)
q.push(2)
q.push(3)
q.push(4)

print(q.pop().data)
print(q.pop().data)
print(q.pop().data)
print(q.pop().data)
print(q.pop().data)
print(q.pop().data)
