import re
message = "To be, or not to be, that is the question"
vowels = re.findall("[AaEeIiOoUuYy]",message)
print(len(vowels))