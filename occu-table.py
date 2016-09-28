import utils.occuTabler
from flask import Flask, render_template
app=Flask(__name__)#crts a flask obj


@app.route("/") #recyclyed, 
def helloworld():
    return 'Welcome to the landing platform <br>Here is a <a href="/occupations">link</a> to the occupations page'


#----------------------------------------------------#

dict = utils.occuTabler.builder("data/occupations.csv")

@app.route("/occupations")
def occupater():
    return render_template("occu-temp.html", title="A Collection of Occupations", dict = dict, ans = utils.occuTabler.getRandomOccupation(dict))
#should return a render template

#--------------------------------------------------#
#Past Experiment
#return render_template("occu-temp.html", title="A Collection of Occupations", dict = builder("data/occupations.csv"), ans = getRandomOccupation(builder("data/occupations.csv")))
#--------------------------------------------------#


    
if __name__=="__main__":
    app.run()
    app.debug = True #auto restarts server when u save
    

