from .generate import generate_bp
from .upload import upload_bp
from .fine_tune import fine_tune_bp

__all__ = ["generate_bp", "upload_bp", "fine_tune_bp"]


# The __all__ list makes the blueprint imports accessible from the routes package
__all__ = ["generate_bp", "upload_bp", "fine_tune_bp"]
