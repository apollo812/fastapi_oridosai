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
    
    url = "https://huggingface.co/datasets/patrickvonplaten/images/resolve/main/aa_xl/000000009.png"

    # init_image = load_image(url).convert("RGB")
    init_image = load_image(image).convert("RGB")
    prompt = "a photo of an astronaut riding a horse on mars"
    image = model(prompt, init_image).images[0]
    # Generate an image based on the image with input text prompts and other parameters using the loaded model.
    # result = model(
    #     prompt = param.prompt,
    #     prompt2 = param.prompt2,
    #     image = image,
    #     strength = param.strength,
    #     num_inference_steps = param.num_inference_steps,
    #     denoising_start = param.denoising_start,
    #     denoising_end = param.denoising_end,
    #     guidance_scale = param.guidance_scale,
    #     negative_prompt = param.negative_prompt,
    #     negative_prompt_2 = param.negative_prompt_2,
    #     num_images_per_prompt = param.num_images_per_prompt,
    #     eta = param.eta,
    #     output_type = param.output_type,
    #     return_dict = param.return_dict,
    #     guidance_rescale = param.guidance_rescale,
    #     # original_size = param.original_size,
    #     # crops_coords_top_left = param.crops_coords_top_left,
    #     # target_size = param.target_size,
    #     # negative_original_size = param.negative_original_size,
    #     # negative_crops_coords_top_left = param.negative_crops_coords_top_left,
    #     # negative_target_size = param.negative_target_size,
    #     aesthetic_score = param.aesthetic_score,
    #     negative_aesthetic_score = param.negative_aesthetic_score,
    #     clip_skip = param.clip_skip
    # )

    return image                    # Return the generated image.
