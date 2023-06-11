"""The main file of the application. This is where hypercorn comes to play."""

# System Imports

# Package Imports
from fastapi import FastAPI

# Local Imports
from api.open_ai_api import AIApi
from api.meta.schemas import GPTPrompt

# create main server
app = FastAPI(
    title="Quack'R Code",
    description="Makes you an epic QR code for whatever site you want",
    version="1.0.0",
)


@app.post("/test-gpt")
async def test_chatgpt_prompt(payload: GPTPrompt) -> str:
    # setup api and send first message back to client
    ai_api = AIApi()
    resp: str = await ai_api.get_stable_diffusion_prompt(payload.user_prompt)
    print(resp)
    return resp
