print("Hello, World!")
name = "Roy"
age = 18
print(name, "is", age, "years old.")

is_data_analyst = True
print(type(is_data_analyst))
minor = bool(age < 18)

if name:
    if age > 18:
        print(name, "Is an adult?", minor)
    else:
        print(name, "Is a minor?", minor)
        
retired = "51"
print(retired[0])
user_age = input("What is your age? ")
print("Can User stop working now?", age <= int(retired))

