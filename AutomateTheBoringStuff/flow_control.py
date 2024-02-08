print("Comparison Operators and data types")
print(42 == 42)  #Should return True 
print("\n")
print(42 == 'hello') #Should return False
print("\n")
print(42 == '42') #Should return False
print("\n")
print(43 == 42) #Should return False
print("\n")
print (2 != 3) #Should return True
print("\n")
print(2 != 2) #Should return False
print("\n")
print('hello' == 'hello') #Should return True
print("\n")
print('hello' == 'Hello') #Should return False
print("\n")
myAge = 32
print(myAge < 30) #Should return False
print("\n")
print (myAge > 30) #Should return True
print("\n")
print(42 == 42.0) #Should return True


#Boolean Operators
print("Boolean Operators")
print("\n")
print(True and True) #Should return True
print("\n")
print(True and False) #Should return False
print("\n")
print(False and False) #Should return False
print("\n")
print(True or True) #Should return True
print("\n")
print(True or False) #Should return True
print("\n")
print(False or False) #Should return False
print("\n")

#Not Operator
print("Not Operator")
print(not True) #Should return False
print("\n")
print(not False) #Should return True
print("\n")
print(not (4 < 2)) #Should return True
print("\n")

#Fun with Truth Tables
print("Fun with Truth Tables")
print((4 < 2) and (2 < 4)) #Should return False
print("\n")
print((4 < 2) or (2 < 4)) #Should return True
print("\n")
print(not (4 < 2)) #Should return True
print("\n")

#Mixing Boolean and Comparison Operators
print("Mixing Boolean and Comparison Operators")
print((4 < 2) and (2 < 4)) #Should return False
print("\n")
print((4 < 2) or (2 < 4)) #Should return True
print("\n")
print(not (4 < 2)) #Should return True
print("\n")
print((myAge > 30) and (myAge < 33)) #Should return True
print("\n")
print("Enter your pets name")
myPet = input()
print("\n")
print("your pets name is " + str(len(myPet)) + " letters long") #Should return 3
print("\n")
print((myAge > 30) and (myPet == "Navi")) #Should return True
print("\n")
print((myAge > 30) or (myPet == "Navi")) #Should return True
print("\n")
print(not (myAge > 30) or (myPet != "Navi")) #Should return False