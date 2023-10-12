import re

def check(m):
    pattern=re.compile("(#\w+)")
    x=pattern.findall(m)
    if x:
        print("Hashtags: ",x)
        
def main():
    caption=input("Enter caption:")
    check(caption)

main()