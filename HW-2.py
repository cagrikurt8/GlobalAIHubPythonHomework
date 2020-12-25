name = input("Name=> ")
surname = input("Surname=> ")
age = int(input("Age=> "))
birth_year = int(input("Birth Year=> "))

data_list = [name, surname, age, birth_year]
print("\n")
for i in data_list:
    idx = data_list.index(i)
    if idx == 0:
        print(f"Name: {i}")
    elif idx == 1:
        print(f"Surname: {i}")
    elif idx == 2:
        print(f"Age: {i}")
    else:
        print(f"Birth Year: {i}")
print("\n")
print("You can't go out because it's too dangerous") if age < 18 else print("You can go out to the street")
