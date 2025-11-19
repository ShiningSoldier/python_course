import requests
import os
import time
from PIL import Image, ImageDraw, ImageFont

API_URL = "https://picsum.photos"
SAVE_PATH = "static/pictures"

class PictureHandler:
    def __init__(self, width, height, motto):
        self.width = width
        self.height = height
        self.motto = motto

        self.raw_data = None
        self.file_path = None
        self.file_name = None

    def get_picture(self):
        self.raw_data = requests.get(f"{API_URL}/{self.width}/{self.height}")

    def create_dir(self):
        os.makedirs(SAVE_PATH, exist_ok=True)

    def save_picture(self):
        timestamp = str(time.time())
        self.file_path = os.path.join(SAVE_PATH, f"image_{self.width}x{self.height}x{timestamp}.jpg")
        with open(self.file_path, "wb") as f:
            f.write(self.raw_data.content)
        self.file_name = os.path.basename(self.file_path)
    
    def add_motto(self):
        img = Image.open(self.file_path)
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("arial.ttf", size=18)
        draw.text((50, 50), self.motto, font=font, fill="white")
        img.save(self.file_path)
