from flask import Flask, render_template, request, redirect, url_for, jsonify
from meme_generator import create_app
import base64

app = create_app()

@app.route("/")
def index():
    return render_template("index.html")

# Generate images
@app.route("/generate", methods=["POST"])
def generate_image():
    prompt = request.form.get("prompt")
    batch_size = int(request.form.get("batch_size", 1))

    # Assuming `generate_images` returns a list of PIL images
    generated_images = generate_images(prompt, batch_size)
    images_base64 = [base64.b64encode(img).decode('utf-8') for img in generated_images]
    
    return render_template("results.html", images=images_base64)

# Upload images for fine-tuning
@app.route("/upload", methods=["POST"])
def upload_image():
    file = request.files["file"]
    prompt = request.form.get("prompt", "")
    
    # Store the uploaded image and prompt as per your existing upload logic
    upload_result = upload_image_to_db(file, prompt)  # Define this helper function as needed

    return render_template("results.html", message="Image uploaded successfully" if upload_result else "Upload failed.")

# Start fine-tuning
@app.route("/fine_tune", methods=["POST"])
def fine_tune():
    result = fine_tune_model()  # Assuming this function starts fine-tuning
    
    return render_template("results.html", message=result)

if __name__ == "__main__":
    app.run(debug=True)
