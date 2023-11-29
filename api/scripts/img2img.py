import os
import sys

from PIL import Image
from models.img2img_model import Img2ImgRequest
from utils.load_sdxl_base_model import load_sdxl_base_model
from utils.load_sdxl_refiner_model import load_sdxl_refiner_model
from diffusers.utils import load_image

# Function for generating images from images with text prompts.
def img2img(param: Img2ImgRequest, image):
    # Load the refiner model for image-to-image generation.
    model = load_sdxl_refiner_model()
    
    init_image = load_image(image).convert("RGB")
    # Generate an image based on the image with input text prompts and other parameters using the loaded model.
    image = model(
        prompt=param.prompt, 
        negative_prompt=param.negative_prompt,
        image=init_image, 
        strength=param.strength, 
        guidance_scale=param.guidance_scale,
        num_inference_steps=param.num_inference_steps
    ).images[0]
    
    return image                    # Return the generated image.

# Function for generating images from images with text prompts.
def img2img_url(param: Img2ImgRequest):
    # Load the refiner model for image-to-image generation.
    model = load_sdxl_refiner_model()
    
    init_image = load_image(param.image).convert("RGB")
    # Generate an image based on the image with input text prompts and other parameters using the loaded model.
    image = model(
        prompt=param.prompt, 
        negative_prompt=param.negative_prompt,
        image=init_image, 
        strength=param.strength, 
        guidance_scale=param.guidance_scale,
        num_inference_steps=param.num_inference_steps
    ).images[0]
    
    return image                    # Return the generated image.
