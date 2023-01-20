# This quiz game is basically a quiz which based on the python knowledge 
print("welcome to the python quiz")
# It will ask you want to play or not
playing=input("Do you want to play? ")
if playing.lower()!="yes":
  quit()
else:
    username = input("Enter your username: ")
    print(str(username) + " Lets Start the quiz")
print("           ")
# This score Function will count your numbers that how much you score in the quiz
score = 0

#The answers Function will provide you an answer of that question which one is wrong and give you correct answer
answer1="guido van rossum"
answer2="no"
answer3="lambda"
answer4="preferred installer program"
answer5="getopt"
answer6="no"
answer7=9
answer8="turtle.bgcolor()"
answer9=1991
answer10="constructor"
# Here i used the question function for each questions and providing the number according to serial wise
# 1 
# if and elif Function is used for condition statement
question1 = input("Who developed python language? : ")
if question1.lower() == (answer1): 
    print("Your answer " + str(question1) + " is correct") 
    print("           ")
    score += 1
elif question1 != (answer1):
    print("Your answer " + str(question1) + " is incorrect")
    print("correct answer is guido van rossum ")
    print("           ")
    score=score
#2
# lower function is used for case sensitive
question2 = input("Is python case sensitive when dealing with identifiers? : ")
if question2.lower() == (answer2): 
    print("Your answer " + str(question2) + " is correct")
    print("           ")
    score += 1
elif question2 != (answer2):
    print("Your answer " + str(question2) + " is incorrect")
    print("correct answer is no ")
    print("           ")
    score=score
#3
# == and != both sign is used for comparsion 
question3 = input("Python supports the creation of anonymous functions at runtime using a construct called------ : ")
if question3.lower() == (answer3):
    print("Your answer " + str(question3) + " is correct")
    print("           ")
    score += 1
elif question3 != (answer3):
    print("Your answer " + str(question3) + " is incorrect")
    print("correct answer is lambda ")
    print("           ")
    score=score
#4
question4 = input("What does pip stand for python? : ")
if question4.lower() == (answer4):
    print("Your answer " + str(question4) + " is correct")
    print("           ")
    score += 1
elif question4 != (answer4):
    print("Your answer " + str(question4) + " is incorrect")
    print("correct answer is preferred installer program ")
    print("           ")
    score=score
#5
question5 = input("Which module in the python standard library parses options recived from the command line? : ")
if question5.lower() == (answer5):
    print("Your answer " + str(question5) + " is correct")
    print("           ")
    score += 1
elif question5 != (answer5):
    print("Your answer " + str(question5) + " is incorrect")
    print("correct answer is getopt ")
    print("           ")
    score=score
#6
question6 = input("Is there a length limit for an identifier in python : ")
if question6.lower() == (answer6):
    print("Your answer " + str(question6) + " is correct")
    print("           ")
    score += 1

elif question5 != (answer6):
    print("Your answer " + str(question6) + " is incorrect")
    print("correct answer is no ")
    print("           ")
    score=score
#7
question7 = int(input("What is output of print(math.pow(3,2))?(please enter integers) : "))
if question7 == (answer7):
    print("Your answer " + str(question7) + " is correct")
    print("           ")
    score += 1

elif question7 != (answer7):
    print("Your answer " + str(question7) + " is incorrect")
    print("correct answer is 9 ")
    print("           ")
    score=score
#8
question8 = input("command to change background colour in python is ----- : ")
if question8 == (answer8):
    print("Your answer " + str(question8) + " is correct")
    print("           ")
    score += 1

elif question8 != (answer8):
    print("Your answer " + str(question8) + " is incorrect")
    print("correct answer is turtle.bgcolor() ")
    print("           ")
    score=score
#9
question9 = int(input("In which year python was introduced? (please enter integers) : "))
if question9 == (answer9):
    print("Your answer " + str(question9) + " is correct")
    print("           ")
    score += 1

elif question9 != (answer9):
    print("Your answer " + str(question9) + " is incorrect")
    print("correct answer is 1991 ")
    print("           ")
    score=score
#10
question10 = input("---- is used to create an object. : ")
if question10.lower() == (answer10):
    print("Your answer " + str(question10) + " is correct")
    print("           ")
    score += 1

elif question10 != (answer10):
    print("Your answer " + str(question10) + " is incorrect")
    print("correct answer is constructor ")
    print("           ")
    score=score
print("The End ")
print("           ")
# print command is used to printing the score and also if the score range is 6 to 10 then it will print "Good Score" otherwise it will print "Need more practice"
print(str(username) + " got "+ str(score) + " questions correct out of 10")
percent = (str(username) + " you got "+ str(score/10 * 100) + " percent")
print(percent)
if  score == 10:
    print("Perfect score")
elif  score> 6 < 10:
    print("Good score")
else:
    print("Need more practice")
