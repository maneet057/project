from flask import Flask, render_template, request, render_template_string
import pandas as pd
import numpy as np
import qna as qna
import ques_and_ans as ques_and_ans
import text_ques as text_ques
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route("/generate_questions",methods=['POST'])
def function_questions():
    text=request.form.get("search")
    result=qna.generate(text)
    print(result)
    return render_template("text_questions.html", result=result)

@app.route("/generate_qna",methods=['POST'])
def function_ques_and_answer():
    text=request.form.get("search")
    result=ques_and_ans.generate(text)
    print(result)
    return render_template("text_questions.html", result=result)

@app.route("/generate_answer",methods=['POST'])
def function_answer():
    text=request.form.get("search")
    question=request.form.get("question")
    result=text_ques.generate(text,question)
    print(result)
    return render_template("text_answer.html", result=result)
if __name__=='__main__':
    app.run(debug=True)