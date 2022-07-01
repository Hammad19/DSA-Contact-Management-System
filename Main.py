#Linear Search
#Binary Search
#ARRAY
#Bubble Sort
#Selection Sort
#Stack
#LinkedList

class Node:
  
    # Function to initialise the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as null
  
  
# Linked List class contains a Node object
class LinkedList:
  
    # Function to initialize head
    def __init__(self):
        self.head = None
  
  
    # Functio to insert a new node at the beginning
    def append(self, new_data):
  
        # 1. Create a new node
        # 2. Put in the data
        # 3. Set next as None
        new_node = Node(new_data)
  
        # 4. If the Linked List is empty, then make the
        #    new node as head
        if self.head is None:
            self.head = new_node
            return
  
        # 5. Else traverse till the last node
        last = self.head
        while (last.next):
            last = last.next
  
        # 6. Change the next of last node
        last.next =  new_node
  
    
    def printList(self):
        temp = self.head
        while (temp):
            print ("\n\t" + str(temp.data))
            temp = temp.next
  


stack = []  
def bubbleSort(arr):
    n = len(arr)
  
    for i in range(n-1):
        for j in range(0, n-i-1):
  
            
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]

def insertion_sort(arr):
    for step in range(1, len(arr)):
        key = arr[step]
        j = step - 1
        while j >= 0 and key > arr[j]:
            arr[j + 1] = arr[j]
            j = j - 1
            arr[j + 1] = key

def binary_search(arr, low, high, x):

        if high >= low:
            mid = (high + low) // 2
            if int(arr[mid]) == x:
                return arr[mid]
            elif int(arr[mid]) > x:
                return binary_search(arr, low, mid - 1, x)
            else:
                return binary_search(arr, mid + 1, high, x)
     
        else:
            return -1


def linearsearch(arr, x):
  
    for i in range(len(arr)):
  
        if int(arr[i]) == int(x):
            return arr[i]
  
    return -1
import os

class Contacts:
    
    contacts = []
    def __init__(self,emailaccount,name,phone_number,email,address):
        self.emailaccount=emailaccount
        self.name=name.lower()
        self.phone = phone_number
        self.email= email
        self.address = address

    
    def getallcontactno(self):
            file= str(self.emailaccount)+ "contacts.txt"
            if os.path.exists(file):
                for line in open(file, "r").readlines():
                    data = line.split(',')
                    self.contacts.append((data[1]))
                    
    def iscontactalreadytaken(self):
        self.contacts =[]
        self.getallcontactno()
        if(linearsearch(self.contacts,self.phone) == -1):
            return False
        else:
            return True
        
              
    def AddContacts(self):
        file= str(self.emailaccount)+ "contacts.txt"
        f = open(file,"a+")
        if(self.iscontactalreadytaken()==False):
            f.write(str(self.name) + "," 
                    + str(self.phone)+ "," 
                    + str(self.email) +"," 
                    + str(self.address) +"," 
                    + "\n")
        else:
            print("\tContact Number Already In List")
        f.close()
    def DisplayContacts(self):
        self.contacts = []
        self.getallcontactno()
        ascdes = int(input("\t1. Ascending Order\n\t2. Descending Order\n\t3. Back"))
        if(ascdes == 1):
            stack.append(self.DisplayContacts)
            bubbleSort(self.contacts)
            file= str(self.emailaccount)+ "contacts.txt"
            if(os.path.exists(file)):
                for i in range(len(self.contacts)):
                    for line in open(file, "r").readlines():
                        data=line.split(',')
                        if(self.contacts[i] == data[1]):
                            print()
                            print(str("\tContact"))
                            print("\tName: " + str(data[0]))
                            print("\tPhone: " + str(data[1]))
                            print("\tEmail: " + str(data[2]))
                            print("\tAddress: " + str(data[3]))
            else:
                print("\tNo Contacts in Your Account")
                
        elif(ascdes== 2):
            stack.append(self.DisplayContacts)
            insertion_sort(self.contacts)
            file= str(self.emailaccount)+ "contacts.txt"
            if(os.path.exists(file)):
                for i in range(len(self.contacts)):
                    for line in open(file, "r").readlines():
                        data=line.split(',')
                        if(self.contacts[i] == data[1]):
                            print()
                            print(str("\tContact"))
                            print("\tName: " + str(data[0]))
                            print("\tPhone: " + str(data[1]))
                            print("\tEmail: " + str(data[2]))
                            print("\tAddress: " + str(data[3]))
                        
        elif(ascdes == 3):
            stack.pop()()
            
            
        str(input("\tPress Any Key"))
        stack.pop()()
    
    def DeleteContacts(self):
        self.contacts = []
        self.getallcontactno()
        file= str(self.emailaccount)+ "contacts.txt"
        file2= str(self.emailaccount)+ "tempcontacts.txt"
        f = open(file,"r")
        f2 = open(file2,"w")
        for line in f.readlines():
            data = line.split(',')
            #Linear Search
            if(str(self.phone)==str(data[1])):  
                continue
            else:   
                f2.write(
                    str(data[0]) + "," + 
                    str(data[1])+ "," + 
                    str(data[2]) +"," + 
                    str(data[3]) +",\n" )
                
        f.close()
        f2.close()
        str(input("\n\tSuccessfully Deleted\n\tPress Any Key To Go Back To The main menu\n\n"))
        self.MoveData(file2,file)
        stack.pop()()
        
    def DeleteAllContacts(self):
        confirmation = str(input("Are You Sure You Want To Delete All Contacts Y/N"))
        file= str(self.emailaccount)+ "contacts.txt"
        if (os.path.exists(file)) and (confirmation =='Y'):
            os.remove(file)
        
        str(input("\n\tSuccessfully Deleted All Contacts\n\tPress Any Key To Go Back To The main menu\n\n"))
        stack.pop()()
         
        
        
    def EditContacts(self):
        file= str(self.emailaccount)+ "contacts.txt"
        file2= str(self.emailaccount)+ "tempcontacts.txt"
        x = open(file2,"w")
        for line in open(file,"r").readlines():
            data = line.split(',')
            print()
            print()
            #Linear Search
            if(str(self.phone)==str(data[1])):
                x.write(str(input('\tEnter New Name: '))+ "," 
                         + str(input('\tEnter New Phone Number: ')) +","
                         + str(input('\tEnter New Email: '))+ ","
                         + str(input('\tEnter Your New Address: '))
                         + ",\n")        
            else:
                x.write(str(data[0]) + "," + 
                         str(data[1])+ "," + 
                         str(data[2]) +"," + 
                         str(data[3])+ ",\n" )
                         
        x.close()
        str(input("\n\tSuccessfully Edited\n\tPress Any Key To Go Back To The main menu\n\n"))
        self.MoveData(file2,file)
        stack.pop()()
    

    
# Python 3 program for recursive binary search.
# Modifications needed for the older Python 2 are found in comments.
 
# Returns index of x in arr if present, else -1
    
    def SearchContacts(self):
        self.contacts = []
        self.getallcontactno()
        var = True
        file= str(self.emailaccount)+ "contacts.txt"
        for line in open(file,"r").readlines():
            data = line.split(',')
            index = binary_search(self.contacts,0, len(self.contacts)-1,int(self.phone))
            if(index== data[1]):
                print("\tName: " + str(data[0]))
                print("\tPhone: " + str(data[1]))
                print("\tEmai;: " + str(data[2]))
                print("\tAddress: " + str(data[3]))
                str(input("\tPress Any Key To Go Back To The main menu\n\n"))
                var = True
                
        if(var == False):
            print("\tNo Contact Found")
        
        stack.pop()()
                

    def MoveData(self,file,file2):
         with open(file,"r") as f:
            with open(file2, "w+") as f1:
                for line in f:
                    f1.write(line)
                
                f.close()
                f1.close()
    
         if os.path.exists(file):
             os.remove(file)
         else:
            print("The file does not exist")
    
        
class User:
    def __init__(self,name,email,password):
        
        self.name=name.lower()
        self.email=email
        self.password = password
    
    def Register(self):
        f = open("Users.txt","a+")
        #Searching Algorithm Can Be Applied Here to Search
        if(True):
            f.write(str(self.name) 
                    + "," + str(self.email)+ "," 
                    + str(self.password)
                    + ",\n")   
            print("\tSuccessFully Registered")
            f.close() 
        else:
            print('\tThis Email is Already in Use')
        
        
    def Login(self):
        
        x=''
        if(os.path.exists("Users.txt")):
            for line in open("Users.txt", "r").readlines():
                data = line.split(',')
                if(self.email==data[1] and self.password == data[2]):
                    self.name = data[0]
                    self.email =data[1]
                    self.password= data[2]
                    self.WelcomeUser()
                else:
                    x = 'notfound'
                    
            if(x=='notfound'):
                print("\tInvalid Email or Password")
        else:
            print("\n\tNo User Registered")
            
            
    def WelcomeUser(self):
        while(True):
            print('\t\t\t***********************************************')
            print("\t\t\t           "+ self.name+ "! Welcome To CMS ")
            print('\t\t\t***********************************************')
            
            llist = LinkedList()
            llist.append("1. Add Contacts")
            llist.append("2. Display Contacts")
            llist.append("3. Edit Contacts")
            llist.append("4. Search Contacts")
            llist.append("5. Delete Contacts")
            llist.append("6. Delete All Contacts")
            llist.append("7. Log Out") 
            llist.printList()
            select=input("\tEnter Your Selection (1-6): ")
            if select=='1':
                stack.append(self.WelcomeUser)
                c = Contacts(self.email,
                             input("\tEnter Name:"),
                             input("\tEnter Phone Number:"),
                             input("\tEnter Email:"),
                             input("\tEnter Address:"),
                             )
                c.AddContacts()
            
                
            
            elif select=='2':
                stack.append(self.WelcomeUser)
                c = Contacts(self.email,
                             'none',
                             'none',
                             'none',
                             'none',
                             )
            
                c.DisplayContacts()
                
            elif select=='3':
                stack.append(self.WelcomeUser)
                c = Contacts(self.email,
                             'none',
                             input("\tEnter Phone Number:"),
                             'none',
                             'none',
                             )
                c.EditContacts()
                
            elif select=='4':
                stack.append(self.WelcomeUser)
                c = Contacts(self.email,
                             'none',
                             input("\tEnter Phone Number:"),
                             'none',
                             'none'
                             )
                c.SearchContacts()
            
            elif select=='5':
                stack.append(self.WelcomeUser)
                c = Contacts(self.email,
                             'none',
                             input("\tEnter Phone Number:"),
                             'none',
                             'none',
                             )
                c.DeleteContacts()
            
            elif select=='6':
                stack.append(self.WelcomeUser)
                c = Contacts(self.email,
                             'none',
                             'none',
                             'none',
                             'none',
                             )
                c.DeleteAllContacts()
            elif select=='7':
                stack.pop()()
            
            else:
                print("\tWrong Input")
                
    
            
print('*******************************************************')
print('       CONTACT  MANAGEMENT  SYSTEM ')
print('*******************************************************')
print('*******************************************************')
print('*******************************************************')


def runfunc():
    while(True):
        llist = LinkedList()
        llist.append("1. Login")
        llist.append("2. Register")
        llist.append("3. Exit")
        llist.printList()
        select=input("Enter Your Selection (1-3): ")
        if select=='1':
            stack.append(runfunc)
            user= User('none',input("\tEnter Your Email:"),input("\tEnter Your Password:"),)
         
            user.Login()
                
        elif select=='2':
            stack.append(runfunc)
            user= User(
                
                input("\tEnter Your Name:"),input("\tEnter Your Email:"),input("\tEnter Your Password:"))
            
            user.Register()
            
        elif select=='3':
            
            break
        
        else:
            print('Wrong Input')
            
            

runfunc()