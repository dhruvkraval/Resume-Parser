from flask import Flask, render_template, request
import test
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        print("hi")
    return render_template('UI.html')


if __name__ == '__main__':
    # test.testing()
    app.run()
