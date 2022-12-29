# vexEye
 A lean and mean API that functions off of python webscraping capabilities

## GAVE UP ON TRYING TO FIND A SIMPLE HOSTING OPTION
## JUST USE THE FUNCTIONS DIRECTLY LOLOLOLOL

### 1) Clone project

### 2) Install requirements
pip install -r requirements.txt
### 3) import functions
from utility.util import findAllComps, findAllParticipating, findAllScheduled

### 4) Call functions and use!
countryCode -> int (Default is: 244 (US country code))<br>
regionCode -> int (Default is: 62 (WA region code))<br>
teamCode -> string (Default is: "44244M" (Mukilteo Robotics Modulo))
===== findAllParticipating(countryCode, regionCode, teamCode) ===== <br>
Finds all matches that a team has participated in or will participate in the current season. Returns a json string.
<br>
===== findAllScheduled(countryCode, regionCode, teamCode) ===== <br>
Finds all matches that a team are SCHEDULED for. Past cases are not outputted. Returns a set of json objects.
<br>
===== findAllComps(countryCode, regionCode) ===== <br>
Finds all competitions in a certain region regarless of participation or not.
