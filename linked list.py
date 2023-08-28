# Linked_List Project
class Node:
    def __init__(self, ID, name, age, Next):
        self.ID = ID
        self.name = name
        self.age = age
        self.next = Next
class Linked_list:
    def __init__(self, head=None):
        self.head = None

    def show(self):
        if self.head == None:
            print('Its Empty')
        else:
            a = self.head
            while True:
                print(a.ID, a.name, a.age)
                if a.next == None:
                    break
                else:
                    a = a.next

    def add(self, ID, name, age):
        if self.head == None:
            self.head = Node(ID, name, age, None)
        else:
            p = self.head
            while p.next != None:
                p = p.next
            p.next = Node(ID, name, age, None)


    def find(self, id):
        if self.head == None:
            print('Its Empty')
            return
        p = self.head
        while True:
            if p.ID == id:
                print('found')
                print('id : {0}, name : {1}, age : {2}'.format(p.ID, p.name, p.age))
                break
            if p.next == None:
                print('not found')
                break
            p = p.next

    def deletee(self, id):
        if self.head.ID == id:
            self.head = self.head.next
        else:
            q = self.head
            while True:
                if q.next == None:
                    break
                if q.next.ID == id:
                    q.next = q.next.next
                    break
                q = q.next

ob = Linked_list()

print('1 :show \n2 : add\n3 : find\n4 : deletee')
try:
    func = int(input('please enter a number of function:'))
    if func == 1:
        ob.show()
    elif func == 2:
        ID = int(input('please enter ID:'))
        name = (input('please enter name:'))
        age = int(input('please enter age:'))
        ob.add(ID, name, age)
    elif func == 3:
        if ob.head != None:
            id = int(input('please enter ID:'))
        ob.find(id)
    elif func == 4:
        if ob.head != None:
            id = int(input('please enter ID:'))
        ob.deletee(id)

    while 0 < func < 5:
        func = int(input('please enter a number of function:'))
        if func == 1:
            ob.show()
        elif func == 2:
            ID = int(input('please enter ID:'))
            name = (input('please enter name:'))
            age = int(input('please enter age:'))
            ob.add(ID, name, age)
        elif func == 3:
            if ob.head != None:
                id = int(input('please enter ID:'))
            ob.find(id)
        elif func == 4:
            if ob.head != None:
                id = int(input('please enter ID:'))
            ob.deletee(id)

except:
    print('')
