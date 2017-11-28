from random import randint

n1 = randint (1,9)
n2 = randint (1,9)
n3 = randint (1,9)
n4 = randint (1,9)
numberswrong = 0
print (n1,n2,n3,n4)
guess1 = input("guess the first number")
guess2 = input("guess the second number")
guess3 = input("guess the third number")
guess4 = input("guess the fourth number")
guess1 = int (guess1)
guess2 = int (guess2)
guess3 = int (guess3)
guess4 = int (guess4)
if guess1 != n1:
    numberswrong +=1
else:
    numberswrong +=0   
if guess2 != n2:
    numberswrong +=1
else:
    numberswrong +=0 
if guess3 != n3:
    numberswrong +=1
else:
    numberswrong +=0 
if guess4 != n4:
    numberswrong +=1
else:
    numberswrong +=0 
print ("you got",numberswrong, "numbers wrong")
if numberswrong == 0:
    print ("Well done")
while numberswrong != 0:
    guess1 = input("guess the first number")
    guess2 = input("guess the second number")
    guess3 = input("guess the third number")
    guess4 = input("guess the fourth number")
    guess1 = int (guess1)
    guess2 = int (guess2)
    guess3 = int (guess3)
    guess4 = int (guess4)
    if guess1 != n1:
        numberswrong +=1
    else:
        numberswrong +=0   
    if guess2 != n2:
        numberswrong +=1
    else:
        numberswrong +=0 
    if guess3 != n3:
        numberswrong +=1
    else:
        numberswrong +=0 
    if guess4 != n4:
        numberswrong +=1
    else:
        numberswrong +=0 
    print ("you got",numberswrong, "numbers wrong")
print ("Well done")