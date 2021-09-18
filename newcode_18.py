#building a multiple choice question
from question import Question
question_prompts = [
    "What is the color of apples? \n(a)Pink \n(b)Red \n(c)Yellow \n(d)Blue \n\n",
    "What is the color of banana? \n(a)Pink \n(b)Red \n(c)Yellow \n(d)Blue \n\n",
    "What is the color of kiwi? \n(a)Green \n(b)Red \n(c)Yellow \n(d)Blue \n\n",
    "What is the color of orange? \n(a)Pink \n(b)Orange \n(c)Yellow \n(d)Blue \n\n"
]

questions = [
    Question(question_prompts[0], "b"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "a"),
    Question(question_prompts[3], "b")
]


def run_test(questions):
    score = 0 
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " Correct")  

run_test(questions)          