import torch
from diffusers import StableDiffusionPipeline
import os

MODEL_PATH = "models/v1-5-pruned-emaonly.safetensors"

class ImageEngine:
    def __init__(self):
        print("🖼️ Loading Stable Diffusion (CPU)...")
        self.pipe = StableDiffusionPipeline.from_single_file(
            MODEL_PATH,
            torch_dtype=torch.float32
        )
        self.pipe = self.pipe.to("cpu")
        print("✅ Image Engine Ready")

    def generate(self, prompt, output_path):
        image = self.pipe(
            prompt,
            num_inference_steps=20
        ).images[0]

        image.save(output_path)

image_engine = ImageEngine()

