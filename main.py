from fastapi import FastAPI
import json
from util import findAllComps, findAllParticipating, findAllScheduled, scrapeLeagueDates

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/findAllComps/")
async def allComps(countryCode: int=244, regionCode: int=62):
    json_Marika = json.dumps([ob.toDict() for ob in await findAllComps(countryCode, regionCode)])
    return json_Marika

@app.get("/finders")
async def boot(countryCode: int=233):
    return {"message":countryCode}

@app.get("/findAllParticipating")
async def allParticipating(countryCode: int=244, regionCode: int=62, teamCode: str="44244M"):
    json_Kosaki = json.dumps([ob.toDict() for ob in await findAllParticipating(countryCode, regionCode, teamCode)])
    return json_Kosaki

@app.get("/util/scheduled")
async def scheduled(countryCode: int=244, regionCode: int=62, teamCode: str="44244M"):
    json_Chitoge = json.dumps(await findAllScheduled(countryCode, regionCode, teamCode))
    return json_Chitoge
