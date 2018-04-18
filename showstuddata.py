from flask import Flask, render_template, request

app=Flask(__name__)


"""To save the information into the file"""


def save_val(n1,c1,n2,c2):
    todos=open('studentInfo.log','a')
    print(n1,' ',c1,' ',n2,' ',c2,' ',file=todos)
    todos.close()

@app.route('/')
def enterdetail() -> 'html' :
    return render_template('entry.html',the_title="Welcome to entering data")


"""App route method for taking the values from the user"""


@app.route('/enterval',methods=['Post'])                
def enterval() -> 'html' :
    name1=request.form['name1']
    con1=request.form['con1']
    name2=request.form['name2']
    con2=request.form['con2']
    save_val(name1,con1,name2,con2)
    return render_template('end.html')

app.run(debug=True)
