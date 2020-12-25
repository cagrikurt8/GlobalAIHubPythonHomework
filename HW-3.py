user_name = input("Your name=> ")
print(f"Welcome {user_name}")

word = "machine learning"
lst = list(word)
attempt = 0
lst1 = word.split()
print("\nPredict the words!(Do not enter the gaps and if you enter a wrong letter, start to predict from the beginning.)\n")

for i in range(len(lst1)):
    print(len(lst1[i]) * "-")

x = 0

while True:
    if lst[x] != " ":
        prediction = input("=>")
        if prediction != lst[x]:
            attempt += 1
            if 3 - attempt == 1:
                print(f"You have {3 - attempt} attempt left.")
            else:
                print(f"You have {3- attempt} attempts left.")
            x = 0
            if attempt == 3:
                break
        else:
            x += 1
    elif lst[x] == " ":
        x += 1
    if x == len(lst):
        break
if attempt == 3:
    print("You couldn't predict the word!")
else:
    print("Congratulations! These were the words.")
