# Enter your code here. Read input from STDIN. Print output to STDOUT
from html.parser import HTMLParser
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        for name, value in attrs:
            print("-> {} > {}".format(name, value))
    def handle_endtag(self, tag):
        print("End   :", tag)
    def handle_startendtag(self, tag, attrs):
        print("Empty :", tag)
        for name, value in attrs:
            print("-> {} > {}".format(name, value))
n = int(input())
html = ""
for _ in range(n):
    html += input()
parser = MyHTMLParser()
parser.feed(html)