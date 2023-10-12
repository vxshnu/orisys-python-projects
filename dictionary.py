dict={}
suggest=[]
def find(s):
    if s in dict:
        return dict[s]
    else:
        print("Word not found \nSimilar words")
        c=s[0]
        i=0
        for word in dict:
            if c==word[0]:
                print(word)
                i=i+1
        if i==0:
            print("No Suggestions");
        return ""

def main():
    while(True):
        word=input("Enter word:")
        dict[word]=input("Enter the meaning:")
        choice=int(input("To continue enter 1 else 0:"))
        if choice == 0:
            break
    while(True):
        x=input("Enter the word to be searched:")
        y=find(x)
        print(y)
        choice=int(input("To search enter 1 else 0:"))
        if choice == 0:
            break
main()