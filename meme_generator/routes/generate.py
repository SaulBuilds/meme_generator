from flask import Blueprint, request, jsonify
from meme_generator.services.hf_client import generate_images


generate_bp = Blueprint("generate", __name__, url_prefix="/generate")

@generate_bp.route("/", methods=["POST"])
def generate():
    data = request.get_json()
    prompt = data.get("prompt")
    batch_size = data.get("batch_size", 1)

    if not prompt:
        return jsonify({"error": "Prompt is required"}), 400

    generated_images = generate_images(prompt, batch_size)
    return jsonify({"images": generated_images})
