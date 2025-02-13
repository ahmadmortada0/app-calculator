# 2 ways to solve the equation 
magic = input("wanna see a magic trick Y/N :" )

if  magic=="Y":
    num = int(input("Choose a num :"))
# first way 
if num == 0 :
    print ("the number is even")
elif num%2==0:
    print("the number is even")
else :
    print("the number is odd")
#second way
fnum = float(num)
power= fnum/2
if num == 0 :
    print ("the number is even")
elif (fnum/2)/int(power)-1==0:
    print("the number is even")
else :
    print("the number is odd")