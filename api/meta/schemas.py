from pydantic import BaseModel


# just doing this one for the naming and in case I need something later
class QuackRBase(BaseModel):
    pass


class GPTPrompt(QuackRBase):
    user_prompt: str
