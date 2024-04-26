import g4f


class GPT:
    def __init__(self):
        pass

    def generation(self, prompt, model):   
        response = g4f.ChatCompletion.create(
            model=model,
            messages=prompt,
            provider="Aichatos",)
        return response
