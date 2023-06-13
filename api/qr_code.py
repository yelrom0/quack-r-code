"""
qr_code.py
The backend QR code and image functions of this application.
Most of this code is repurposed from my previously written chat bot
"""

# System Imports
from io import BytesIO

# Package Imports
from qrcode import QRCode
from qrcode.constants import ERROR_CORRECT_Q
from qrcode.image.pil import Image


class QRAPI:
    def __init__(self, url: str, error_correction: int = ERROR_CORRECT_Q):
        qr_code: QRCode = QRCode(
            version=1,
            error_correction=error_correction,
            border=0,
        )
        qr_code.add_data(url)
        qr_code.make(fit=True)
        self.img: Image = qr_code.make_image(
            fill_color="black",
            back_color="white",
        )

    def get_qr_code_as_pil(self) -> Image:
        return self.img

    def get_qr_code_as_bytes(self) -> bytes:
        byte_arr = BytesIO()
        self.img.save(byte_arr)
        return byte_arr.getvalue()

    def get_resized_image(self, resolution: int) -> Image:
        # convert to rgb then resize based on the provided resolution
        working_image: Image = self.img.convert("RGB")
        W, H = working_image.size
        k = float(resolution) / min(H, W)
        H *= k
        W *= k
        H = int(round(H / 64.0)) * 64
        W = int(round(W / 64.0)) * 64
        img: Image = working_image.resize((W, H), resample=Image.LANCZOS)
        return img

    def get_post_ai_img_as_pil(self) -> Image:
        return self.post_ai_img

    def _store_post_ai_img(self, image: Image) -> None:
        self.post_ai_img = image

    def _get_post_ai_img_as_bytes(self) -> bytes:
        byte_arr = BytesIO()
        self.post_ai_img.save(byte_arr)
        return byte_arr.getvalue()

    post_ai_img = property(
        fget=_get_post_ai_img_as_bytes,
        fset=_store_post_ai_img,
        doc="The latest image after AI processing",
    )
