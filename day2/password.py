import re

def check(m):
    pattern=re.compile("(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$")
    x=pattern.findall(m)
    if x:
        print("Valid password : ",m)
    else:
        print("Invalid password : ",m)
        
def main():
    password=input("Enter the password:")
    check(password)

main()