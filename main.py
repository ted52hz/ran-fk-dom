import feedparser
from wordcloud import WordCloud
import re

# RSS feed URL
edu_rss_url = 'https://tuoitre.vn/rss/giao-duc.rss'
news_rss_url = 'https://tuoitre.vn/rss/thoi-su.rss'
life_rss_url = 'https://tuoitre.vn/rss/nhip-song-so.rss'


def wordcloud_generator(url, title):
    feed = feedparser.parse(url)
    write = ""
    for entry in feed.entries:
        match = re.search(r'</a>([^<]*)$', entry.summary, re.DOTALL)
        text_between_a_and_brackets = match.group(1).strip()
        write += text_between_a_and_brackets + "\n"
    wordcloud = WordCloud(width=800, height=400,
                          background_color='white').generate(write)
    wordcloud.to_file(title + '.png')


def read_rss(url):
    feed = feedparser.parse(url)
    write = ""
    for entry in feed.entries:
        match = re.search(r'</a>([^<]*)$', entry.summary, re.DOTALL)
        text_between_a_and_brackets = match.group(1).strip()
        write += "- ." + text_between_a_and_brackets + "\n"
    return write


read_rss(edu_rss_url)
edu_image = wordcloud_generator(edu_rss_url, 'Edu')
news_image = wordcloud_generator(news_rss_url, 'News')
lifes_image = wordcloud_generator(life_rss_url, 'Life')

edu_writer = read_rss(edu_rss_url)
news_writer = read_rss(news_rss_url)
life_writer = read_rss(life_rss_url)

md = open("./README.md", 'w')
md.write("# Tuoi Tre RSS \n")
md.write("\n")
md.write('## Giáo dục \n')
md.write(edu_writer)
md.write("![Edu](Edu.png)")
md.write("\n")
md.write('## Thời Sự \n')
md.write(news_writer)
md.write("![New](News.png)")
md.write("\n")
md.write('## Nhịp sống số \n')
md.write(life_writer)
md.write("![life](Life.png)")
md.write("\n")
