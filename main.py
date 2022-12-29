import os
from fastapi import FastAPI
import json
from utility.util import findAllComps, findAllParticipating, findAllScheduled


stage = os.environ.get('STAGE', None)
openapi_prefix = f"/{stage}" if stage else"/"
app = FastAPI(title="VexEye", openapi_prefix=openapi_prefix)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/findAllComps")
async def allComps(countryCode: int=244, regionCode: int=62):
    json_Marika = json.dumps([ob.toDict() for ob in await findAllComps(countryCode, regionCode)])
    return json_Marika

@app.get("/findAllParticipating")
async def allParticipating(countryCode: int=244, regionCode: int=62, teamCode: str="44244M"):
    json_Kosaki = json.dumps([ob.toDict() for ob in await findAllParticipating(countryCode, regionCode, teamCode)])
    return json_Kosaki

@app.get("/util/scheduled")
async def scheduled(countryCode: int=244, regionCode: int=62, teamCode: str="44244M"):
    json_Chitoge = json.dumps(await findAllScheduled(countryCode, regionCode, teamCode))
    return json_Chitoge
