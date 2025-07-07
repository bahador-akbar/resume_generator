from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    name = request.form['name']
    job_title = request.form['job_title']
    summary = request.form['summary']
    skills = request.form['skills']
    experience = request.form['experience']
    education = request.form['education']

    # ساخت رزومه و کاورلتر ساده
    resume = f"""
    Name: {name}
    Job Title: {job_title}

    Summary:
    {summary}

    Skills:
    {skills}

    Experience:
    {experience}

    Education:
    {education}
    """

    cover_letter = f"""
    Dear Hiring Manager,

    I am writing to express my interest in the {job_title} position. With a background in {summary}, and proven skills in {skills}, I believe I am an ideal candidate for this role.

    I look forward to the opportunity to contribute to your team.

    Sincerely,  
    {name}
    """

    return render_template('result.html', resume=resume, cover_letter=cover_letter)

if __name__ == '__main__':
    app.run(debug=True)

