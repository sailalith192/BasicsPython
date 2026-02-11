user_name = input("What's your name?")
user_age = int(input("What's your age?"))
Account_balance = int(input("How much do you have in your wallet? "))
print(user_name)
print(user_age)
print(Account_balance)
if user_age < 18:
    print(f"sorry{user_name},you must be 18 to use System")
elif user_age >=18  and Account_balance < 100:
    print("Access Denied: Minimum deposit of 100 required.")
else:
    print(f"Welcome to the System!!! {user_name}!")