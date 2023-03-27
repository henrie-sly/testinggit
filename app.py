character_name = "John"
character_age = "35"
is_male = False
print("The name of the man is " + character_name + ", ")
print("he is " + character_age + " years old, ")

character_name = "Mike"
print("and he is not happy with the name " + character_name + " ")
phrase = "Giraffe Academy"
print(phrase +" is cool")
print(phrase.replace("Giraffe","Umbrella"))
name = input ("Enter your name:")
print("Hello"+ name +"!")
color = input("Enter the name of the color:")
plural_noun = input("Enter the plural noun:")
celebrity = input("Enter the name of the celebrity:")
print("Roses are " + color)
print(plural_noun + "are blue")
print("I love " + celebrity)

friends = ["Alexander", "David", "Henry", " Rachael"]
print(friends.index("David"))
coordinates = (4,6)
print(coordinates)

def sayhi(name, age):
    print("Hello "+ name + " you are " + str(age))

sayhi("Mike", 34)
sayhi("Gerald", 45)

"IF STATEMENTS"
is_male = False
is_tall = False
if is_male and is_tall:
    print("You are a tall male")

elif is_male and not (is_tall):
    print("You are a short male")

elif not (is_male) and is_tall:
    print("You are tall but not a male")
else:
    print("You are not a male or tall")

"IF STATEMENTS WITH COMPARISONS"
def max_num (num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print (max_num(300, 789, 60))

"A SIMPLE CALCULATOR"
num1 = float(input("Enter the first number: "))
opp = input("Enter the operator: ")
num2 = float(input("Enter the second number: "))

if opp == "+":
    print(num1+num2)
elif opp == "-":
    print(num1-num2)
elif opp == "/":
    print(num1/num2)
elif opp == "*":
    print(num1*num2)
else:
    print("Invalid operator")

"CREATING A DICTIONARY"
monthConversions = {
  0: "January",
  1: "February",
  2: "March",
  3: "April",
  4: "May",
  5: "June",
  6: "July",
  7: "August",
  8: "September",
  9: "October",
  10: "November",
  11: "December",
}
print(monthConversions[1])

"WHILE CONDITIONS"
i = 1
while i <= 10:
    print(i)
    i += 1
else:
    print("The loop comes to an end ")

"Creating a guessing game"
print("What's that thing no matter how you try to dry it off it always remain wet")
secret_word = "Tongue"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not (out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter the right word: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
        print("You've ran out of guesses, YOU LOSE")
else:
        print("You got the correct word, YOU WIN!!!")
