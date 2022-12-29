import requests
import re
from bs4 import BeautifulSoup
from datetime import datetime, date
from requests_html import HTMLSession
import json

from comp import Comp

def scrapeParticipants(link) :
    teams = []
    session = HTMLSession()
    response = session.get(link)

    #TODO HERE
    response.html.render(sleep=3, timeout=20)
    content = response.html.find("tbody tr")

    for team in content:
        teamCode = team.find('td')[0].text
        if re.search("^\d.*[a-zA-Z]$", teamCode):
            teams.append(teamCode)

    return teams 


def scrapeLeagueDates(link) :
    dates = []
    session = HTMLSession()
    response = session.get(link)
    response.html.render(sleep=3, timeout=20)
    content = response.html.find("summary")

    for summary in content:
        dates.append(summary.text.split("Date: ")[1])
    
    return dates


def findAllComps(countryCode=244, regionCode=62):
    today = date.today().strftime("%d-%m-%Y")
    competitions = []
    for i in range(1,6):
        page = requests.get(f"https://www.robotevents.com/robot-competitions/vex-robotics-competition?\
                            country_id={countryCode}&\
                            country_region_id={regionCode}&\
                            seasonId=&\
                            eventType=&\
                            eventTag=&\
                            name=&\
                            grade_level_id=&\
                            level_class_id=&\
                            from_date={today}&\
                            to_date=&\
                            event_region=&\
                            city=&\
                            page={i}")
        soup = BeautifulSoup(page.content, "html.parser")
    
        for competition in soup.select("div.results div.card-body"):
            if (len(competition.select("a")) != 0):
                aName = competition.select("a")[0].text
                link = competition.select("a")[0]['href']

                if ("League" in aName or "league" in aName):
                    # TODO await here TANKS efficiency
                    dates = scrapeLeagueDates(link)
                else:
                    dates = [competition.select("p")[4].text.split("Date:")[1].strip()]
                    # may tank efficiency 
                    dates = dates[0].split(" - ") if (len(dates[0].split(" - ")) > 1) else dates

                aName = aName.split(", ")

                if len(aName) == 1:
                    aName = ["", aName[0], ""]

                # TODO await here TANKS efficiency
                participants = scrapeParticipants(f"{link}#teams")
                comp = Comp(
                    aName[1],
                    aName[2],
                    competition.select("badge"),
                    aName[-1],
                    link,
                    dates,
                    participants
                )
                print(comp.name, comp.dates)
                competitions.append(comp)
    return json.dumps([ob.toDict() for ob in competitions], indent=2)


def findAllParticipating(countryCode=244, regionCode=62, teamCode="44244M"):
    compsAttending = []
    competitions = findAllComps(countryCode, regionCode)

    for comp in competitions:
        if teamCode in comp.participants:
            compsAttending.append(comp)

    return json.dumps([ob.toDict() for ob in compsAttending], indent=2)


def findAllScheduled(countryCode=244, regionCode=62, teamCode="44244M"):
    compsScheduled = []
    competitions = findAllComps(countryCode, regionCode)

    for comp in competitions:
        if teamCode in comp.participants:
            for competitionDate in comp.dates:
                if datetime.strptime(competitionDate, '%d-%b-%Y').date() > date.today(): 
                    compsScheduled.append({"compName":comp.name, "compDate":competitionDate})

    return json.dumps(compsScheduled, indent=2)
    
# print(findAllScheduled())
# asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
print(findAllComps())
# json_Mariko = json.dumps([ob.toDict() for ob in allcomps], indent=2)
# print(json_Mariko)

# asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
# print(asyncio.run(scrapeLeagueDates("https://www.robotevents.com/robot-competitions/vex-robotics-competition/RE-VRC-22-0554.html#general-info")))
# print(asyncio.run(scrapeParticipants("https://www.robotevents.com/robot-competitions/vex-robotics-competition/RE-VRC-22-9996.html#teams")))


