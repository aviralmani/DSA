class node():
    def __init__(self,data=None):
        self.data = data
        self.next = None

class Create():
    def __init__(self):
        self.head = None;                     '''Creates a head node that itself does not contain any data but contains pointer(next) which points to the first node. 
                                                    Since init is only called 1 time at the initiation'''

    def append(self,data):
        new_node = node(data)
        if self.head:
            cur_node = self.head
            while cur_node.next != None:
                cur_node = cur_node.next
            cur_node.next = new_node
        else:
            self.head = new_node

    def length(self):
        cur_node = self.head
        total = 0
        while cur_node != None:
            total+=1
            cur_node = cur_node.next
        return total

    def display(self):
        element = []
        cur_node = self.head
        while cur_node != None:
            element.append(cur_node.data)
            cur_node = cur_node.next
        return print(element);

    def get(self, index):
        if index>=self.length():
            print('Index out of range.')
            return None
        cur_node = self.head
        curr_index = 0
        while True:
            cur_node = cur_node.next
            if curr_index == index:
                return cur_node.data
            curr_index=+1

    def erase(self, index):
        if index < 0:
            index = self.length() + index +1
        if index>=self.length() or index < 0:
            print('Index out of range.')
            return None

        cur_node = self.head
        cur_index = 0
        while True:
            if cur_index == index:
                cur_node.next = cur_node.next.next
                return None
            cur_node = cur_node.next
            cur_index += 1

    def appendInter(self,index,data):
        new_node = node(data)
        if index > self.length():
            print('Index out on range.')
            return None
        elif index == 0:                            # Insert at begining
            new_node.next = self.head
            self.head = new_node
        elif index == self.length():                # Insert at last
            cur_node = self.head
            while cur_node.next != None:
                cur_node = cur_node.next
            cur_node.next = new_node
        else:                                       # Insert at perticular index
            cur_node = self.head
            for i in range(index-1):
                cur_node = cur_node.next
            new_node.next = cur_node.next
            cur_node.next = new_node
            return None

    def reverse(self):
        last_node = self.head
        while last_node.next != None:
            last_node = last_node.next
        tail = last_node
        for x in range(self.length()+1):        # Remeber to +1 since last number also needs to be set.
            pre_node = self.head
            while pre_node.next != tail:
                pre_node = pre_node.next
            tail.next = pre_node
            tail = pre_node
        self.head = last_node
        tail.next=None




# l1 = Create()                                 # Initiation
#
# l1.append(1)
#
# # print(l1.length())
# l1.append(2)
# l1.append(3)
# l1.append(7)
# l1.display()
# l1.appendInter(1,4)
# l1.display()
# l1.appendInter(5,6)
# l1.display()
# # l1.reverse()
# l1.reverse()
# l1.display()
