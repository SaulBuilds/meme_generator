import os

class InstanceConfig:
    HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY", "")
    SECRET_KEY = os.getenv("SECRET_KEY", "your_secret_key_here")
