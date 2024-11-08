from transformers import pipeline
from flask import current_app

def generate_images(prompt, batch_size=1):
    hf_api_key = current_app.config["HUGGINGFACE_API_KEY"]
    image_generator = pipeline("text-to-image-generation", model="stabilityai/stable-diffusion", use_auth_token=hf_api_key)

    images = []
    for _ in range(batch_size):
        image = image_generator(prompt)
        images.append(image)
    
    return images
