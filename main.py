from flask import Flask, render_template, request
import DescriptionMatch
import suggestions
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
        rating = DescriptionMatch.resume_rating(resumeText, jobdescription)
        ret = suggestions.suggestions(jobdescription,resumeText)
    return render_template('pass.html', name=rating, suggestions = ret)

if __name__ == '__main__':
    # test.testing()
    app.run()
