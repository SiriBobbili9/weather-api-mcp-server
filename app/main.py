
from fastapi import FastAPI, HTTPException, Query
import httpx

from app.services.tools import get_weather

app = FastAPI(title="Weather API")


@app.get("/")
async def root():
    return {"message": "Weather API is running"}


@app.get("/weather")
async def weather(city: str = Query(min_length=1)):
    try:
        return await get_weather(city)
    except ValueError as exc:
        raise HTTPException(status_code=404, detail=str(exc))
    except httpx.HTTPError:
        raise HTTPException(
            status_code=502,
            detail="Unable to fetch weather from the external API",
        )
    except (KeyError, TypeError):
        raise HTTPException(
            status_code=502,
            detail="Unexpected response from the weather API",
        )
