"""The main file of the application. This is where hypercorn comes to play."""

# System Imports

# Package Imports
from fastapi import FastAPI
from fastapi.responses import Response

# Local Imports
from api.open_ai_api import AIApi
from api.qr_code import QRAPI
from api.meta.schemas import GPTPrompt, QRCode
from api.stable_diffusion_api import StableDiffusionAPI

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


@app.post(
    "/test-qr",
    responses={200: {"content": {"image/png": {}}}},
    response_class=Response,
)
def test_qr_code(payload: QRCode) -> Response:
    """setup api and send qr code representing the url back to client"""
    qr_api = QRAPI(url=payload.url)
    return Response(
        content=qr_api.get_qr_code_as_bytes(),
        media_type="image/png",
    )


@app.post(
    "/create-qr",
    responses={200: {"content": {"image/png": {}}}},
    response_class=Response,
)
async def create_qr_code(
    qr_data: QRCode,
    prompt: GPTPrompt,
) -> Response:
    """Generate fancy AI QR code using the prompt and url provided"""
    gpt_api = AIApi()
    resp: list[str] = await gpt_api.get_stable_diffusion_prompt(
        prompt.user_prompt,
    )
    qr_api = QRAPI(
        url=qr_data.url,
    )
    diffusion_api = StableDiffusionAPI()
    diffusion_api.convert_qr(
        qr=qr_api,
        prompt=resp[0],
        negative_prompt=resp[1],
        steps=20,
    )
    return Response(
        content=qr_api.post_ai_img,
        media_type="image/png",
    )
