# poem = """Machli jal ki raani hai
# jeevan uska pani hai"""
# print(poem);

# import os;
# print(os.listdir());

# x = 5 * 1
# y = 5 * 2
# z = 5 * 3
# print(x,"\n",y,"\n",z)

# string1 = "Satyam"
# Bolleantype = True
# integertype = 5+ 6
# floattype = 5 + 8.99

# print(string1)
# print(Bolleantype)
# print(integertype)
# print(floattype)

# print(type(string1))
# print(type(Bolleantype))
# print(type(integertype))
# print(type(floattype))

# a = 55;
# print(type(a))
# print(a)
# a = "565";
# print(type(a))
# print(a)
# a = float(a);
# print(type(a))
# print(a)

# name = str(input("Your Name : "))
# age = int(input("Your Age : "))
# print(f"My name is {name} My age is {age}")
# print(f"Two years ago My age was {age-2}")

# num1 = int(input("Your First Number : "))
# num2 = int(input("Your Second Number : "))
# print(f"Addition of two numbers = {num1 + num2}")

# a = 56743
# b= 324
# print(f"Quotient : {int(a / b)}")
# print(f"Remainder : {a % b}")
# print(f"dividend : {int(a / b) * b}")

# variabletype = input("input do : ")
# print(type(variabletype))
# print(variabletype)
# variabletype = float(variabletype)
# print(type(variabletype))
# print(variabletype)
# variabletype = int(variabletype)
# print(type(variabletype))
# print(variabletype)
# variabletype = bool(variabletype)
# print(type(variabletype))
# print(variabletype)

# num1 = 44
# num2 = 56
# print(f"number 1 : {num1}")
# print(f"number 2 : {num2}")
# print(f"number 1 is greater than number 2 : {num1 > num2}")
# print(f"number 1 is Smaller than number 2 : {num1 < num2}")

# print("Average Begins")
# number1 = int(input("Enter Number 1 : "))
# number2 = int(input("Enter Number 2 : "))
# print(f"Average : {(number1 + number2)/2}")
# print("Average Ends")

# import math
# print("Here you can square your number")
# Number = int(input("Enter a Number : "))
# print(f"Square root : {math.sqrt(Number)}")

# slicestring = "satyamsharma"
# <-------------slice----------------> 
# print(slicestring[-9:6])

# --------------methods--------------
# ans = slicestring.endswith("a")
# print(ans)
# ans = slicestring.endswith("b")
# print(ans)

# ans = slicestring.count("s")
# print(ans)

# ans = len(slicestring)
# print(ans)

# ans = slicestring.capitalize()
# print(ans)
# ans = slicestring.upper()
# print(ans)

# ans = slicestring.find("t")
# print(ans)

# ans = slicestring.replace("a", "-")
# print(ans)

# -------------Escape--------
# str1 = "satyam\n Achha\t \'bacha\' \\hai\\"
# print(str1)

# -------------greet------------
# name = str(input("Enter Name : "))
# print(f"Good afternoon {name.capitalize()}")

# --------letter using replace---------------
# Name = str(input("Enter Your Name :"))
# Date = str(input("Todays Date :"))
# letterbody = "Dear <|NAME|>,\n\tyou are selected!\n\tDate : <|DATE|>"
# letterbody = letterbody.replace("<|NAME|>", Name)
# letterbody = letterbody.replace("<|DATE|>", Date)
# print(letterbody)

# ---------------find Double Soace--------------------
# string1 = "satyam  sharma   naam  ka  ladka  Hai"
# print(string1.find("  ",7))

# string1 = "satyam  sharma   naam  ka  ladka  Hai"
# print(string1.replace("  "," "))

# list1 = ["dosa", "idli", "sambhar", "daal", "chawal"]
# print(list1)
# print(list1[0])
# print(list1[2])
# list1[0] = "Roti"
# print(list1)

# list1 = [0,1,2,3,4,5,6,7,8,9]
# print(list1[1:8])
# print(list1[4:])
# print(list1[:5])
# print(list1[:-3])
# print(list1[-7:-1])
# print(list1[-8:])

# numlist = [54, 324, 876, 0, 9, 32, 34, 53]
# # numlist.sort()
# print(numlist)
# # numlist.reverse()
# print(numlist)
# # numlist.append("Mohan")
# print(numlist)
# # numlist.insert(2,"Mohan")
# print(numlist)
# # numlist.pop()
# print(numlist)
# numlist.remove(32)
# print(numlist)

# -----------------Tuple---------------
# -----------No Manipulation-----------

# singletuple = (2,);#Single Tuple Creation
# NormalTuple = (1,2,3,4,2,8,6,9,2,8,5,4,3,433);
# # TupleCount = NormalTuple.count(3)
# # TupleCount = len(NormalTuple)
# # TupleCount = NormalTuple.index(8,6)
# TupleCount = NormalTuple[13]
# print(TupleCount)

# fruitlist = []
# fruit1 = input("Enter Fruit 1 : ")
# fruitlist.append(fruit1)
# fruit2 = input("Enter Fruit 2 : ")
# fruitlist.append(fruit2)
# fruit3 = input("Enter Fruit 3 : ")
# fruitlist.append(fruit3)
# fruit4 = input("Enter Fruit 4 : ")
# fruitlist.append(fruit4)
# fruit5 = input("Enter Fruit 5 : ")
# fruitlist.append(fruit5)
# print(f"Fruit List = {fruitlist}")

# sortedMarkList = []
# student1 = int(input("Student 1 marks : "))
# sortedMarkList.append(student1)
# student2 = int(input("Student 2 marks : "))
# sortedMarkList.append(student2)
# student3 = int(input("Student 3 marks : "))
# sortedMarkList.append(student3)
# student4 = int(input("Student 4 marks : "))
# sortedMarkList.append(student4)
# sortedMarkList.sort()
# print(sortedMarkList)

# atuple = (1,"dog",33,4.5,True)
# # atuple[2] = 56 --> Assignment Not Possible
# print(atuple[2])

# list1 = [10,20,50,20]
# print(f"Sum of the list = {list1[0] + list1[1] + list1[2] + list1[3]}")

# -----------------Dictionary-----------------
# -----------------NO INDEXING----------------

# OppWords ={"Narrow" : "wide",     #comma ',' is must for next dictionary set
#             "intentional" : "accidental",#a dictionary has {"key" : "Value" }
#             "light" : "dark",       #there is no position number in dictionary
#             "Delicious" : "awful",
#             "synonyms" : {"up":"above"}
#             }

# OppWords["Deliucious"] = [4,7,23]
# print(OppWords["synonyms"]["up"])

# OppWords ={"Narrow" : "wide",     
#             "intentional" : "accidental",
#             "light" : "dark",       
#             "Delicious" : "awful"
#             }
# # print(OppWords.keys())
# print(type(OppWords.keys()))
# print(list(OppWords.keys()))
# print(OppWords.keys())
# print(type(OppWords.keys()))

# print(OppWords.values())
# print(OppWords.items())

# addOppWords1 = {"Up":"Down" }
# # ----Use  Update to add new key value pair in Dictionary----
# OppWords.update(addOppWords1)
# print(OppWords.items())

# print(list(OppWords.items()))

# print(OppWords.get("Delicious3")) #No error but None
# print(OppWords["Delicious"])
