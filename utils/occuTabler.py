import random

#Builder takes the route to teh wanted file, and processes input
#The input has to be broken into lines, then we make a dict
#The dict is then filled with occupations as the keys,
#and a list of nums and urls as the values

def builder(inFile):
    #file=open("occupations.csv", "r")
    file=open(inFile, "r")
    inputString = file.read()
    brokenInput = str.split(inputString, "\r\n")

    #break things up and open things, we break along /n

    #dict made, VITAL
    dict = {}
    
    #Got rid of non needed info, ie the first and last lines
    refinedInput = brokenInput[1:-2]
    
    #To put every thing in a dict, with the following order
    #keys = job
    #values = in a list (percentage of labor market + urls)
    
    #This blurb of code puts out read in values in a dict
    for line in refinedInput:
        job = ""
        num = ""
        url = ""
        blurb = ""#where the num and url are found in the line, a holder of srts
        info = [] #holds the num and the url
        if(line[0] == '"'):
            line = line[1:]
            run = len(line)-1
            while (run>=0):
                if(line[run] == '"'):
                    job = line[:run]
                    
                    blurb = line[run+2:]
                    loc = blurb.index(",")#the loc of the  1st comma
                    num = blurb[:loc]
                    url = blurb[loc+1:]
                    info.append(num)
                    info.append(url)
                    
                    #num = line[run+2:]
                    run = 0
                    dict[job] = info
                    #dict[job]=num
                    #dict[num] = job
                run-=1
        else:
            pos = line.index(",")
            job = line[:pos]

            blurb = line[pos+1:]
            loc = blurb.index(",")
            num = blurb[:loc]
            url = blurb[loc+1:]
            info.append(num)
            info.append(url)
            
            #num = line[pos+1:]
            dict[job] = info
            #dict[job]=num
            #dict[num] = job
    return dict

#dict = builder("data/occupations.csv")


#Gets a random job, by means of generating a random int, then using the values stored in the
#dict to find an appropriate value
#The upper bound is 997, as 10*99.8 is 998, but we use 0 as a value
#then we set a counter to 0, and increment it by the probabillity of said job,
#times 10, if the randInt is less than our updated couner, we give ans
#otherwise thinking was flawed

def getRandomOccupation(dict):
    randInt = random.randint(0, 997)
    posHold = 0
    for key in dict:
        posHold += (10 * float((dict[key])[0]))
        if(randInt < posHold):
            return key
    #If all goes wrong
    return "No job, Error"+(str(posHold))+":"+(str(randInt))

#for the future
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
    

