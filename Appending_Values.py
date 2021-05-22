class Compute:
    def __init__(self):
        self.l = []
    def add(self,a=0):
        if a == 0:
            a = self.get_val()
        self.l.append(a)
        print('List : ',self.l)
    def remove(self,a=0):
        print('List : ',self.l)
        if a == 0:
            a = self.get_val()
        self.l.remove(a)
        print('List : ',self.l)
    def disp(self):
        print('List : ', self.l)
    @staticmethod
    def get_val():
        return int(input('Enter the Integer data : '))
obj1 =  Compute()
while True:
    print('Enter 1 to ADD value inside the list')
    print('Enter 2 to REMOVE values from the list')
    print('Enter 3 to DISPLAY value of list')
    print('Enter 4 to STOP EXECUTION')
    choice = int(input('Enter your choice : '))
    if choice == 1:
        obj1.add()
    elif choice == 2:
        obj1.remove()
    elif choice == 3:
        obj1.disp()
    elif choice == 4:
        break
    else:
        print('Invalid choice')