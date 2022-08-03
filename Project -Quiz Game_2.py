print("Welcome to python Quiz \n")
playing=input("Do you want to play? \n ")
if playing.lower()!="yes":
    quit()
else:
    username=input("Enter your username: ")
    print(str(username) + " Lets Start the quiz \n")


class Question:
     def _init_(self, prompt, answer):
          self.prompt = prompt
          self.answer = answer

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
    Question(question_prompts[0], "guido van rossum"),
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

def run_quiz(questions):
     score = 0
     for question in questions:
          answer = input(question.prompt)
          if answer.lower() == question.answer:
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

run_quiz(questions)