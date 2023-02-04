from flask import Flask, render_template
import test
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('UI.html')


# app.route('/', methods=['POST'])
# def test():
#     print('hi')


if __name__ == '__UITEST__':
    # test.testing()
    app.run()
