import random

chancedict = { 
  1 : 0.6, 
  2 : 0.596,
  3 : 0.592,
  4 : 0.591,
  5 : 0.586,
  6 : 0.582,
  7 : 0.579,
  8 : 0.575,
  9 : 0.571,
  10 : 0.568,
  11 : 0.565,
  12 : 0.561,
  13 : 0.558,
  14 : 0.554,
  15 : 0.552,
  16 : 0.549,
  17 : 0.545,
  18 : 0.541,
  19 : 0.539,
  20 : 0.536,
  21 : 0.531,
  22 : 0.528,
  23 : 0.525,
  24 : 0.523,
  25 : 0.519,
  26 : 0.517,
  27 : 0.513,
  28 : 0.511,
  29 : 0.507,
  30 : 0.503,
  31 : 0.501,
  32 : 0.498,
  33 : 0.495,
  34 : 0.491,
  35 : 0.489,
  36 : 0.486,
  37 : 0.483,
  38 : 0.480,
  39 : 0.477,
  40 : 0.475,
  41 : 0.471,
  42 : 0.469,
  43 : 0.467,
  44 : 0.464,
  45 : 0.461,
  46 : 0.457,
  47 : 0.456,
  48 : 0.453,
  49 : 0.448,
  50 : 0.447,
  51 : 0.445,
  52 : 0.442,
  53 : 0.439,
  54 : 0.437,
  55 : 0.434,
  56 : 0.430,
  57 : 0.428,
  58 : 0.426,
  59 : 0.423,
  60 : 0.420,
  61 : 0.418,
  62 : 0.416,
  63 : 0.413,
  64 : 0.410,
  65 : 0.408,
  66 : 0.406,
  67 : 0.404,
  68 : 0.401,
  69 : 0.399,
  70 : 0.396,
  71 : 0.393,
  72 : 0.392,
  73 : 0.388,
  74 : 0.387,
  75 : 0.384,
  76 : 20.627,
  77 : 13.946,
  78 : 9.429,
  79 : 6.375,
  80 : 4.306,
  81 : 2.914,
  82 : 1.970,
  83 : 1.332,
  84 : 0.901,
  85 : 0.608,
  86 : 0.411,
  87 : 0.278,
  88 : 0.187,
  89 : 0.126,
  90 : 100
  }

def fiftyfifty(haspulledstandard):
    if not haspulledstandard:
        if random.randrange(0, 100) <= 50:
            return "standard", True
        else:
            return "event", False
    else:
        return "event", False
    
def primoconverter(primos, fates):
    leftover = primos % 160
    primosspent = primos - leftover
    wishes = fates + (primosspent / 160)
    print("Your primogems got you " + str(wishes - fates) + " wishes for " + str(wishes) + " in total.")
    return wishes
    

def wishonce(pity):
    chance = chancedict.get(pity)
    diceroll = random.uniform(0,100)
    if diceroll < chance:
        return True
    else:
        return False
  

def makeawish(wishnumber):
    pityscore = 1
    wishcounter = 0
    pullscounter = {"event" : 0, "standard" : 0}
    haspulledstandard = False
    while wishcounter < wishnumber:
        if wishonce(pityscore):
            successtype, haspulledstandard = fiftyfifty(haspulledstandard)
            pullscounter[successtype] += 1
            pityscore = 1
            wishcounter += 1
        else:
            pityscore += 1
            wishcounter += 1
    return pullscounter
    
def wishrepeater(wishnumber, wishrepeat = 1):
    eventslist = []
    standardslist = []
    repeatcount = 0
    print("Thinking...")
    while repeatcount <= wishrepeat:
        getstdandevnt = makeawish(wishnumber)
        eventspulled = getstdandevnt["event"]
        standardspulled = getstdandevnt["standard"]
        eventslist.append(eventspulled)
        standardslist.append(standardspulled)
        repeatcount += 1
    eventmean = round(sum(eventslist) / len(eventslist), 2)
    standardmean = round(sum(standardslist) / len(standardslist), 2)
    overalllist = eventslist + standardslist
    overallaverage = round(sum(overalllist) / wishrepeat, 2)
    print("In " + str(wishrepeat) + " batches of " + str(wishnumber) + " you pulled an event five star an average of " + str(eventmean) + " times.")
    print("You pulled a standard five star an average of " + str(standardmean) + " times.")
    print("You pulled any five star an average of " + str(overallaverage) + " times.")

runprimos = input("Convert primos? (Y/N)")
if runprimos.upper() == "Y":
    primogems = int(input("How many primogems do you have?"))
    intertwined = int(input("How many intertwined fates do you have?"))
    wishrepeats = int(input("How many trials?"))
    wishrepeater(primoconverter(primogems, intertwined), wishrepeats)   
else:             
    wishnumbers = int(input("How many wishes?"))
    wishrepeats = int(input("How many times?"))
    wishrepeater(wishnumbers, wishrepeats)
                 