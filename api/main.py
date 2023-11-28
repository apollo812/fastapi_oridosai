import os
import sys
import io

# Get the current script's directory
current_script_directory = os.path.dirname(os.path.abspath(__file__))

# Get the project root path
project_root = os.path.abspath(os.path.join(current_script_directory, os.pardir))

# Append the project root and current script directory to the system path
sys.path.append(project_root)
sys.path.append(current_script_directory)

from PIL import Image
from fastapi import Depends, FastAPI, Response, File, UploadFile, Depends
from scripts.txt2img import txt2img, refinerImg
from scripts.img2img import img2img
from models.txt2img_model import Txt2ImgRequest
from models.img2img_model import Img2ImgRequest
from utils.load_sdxl_base_model import load_sdxl_base_model
from utils.load_sdxl_refiner_model import load_sdxl_refiner_model

from starlette.responses import RedirectResponse
from starlette.status import HTTP_201_CREATED

# Create a FastAPI application
app = FastAPI(swagger_ui_parameters={"tryItOutEnabled": True})


# Define a route to handle the root endpoint and redirect to the API documentation
@app.get("/")
async def root():
    # Load base and refiner model at first loading
    load_sdxl_base_model()
    load_sdxl_refiner_model()

    return RedirectResponse(app.docs_url)


# Define a route to handle the text-to-image conversion endpoint
@app.post("/txt2img", status_code=HTTP_201_CREATED)
async def t2i(request_body: Txt2ImgRequest):
    if request_body.model == "base":
        # Perform text-to-image conversion using the provided request body
        result = txt2img(request_body)
    elif request_body.model == "refiner":
        # Perform text-to-image conversion using the provided request body
        result = txt2img(request_body)
        if result is not None:
            # Refiner the generated image by text-to-image base model
            result = refinerImg(result)
        else:
            print("Error: txt2img function returned None")

    result.save("output.png") # Save the resulting image to a file

    # Return the image file as the response content
    with open("output.png", "rb") as f:
        file_content = f.read()

    return Response(content=file_content, media_type="image/png") # Return the image content as the API response


# Define a route to handle the image-to-image conversion endpoint
@app.post("/img2img", status_code=HTTP_201_CREATED)
async def i2i(request_body: Img2ImgRequest = Depends(), file: UploadFile = File(...)):
    received_data= request_body.dict()
    print("re", received_data)
    # Perform text-to-image conversion using the provided request body
    contents = await file.read()
    
    # Convert the file contents to a PIL Image object
    image = Image.open(io.BytesIO(contents))
    print("here", image)
    result = img2img(received_data, image)

    result.save("output.png") # Save the resulting image to a file

    # Return the image file as the response content
    with open("output.png", "rb") as f:
        file_content = f.read()

    return Response(content=file_content, media_type="image/png") # Return the image content as the API response
