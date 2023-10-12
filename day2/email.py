import  re
pattern=re.compile("^[a-z][a-z 0-9]*@(?!hotmail|yahoo)[a-z]+.(?:com|in|org)")
x=pattern.findall(input("Enter the mail id:"))
if not x:
    print("Not a valid email-id")
else:
    print("Valid email-id")