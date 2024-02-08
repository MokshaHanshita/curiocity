from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, template_folder='templates')

# Placeholder for feedback data
feedback_data = []

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/feedback_form')
def feedback_form():
    return render_template('feedback_form.html')

@app.route('/submit_feedback', methods=['POST'])
def submit_feedback():
    feedback = request.form.get('feedback')
    if feedback:
        feedback_data.append(feedback)
    return redirect(url_for('feedback_wall'))

@app.route('/feedback_wall')
def feedback_wall():
    return render_template('feedback_wall.html', feedback_data=feedback_data)

if __name__ == '__main__':
    app.run(debug=True)