import re
def check(m):
    pattern=re.compile("\d+")
    x=pattern.findall(m)
    if x:
        print("Numbers found:",x)
        
def main():
    text=input("Enter text:")
    check(text)

main()