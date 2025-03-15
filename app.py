from flask import Flask, render_template, request
import qrcode
import random

app = Flask(__name__)

# دالة توليد الكود بالصيغة الصحيحة
def generate_custom_code(internal_code):
    fixed_part_1 = "0100000000"
    fixed_part_2 = "1725073110ve090a#"
    
    # توليد 10 أرقام عشوائية مختلفة مع كل طلب جديد
    random_part = "".join(str(random.randint(0, 9)) for _ in range(10))

    return f"{fixed_part_1}{internal_code}{fixed_part_2}{random_part}"

@app.route("/", methods=["GET", "POST"])
def index():
    qr_code_data = None

    if request.method == "POST":
        internal_code = request.form.get("internal_code", "").strip()  # الحصول على الكود الداخلي
        if len(internal_code) == 6 and internal_code.isdigit():  # التأكد إنه 6 أرقام
            qr_code_data = generate_custom_code(internal_code)
            qr = qrcode.make(qr_code_data)
            qr.save("static/qrcode.png")  # حفظ الصورة داخل مجلد static

    return render_template("index.html", qr_code_data=qr_code_data)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
