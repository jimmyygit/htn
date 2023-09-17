from fastapi import FastAPI
import cohere
from typing import List
from pydantic import BaseModel
import os
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware


load_dotenv()


app = FastAPI()
co = cohere.Client(os.getenv("secret_key"))

origins = [
    "http://localhost:5173",
    "http://localhost:4173",
    "https://jotter-y4es.onrender.com",
    "https://jotters.netlify.app",
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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
                    "categories": ["Family", "School", "Career", "To-do"],
                    "note": "Apply to Google",
                }
            ]
        }
    }


@app.post("/categorize")
async def categorize(category: Category):
    BASE_PROMPT = f"""
    We have the following categories: {", ".join(category.categories)}. Which of these categories would you classify the following message under: {category.note}.
    WITH THE CATEGORY NOW DECIDED, assign it to a variable called the_category. 
    Then, provide 1 very brief and very funny suggestion on how to accomplish the aforementioned message.
    Make sure that suggestion is VERY funny, but not mean to anyone--they should be harmless jokes. Assign this suggestion to a variable called the_suggestion
    The format of your answer should be: `the_category|the_suggestion`. Keep the overall answer VERY short, and do NOT explain your answer. MAKE SURE the_suggestion is a complete sentence, so don't end a suggestion with a preposition'."""
    response = co.generate(prompt=BASE_PROMPT)
    return_values = response.generations[0].text.strip().split("|")
    return_category = return_values[0]
    return_suggestion = return_values[1]
    return {"category": return_category, "suggestion": return_suggestion}
