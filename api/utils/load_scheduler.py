import torch
from diffusers import DPMSolverMultistepScheduler, DPMSolverSinglestepScheduler, DDIMScheduler, UniPCMultistepScheduler


# Define a function to load a diffuser scheduler based on the specified scheduler name.
def load_scheduler(scheduler: str, model):
    # Define the main configuration for the diffuser schedulers.
    main_config = {
        'beta_start': 0.00085,
        'beta_end': 0.012,
        'beta_schedule': 'scaled_linear',
        'use_karras_sigmas': True
    }

    # Determine the scheduler based on the input string.
    match scheduler:
        case 'dpmpp_sde_k':
            # Recommend steps 10 ~ 15
            dpmpp_sde_k = DPMSolverSinglestepScheduler(**main_config)
            return dpmpp_sde_k
        case 'dpmpp_2m_k':
            # Recommend steps 20 ~ 30
            dpmpp_2m_k = DPMSolverMultistepScheduler(**main_config)
            return dpmpp_2m_k
        case 'unipc':
            # Recommend steps 20 ~ 30
            unipc = UniPCMultistepScheduler(**main_config)
            return unipc
        case 'ddim':
            # Recommend steps 10 ~ 15
            # guidance_rescale=0.7
            ddim = DDIMScheduler.from_config(
                model.scheduler.config, rescale_betas_zero_snr=True, timestep_spacing="trailing"
            )
            return ddim
