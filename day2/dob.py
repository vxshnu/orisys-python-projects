import re

def check(m):
    pattern=re.compile(r"\b(?:01|02|03|04|05|06|07|08|09|10|11|12)[\/][0-3][0-9][\/]\d{4}\b")
    x=pattern.findall(m)
    if x:
        print("MM/DD/YYYY :",x[0])
    else:
        print("Not in MM/DD/YYYY format")

def main():
    dob=input("Enter the dob:")
    check(dob)
    
main()