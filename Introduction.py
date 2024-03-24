# This is a simple program that displays text to the screen with examples of combining strings.

string1 = " Python was created in the 1890's by Guido van Rossum. "
print("string1 has the following content: " + string1)
print()

string2 = " Python is maintained as an 'open source' project by a group that is called the Python Software Foundation. "
print("string2 has the following content: " + string2)
print()

string3 = " He is affectionately known as Python's \"Benevolent Dictator for Life\". "
print("string3 has the following content: " + string3)
print()

x = string1.replace("1890's","1990's")
print("x has following content: " + x)
print()
print( x.lstrip() + string3.lstrip() + string2.lstrip())
print()