from flask import Flask,request,render_template
from Model import SpellCheckerModule

app = Flask(__name__)

spell_checker_module = SpellCheckerModule()

#routes

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/spell', methods=['POST', 'GET'])
def spell():
    if request.method=='POST':
        text = request.form['text']
        corrected_text = spell_checker_module.correct_spell(text)
        corrected_grammar = spell_checker_module.correct_grammar(text)
        return render_template('index.html', corrected_text = corrected_text,corrected_grammar = corrected_grammar)
@app.route('/grammar', methods=['POST', 'GET'])
def grammar():
     pass


#python main

if __name__ == "__main__":
    app.run(debug=True) 