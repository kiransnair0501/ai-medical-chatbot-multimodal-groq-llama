# 🧠 AI Medical Chatbot: Multimodal Clinical Query Analysis Using Groq-LLaMA Vision Models and Reinforcement-Inspired Evaluation

**AI Medical Chatbot** is an advanced healthcare assistant capable of handling both textual and image-based medical queries. It leverages Meta’s **LLaMA Vision Models** (via **Groq**) to analyze multimodal inputs and provide real-time diagnostic insights.

By integrating powerful **multi-modal AI** with a clean, responsive frontend, the system empowers **medical students, researchers**, and **healthcare enthusiasts** to explore clinical diagnostics in an interactive and intelligent way.

---

## 🚀 Features

- 📝 Accepts **text input** and **image uploads** for symptom diagnosis  
- 🧠 Powered by **Meta’s LLaMA 11B and 90B Vision Models** (via **Groq**)  
- ⚡ Provides **real-time**, intelligent medical query responses  
- 🌐 Built with **FastAPI** and a lightweight **Tailwind CSS frontend**  
- 🏷 Supports **medical image classification and diagnosis**  
- 🎓 Ideal for **medical learning**, **AI demos**, and **research**

---

## 🛠 Tech Stack

**Backend:** Python, FastAPI  
**Frontend:** HTML, Tailwind CSS  
**Models:** LLaMA 11B & 90B (via Groq API)  
**Tools:** Uvicorn, Virtualenv  
**Image Handling:** OpenCV

---

## 📁 Project Structure

```bash
ai-medical-chatbot-multimodal-groq-llama/
├── ai_medical_chatbot-main/
│   ├── app.py              # FastAPI endpoints
│   ├── main.py             # Entry point
│   ├── utils.py            # Helper functions
│   ├── templates/
│   │   └── index.html      # Frontend page
│   └── test*.jpg/png/webp  # Sample input images
├── .env                    # Groq API key (ignored)
├── .gitignore              # Git exclusions
├── requirements.txt        # Python dependencies
└── README.md
```

---

## UI Preview image
![Screenshot 2025-06-14 105222](https://github.com/user-attachments/assets/84dc400a-9f9d-4a15-83c3-b76faf4a7d83)

---

## 🔐 API Keys Required

This project uses **Groq’s LLaMA API** for multimodal image and text processing.

🔗 Get your key here: https://console.groq.com/keys

### ⚠ Important: Never upload your actual API key to GitHub. Use a .env file or environment variables for security.

---

## ⚙ Installation & Setup

1. **Clone the Repository**
    ```bash
    git clone https://github.com/Kushal0006/ai-medical-chatbot.git
    cd ai-medical-chatbot
    ```
    
2. **Create and Activate a Virtual Environment**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```
   
5. **Add Your API Key** : Insert your Groq API key in the appropriate file (main.py or use .env).
   
   
7. **Run the Application**
   ```bash
   uvicorn main:app --reload
   ```
   
9. **Open in Your Browser**
   ```bash
   Go to: http://127.0.0.1:8000
   ```
   
---

## 🙌 Contributors
This project was built as a collaborative academic effort by:

- Kiran S Nair
- Kushal S
- Asritha Y
- Prajwal V

---

## 📄 License
This project is for academic and demonstration purposes only.
Feel free to fork, improve, and contribute — just give credit where due!

---

## 🌐 Citation
Published in the **International Journal of Research Publication and Reviews (IJRPR)**

**📅 May 2025, Volume 6, Issue 5, Pages 1259–1263**,
**ISSN: 2582-7421**

---

## 📬 Feedback

Feel free to open issues or submit pull requests.  
We welcome suggestions to improve functionality and UI/UX!
