from flask import Flask, render_template, url_for
app = Flask(__name__,template_folder='templates', static_folder='static')

posts = [
    {
        'author': 'KRS',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'June 16, 2024'
    },
    {
        'author': 'Maya',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'June 17, 2024'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run(debug=True)