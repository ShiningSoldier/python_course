from flask import Flask, render_template, request
from pictures import PictureHandler
from emails import EmailHandler

app = Flask(__name__)

@app.route("/")
def show_form():
    return render_template("create_postcard.html")

@app.route("/show_send_postcard")
def create_postcard():
    motto = request.args.get("motto")
    pic_handler = PictureHandler(640, 480, motto)
    pic_handler.create_dir()
    pic_handler.get_picture()
    pic_handler.save_picture()
    pic_handler.add_motto()

    return render_template("send_postcard.html", file_name=pic_handler.file_name)

@app.route("/send_postcard", methods=["POST"])
def send_postcard():
    email = request.form["email"]
    image_path = request.form["file_name"]
    email_handler = EmailHandler(email, image_path)
    email_handler.create_dir()
    email_handler.create_message()
    email_handler.attach_postcard()
    email_handler.save_email()

    return render_template("create_postcard.html")
    