#CSV file information used from https://oec.world/en
import csv
import random


listCountries= []
tradeinfo = []
tradedetails = []
continent = []
tradeValue = []


def loadData():
  with open ("Biggest-export-by-country-2020.csv", newline="") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ',')
    for row in csv_reader:
      if "Continent" in row: 
        continue
      listCountries.append(row[3])
      tradeinfo.append(row[6])
      tradedetails.append(row[8])
      continent.append(row[1])
  with open ("World-Exports-Value-2020--Click-to-Select-a-Country.csv", newline="") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ',')
    for row in csv_reader:
      if "Continent" in row: 
        continue
      tradeValue.append(row[6])
    return(len(listCountries))


def makeAnswers(name):
  answerKey = []
  x = random.randint(0, name)
  answerKey.append(listCountries[x])
  answerKey.append(tradeinfo[x])
  answerKey.append(tradedetails[x])
  answerKey.append(continent[x])
  answerKey.append(tradeValue[x])
  return(answerKey)


def main():
  n = loadData()
  keepPlaying = True
  while keepPlaying:
    answerKey = makeAnswers(n)
    print("Trade info:", answerKey[1], "specifically", answerKey[2])
    print("Trade Value: $" + format(float(answerKey[4]), ',.0f'))
    keepPlaying = play(answerKey)
     


def play(answer):
  attempts = 0
  while True:
    response = input("Guess what country it is: ")
    if answer[0] == response:
      print("Correct")
      attempts = attempts + 1
      print("It took", attempts, "attempts to get the right answer.")
      print("")
      yesorno = input("Play again?(yes or no): ")
      if yesorno.lower() == "yes":
        return(True)
      else:
        return(False)
    else:
      print("Incorrect")
      attempts = attempts + 1
      print("The number of attempts is:", attempts)
      if attempts == 10:
        print("Incorrect")
        print("You have run out of turns!")
        print("The answer was: ", answer[0])
        yesorno = input("Play again?(yes or no): ")
        if yesorno.lower() == "yes":
          return(True)
        else:
          return(False)
      if attempts == 3:
        print("HINT: The length of the name of the country is(including spaces):", len(answer[0]))
      if attempts == 6:
        print("HINT: The continent the mystery country is on is:", answer[3])
      if attempts == 8:
        print("HINT: The first letter is:", answer[0][0])
        

print("Welcome to Tradle: The ultimate Country Guessing Game!")
print("You will be given a country's main trade industry, a description about this industry and the country's total export values.")
print("")
print("Here we go!")
main()