from pydantic import BaseModel
from typing import Optional, Union, List


class Txt2ImgRequest(BaseModel):
    # api_key: Optional[str] = ""
    # model: Optional[str] = "base"
    prompt: str
    prompt2: Optional[str] = ""
    height: Optional[int] = 1024
    width: Optional[int] = 1024
    num_inference_steps: Optional[int] = 50
    denoising_end: Optional[float] = 0.0
    guidance_scale: Optional[float] = 5.0
    negative_prompt: Optional[str] = "nude adult porn"
    negative_prompt_2: Optional[str] = "nude adult porn"
    num_images_per_prompt: Optional[int] = 1
    eta: Optional[float] = 0.0
    output_type: Optional[str] = "pil"
    return_dict: Optional[bool] = False
    guidance_rescale: Optional[float] = 0.0
    original_size: Optional[tuple[int, int]] = (1024, 1024)
    crops_coords_top_left: Optional[tuple[int, int]] = (0, 0)
    target_size: Optional[tuple[int, int]] = (1024, 1024)
    negative_original_size: Optional[tuple[int, int]] = (1024, 1024)
    negative_crops_coords_top_left: Optional[tuple[int, int]] = (0, 0)
    negative_target_size: Optional[tuple[int, int]] = (1024, 1024)
