from flask import Flask, render_template, request
import qrcode
import random
import os

app = Flask(__name__)

# دالة توليد الكود بالصيغة الصحيحة
def generate_custom_code(internal_code):
    fixed_part_1 = "0100000000"
    random_part = "".join(str(random.randint(0, 9)) for _ in range(6))  # 6 أرقام عشوائية
    fixed_part_2 = "1725073110ve090a#2127608752238"

    return f"{fixed_part_1}{random_part}{internal_code}{fixed_part_2}"

@app.route("/", methods=["GET", "POST"])
def index():
    qr_code_data = None

    if request.method == "POST":
        internal_code = request.form["internal_code"]  # الكود الداخلي من المستخدم
        qr_code_data = generate_custom_code(internal_code)  # توليد الكود بناءً على الكود الداخلي
        qr = qrcode.make(qr_code_data)
        qr.save("static/qrcode.png")  # حفظ الصورة داخل مجلد static

    return render_template("index.html", qr_code_data=qr_code_data)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
