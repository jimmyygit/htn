from fastapi import FastAPI
import cohere
from typing import List

app = FastAPI()
co = cohere.Client("")


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/cohere")
async def cohere_chat():
    response = co.generate(
        prompt="Please explain to me how LLMs work",
    )
    return {"message": response}

@app.get("/categorize")
async def categorize(categories: List[str], note: str):
    BASE_PROMPT = f"""
    We have the following categories: {categories.split()}. Which of these categories would you classify the following message under: {note}
    """
    response = co.generate(
       prompt=BASE_PROMPT, 
    )
    return {"message": response}