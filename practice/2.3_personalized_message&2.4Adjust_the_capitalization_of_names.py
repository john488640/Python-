#Project: Python personalized message
#By: John Forkens Website:  https://github.com/john488640
#E:\Project\python\Practice\2.3_personalized_message&2.4Adjust_the_capitalization_of_names.py
#P2.3 P21
#This program will print a personalized message to the user.
print("Practice 2.3: Personalized message")
name = "Frank"
message = f"Hello{name},how are you?"
print(message)
#output:
#Hello Frank,how are you?


#Project: Adjust the capitalization of names
#By: John Forkens Website:  https://github.com/john488640
#E:\Project\python\Practice\2.3_personalized_message&2.4Adjust_the_capitalization_of_names.py
#P2.4 P21
#This program will adjust the capitalization of names
print("Practice 2.4: Adjust the capitalization of names")
name = "frank"
message = f"Hello{name},how are you?"
print(message)
message = message.title()
print(message)
message = message.upper()
print(message)
message = message.lower()
print(message)
#output:
#Hello frank,how are you?
#Hello Frank,how are you?
#HELLO FRANK,HOW ARE YOU?
#hello frank,how are you?
