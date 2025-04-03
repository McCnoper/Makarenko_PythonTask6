print("Task 1")
age = int(input("Enter your age "))
if age<18:
    print("Access denied")
    exit()
print("Access granted")
#----------------------
print("Task 2")
quan = int(input("Enter quantity of items "))
if quan>20:
    print("There are not enough items in stock.")
    exit()
print("Your order has been accepted")
#----------------------
print("Task 3")
pas = input("Enter your password ")
if len(pas)<8:
    print("Password is too short")
    exit()
elif pas=="password" or pas=="12345678":
    print("Password is too weak")
    exit()
print("Access granted")
#----------------------
print("Task 4")
temp = int(input("Enter temperature "))
if temp<16:
    print("Temperature is too low. Turn on the heater")
    exit()
elif temp>28:
    print("Temperature is too high. Turn on fan")
    exit()
else:
    print("Temperature is comfortable")
    #----------------------
print("Task 5")
money = int(input("Enter the amount of money "))
if money<10:
    print("Minimal amount of replenishment is 10 hryvnias")
    exit()
elif money>3000:
    print("Maximal amount of replenishment is 3000 hryvnias")
    exit()
print("Replenishment for the amount of", money ,"hryvnias completed successfully!")
