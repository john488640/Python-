#Project: f_value_strings
#By: John Forkens Website:  https://github.com/john488640
#E:\Project\python\\2.3.2_f_value_strings
#2.3 P17
#This program uses variables in the string, which is known as an F-string.

first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)

print(f"Hello,{full_name.title()}")
message = f"Hello, {full_name.title()}"
print(message)

#Output:
#ada lovelace
#Hello,Ada Lovelace
#Hello, Ada Lovelace


#In the above code, we have used an F-string to concatenate the first_name and last_name variables into a single string. The f before the string allows us to use variables in the string.
#F字符串是一种字符串，它允许在字符串中使用变量。在上面的代码中，我们使用了F字符串将first_name和last_name变量连接成一个字符串。在字符串前面加上f表示这是一个F字符串，这样就可以在字符串中使用变量了。