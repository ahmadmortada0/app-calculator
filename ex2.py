# 2 ways to solve the equation 
magic = input("wanna see a magic trick Y/N :" )

if  magic=="Y":
    num = int(input("Choose a num :"))
# first way 
if num == 0 :
    print ("even")
elif num%2==0:
    print("even")
else :
    print("odd")