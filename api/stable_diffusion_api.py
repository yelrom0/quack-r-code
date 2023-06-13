# System Imports

# Package Imports
from diffusers import ControlNetModel, DiffusionPipeline
from torch import float16, manual_seed

# Local Imports
from api.meta.enums import DeviceTypes
from api.qr_code import QRAPI


class StableDiffusionAPI:
    def __init__(
        self,
        device_type=DeviceTypes.CPU,
    ):
        self.controlnet = ControlNetModel.from_pretrained(
            "lllyasviel/control_v11f1e_sd15_tile",
            torch_dtype=float16,
        )
        self.pipe = DiffusionPipeline.from_pretrained(
            "runwayml/stable-diffusion-v1-5",
            custom_pipeline="stable_diffusion_controlnet_img2img",
            controlnet=self.controlnet,
            torch_dtype=float16,
        )

        match device_type:
            case DeviceTypes.CPU:
                self.pipe = self.pipe.to("cpu")
            case DeviceTypes.GPU:
                self.pipe = self.pipe.to("cuda")
            case DeviceTypes.MAC:
                self.pipe = self.pipe.to("mps")

        self.pipe.enable_xformers_memory_efficient_attention()

    def convert_qr(
        self,
        qr: QRAPI,
        prompt: str,
        negative_prompt: str,
        resolution: int = 1024,
        strength: float = 1.0,
        steps: int = 32,
    ) -> None:
        working_image = qr.get_resized_image(resolution)
        qr.post_ai_img = self.pipe(
            image=working_image,
            prompt=prompt,
            negative_prompt=negative_prompt,
            controlnet_conditioning_image=working_image,
            width=working_image.size[0],
            height=working_image.size[1],
            strength=strength,
            generator=manual_seed(0),
            num_inference_steps=steps,
        ).images[0]
