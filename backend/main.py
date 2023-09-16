from fastapi import FastAPI
import cohere

app = FastAPI()
co = cohere.Client("")


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/cohere")
async def root():
    response = co.generate(
        prompt="Please explain to me how LLMs work",
    )
    return {"message": response}
