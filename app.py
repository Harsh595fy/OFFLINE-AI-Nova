from flask import Flask, request, jsonify, render_template
from ai_engine import get_ai_response
from image_engine import image_engine
import uuid, os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("chat.html")

# 🔹 TEXT CHAT (OLD)
@app.route("/api/ai/chat", methods=["POST"])
def ai_chat():
    data = request.json
    reply = get_ai_response(
        data.get("message", ""),
        subject=data.get("subject", "General"),
        use_local=data.get("use_offline", False),
        language=data.get("language", "english")
    )
    return jsonify({"reply": reply, "success": True})

# 🔹 IMAGE GENERATION (NEW)
@app.route("/api/ai/image", methods=["POST"])
def ai_image():
    prompt = request.json.get("prompt", "")

    filename = f"{uuid.uuid4().hex}.png"
    output_dir = "static/generated"
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, filename)

    image_engine.generate(prompt, output_path)

    return jsonify({
        "success": True,
        "image_url": f"/static/generated/{filename}"
    })

if __name__ == "__main__":
    print("🚀 Nova AI Running on http://127.0.0.1:5000")
    app.run(debug=True)

