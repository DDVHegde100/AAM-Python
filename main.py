user_input = str(input("Enter a Phrase: "))
text = user_input.split()
acro = " "
for i in text:
    acro = acro+str(i[0]).upper()
print(acro)
