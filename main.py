from flask import Flask, render_template
from post import Post

app = Flask(__name__)
new_post = Post()

@app.route('/')
def home():
    return render_template("index.html", post=new_post)

@app.route('/post/<int:num>')
def get_post(num):
    post_data = new_post.getPost(num)
    return render_template("post.html", num=num, post_data = post_data)

if __name__ == "__main__":
    app.run(debug=True)
