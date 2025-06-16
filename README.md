# 🧠 AI Medical Chatbot  
**Multimodal Clinical Query Analysis Using Groq-LLaMA Vision Models**

A powerful AI-driven medical assistant that processes **text and image-based queries** using **Groq’s LLaMA Vision Models**. Built with **FastAPI** and a clean **Tailwind CSS** frontend, this tool delivers real-time diagnostic insights for education, research, and clinical exploration.

---

## ✨ Key Features

- 📝 Accepts **text and image inputs** for medical diagnosis  
- 🤖 Integrates Meta’s **LLaMA 11B & 90B Vision Models** via **Groq API**  
- ⚡ Offers fast, intelligent diagnostic responses  
- 🛠 Built with **FastAPI (backend)** and **Tailwind CSS (frontend)**  
- 🩺 Supports **medical image classification and reasoning**  
- 🎓 Perfect for **medical learning**, **demonstrations**, and **research projects**

---

## 🧰 Tech Stack

- **Backend:** Python, FastAPI  
- **Frontend:** HTML, Tailwind CSS  
- **AI Models:** LLaMA 11B & 90B (via Groq)  
- **Tools:** Uvicorn, Virtualenv  
- **Image Processing:** OpenCV

---

## 📁 Directory Structure

```
ai-medical-chatbot-multimodal-groq-llama/
├── ai_medical_chatbot-main/
│   ├── app.py              # FastAPI routes
│   ├── main.py             # App entry point
│   ├── utils.py            # Utility functions
│   ├── templates/
│   │   └── index.html      # Frontend layout
│   └── test*.jpg/png       # Sample medical images
├── .env                    # API key file (git-ignored)
├── .gitignore              # Files to exclude from Git
├── requirements.txt        # Python dependencies
└── README.md               # Project overview
```

---

## 🖼 UI Preview

![UI Preview](https://github.com/user-attachments/assets/84dc400a-9f9d-4a15-83c3-b76faf4a7d83)

---

## 🔐 API Access

This app uses **Groq's API** for multimodal inference.  
👉 Get your API key: [https://console.groq.com/keys](https://console.groq.com/keys)

> ⚠️ **Important:** Never upload your API key to GitHub. Store it securely in a `.env` file or use environment variables.

---

## 🛠 Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/k1ransnair/ai-medical-chatbot-multimodal-groq-llama.git
cd ai-medical-chatbot-multimodal-groq-llama
```

### 2. Create and activate a virtual environment (Windows example)

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add your Groq API key

```bash
# Create a file named `.env` in the root directory and add:
GROQ_API_KEY=your_key_here
```
Or export as an environment variable.

### 5. Run the application

```bash
uvicorn main:app --reload
```

Open in your browser: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 👥 Contributors

- Kiran S Nair  
- Kushal S  
- Asritha Y  
- Prajwal V  

---

## 📄 License

This project is for academic and demonstration purposes only.  
Feel free to fork, improve, and contribute—just give credit where due!

---

## 📰 Citation

Published in the **International Journal of Research Publication and Reviews (IJRPR)**  
**May 2025 · Volume 6 · Issue 5 · pp. 1259–1263**  
**ISSN 2582‑7421**

---

## 💬 Feedback

Have suggestions or found an issue?  
Open an issue or submit a pull request—contributions are welcome!
