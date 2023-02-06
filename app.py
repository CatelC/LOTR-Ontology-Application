from flask import Flask,render_template,request,redirect
app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def home():
    if request.method== 'POST' :
        if request.form["button"]=="MoteurRecherche" :
            return redirect('/recherche')
        elif request.form["button"]=="SentimentAna":
            return redirect('/analyse')
    return render_template('home.html')

@app.route('/recherche', methods=['POST','GET'])
def predict():
    if request.method == 'POST':
        if request.form["img"]=="MoteurRecherche" :
            return redirect('/')
    return render_template('moteurRecherche.html')
    
    