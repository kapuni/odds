import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import  os
import  re

from wordcloud import WordCloud
import jieba

app_path = os.path.dirname(os.path.dirname(__file__))

stop_words_txt = os.path.join(app_path, 'stopwords.txt')

with  open (stop_words_txt) as f:
    for line in f:
        STOP_WORDS.add(line[:-1])

file = './weibo_data.csv'
weibo_datas = pd.read_csv(file)

contend_weibo = weibo_datas('weibo_cont')
contend_weibo_cut = contend_weibo.apply(jieba.cut)

def filter_words(words, stop_words):
    result = [w for w in words if w not in stop_words and len(w)>1 / and re.match("^[\u4e00-\u9fa5]{0,}$", w)]
    return result

word_freq = dict()

for one in contend_weibo_cut:
    row = filter_words(list(one), STOP_WORDS)
    if row:
        for word in row:
            word_freq[word] = word_freq.get(word, 0) + 1

font_path = os.path.join(app_path, 'simkai.ttf')

word_cloud = WordCloud(font_path=font_path,
                       background_color='white',
                       max_words=200,
                       max_font_size=100,
                       random_state=42,
                       width=600, height=400, margin=2,
                       )

word_cloud.generate_from_frequencies(word_freq)

plt.figure()
plt.imshow(word_cloud)
plt.axis("off")

plt.show()