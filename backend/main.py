from fastapi import FastAPI
import cohere
from typing import List
from pydantic import BaseModel
import os
from dotenv import load_dotenv

load_dotenv()


app = FastAPI()
co = cohere.Client(os.getenv("secret_key"))


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/cohere")
async def cohere_chat():
    response = co.generate(
        prompt="Please explain to me how LLMs work",
    )
    return {"message": response}


class Category(BaseModel):
    categories: List[str]
    note: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "categories": ["Family", "School", "Job", "Todo"],
                    "note": "Apply to Google",
                }
            ]
        }
    }


@app.post("/categorize")
async def categorize(category: Category):
    BASE_PROMPT = f"""
    We have the following categories: {", ".join(category.categories)}. 
    Please return only one of the categories listed before. Trim spaces.
    Which of these categories would you classify the following message under: {category.note}"""
    response = co.generate(prompt=BASE_PROMPT)
    return_category = response.generations[0].text.strip()
    return {"message": return_category}
