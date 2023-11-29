import torch
import numpy as np

from typing import Union, List
from PIL import Image
from pydantic import BaseModel
from typing import Optional, Union, List

# Definition of the Img2ImgRequest model using Pydantic's BaseModel.
# This model specifies the parameters accepted by the img2img function for generating images from images with text prompts.
# Details about what each parameter means are explained in the documentation.

class Img2ImgRequest(BaseModel):
    api_key: Optional[str] = ""
    prompt: Optional[str] = "High resolution"
    prompt2: Optional[str] = ""
    image: Optional[str] = ""
    strength: Optional[float] = 0.75
    num_inference_steps: Optional[int] = 50
    denoising_start: Optional[float] = 0.0085
    denoising_end: Optional[float] = 0.12
    guidance_scale: Optional[float] = 7.5
    negative_prompt: Optional[str] = "nude adult porn"
    negative_prompt_2: Optional[str] = "nude adult porn"
    num_images_per_prompt: Optional[int] = 1
    eta: Optional[float] = 0.0
    output_type: Optional[str] = "pil"
    return_dict: Optional[bool] = False
    guidance_rescale: Optional[float] = 0.0
    # original_size: Optional[tuple[int, int]] = (1024, 1024)
    # crops_coords_top_left: Optional[tuple[int, int]] = (0, 0)
    # target_size: Optional[tuple[int, int]] = (1024, 1024)
    # negative_original_size: Optional[tuple[int, int]] = (1024, 1024)
    # negative_crops_coords_top_left: Optional[tuple[int, int]] = (0, 0)
    # negative_target_size: Optional[tuple[int, int]] = (1024, 1024)
    aesthetic_score: Optional[float] = 6.0
    negative_aesthetic_score: Optional[float] = 2.5
    clip_skip: Optional[int] = 1
