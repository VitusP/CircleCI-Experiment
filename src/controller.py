from flask import Flask, render_template
import markdown
import os


app = Flask(__name__) # template_folder=os.path.join(os.getcwd(), 'src/templates/'

@app.route('/')
def index():
    with open(os.path.join(os.getcwd(), 'src', 'templates', 'Home.md'), 'r') as f:
        content = f.read()
        md = markdown.markdown(content)
    return render_template('index.html', content=md)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8080)
