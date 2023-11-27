import torch
from diffusers import StableDiffusionXLPipeline


# Load the SDXL base model.
def load_sdxl_base_model():
    # Create an instance of StableDiffusionXLPipeline and load the pretrained model from the specified model_path.
    # Configure the pipeline to use 16-bit floating point precision (torch.float16) and enable SafeTensors for additional safety checks.
    # Move the pipeline to the CUDA (GPU) device for faster computation.
    model_path = "stabilityai/stable-diffusion-xl-base-1.0"
    
    pipeline = StableDiffusionXLPipeline.from_pretrained(
        model_path, 
        torch_dtype=torch.float16, 
        variant="fp16", 
        use_safetensors=True,
        add_watermarker=False
    ).to("cuda")
    
    return pipeline     # Return the loaded and configured SDXL base model pipeline.
