import os
import gc
import time
import random
import argparse
from pathlib import Path

from api.utils.read_json import read_json
from api.src.oridosai_api import OridosAIAPI


def generate_payload_and_image_lists(test_dir):
    # Initialize
    payload_list = []
    image_path_list = []

    # Iterate through each subfolder in the root directory
    for subdir in sorted(os.listdir(test_dir)):
        subdir_path = os.path.join(test_dir, subdir)

        # Check if it's a directory
        if os.path.isdir(subdir_path):
            # Construct paths for payload.json and output.png
            payload_json_path = os.path.join(subdir_path, "payload.json")
            output_png_path = os.path.join(subdir_path, "output.png")

            # Check if payload.json and output.png exist in the folder
            if os.path.isfile(payload_json_path):
                payload_list.append(payload_json_path)

            # Add image path
            image_path_list.append(output_png_path)

    return payload_list, image_path_list


def main(args):
    """
    main entry point
    """
    # Generate payload and image lists
    payload_list, image_path_list = generate_payload_and_image_lists(args.test_dir)

    # Loop over number of requests
    for i in range(len(payload_list)):
    
        # Timer
        start_time = time.time()
        
        # json data
        data = read_json(payload_list[i])

        # Change the seed
        data["seed"] = random.randint(10, 2**32 - 1)

        # Call oridosai API
        downloader = OridosAIAPI(args.api_url, data, image_path_list[i])
        downloader.execute()

        # Print time
        end_time = time.time()
        msg = f"Total processing time for payload no. {str(i)}: {end_time - start_time} seconds"
        print(msg)

    # Delete class objects and clean the buffer memory using the garbage collection
    gc.collect()


if __name__ == "__main__":
    """
    Form command lines
    python3 main_request.py --api_url "https://98qjbqboqy17x9-5000.proxy.runpod.net/txt2img" --payload "payload.json" --image_path "/home/jupiter/github/txt2img-sdxl-p1/output_images/output_image01.png"
    """
    # Clean up buffer memory
    gc.collect()

    # Current directory
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Test directory
    test_dir = os.path.join(current_dir, "test", "regression_txt2img")
    
    # URL
    api_url = "https://n33y73bqi4ri05-5000.proxy.runpod.net/txt2img"

    parser = argparse.ArgumentParser(description="Download an image from a POST request.")
    parser.add_argument("--api_url", type=str, default=api_url, help="URL to send the POST request to")
    parser.add_argument("--test_dir", type=Path, default=test_dir, help="test directory")
    args = parser.parse_args()

    # main call
    main(args)
