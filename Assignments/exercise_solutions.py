# 1. Simple Message
message1 = "Hi! I'm running Python and Python is not available"
print(message1)
# 2. Simple Messages
message2 = "Hi! I'm running Python and Python is available but not available"
print(message2)
message3 : str = "Hi! I'm running Python and Python is available now but not available"
print(message3)
# 3. Personal Message
name = "Tarzan"
print(f"Hello {name}, would you like to learn some Python today?")
# 4. Name Cases
name = "Katherine Mansfield"
print(name.title())
print(name.upper())
print(name.lower())
# 5. Famous Quote
author = "Louis Pasteur"
quote = "In the fields of observation chance favors only the prepared mind."
print(f'{author} once said, "{quote}"')
# 6. Famous Quote 2
famous_person = "Muhammad Ali Jinnah"
message = (f'{famous_person} famous quote, "I do not believe in taking the right decision, I take a decision and make it right"')
print(message)
# 7. Stripping Names
name = "\tTooba Yousaf\t"
print(name)
print(name.strip())
print(name.lstrip())
print(name.rstrip())
# 8. Variable Sum
x : int = 5
y : int = 10
z : int = 15
sum = x + y + z
print(sum)
# 9. Variable Swap
a = 11
b = 22
print(f'Before swap: a = {a}, b = {b}')
print(f'After swap: a = {b}, b = {a}')
# 10. Favorite Color
fav_color = "Blue"
print(fav_color)
color = fav_color
print(color)
# 11. Changing Pet Name
pet_name : str = "Buddy"
pet_nme : str = "Max"
print(pet_name)
# 12. Observing Name Error
variable = "Sunshine"
# print(sunsine)
# NameError: name 'sunsine' is not defined
#  print(sunsine)

# 13. Reassigning Score
score = 100
print(score)
score = 50
print(score)
# 14. City Name
city : str = "England"
print(city)
# 15. Title Case Text
text : str = "python programming"
print(text.title())
# 16. Lowercase Conversion
textt : str = "PyThOn PrOgRaMmInG"
print(text.lower())
# 17. Uppercase Conversion
txt : str = "pYtHON pRoGrAmMiNg"
print(txt.upper())
# 18. Current Temperature
temperature = 25
print(f"The current temperature is {temperature} degrees.")
# 19. Printing a Poem
poem = """If You Are Cold,\n\t❤ Tea Will Warm You;\nIf You Are Too Heated,\n\tIt Will Cool You;\nIf You Are Depressed,\n\tIt Will Cheer You;\nIf You Are Excited,\n\tIt Will Calm You;"""
print(poem)