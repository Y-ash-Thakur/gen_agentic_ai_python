import tiktoken

enc = tiktoken.encoding_for_model("gpt-4o")

text = "Hey There! My name is Yash Thakur"
tokens = enc.encode(text)

#Tokens:  [25216, 3274, 0, 3673, 1308, 382, 865, 1229, 748, 115303]
print("Tokens: ", tokens)

decoded = enc.decode([25216, 3274, 0, 3673, 1308, 382, 865, 1229, 748, 115303])
print("Decoded: ", decoded)