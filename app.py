import g4f


class GPT:
    def __init__(self):
        pass

    def generation(self, prompt, model):   
        print(prompt) 
        if prompt == "/exit":
            return False
        respose = g4f.ChatCompletion.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
        ) 
        return respose


if __name__ == "__main__":
    gpt = GPT("Привет, напиши код для прогноза погоды", "gpt-3.5-turbo")
    print(gpt.generation(gpt.prompt, gpt.model))
