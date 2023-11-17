FROM runpod/pytorch:2.1.0-py3.10-cuda11.8.0-devel-ubuntu22.04 as base

# Define a build argument named PROJECT with a default value of 'api'.
ARG PROJECT=api

# Update package index and install libgl1-mesa-glx package.
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx

# Create a non-root user to run the app with.
RUN groupadd --gid 1000 user &&  adduser --disabled-password --gecos '' --uid 1000 --gid 1000 user

# Set the working directory for the subsequent commands.
WORKDIR /home/user

# Copy the requirements.txt file and install the Python dependencies.
COPY --chown=user:user ./requirements.txt ./
RUN pip install -r requirements.txt

# Switch to the non-root user for security purposes.
USER user


# Create a new stage named 'dev' based on the 'base' stage.
FROM base as dev

# Copy the project files into the container.
COPY --chown=user:user ./$PROJECT /home/user/$PROJECT
# Define the command to run when the container starts.
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "5000", "--reload"]


# Create a new stage named 'test' based on the 'base' stage.
FROM base as test

# Copy the project files into the container.
COPY --chown=user:user ./$PROJECT /home/user/$PROJECT
# Create a directory for mypy cache and change its ownership to the non-root user.
RUN mkdir /home/user/.mypy_cache && chown -R user:user /home/user/.mypy_cache

# Set the default target stage to 'dev'.
FROM dev
