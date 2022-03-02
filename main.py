from flask import Flask, render_template
# from text import BlogPost
import requests

app = Flask(__name__)
data = requests.get(url="https://api.npoint.io/ef7d3aa7f50c686498ba")
blog_data = data.json()
# all_posts = [BlogPost(data["id"], data["title"], data["subtitle"], data["body"], data["author"], data["date"]) for data
#              in blog_data]


@app.route("/")
def home_page():
    return render_template("index.html", posts=blog_data)

@app.route("/contact.html")
def contact_page():
    return render_template('contact.html')

@app.route("/about.html")
def about_page():
    return render_template('about.html')


@app.route("/post/<int:num>")
def get_post(num):
    requested_post = None
    for post in blog_data:
        if post["id"] == num:
            requested_post = post

    return render_template(f"post.html", post=requested_post, image=f"image{num}.jpg")


if __name__ == "__main__":
    app.run(debug=True, host='localhost', port='5000')
