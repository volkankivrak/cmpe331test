# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.




# See PyCharm help at https://www.jetbrains.com/help/pycharm/

"""
Stage : Development -01
@author : Volkan Kıvrak , 120202101
@author : Amin Habiballah , 119202002

Stage : Development -02
@author : Kurt Godel , 3333333
@author : Alan Turing , 4444444

Stage : Code Review
@author : Donald Knuth , 5555555
@author : Grace Hopper , 6666666
"""

html_doc = """<html><head><title>IMDb Top 250 Movies</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="https://www.imdb.com/chart/top/" class="movie" id="link1">Elsie</a>,
<a href="https://www.imdb.com/chart/top/" class="movie" id="link2">Lacie</a> and
<a href="https://www.imdb.com/chart/top/" class="movie" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser')

print(soup.prettify())
# <html>
#  <head>
#   <title>
#    The Dormouse's story
#   </title>
#  </head>
#  <body>
#   <p class="title">
#    <b>
#     The Dormouse's story
#    </b>
#   </p>
#   <p class="story">
#    Once upon a time there were three little sisters; and their names were
#    <a class="sister" href="https://www.imdb.com/chart/top/" id="link1">
#     Elsie
#    </a>
#    ,
#    <a class="sister" href="https://www.imdb.com/chart/top/" id="link2">
#     Lacie
#    </a>
#    and
#    <a class="sister" href="https://www.imdb.com/chart/top/" id="link3">
#     Tillie
#    </a>
#    ; and they lived at the bottom of a well.
#   </p>
#   <p class="story">
#    ...
#   </p>
#  </body>
# </html>

soup.title
# <title>The Dormouse's story</title>

soup.title.name
# u'title'

soup.title.string
# u'The Dormouse's story'

soup.title.parent.name
# u'head'

soup.p
# <p class="title"><b>The Dormouse's story</b></p>

soup.p['class']
# u'title'

soup.a
# <a class="sister" href="https://www.imdb.com/chart/top/" id="link1">Elsie</a>

soup.find_all('a')
# [<a class="sister" href="https://www.imdb.com/chart/top/" id="link1">Elsie</a>,
#  <a class="sister" href="https://www.imdb.com/chart/top/" id="link2">Lacie</a>,
#  <a class="sister" href="https://www.imdb.com/chart/top/" id="link3">Tillie</a>]

soup.find(id="link3")
# <a class="sister" href="https://www.imdb.com/chart/top/" id="link3">Tillie</a>

