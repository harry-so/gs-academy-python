import json
from urllib.request import urlopen
from random import shuffle
from flask import Flask, render_template
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route("/")
def index():
    """初期画面を表示します."""
    return render_template("index.html")

@app.route("/api/recommend_article")
def api_recommend_article():
    """はてブのホットエントリーから記事を入手して、ランダムに1件返却します."""
    import ssl
    ssl._create_default_https_context = ssl._create_unverified_context

    url = "http://feeds.feedburner.com/hatena/b/hotentry"
    response = urlopen(url)
    html = response.read().decode("utf-8")

    soup = BeautifulSoup(html, "html.parser")

    items = soup.select("item")
    shuffle(items)
    item = items[0]
    print(item)

    title = item.find("title").string
    link = item.get('rdf:about')

    return json.dumps({
        "content" : title,
        "link" : link
    })

@app.route("/api/show_time")
def api_showTime():
    """
        **** ここを実装します（発展課題） ****
        ・自分の好きなサイトをWebスクレイピングして情報をフロントに返却します
        ・お天気APIなども良いかも
        ・関数名は適宜変更してください
    """
    import datetime
    a = datetime.datetime.now()

    return json.dumps({
        "year" : a.year,
        "month" : a.month,
        "day" : a.day,
        "hour" : a.hour,
        "minute" : a.minute
    })

if __name__ == "__main__":
    app.run(debug=True, port=5004)
