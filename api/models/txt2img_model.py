from pydantic import BaseModel
from typing import Optional


# Definition of the Txt2ImgRequest model using Pydantic's BaseModel.
# This model specifies the parameters accepted by the txt2img function for generating images from text prompts.
# Details about what each parameter means are explained in the documentation.

class Txt2ImgRequest(BaseModel):
    """
    This class defines the model for the Txt2ImgRequest using Pydantic's BaseModel, specifying parameters for image generation:
    - api_key: Optional API key for authentication purposes, default is an empty string.
    - scheduler_name: Specifies the scheduler name for the image generation process. Options include 'dpmpp_sde_k', 'dpmpp_2m_k', 'unipc', 'ddim'. Default is 'unipc'. If you set scheduler_name = "" empty string, it will use base model only.
    - prompt: Primary text prompt based on which the image is generated.
    - prompt2: Secondary text prompt, used if additional context or details are required. Default is empty.
    - num_inference_steps: Number of inference steps in the image generation process. Default is 25.
    - seed: Seed for random number generator to ensure reproducibility. Default is -1 (no specific seed).
    - height: Height of the generated image in pixels. Default is 1024.
    - width: Width of the generated image in pixels. Default is 1024.
    - denoising_end: Denoising end value, influencing the clarity of the generated image. Default is 0.0.
    - guidance_scale: Guidance scale, affecting the adherence to the prompt. Higher values lead to closer matches. Default is 7.0.
    - negative_prompt: Negative prompt to specify what should not appear in the image. Default is "nude adult porn".
    - negative_prompt_2: Secondary negative prompt, similar purpose as the first negative prompt. Default is "nude adult porn".
    - num_images_per_prompt: Number of images to generate for each prompt. Default is 1.
    - eta: Eta value, influencing the randomness in the generation process. Default is 0.0.
    - output_type: Output type of the image, e.g., 'pil' for Python Imaging Library format. Default is "pil".
    - return_dict: Whether to return a dictionary. Default is False.
    - guidance_rescale: Guidance rescale value, possibly used to refine image details. Default is 0.0.
    - original_size: Original size of the image as a tuple (width, height). Default is (1024, 1024).
    - crops_coords_top_left: Coordinates of the top-left corner for cropping, as a tuple (x, y). Default is (0, 0).
    - target_size: Target size of the image after processing, as a tuple (width, height). Default is (1024, 1024).
    - negative_original_size: Original size for negative prompt processing, similar to 'original_size'. Default is (1024, 1024).
    - negative_crops_coords_top_left: Coordinates for cropping in negative prompt processing, similar to 'crops_coords_top_left'. Default is (0, 0).
    - negative_target_size: Target size for negative prompt processing, similar to 'target_size'. Default is (1024, 1024).
    - model: Specifies the model to be used for image generation. Options include 'base', 'refiner'. Default is 'base'.
    - refiner_prompt: Refiner prompt for additional details or quality improvements in the image generation. Default is a descriptive string.
    """
    api_key: Optional[str] = ""
    scheduler_name: Optional[str] = "unipc"         # dpmpp_sde_k, dpmpp_2m_k, unipc, ddim
    prompt: Optional[str] = "An image a happy couple walking along the beach, beautiful sunset, amazing full view, detailed, 8k"
    prompt2: Optional[str] = ""
    num_inference_steps: Optional[int] = 25
    seed: Optional[int] = -1
    height: Optional[int] = 1024
    width: Optional[int] = 1024
    denoising_end: Optional[float] = 0.0
    guidance_scale: Optional[float] = 7.0
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
    model: Optional[str] = "base"   #"base", "refiner"
    refiner_prompt: Optional[str] = "high resolution, realistic, 8k, decent, beautiful, high quality"
