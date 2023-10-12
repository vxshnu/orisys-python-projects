import re
def check(m):
    pattern=re.compile(r"[+]\d{1,3}\s\b\d{10}\b|\b^\d{10}\b")
    x=pattern.findall(m)
    if x:
        print("Number is valid:",x)
        
def main():
    with open("content.py", "r") as file:
        for line in file:
            check(line)    
main()