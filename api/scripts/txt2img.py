import os
import sys

from PIL import Image
from models.txt2img_model import Txt2ImgRequest
from utils.load_sdxl_base_model import load_sdxl_base_model
from utils.load_sdxl_refiner_model import load_sdxl_refiner_model

MODEL_TYPE = "server"
MODEL_LOAD_TYPE = "pretrained"
MODEL = "base"
OUTPUT_PATH = "output"


def txt2img(param: Txt2ImgRequest):
    # Load stable diffusion xl model
    if param.model == "base":
        model = load_sdxl_base_model(MODEL_TYPE, MODEL_LOAD_TYPE)
    elif param.model == "refiner":
        model = load_sdxl_refiner_model(MODEL_TYPE, MODEL_LOAD_TYPE)
    else:
        model = load_sdxl_base_model(MODEL_TYPE, MODEL_LOAD_TYPE)

    # txt2img
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

    print(result)
    return result.images[0]
