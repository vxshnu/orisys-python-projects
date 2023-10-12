import re
def check(m):
    pattern=re.compile("(?:www.)?([a-z . 0-9]*[a-z . 0-9]+.(?:com|in|org))")
    x=pattern.findall(m)
    print("URL :",x[0])
        
def main():
    urls=input("Enter the URL:")
    check(urls)
main()