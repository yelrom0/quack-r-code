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
from qrcode.image.pil import PilImage


class QRAPI:
    def __init__(self, url: str, error_correction: int = ERROR_CORRECT_Q):
        qr_code: QRCode = QRCode(
            version=1,
            error_correction=error_correction,
            border=0,
        )
        qr_code.add_data(url)
        qr_code.make(fit=True)
        self.img: PilImage = qr_code.make_image(
            fill_color="black",
            back_color="white",
        )

    def get_qr_code_as_pil(self) -> PilImage:
        return self.img

    def get_qr_code_as_bytes(self) -> bytes:
        byte_arr = BytesIO()
        self.img.save(byte_arr)
        return byte_arr.getvalue()
