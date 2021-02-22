
import csv
from selenium import webdriver

browser = webdriver.Chrome()

#url = 'https://www.esportsearnings.com/games/164-league-of-legends/top-players'
#browser.get(url)


def gatherData(baseUrl, filename):
	playerIDs = []
	realNames = []
	gameTotals = []
	overallTotals = []
	percentOfTotals = []
	bDays = []
	countries = []

	print("Collecting data into " + filename)

	x = 0
	url = baseUrl
	for i in range(1, 501):
		print("value of i: " + str(i))
		browser.get(url)
		x += 1

		playerID = browser.find_element_by_xpath("/html/body/div[3]/div/main/div[2]/div/table/tbody/tr[" + str(x) + "]/td[2]/a[2]").text
		#print(playerID)
		playerIDs.append(playerID)

		realName = browser.find_element_by_xpath("/html/body/div[3]/div/main/div[2]/div/table/tbody/tr[" + str(x) + "]/td[3]/a").text
		#print(realName)
		realNames.append(realName)

		gameTotal = browser.find_element_by_xpath("/html/body/div[3]/div/main/div[2]/div/table/tbody/tr[" + str(x) + "]/td[4]").text
		#print(gameTotal)
		gameTotals.append(gameTotal)

		overallTotal = browser.find_element_by_xpath("/html/body/div[3]/div/main/div[2]/div/table/tbody/tr[" + str(x) + "]/td[5]").text
		#print(overallTotal)
		overallTotals.append(overallTotal)

		percentOfTotal = browser.find_element_by_xpath("/html/body/div[3]/div/main/div[2]/div/table/tbody/tr[" + str(x) + "]/td[6]").text
		#print(percentOfTotal)
		percentOfTotals.append(percentOfTotal)

		#Entering the player profile

		#This does not work because Another element is covering the element you are trying to click.
		#browser.find_element_by_xpath('/html/body/div[3]/div/main/div[2]/div/table/tbody/tr[1]/td[2]/a[2]').click()

		element = browser.find_element_by_xpath("/html/body/div[3]/div/main/div[2]/div/table/tbody/tr[" + str(x) + "]/td[2]/a[2]")
		browser.execute_script("arguments[0].click();", element)

		bDay = browser.find_element_by_xpath("/html/body/div[2]/div/main/div[2]/div/div[1]/div[2]/div/div[1]/div/div[2]/div[2]").text
		#print(bDay)
		bDays.append(bDay)

		country = browser.find_element_by_xpath("/html/body/div[2]/div/main/div[2]/div/div[1]/div[2]/div/div[2]/div").text
		#print(country)
		#Fixing country names that are written incorrectly on the website
		if country == "Korea, Republic of":
			country = "Republic of Korea"
		
		if country.find("Viet") != -1:
			country = "Vietnam"

		countries.append(country)

		#Moving to the next page when all 100 players have been scanned
		if i == 100:
			url = baseUrl + "-x100"
			x -= 100

		if i == 200:
			url = baseUrl + "-x200"
			x -= 100

		if i == 300:
			url = baseUrl + "-x300"
			x -= 100

		if i == 400:
			url = baseUrl + "-x400"
			x -= 100
			

	#print(playerIDs)
	#print(realNames)
	#print(gameTotals)
	#print(overallTotals)
	#print(percentOfTotals)
	#print(bDays)
	#print(countries)


	#Exporting all data to a csv file
	file = filename + ".csv"
	with open(file, 'w', newline = '', encoding = "utf-16") as csvfile:

		fieldnames = ["Player ID", "Name", "Total Earnings (Game)", "Total Earnings (Overall)", "% of Total", "Birthday", "Country"]

		thewriter = csv.DictWriter(csvfile, fieldnames = fieldnames)

		thewriter.writeheader()

		for i in range(len(playerIDs)):

			thewriter.writerow({'Player ID': playerIDs[i], "Name": realNames[i], "Total Earnings (Game)": gameTotals[i], "Total Earnings (Overall)": overallTotals[i], "% of Total": percentOfTotals[i], "Birthday": bDays[i], "Country": countries[i]})

	print("DONE.")




#Using simplified filenames for further use in Stata
#Dota
gatherData("https://www.esportsearnings.com/games/231-dota-2/top-players", "Data1")
#CSGO
gatherData("https://www.esportsearnings.com/games/245-counter-strike-global-offensive/top-players", "Data2")
#Fortnite
gatherData("https://www.esportsearnings.com/games/534-fortnite/top-players", "Data3")
#League of Legends
gatherData("https://www.esportsearnings.com/games/164-league-of-legends/top-players", "Data4")
#Starcraft 2
gatherData("https://www.esportsearnings.com/games/151-starcraft-ii/top-players", "Data5")
#Overwatch
gatherData("https://www.esportsearnings.com/games/426-overwatch/top-players", "Data6")
#PUBG
gatherData("https://www.esportsearnings.com/games/504-playerunknowns-battlegrounds/top-players", "Data7")
#Hearthstone
gatherData("https://www.esportsearnings.com/games/328-hearthstone/top-players", "Data8")
#Arena of Valor
gatherData("https://www.esportsearnings.com/games/529-arena-of-valor/top-players", "Data9")
#Heroes of the Storm
gatherData("https://www.esportsearnings.com/games/371-heroes-of-the-storm/top-players", "Data10")
