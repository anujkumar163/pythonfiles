import random
class GenerateData:
    def __init__(self, df, num_ques, form):
        self.df = df
        self.num_ques = num_ques
        self.form = form
    def generate_eng2ger(self):
        question = []
        data_len = len(self.df)+1
        n = random.randint(0, data_len)
        lst = []
        options = []
        for i in range(3):
            no = random.randint(0, data_len)
            lst.append(no)
            lst.append(n)
            lst = random.sample(lst, len(lst))
    
    ### Creating the question
            question.append(f'Select a german word for "{self.df.iloc[n, 1]}":')
    
    ### Creating options/choices
        for l in lst:
            options.append(f'{self.df.iloc[l, 0]}')
### Allocating the answer
            answer = self.df.iloc[n, 0]
        return question, options, answer
obj = GenerateData
print(obj)
      
