import os
from email.message import EmailMessage
from flask import url_for, current_app

OUTPUT_DIR = "outgoing_emails"

class EmailHandler:
    def __init__(self, email, image_name):
        self.email = email
        self.image_name = image_name
        self.msg = None

    def create_dir(self):
        os.makedirs(OUTPUT_DIR, exist_ok=True)

    def create_message(self):
        self.msg = EmailMessage()
        self.msg["Subject"] = "Your postcard"
        self.msg["From"] = "no-reply@example.com"
        self.msg["To"] = self.email
        self.msg.set_content("Here is your postcard!")

    def attach_postcard(self):
        image_path = os.path.join(
            current_app.static_folder,
            "pictures",
            self.image_name
        )

        with open(image_path, "rb") as f:
            self.msg.add_attachment(f.read(),
                            maintype="image",
                            subtype="jpeg",
                            filename=self.image_name)
            
    def save_email(self):
        out_file = os.path.join(OUTPUT_DIR, f"{self.email.replace('@','_')}.eml")
        with open(out_file, "wb") as f:
            f.write(self.msg.as_bytes())

        print("Email saved!")