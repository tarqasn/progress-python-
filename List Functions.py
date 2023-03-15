l1=[]
n=int (input ("How many elements you want to enter: "))
print ("Enter elements")
for i in range (n) :
    ele=int (input ())
    l1.append (ele)
    print ("The entered list is: ",l1, '\n')
while True:
    print ("\nLIST OPERATIONS")
    print ("1. Append an element")
    print ("2. Insert an element at desired position")
    print ("3. Append a list to given list")
    print ("4. Modify an existing element")
    print ("5. Delete existing element by its position")
    print ("6. Delete existing element by its value")
    print ("7. Exit\n")
    choice=int (input ("Enter your choice (1-7): "))
    if choice==1:
        element=int (input ("Enter the element to be appended: "))
        l1.append(element)
        print ("New list: ", l1, '\n')
    elif choice==2:
        element=int (input ("Enter the element to be inserted: "))
        pos=int (input ("Enter the position: "))
        l1.insert(pos, element)
        print ("New list: ", l1, '\n')
    elif choice==3:
        new_list=list (eval (input ("Enter the list to be appended: ")))
        l1.extend(new_list)
        print ("New list: ", l1, '\n')
    elif choice==4:
        pos=int (input ("Enter position of element to be modified: "))
        new_element=int (input ("Enter new element: "))
        list [pos] =new_element
        print ("New list: ", l1, '\n')
    elif choice==5:
        pos=int (input ("Enter position of element to be deleted: "))
        l1.pop (pos)
        print ("New list: ", l1, '\n')
    elif choice==6:
        element=int (input ("Enter element to be deleted: "))
        l1.remove(element)
        print ("New list: ", l1, '\n')
    elif choice==7:
        break
    else:
        print ("Invalid choice")
