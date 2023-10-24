#Write an if-elif-else chain that determines a person’s stage of life. Set a value for the variable age, and then:
age=2
if age< 2:
    print(" you  are a baby")
elif age >=2 and age <4:
    print( " you are a toddler")
elif age >=4 and age <13:
    print(" you are a kid")
elif age >=13 and age<20:
    print(" you are still a teenager")
elif age >=20 and age<65:
    print(" you are a adult person")
elif age>=65:
    print(" you are a elder")
else:
    print("age is invalid")