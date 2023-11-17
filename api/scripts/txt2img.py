import os
import sys

from PIL import Image
from models.txt2img_model import Txt2ImgRequest
from utils.load_sdxl_base_model import load_sdxl_base_model
from utils.load_sdxl_refiner_model import load_sdxl_refiner_model


# Function for generating images from text prompts.
def txt2img(param: Txt2ImgRequest):
    # Load the Stable Diffusion XL model based on the specified parameter.
    if param.model == "base":
        model = load_sdxl_base_model()      # Load the base model for text-to-image generation.
    elif param.model == "refiner":
        model = load_sdxl_refiner_model()   # Load the refiner model for text-to-image generation.
    else:
        model = load_sdxl_base_model()      # Default to loading the base model if no valid model parameter is provided.

    # Generate an image based on the input text prompts and other parameters using the loaded model.
    result = model(
        prompt = param.prompt,
        prompt2 = param.prompt2,
        height = param.height,
        width = param.width,
        num_inference_steps = param.num_inference_steps,
        denoising_end = param.denoising_end,
        guidance_scale = param.guidance_scale,
        negative_prompt = param.negative_prompt,
        negative_prompt_2 = param.negative_prompt_2,
        num_images_per_prompt = param.num_images_per_prompt,
        eta = param.eta,
        output_type = param.output_type,
        return_dict = param.return_dict,
        guidance_rescale = param.guidance_rescale,
        original_size = param.original_size,
        crops_coords_top_left = param.crops_coords_top_left,
        target_size = param.target_size,
        negative_original_size = param.negative_original_size,
        negative_crops_coords_top_left = param.negative_crops_coords_top_left,
        negative_target_size = param.negative_target_size
    )

    return result[0][0]                     # Return the generated image.
