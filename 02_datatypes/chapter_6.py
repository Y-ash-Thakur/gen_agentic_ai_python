# Strings

chai_type = "Masala Chai"
customer_name = 'Priya'

chai_description = "Aromatic and bold"
print(f"Order for {customer_name}: {chai_type} please!")
print(f"first word: {chai_description[:8]}")
print(f"Last word: {chai_description[12:]}")
print(f"Reversed description: {chai_description[::-1]}")

label_text = "Chai Special"
encoded_label = label_text.encode('utf-8')
print(f"Non Encoded Label: {label_text}")
print(f"Encoded label: {encoded_label}")
decoded_label = encoded_label.decode('utf-8')
print(f"Decoded label: {decoded_label}")