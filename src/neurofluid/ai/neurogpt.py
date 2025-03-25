import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer

class NeuroGPT:
    def __init__(self, model_path="neurofluid-gpt"):
        self.tokenizer = GPT2Tokenizer.from_pretrained(model_path)
        self.model = GPT2LMHeadModel.from_pretrained(model_path)
        
    def generate_thought(self, initial_text, max_length=100):
        inputs = self.tokenizer(initial_text, return_tensors="pt")
        outputs = self.model.generate(**inputs, max_length=max_length)
        return self.tokenizer.decode(outputs[0])
