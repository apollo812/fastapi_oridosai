import os
import sys
import torch

from typing import Union, List
import numpy as np
from PIL import Image
from models.txt2img_model import Txt2ImgRequest
from utils.load_sdxl_base_model import load_sdxl_base_model
from utils.load_sdxl_refiner_model import load_sdxl_refiner_model
from utils.load_scheduler import load_scheduler
from diffusers.utils import load_image

# Function for generating images from text prompts.
def txt2img(param: Txt2ImgRequest):
    # Load the base model for text-to-image generation.
    model = load_sdxl_base_model()

    # Define parameters for text-to-image generation.
    params = {
        'prompt': [param.prompt],
        'prompt2' : [param.prompt],
        'height' : param.height,
        'width' : param.width,
        'num_inference_steps' : param.num_inference_steps,
        'denoising_end' : param.denoising_end,
        'guidance_scale' : param.guidance_scale,
        'negative_prompt' : param.negative_prompt,
        'negative_prompt_2' : param.negative_prompt_2,
        'num_images_per_prompt' : param.num_images_per_prompt,
        'eta' : param.eta,
        'output_type' : param.output_type,
        'return_dict' : param.return_dict,
        'guidance_rescale' : 0.7 if param.scheduler_name == "ddim" else param.guidance_rescale,
        'original_size' : param.original_size,
        'crops_coords_top_left' : param.crops_coords_top_left,
        'target_size' : param.target_size,
        'negative_original_size' : param.negative_original_size,
        'negative_crops_coords_top_left' : param.negative_crops_coords_top_left,
        'negative_target_size' : param.negative_target_size
    }
    
    # Load the scheduler based on the specified scheduler name.
    if param.scheduler_name != "":
        # Initialize a random number generator for CUDA.
        generator = torch.Generator(device='cuda').manual_seed(param.seed)
        
        model.scheduler = load_scheduler(param.scheduler_name)
        
        # Generate an image using the base model and provided parameters.
        sdxl_img = model(**params, generator=generator)
    else:
        # Generate an image using the base model and provided parameters.
        sdxl_img = model(**params)

    # Return the generated image.
    return sdxl_img[0][0]                     

# Function for refiner images using sdxl refiner model.
def refinerImg(img: Union[
        torch.Tensor,
        Image.Image,
        np.ndarray,
        List[torch.Tensor],
        List[Image.Image],
        List[np.ndarray]
    ], refiner_prompt: str
):
    # Load the refiner model for image-to-image generation.
    model = load_sdxl_refiner_model()

    init_image = load_image(img).convert("RGB")
    prompt = refiner_prompt

    # Generate an image based on the image with input text prompts and other parameters using the loaded model.
    image = model(prompt, image=init_image).images[0]

    return image                     # Return the generated image.
