from flask import Blueprint, request, jsonify
from meme_generator.models import UserImage
from meme_generator.database import db
import uuid

upload_bp = Blueprint("upload", __name__, url_prefix="/upload")

@upload_bp.route("/", methods=["POST"])
def upload():
    file = request.files.get("file")
    prompt = request.form.get("prompt", "")

    if not file:
        return jsonify({"error": "File is required"}), 400

    image_id = str(uuid.uuid4())
    new_image = UserImage(id=image_id, user_id="user1", image=file.read(), prompt=prompt)

    db.session.add(new_image)
    db.session.commit()

    return jsonify({"message": "Image uploaded successfully", "image_id": image_id})
