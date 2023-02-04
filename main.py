from flask import Flask, render_template, request
import test
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        if request.form.get('action1') == 'VALUE1':
           print("hi")
    return render_template('index.html')


if __name__ == '__main__':
    # test.testing()
    app.run()
