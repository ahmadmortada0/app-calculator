age= int(input("Enter Your Age :"))
if age <100:
  if age<=4:
    print("The ticket is unavaible cause your age is "+ str(age))
  elif age<=8:
    print ("TIcket price is 5$")
  elif age <=15 :
      print ("TIcket price is 15$")
  else :
    print ("ticket price is 20$")
else:
  print ("Go rest in your grave ")
