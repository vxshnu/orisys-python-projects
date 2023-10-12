#Vowel and Consonants
vowel=0
cons=0
def check(a):
    n=len(a)
    global vowel
    global cons
    for char in a:
        char=char.lower()
        if char in 'aeiou':
            vowel+=1
            print(f"Letter {char} is vowel")
        elif char >= 'a' and char<= 'z'  :
            cons+=1
            print(f"Letter {char} is consonant")

def main():
    s=input("Enter the string:")
    s.lower()
    check(s)
    print(f"Vowels:{vowel}  \nConsonants{cons}")
main()