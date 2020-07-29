# dependencies
from bs4 import BeautifulSoup
import sys

# read in the html file as a string
f = open(sys.argv[1], "r")
html_doc = f.read()

# soup object
soup = BeautifulSoup(html_doc, 'html.parser')

# output the html_doc
print(soup.prettify())
