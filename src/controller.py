from flask import Flask, render_template
import markdown
import os

isDebug = os.environ.get('DEBUG', False)
app = Flask(__name__)


@app.route('/')
def portfolio():
    return render_template('portfolio.html')

@app.route('/settings')
def settings():
    md_file = os.path.join(os.path.dirname(__file__), 'templates/homepage.md')
    with open(md_file, 'r') as f:
        content = f.read()
        md = markdown.markdown(content)
    return render_template('index.html', content=md)

if __name__ == '__main__':
    app.run(debug=isDebug, host="0.0.0.0", port=8080)
