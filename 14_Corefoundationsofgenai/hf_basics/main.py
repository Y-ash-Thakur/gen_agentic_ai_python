from transformers import pipeline

pipe = pipeline("text-generation", model="distilgpt2")
print(pipe("Explain AI:", max_length=50))