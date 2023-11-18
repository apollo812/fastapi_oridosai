import os
import gc
import time
import argparse
from pathlib import Path

from api.utils.read_json import read_json
from api.src.oridosai_api import OridosAIAPI


def main(args):
    """
    main entry point
    """
    # Initialize
    image_path_list = args.image_path
    payload_list = args.payload

    # Loop over number of requests
    for i in range(len(payload_list)):
    
        # Timer
        start_time = time.time()
        
        # json data
        data = read_json(payload_list[i])

        # Call oridosai API
        downloader = OridosAIAPI(args.api_url, data, image_path_list[i])
        downloader.execute()

        # Print time
        end_time = time.time()
        msg = f"Total processing time for payload no. {str(i)}: {end_time - start_time} seconds"
        print(msg)

    # Delete class objects and clean the buffer memory using the garbage collection
    gc.collect()

if __name__ == '__main__':
    """
    Form command lines
    python3 main_request.py --api_url "https://98qjbqboqy17x9-5000.proxy.runpod.net/txt2img" --payload "payload.json" --image_path "/home/jupiter/github/txt2img-sdxl-p1/output_images/output_image01.png"
    """
    # Clean up buffer memory
    gc.collect()

    # Current directory
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # list of payload
    payload = [
    os.path.join(current_dir, "test", "regression", "rtest_000", "payload.json"),
    os.path.join(current_dir, "test", "regression", "rtest_001", "payload.json"),
    os.path.join(current_dir, "test", "regression", "rtest_002", "payload.json"),
    os.path.join(current_dir, "test", "regression", "rtest_003", "payload.json"),
    ]

    # Input image directory
    image_path = [
        os.path.join(current_dir, "test", "regression", "rtest_000", "output.png"),
        os.path.join(current_dir, "test", "regression", "rtest_001", "output.png"),
        os.path.join(current_dir, "test", "regression", "rtest_002", "output.png"),
        os.path.join(current_dir, "test", "regression", "rtest_003", "output.png"),
    ]
    
    # URL
    api_url = "https://98qjbqboqy17x9-5000.proxy.runpod.net/txt2img"

    parser = argparse.ArgumentParser(description='Download an image from a POST request.')
    parser.add_argument('--api_url', type=str, default=api_url, help='URL to send the POST request to')
    parser.add_argument('--payload', type=list, default=payload, help='JSON string with the data to send in the request')
    parser.add_argument('--image_path', type=list, default=image_path, help='Path to save the downloaded image')
    args = parser.parse_args()

    # main call
    main(args)
