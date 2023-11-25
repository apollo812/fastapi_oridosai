import os
import sys
import torch

from typing import Union, List
import numpy as np
from PIL import Image
from models.txt2img_model import Txt2ImgRequest
from utils.load_sdxl_base_model import load_sdxl_base_model
from utils.load_sdxl_refiner_model import load_sdxl_refiner_model
from diffusers import DPMSolverMultistepScheduler

# Function for generating images from text prompts.
def txt2img(param: Txt2ImgRequest):
    # Load the base model for text-to-image generation.
    model = load_sdxl_base_model()
    
    # DPM++ SDE Karras Scheduler 
    # Recommend steps 20 ~ 30
    common_config = {
        'beta_start': 0.00085,
        'beta_end': 0.012,
        'beta_schedule': 'scaled_linear',
        "use_karras_sigmas": True
    }

    dpmpp_2m_k = DPMSolverMultistepScheduler(**common_config)
    model.scheduler = dpmpp_2m_k
    generator = torch.Generator(device='cuda').manual_seed(-1)
    generator.manual_seed(-1)

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
        'guidance_rescale' : param.guidance_rescale,
        'original_size' : param.original_size,
        'crops_coords_top_left' : param.crops_coords_top_left,
        'target_size' : param.target_size,
        'negative_original_size' : param.negative_original_size,
        'negative_crops_coords_top_left' : param.negative_crops_coords_top_left,
        'negative_target_size' : param.negative_target_size
    }

    sdxl_img = model(**params, generator=generator)

    return sdxl_img[0][0]                     # Return the generated image.


# Function for refiner images using sdxl refiner model.
def refinerImg(img: Union[
        torch.Tensor,
        Image.Image,
        np.ndarray,
        List[torch.Tensor],
        List[Image.Image],
        List[np.ndarray]
    ]
):
    # Load the refiner model for image-to-image generation.
    model = load_sdxl_refiner_model()
    
    # Generate an image based on the image with input text prompts and other parameters using the loaded model.
    result = model(
        prompt = "high resolution, realistic, realistic, 8k",
        prompt2 = "high resolution, realistic, realistic, 8k",
        image = img,
        strength = 0.3,
        num_inference_steps = 50,
        denoising_start = 0.0,
        denoising_end = 0.0,
        guidance_scale = 7.0,
        negative_prompt = "nude adult porn",
        negative_prompt_2 = "nude adult porn",
        num_images_per_prompt = 1,
        eta = 0.0,
        output_type = "pil",
        return_dict = False,
        guidance_rescale = 0.0,
        original_size = (1024, 1024),
        crops_coords_top_left = (0, 0),
        target_size = (1024, 1024),
        negative_original_size = (1024, 1024),
        negative_crops_coords_top_left = (0, 0),
        negative_target_size = (1024, 1024),
        aesthetic_score = 6.0,
        negative_aesthetic_score = 2.5,
        clip_skip = 1,
    )

    return result[0][0]                     # Return the generated image.
