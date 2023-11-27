import torch
from diffusers import StableDiffusionXLImg2ImgPipeline


# Load the SDXL refiner model.
def load_sdxl_refiner_model():
    # Initialize the StableDiffusionXLPipeline model from the pretrained weights
    # Set the torch precision to float16 and enable the use of SafeTensors for enhanced safety
    # Move the model to the CUDA device for accelerated computations
    model_path = "stabilityai/stable-diffusion-xl-refiner-1.0"
    
    pipeline = StableDiffusionXLImg2ImgPipeline.from_pretrained(
        model_path, 
        torch_dtype=torch.float16, 
        variant="fp16", 
        use_safetensors=True,
        add_watermarker=False
    ).to("cuda")
    
    return pipeline     # Return the loaded and configured SDXL refiner model
