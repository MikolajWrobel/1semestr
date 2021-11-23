import re
message = "To be, or not to be, that is the question"
words = re.findall("\w{1,100}",message)
print(len(words))