import os
from dotenv import load_dotenv
from fastapi import FastAPI, responses

load_dotenv()

app = FastAPI(title=os.getenv("APP_NAME", "Pilar API"))

@app.get("/", include_in_schema=False)
def root():
    return responses.RedirectResponse(url='/docs')