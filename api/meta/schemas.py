from pydantic import BaseModel
from qrcode.constants import (
    ERROR_CORRECT_Q,
)


# just doing this one for the naming and in case I need something later
class QuackRBase(BaseModel):
    pass


class GPTPrompt(QuackRBase):
    user_prompt: str


class QRCode(QuackRBase):
    url: str
    error_correction: int | None = ERROR_CORRECT_Q
