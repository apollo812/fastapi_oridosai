import torch
from diffusers import StableDiffusionXLPipeline


# Load the SDXL refiner model.
def load_sdxl_refiner_model():
    # Initialize the StableDiffusionXLPipeline model from the pretrained weights
    # Set the torch precision to float16 and enable the use of SafeTensors for enhanced safety
    # Move the model to the CUDA device for accelerated computations
    pipeline = StableDiffusionXLPipeline.from_pretrained(
        model_path, torch_dtype=torch.float16, variant="fp16", use_safetensors=True
    ).to("cuda")
    
    return pipeline     # Return the loaded and configured SDXL refiner model
