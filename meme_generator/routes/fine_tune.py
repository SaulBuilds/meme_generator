from flask import Blueprint, jsonify
from meme_generator.services.model_trainer import fine_tune_model

fine_tune_bp = Blueprint("fine_tune", __name__, url_prefix="/fine_tune")

@fine_tune_bp.route("/", methods=["POST"])
def fine_tune():
    result = fine_tune_model()
    return jsonify({"message": "Fine-tuning started", "status": result})
