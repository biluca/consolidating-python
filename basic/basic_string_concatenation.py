# "Uggly" Way #
name = "José Cuervo"
age = 53

# print(name + "is " + age + " year old.") # this script will fail (age is not a String)
print(name + " is " + str(age) + " years old.")

# "Elegant" Way #
name = "Jean Bean"
age = 68

print(f"{name}  is {age}  years old.")
