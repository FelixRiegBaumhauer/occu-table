from flask import Flask, render_template

app=Flask(__name__)

import random


@app.route("/") #recyclyed, 
def helloworld():
    return "To access, type occupations in the top thing"

#breka things up and open things, we break along /n

def builder(inFile):
    #file=open("occupations.csv", "r")
    file=open(inFile, "r")
    inputString = file.read()
    brokenInput = str.split(inputString, "\r\n")


    #dict made, VITAL
    dict = {}
    
    
    #Got rid of non needed info
    refinedInput = brokenInput[1:-2]
    
    
    #To put every thing in a dict, with the following order
    #keys = job
    #values = percentage of labor market
    
    #This blurb of code puts out read in values in a dict
    for line in refinedInput:
        job = ""
        num = ""
        if(line[0] == '"'):
            line = line[1:]
            run = len(line)-1
            while (run>=0):
                if(line[run] == '"'):
                    job = line[:run]
                    num = line[run+2:]
                    run = 0
                    dict[job]=num
                    #dict[num] = job
                    #print job+"----"+num
                run-=1
        else:
            pos = line.index(",")
            job = line[:pos]
            num = line[pos+1:]
            dict[job]=num
            #dict[num] = job
            #print(job+"---"+num)
    return dict
            
#print dict

dict = builder("occupations.csv")

#Gets a random job, by means of generating a random int, then using the values stored in the
#dict to find an appropriate value
def getRandomOccupation(dict):
    randInt = random.randint(0, 997)
    posHold = 0
    for key in dict:
        posHold += (10 * float(dict[key]))
        if(randInt < posHold):
            return key
    #If all goes wrong
    return "No job, Error"+(str(posHold))+":"+(str(randInt))


#quick Test, tests quicklly
def quickTest():
	results = {}
	#lengthHold = len(dict)
	#while (lengthHold > 0):
	for key in dict:
		results[key]=0
	counter=0
	while (counter < 10000):
		counter+=1
		rand = getRandomOccupation()
		results[rand] = results[rand]+1
	output = ""
	for key in results:
            val = (str)(results[key] / 100.00)
	    #output+=(key+" happend "+(str)(results[key])+"/10000 times\n")#key in results is the name of proffesion
            output+=key+" had a "+val+"% rating\n"
        return output

#Use this to run
#print "\nRandomlly chosen job: "+getRandomOccupation(dict)+"\n"

#Use this to validate the correctness of the code
#print quickTest()
    


#--------------------------------------#


@app.route("/occupations")
def occupater():
    return render_template("occu-temp.html", title="A Collection of Occupations", dict = dict, ans = getRandomOccupation(dict))
#should return a render template

    
if __name__=="__main__":
    app.run()
    app.debug = True #this is comment
    

