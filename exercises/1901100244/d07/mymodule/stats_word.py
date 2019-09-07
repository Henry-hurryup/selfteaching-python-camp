# -*- coding: UTF-8 -*-

# Filename : stats_word.py
# author by : @shen-huang

# 模块的用法

text = '''
愚公移山

太行，王屋二山的北面，住了一個九十歲的老翁，名叫愚公。二山佔地廣闊，擋住去路，使他和家人往來極為不便。

一天，愚公召集家人說：「讓我們各盡其力，剷平二山，開條道路，直通豫州，你們認為怎樣？」
大家都異口同聲贊成，只有他的妻子表示懷疑，並說：「你連開鑿一個小丘的力量都沒有，怎可能剷平太行、王屋二山呢？況且，鑿出的土石又丟到哪裏去呢？」

大家都熱烈地說：「把土石丟進渤海裏。」
於是愚公就和兒孫，一起開挖土，把土石搬運到渤海去。
愚公的鄰居是個寡婦，有個兒子八歲也興致勃勃地走來幫忙。
寒來暑往，他們要一年才能往返渤海一次。

住在黃河河畔的智叟，看見他們這樣辛苦，取笑愚公說：「你不是很愚蠢嗎？你已一把年紀了，就是用盡你的氣力，也不能挖去山的一角呢？」

愚公歎息道：「你有這樣的成見，是不會明白的。你比那寡婦的小兒子還不如呢！就算我死了，還有我的兒子，我的孫子，我的曾孫子，他們一直傳下去。而這二山是不會加大的，總有一天，我們會把它們剷平。」

智叟聽了，無話可說。

二山的守護神被愚公的堅毅精神嚇倒，便把此事奏知天帝。天帝佩服愚公的精神，就命兩位大力神揹走二山。

How The Foolish Old Man Moved Mountains
Yugong was a ninety-year-old man who lived at the north of two high
mountains, Mount Taixing and Mount Wangwu.
Stretching over a wide expanse of land, the mountains blocked
yugong’s way making it inconvenient for him and his family to get
around.
One day yugong gathered his family together and said,”Let’s do our
best to level these two mountains. We shall open a road that leads
to Yuzhou. What do you think?”
All but his wife agreed with him.
“You don’t have the strength to cut even a small mound,” muttered
his wife. “How on earth do you suppose you can level Mount Taixin
and Mount Wanwu? Moreover, where will all the earth and rubble go?”
“Dump them into the Sea of Bohai!” said everyone.
So Yugong, his sons, and his grandsons started to break up rocks and
remove the earth. They transported the earth and rubble to the Sea
of Bohai.
Now Yugong’s neighbour was a widow who had an only child eight years
old. Evening the young boy offered his help eagerly.
Summer went by and winter came. It took Yugong and his crew a full
year to travel back and forth once.
On the bank of the Yellow River dwelled an old man much respected
for his wisdom. When he saw their back-breaking labour, he ridiculed
Yugong saying,”Aren’t you foolish, my friend? You are very old now,
and with whatever remains of your waning strength, you won’t be able
to remove even a corner of the mountain.”
Yugong uttered a sigh and said,”A biased person like you will never
understand. You can’t even compare with the widow’s little boy!”
“Even if I were dead, there will still be my children, my
grandchildren, my great grandchildren, my great great grandchildren.
They descendants will go on forever. But these mountains will not
grow any taler. We shall level them one day!” he declared with
confidence.
The wise old man was totally silenced.
When the guardian gods of the mountains saw how determined Yugong
and his crew were, they were struck with fear and reported the
incident to the Emperor of Heavens.
Filled with admiration for Yugong, the Emperor of Heavens ordered
two mighty gods to carry the mountains away.
'''

def stats_text_en(text: str) -> str:
    import re  # 加载正则表达式模块
    from nltk.tokenize import regexp_tokenize  # 加载正则表达式分词函数

    pattern = r"""             # 设置以编写较长的正则条件
        (?x)(?:[A-Z]\.)+       # 缩略词
        |\$?\d+(?:\.\d+)?%?    # 货币、百分数
        |\w+(?:[-']\w+)*       # 用连字符链接的词汇
        |\.\.\.                # 省略符号
        |(?:[.,;"'?():-_`])    # 特殊含义字符
        """

    # 去掉 text 里的多余符号、双字节字符和空格，
    # 修改常见缩略词写法，添加分词用空格，全文转为小写
    text2 = re.sub(r",|\*|!", " ", text)
    text2 = re.sub("—", " ", text2)
    text2 = re.sub("(?i)let['’]s", "letus", text2)
    text2 = re.sub("(?i)don['’]t", "donot", text2)
    text2 = re.sub("(?i)can['’]t", "cannot", text2)
    text2 = re.sub("(?i)isn['’]t", "isnot", text2)
    text2 = re.sub("(?i)aren['’]t", "arenot", text2)
    text2 = re.sub("(?i)won['’]t", "willnot", text2)
    text2 = re.sub("([0-9A-Za-z]*)['’]([0-9A-Za-z]*)", "\\1 ’\\2", text2)
    text2 = re.sub("\n", " ", text2)
    text2 = re.sub(" +", " ", text2)
    text2 = re.sub(r"[\u0391-\uFFE5]", "", text)
    text2 = str.lower(text2)

    # 分词，去掉空元素，排序
    text3 = regexp_tokenize(text2, pattern)
    text3 = [i for i in text3 if i != '' and i != '.']
    text3 = sorted(text3)

    # 生成非重复单词列表
    text4 = []
    [text4.append(w) for w in text3 if w not in text4]

    # 生成词频统计字典
    text_freq = {w: text3.count(w) for w in text4}

    # 调整缩略词写法
    text_freq["let’s"] = text_freq.pop["letus"]
    text_freq["don’t"] = text_freq.pop["donot"]
    text_freq["can’t"] = text_freq.pop["cannot"]
    text_freq["isn’t"] = text_freq.pop["isnot"]
    text_freq["aren’t"] = text_freq.pop["arenot"]
    text_freq["won’t"] = text_freq.pop["willnot"]

    # 按词频排序
    text_freq = sorted(text_freq.items(), key=lambda x: x[1], reverse=True)
    text_freq = dict(text_freq)

    # 返回数组
    return text_freq


def stats_text_cn(text: str) -> str:
    import re  # 加载正则表达式模块

    # 去掉 text 里除汉字外的符号
    text2 = re.sub(r"[^\u4E00-\u9FA5]", "", text)

    # 分词，排序
    text3 = re.split("", text2)
    text3 = sorted(text3)

    # 生成非重复汉字列表
    text4 = []
    [text4.append(w) for w in text3 if w not in text4]

    # 生成字频统计字典
    text_freq = {w: text3.count(w) for w in text4}

    # 按字频排序
    text_freq = sorted(text_freq.items(), key=lambda x: x[1], reverse=True)
    text_freq = dict(text_freq)

    # 返回数组
    return text_freq


def stats_text(text: str) -> str:
    text_freq_en = stats_text_en(text)
    text_freq_cn = stats_text_cn(text)
    print("1. 字符串样本中英文单词词频统计")
    print("单词\t词频")
    for key, value in text_freq_en.items():
        print('{key}\t{value}'.format(key=key, value=value))
    
