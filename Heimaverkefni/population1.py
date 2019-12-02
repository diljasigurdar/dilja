yearStr = input("Years: ")
yearInt = int(yearStr)

if yearInt < 0:                                             #ef að sett er inn neikvæða tölu þá leyfir forritið ekki að halda áfram
    print("Invalid input!")
else:                                                       #ef sett er inn viðeigandi tölu þá reiknar forritið út tiltekin fólksfjölda
    startPopulation = int(307357870)                        #fólksfjöldi í byrjun
    birthsPerYear = float((3600*24*365)/7)                  #útreiknaður fæðingarfjöldi á einu ári
    deathsPerYear = float((3600*24*365)/13)                 #útreiknuð dauðsföll á einu ári
    immigrantsPerYear = float((3600*24*365)/35)             #útreiknaður fjöldi innflytjenda yfir eitt ár

    curPopulation = int(startPopulation + (birthsPerYear + immigrantsPerYear - deathsPerYear) * yearInt)      

    print ("New population after " + yearStr + " years is " + str(curPopulation))
    
