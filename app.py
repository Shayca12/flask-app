from flask import Flask, request, render_template_string, jsonify

app = Flask(__name__)

PAGE = """
<!doctype html>
<html lang="he">
  <head>
    <meta charset="utf-8" />
    <title>שלום!</title>
  </head>
  <body style="font-family: Arial; padding: 24px;">
    <h2>הכנס שם</h2>
    <form method="POST">
      <input name="name" placeholder="לדוגמה: שי" required />
      <button type="submit">שלח</button>
    </form>

    {% if name %}
      <h3>שלום {{ name }} 👋</h3>
    {% endif %}
  </body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    name = ""
    if request.method == "POST":
        name = request.form.get("name", "").strip()
    return render_template_string(PAGE, name=name)

@app.route("/AI", methods=["GET"])
def ai():
    return jsonify({"message": "Activate AI for next buy"})

if __name__ == "__main__":
    # 0.0.0.0 כדי שיעבוד בתוך Docker
    app.run(host="0.0.0.0", port=5000)

