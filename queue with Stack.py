class Queue_Stack:
    def __init__(self):
        self.stack_1=[]
        self.stack_2=[]

    def Enqueue(self,item):
        self.stack_1.append(item)

    def Dequeue(self):
        if (self.stack_1==[] and self.stack_2==[]):
            print("Queue empty")
        elif ((len(self.stack_1)>0) and (len(self.stack_2)==0)):
            while(len(self.stack_1)):
                  popped_item=self.stack_1.pop()
                  self.stack_2.append(popped_item)
            print("Popped item : ",self.stack_2.pop())
            while(len(self.stack_2)):
                  popped_item=self.stack_2.pop()
                  self.stack_1.append(popped_item)
            
            
        
    def Display(self):
        if (self.stack_1==[]):
            print("Queue empty")
        else:
            for item in self.stack_1:
                print(item," --- ",end="")
    def Peek(self):
        print("Peek element : ",self.stack_1[0])

    def Contains(self,item):
        if self.stack_1==[]:
            print("Stack is empty")
        else:
            for i in self.stack_1:
                if i==item:
                    print("Element exists")
        
print("Implementation of Queue Using Stack")
obj=Queue_Stack()
while True:
    print("1) Enqueue \n2) Dequeue  \n3) Display  \n4) Contains \n5) Peek")
    choice=int(input())
    if choice==1:
        size=int(input("Enter Size of Queue : "))
        for item in range (size):
            n=int(input("Enter element to add : "))
            obj.Enqueue(n)
        obj.Display()
        print()
    elif choice==2:
        obj.Dequeue()
        obj.Display()
        print()
    elif choice==3:
        obj.Display()
        print()
    elif choice==4:
        n1=int(input("Enter element to Search for : "))
        obj.Contains(n1)
        print()
    elif choice==5:
        obj.Peek()
        print()
    else:
        print("Enter correct choice")
        print()
