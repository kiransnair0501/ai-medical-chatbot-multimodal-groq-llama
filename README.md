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
ai-medical-chatbot-multimodal-groq-llama/
├── ai_medical_chatbot-main/
│ ├── app.py # FastAPI routes
│ ├── main.py # App entry point
│ ├── utils.py # Utility functions
│ ├── templates/
│ │ └── index.html # Frontend layout
│ └── test*.jpg/png # Sample medical images
├── .env # API key file (git-ignored)
├── .gitignore # Files to exclude from Git
├── requirements.txt # Python dependencies
└── README.md # Project overview


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

### 1. Clone the Repository

```bash
git clone https://github.com/k1ransnair/ai-medical-chatbot-multimodal-groq-llama.git
cd ai-medical-chatbot-multimodal-groq-llama

###2. Create a Virtual Environment
bash
Copy
Edit
python -m venv .venv
.venv\Scripts\activate  # On Windows

###3. Install Required Packages
bash
Copy
Edit
pip install -r requirements.txt

###4. Add Your API Key
Add your Groq API key in .env or directly in main.py (not recommended).

###5. Run the App
bash
Copy
Edit
uvicorn main:app --reload
Visit: http://127.0.0.1:8000

##👥 Contributors
Kiran S Nair

Kushal S

Asritha Y

Prajwal V

##📄 License
This project is for academic and demonstration purposes only.
Feel free to fork, improve, and contribute — just give credit where due.