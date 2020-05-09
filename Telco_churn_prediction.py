from flask import Flask, request, render_template, redirect
import pickle

app = Flask("__name__")


# load the model from disk
loaded_model = pickle.load(open('logistic_churn_model.sav', 'rb'))

@app.route('/')
def hello():
    return render_template("churn.html")



@app.route("/home")
def home():
    return redirect('/')

@app.route('/',methods=['POST'])
def submit_data():
    
    inputQuery1 = float(request.form['query1'])
    inputQuery2 = float(request.form['query2'])
    inputQuery3 = float(request.form['query3'])
    inputQuery4 = float(request.form['query4'])
    inputQuery5 = float(request.form['query5']) 
    inputQuery6 = float(request.form['query6'])
    inputQuery7 = float(request.form['query7'])
    inputQuery8 = float(request.form['query8'])
    inputQuery9 = float(request.form['query9'])
    inputQuery10 = float(request.form['query10'])
    inputQuery11 = float(request.form['query11'])
    inputQuery12 = float(request.form['query12'])
    inputQuery13 = float(request.form['query13'])
    inputQuery14 = float(request.form['query14'])
    inputQuery15 = float(request.form['query15'])
    inputQuery16 = float(request.form['query16'])
    inputQuery17 = float(request.form['query17'])
    inputQuery18 = float(request.form['query18'])
    inputQuery19 = float(request.form['query19'])
    inputQuery20 = float(request.form['query20'])
    inputQuery21 = float(request.form['query21'])
    inputQuery22 = float(request.form['query22'])
    inputQuery23 = float(request.form['query23'])
    inputQuery24 = float(request.form['query24'])
    inputQuery25 = float(request.form['query25'])
    inputQuery26 = float(request.form['query26'])
    inputQuery27 = float(request.form['query27'])
    inputQuery28 = float(request.form['query28'])

    data = [[inputQuery1, inputQuery2, inputQuery3, inputQuery4, inputQuery5, inputQuery6, inputQuery7, inputQuery8, inputQuery9, inputQuery10, inputQuery11, inputQuery12, inputQuery13, inputQuery14, inputQuery15, inputQuery16, inputQuery17, inputQuery18, inputQuery19, inputQuery20, inputQuery21, inputQuery22, inputQuery23, inputQuery24, inputQuery25, inputQuery26, inputQuery27, inputQuery28]]
    
    prediction=loaded_model.predict(data)
    if prediction==1:
        output="Churned !"
    else:
        output="Not Churned"
        
    
    
    return render_template("churn.html",output1=output, query1 = request.form['query1'], query2 = request.form['query2'],query3 = request.form['query3'],query4 = request.form['query4'],query5 = request.form['query5'], query6 = request.form['query6'], query7 = request.form['query7'],query8 = request.form['query8'],query9 = request.form['query9'],query10 = request.form['query10'], query11 = request.form['query11'], query12 = request.form['query12'],query13 = request.form['query13'],query14 = request.form['query14'],query15 = request.form['query15'], query16 = request.form['query16'], query17 = request.form['query17'],query18 = request.form['query18'],query19 = request.form['query19'],query20 = request.form['query20'],query21 = request.form['query21'],query22 = request.form['query22'],query23 = request.form['query23'],query24 = request.form['query24'],query25 = request.form['query25'],query26 = request.form['query26'],query27 = request.form['query27'],query28 = request.form['query28'])
    
    
    
    
    
if __name__ =="__main__":
    
    
    app.run()