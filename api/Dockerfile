FROM runpod/pytorch:2.1.0-py3.10-cuda11.8.0-devel-ubuntu22.04 as base
 
ARG PROJECT=api

RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx

# RUN pip install httpx pytest black isort mypy fastapi uvicorn diffusers transformers accelerate safetensors omegaconf invisible-watermark>=0.2.0 --root-user-action=ignore

# Create a non-root user to run the app with.
RUN groupadd --gid 1000 user &&  adduser --disabled-password --gecos '' --uid 1000 --gid 1000 user
USER user

WORKDIR /home/user

COPY --chown=user:user ./requirements.txt ./requirements-test.txt ./

FROM base as dev

COPY --chown=user:user ./$PROJECT /home/user/$PROJECT
RUN pip install -r requirements.txt
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "5000", "--reload"]


FROM base as test

COPY --chown=user:user ./$PROJECT /home/user/$PROJECT
RUN pip install -r requirements-test.txt
RUN mkdir /home/user/.mypy_cache && chown -R user:user /home/user/.mypy_cache

# Default target.
FROM dev
