from flask import Flask, render_template, request
import DescriptionMatch
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('UI.html')

@app.route('/',methods =['POST'])
def getValue():
    #name, value
    if request.form.get('action1') == 'Submit':
        jobdescription = request.form.get('jobdescription')
        resumeText = request.form.get('resumepaste')
        DescriptionMatch.takeInput(resumeText, jobdescription)
    return render_template('ui.html')

if __name__ == '__main__':
    # test.testing()
    app.run()
