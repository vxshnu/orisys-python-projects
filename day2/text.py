import re
def check(m):
    pattern=re.compile("https?:\/\/\S+")
    x=pattern.findall(m)
    if x:
        print("URLs found:",x)
        
def main():
    text=input("Enter text:")
    check(text)

main()