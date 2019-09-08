yearStr = input("Years: ")
yearInt = int(yearStr)

startPopulation = int(307357870)                                    #fólksfjöldi í byrjun
birthsPerYear = float((3600*24*365)/7)                              #útreiknaður fæðingarfjöldi á einu ári
deathsPerYear = float((3600*24*365)/13)                             #útreiknuð dauðsföll á einu ári
immigrantsPerYear = float((3600*24*365)/35)                         #útreiknaður fjöldi innflytjenda yfir eitt ár

curPopulationFloat = startPopulation + (birthsPerYear + immigrantsPerYear - deathsPerYear) * yearInt

curPopulation = int(startPopulation + (birthsPerYear + immigrantsPerYear - deathsPerYear) * yearInt)       #núverandi

if yearInt < 0:                                                     #ef að sett er inn tölu minni en 1 þá leyfir forritið ekki að halda áfram
    print("Invalid input!")
else:                                                               #ef sett er inn viðeigandi tölu þá reiknar forritið út tiltekin fólksfjölda
    print ("New population after " + yearStr + " years is: " + str(curPopulation) + " float: " + str(curPopulationFloat))






#Gerum ráð fyrir því að núverandi fólksfjöldi í USA sé 307.357.870 og upplýsingar um fjölgun/fækkun séu eftirfarandi:

#fæðing á 7 sekúnda fresti
#dauðsfall á 13 sekúnda fresti
#nýr innflytjandi á 35 sekúnda fresti
#Skrifið forrit sem tekur árafjölda sem inntak (sem heiltölu) og skrifar út áætlaðan fólksfjölda (sem heiltölu) 
# eftir gefinn árafjölda.  Ef árafjöldinn er negatíf tala þá skal forritið skrifa út "Invalid input!"  
# Gerið ráð fyrir því að það séu nákvæmlega 365 dagar í ári.  

#Við útreikning á áætluðum fólksfjölda skal nota rauntölur (float).

#Dæmi: Ef inntakið er "2" þá skrifar forritið út áætlaðan fjólksfjölda eftir 2 ár á þennan máta:

#New population after 2 years is X
#(þar sem X heiltöluhlutinn af hinum útreiknaða fólksfjölda)
 
#Textinn í input setningunni skal vera svona:
#input("Years: ")