from meme_generator.database import db

class UserImage(db.Model):
    __tablename__ = "user_images"
    id = db.Column(db.String, primary_key=True)
    user_id = db.Column(db.String, nullable=False)
    image = db.Column(db.LargeBinary, nullable=False)
    prompt = db.Column(db.String, nullable=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
