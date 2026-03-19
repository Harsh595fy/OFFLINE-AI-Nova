# 🚀 OFFLINE-AI-Nova

**OFFLINE-AI-Nova** is a powerful offline AI system that can generate text, images, and code without internet access. Designed for privacy, speed, and local execution.

---

## 🧠 Features

- ✨ **Text Generation** — Chat, Notes, Answers
- 🎨 **Image Generation** — AI Art
- 💻 **Code Generation** — Python, Java, Web, and more
- 🔒 **100% Offline** — No internet required
- ⚡ **Optimized** for mid-range systems

---

## 💻 System Requirements

| Component | Requirement |
|-----------|-------------|
| CPU | Intel i5 11th Gen or higher |
| RAM | Minimum 8 GB |
| Storage | At least 15 GB free |
| OS | Linux / Windows |

---

## 📁 Project Structure

```
OFFLINE-AI-Nova/
│── models/
│   ├── mistral-7b-instruct-v0.2.Q4_K_M.gguf
│   ├── v1-5-pruned-emaonly.safetensors
│
│── app.py
|__ ai_engine.py
|__ image_engine.py
│── requirements.txt
|__ arequirements.txt
│── README.md
```

---

## 📦 Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/OFFLINE-AI-Nova.git
cd OFFLINE-AI-Nova
```

### 2️⃣ Create Models Folder

```bash
mkdir models
```

### 3️⃣ Download Required Models

Place the following models inside the `models/` folder:

**🔹 Text Model (LLM)**
- `mistral-7b-instruct-v0.2.Q4_K_M.gguf`

**🔹 Image Model (Stable Diffusion)**
- `v1-5-pruned-emaonly.safetensors`

#### 🔗 Model Download Sources

📥 **Mistral Model**
> https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.2-GGUF

📥 **Stable Diffusion Model**
> https://huggingface.co/runwayml/stable-diffusion-v1-5

### 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 5️⃣ Run the AI

```bash
python app.py
```

---

## 🧩 Technologies Used

| Layer | Technology |
|-------|------------|
| 🧠 LLM | Mistral 7B (GGUF format) |
| 🎨 Image AI | Stable Diffusion v1.5 |
| 🐍 Backend | Python |
| ⚙️ Inference | llama.cpp / diffusers |

---

## 🔥 Future Updates

- 🎤 Voice control
- 🖥️ GUI Interface
- 📱 Mobile support
- 🌍 Multi-language support

---

## 👨‍💻 Author

**Harsh Singh Rao**
*Cybersecurity Enthusiast | AI Developer*

---

## ⭐ Support

If you like this project:

- ⭐ **Star** the repo
- 🍴 **Fork** it
- 📢 **Share** it

---
