from Question import Question 

question_prompts = [
    'what color are apple?\n(a) red/breen\n(b) purple\n(c) orange\n\n',
    'what color are bananas/\n(a) teal\n(b) magenta\n(c) yellow\n\n\n',
    'what color are strawberries/\n(a) Yellow\n(b) Red\n(c) Blue\n\n'
] 
questions = [
    Question(question_promts[0], "a"  ),
    Question(question_promts[1], "c"  ),
    Question(question_promts[2], "b"  ),
]
def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt) 
        if answer == question.answer:
            score += 1
    print("you got" + str(score) + "/" + str(len(questions)) + "correct" )
run_test(questions)           