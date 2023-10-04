import random 
x= str(input("Do you want to roll the dice? Yes or No-- "))
#no=int(input("Roll your dice and enter the digit obtained (1,6): "))  
response = "Yes" 
while response=="Yes":
    no = random.randint(1,6) 
    if no==1:
        print("[------]")
        print("[      ]")
        print("[   0  ]") 
        print("[      ]")
        print("[------]") 
    if no==2:
        print("[------]")
        print("[      ]")
        print("[   0  ]")
        print("[   0  ]")
        print("[      ]")
        print("[------]")
    if no==3:
        print("[------]")
        print("[      ]")
        print("[   0  ]")
        print("[   0  ]")
        print("[   0  ]")
        print("[------]")
    if no==4:
        print("[------]")
        print("[0    0]") 
        print("[0    0]")
        print("[      ]")
        print("[------]")
    if no==5:
        print("[------]")
        print("[0    0]")
        print("[   0  ]")
        print("[0    0]")
        print("[------]")
    if no==6:
        print("[------]")
        print("[0    0]")
        print("[0    0]")
        print("[0    0]")
        print("[------]")


        print("press y to roll again and n to stop")
        break  
    
    

