n = "hello world"
print(n)

# to get the text from input

# name = input("Your name : ")
# print(name)


# String Comparison

#To test if two strings are equal use the equality operator (==).

first_string = "Rabiul Hasan"
last_string = "Rabiul hasan"
if first_string == last_string:
    print("Both string are same")

# To test if two strings are not equal use the inequality operator (!=)
string_one = "Hasan"
string_two = "Rabiul"
if string_one != string_two :
    print("Both string are not same")

print('C:\some\name')
# C:\some
# ame

print(r'C:\some\name')  # note the r before the quote means raw string
# C:\some\name


#produces the following output (note that the initial newline is not included for \):
print("""\
    How is life 
    Rabiul Hasan
""")
# concatenate string
print("Rabiul" + " " + "Hasan")
print("Rabiul " "Hasan")

# character show using index
word = "python"
print(word[0])
print(word[2])

# character show using negetive index
print(word[-1]) # print last character

print(word[2:5])  # tho
print('J'+word[1:])

word = "hasan"
print('py' + word[:2])

print(len(word)) # 5 string length count function

