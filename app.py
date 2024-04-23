import g4f

class GPT:
    def __init__(self, prompt, model):
        self.prompt = prompt
        self.model = model


    def generation(prompt, model):    
        respose = g4f.ChatCompletion.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
        ) 
        return respose
        
