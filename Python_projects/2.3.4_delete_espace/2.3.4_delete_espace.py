#Project: delete escape  in Python
#By: John Forkens Website:  https://github.com/john488640
#E:\Project\python\2.3.4_delete_espace
#2.3.4 P18-19
#This program will delete escape.

#lstrip()
favorite_languages = '  Python'
print(favorite_languages)
print('I will delete the escape using lstrip() method.')
print(favorite_languages.lstrip())

#rstrip()
favorite_languages = 'Python  '
print(favorite_languages)
print("I will delete espace using rstrip() method.")
print(favorite_languages.rstrip())
print(favorite_languages.rstrip())

#strip()
favorite_languages = '  Python  '
print(favorite_languages)
print("I will delete espace using strip() method.")
print(favorite_languages.strip())
