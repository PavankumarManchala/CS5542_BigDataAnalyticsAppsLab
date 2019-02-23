import nltk
from nltk import word_tokenize
import linecache
nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer
wordnet_lemmatizer = WordNetLemmatizer()
from nltk.corpus import stopwords
nltk.download('stopwords')
import matplotlib.pyplot as plot
plot.rcdefaults()
import numpy as np



linecounter = 0
cupcakes_count = 0
icecream_count = 0
soup_count = 0

f = open('Extracted_tokens.txt','a')
f1 = open('Extracted_urls.txt','a')
punctuations = "?:!.,;"
stop_words = set(stopwords.words('english'))
with open('C:\BigDataAnalyticsAppns\Lab1\SBU_captioned_photo_dataset_captions.txt','r') as file:
    for line in file:
        linecounter = linecounter + 1
        tokens = word_tokenize(line)
        for word in tokens:
            if word in punctuations:
                tokens.remove(word)
            if word in stop_words:
                tokens.remove(word)
            #new_tokens = set(tokens)
        for word in tokens:
            lemmit_word = wordnet_lemmatizer.lemmatize(word, pos="v")
            if 'cupcakes' == lemmit_word:
                cupcakes_count = cupcakes_count + 1
                f.writelines(line)
                line1 = linecache.getline('C:\BigDataAnalyticsAppns\Lab1\SBU_captioned_photo_dataset_urls.txt', linecounter)
                f1.writelines(line1)
            if 'icecream' == lemmit_word:
                icecream_count = icecream_count + 1
                f.writelines(line)
                line1 = linecache.getline('C:\BigDataAnalyticsAppns\Lab1\SBU_captioned_photo_dataset_urls.txt', linecounter)
                f1.writelines(line1)
            if 'soup' == lemmit_word:
                soup_count = soup_count + 1
                f.writelines(line)
                line1 = linecache.getline('C:\BigDataAnalyticsAppns\Lab1\SBU_captioned_photo_dataset_urls.txt', linecounter)
                f1.writelines(line1)
objects = ('cupcakes', 'icecream', 'soup')
y_pos = np.arange(len(objects))
performance = [cupcakes_count,icecream_count,soup_count]
plot.bar(y_pos, performance, align='center', alpha=0.5)
plot.xticks(y_pos, objects)
plot.show()
