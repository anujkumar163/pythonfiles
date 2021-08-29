class question:
    def __init__(self, prompt,  answer):
        self.prompt = prompt
        self.answer = answer


question_prompts = [
    "is eath is round", "T/F",
    "is i am a boy", "T/F",
    "is my name is anuj", "T/F",
]  

questions = [
    question(question_prompts[0], "T")
    
]

def run_quiz():
    score = 0
    print("True or False"+ s[0])
    guess = input("Enter T or F")  
    if guess == s[1]:
        print("correct!")
        score += 1
    else:
        print("Incorrect")
print("Your final sum is: " + str(sum))
run_quiz()        

               
    
