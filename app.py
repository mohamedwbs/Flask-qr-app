from flask import Flask, render_template, request
import qrcode
from io import BytesIO
import base64

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    qr_base = "0100000000"
    suffix = "1725073110ve090a#2127608752238"
    
    qr_code_img = None
    if request.method == "POST":
        user_input = request.form["user_code"]
        full_code = qr_base + user_input + suffix

        # توليد كود QR
        qr = qrcode.make(full_code)
        buffer = BytesIO()
        qr.save(buffer, format="PNG")
        buffer.seek(0)
        qr_base64 = base64.b64encode(buffer.getvalue()).decode()

        qr_code_img = f"data:image/png;base64,{qr_base64}"

    return render_template("index.html", qr_code_img=qr_code_img)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

