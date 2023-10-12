import re
def check(m):
    pattern=re.compile(r"(?:\b[01][0-9]?[0-9]?\b|\b[2][0-5][0-5]\b).(?:\b[01][0-9]?[0-9]?\b|\b[2][0-5][0-5]\b).(?:\b[01][0-9]?[0-9]?\b|\b[2][0-5][0-5]\b).(?:\b[01][0-9]?[0-9]?\b|\b[2][0-5][0-5]\b)")
    x=pattern.findall(m)
    if x:
        print("Valid IPv4 address")
    else:
        print("Invalid IPv4 address")

def main():
    ipv4=input("Enter the IPv4 address:")
    check(ipv4)

main()