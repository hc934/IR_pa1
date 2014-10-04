import string
import urllib
from stemming.porter import stem

news = urllib.urlopen('https://ceiba.ntu.edu.tw/course/35d27d/content/28.txt')
str = news.read()

# lowercase
str = str.lower()

# tokenization
str = str.translate(string.maketrans("",""),string.punctuation)
list = str.split()

# Porter's stemmer
stemlist = []
for x in list:
	stemlist.append(stem(x))

# stopword removal
page = urllib.urlopen('http://ir.dcs.gla.ac.uk/resources/linguistic_utils/stop_words')
stopwords_list = page.read().split()
result = [x for x in stemlist if x not in stopwords_list]

# write to file
outstring = " ".join(result)
output = open("output1.txt", "wb+")
output.write(outstring)
output.close()
