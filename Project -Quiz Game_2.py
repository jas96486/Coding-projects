# The quiz game is updated version of my old project which name is Quiz game_1
print("Welcome to python Quiz \n")
playing=input("Do you want to play? \n ")
if playing.lower()!="yes": # Here if and else function is used for condition statement
    quit()
else:
    username=input("Enter your username: ")
    print(str(username) + " Lets Start the quiz \n")


class Question: # Class Function is used to bulid an own function like i created prompt and answer
     def _init_(self, prompt, answer):
          self.prompt = prompt
          self.answer = answer
# Here i used question_prompts function for all questions and it will print the question according to the serial wise
question_prompts = [
    "Who developed python language?: \n",
    "Is python case sensitive when dealing with identifiers?: \n",
    "Python supports the creation of anonymous functions at runtime using a construct called------: \n",
    "What does pip stand for python?: \n",
    "Which module in the python standard library parses options recived from the command line?: \n",
    "Is there a length limit for an identifier in python: \n",
    "What is output of print(math.pow(3,2))?(please enter integers): \n",
    "command to change background colour in python is -----: \n",
    "In which year python was introduced? (please enter integers): \n",
    "---- is used to create an object.: \n",

]

questions = [
    Question(question_prompts[0], "guido van rossum"), # Here i put the question number used by index function and also provide their answers
    Question(question_prompts[1], "no"),
    Question(question_prompts[2], "lambda"),
    Question(question_prompts[3], "preferred installer program"),
    Question(question_prompts[4], "getopt"),
    Question(question_prompts[5], "no"),
    Question(question_prompts[6], "9"),
    Question(question_prompts[7], "turtle.bgcolor()"),
    Question(question_prompts[8], "1991"),
    Question(question_prompts[9], "constructor"),


]
#  run_quiz function is used to arrange all the questions
def run_quiz(questions):
     score = 0
     for question in questions:
          answer = input(question.prompt) # input function is used to put the answer in the blank area
          if answer.lower() == question.answer: # lower function is used for case sensitive such as lowercase and uppercase letter
               score += 1
               print("your answer " + str(answer) + " is correct\n")
          else:
              print("your answers " + str(answer) + " is incorrect\n")
     print("THE END\n")
     print("you got", score, "out of", len(questions), "correct")
     print("your got "+ str(score/10 * 100) + " percent")
     if score == 10:
         print("Perfect score")
     elif score > 6 < 10:
         print("Good score")
     else:
         print("Need more practice")

run_quiz(questions) #  run_quiz function will run all the questions one by one 
