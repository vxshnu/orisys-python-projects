import re

def check(m):
    pattern=re.compile("(?:<[a-z 0-9]+>)+([a-z 0-9 A-Z .]*)")
    x=pattern.findall(m)
    if x:
        print("TAG :",x[0])

def main():
    tag=input("Enter the string with HTML tag:")
    check(tag)
    
main()