🧠 AI Medical Chatbot
Multimodal Clinical Query Analysis with Groq-LLaMA Vision Models & Reinforcement-Inspired Evaluation
AI Medical Chatbot is an intelligent healthcare assistant that processes both text and image-based queries. Leveraging Meta’s LLaMA Vision Models through Groq, it delivers real-time diagnostic insights for educational and research purposes.

With a sleek frontend and powerful AI backend, this tool enables medical students, researchers, and AI enthusiasts to engage with clinical data in a smart, multimodal environment.

🚀 Key Features
📝 Accepts text and image inputs for medical diagnosis

🧠 Integrates Meta’s LLaMA 11B & 90B Vision Models via Groq API

⚡ Offers fast, intelligent diagnostic responses

🌐 Built with FastAPI (backend) and Tailwind CSS (frontend)

🏷 Supports medical image classification and reasoning

🎓 Perfect for medical learning, demonstrations, and research projects

🛠 Tech Stack
Backend: Python, FastAPI

Frontend: HTML, Tailwind CSS

AI Models: LLaMA 11B & 90B (via Groq)

Tools: Uvicorn, Virtualenv

Image Processing: OpenCV

📁 Directory Structure
bash
Copy
Edit
ai-medical-chatbot-multimodal-groq-llama/
├── ai_medical_chatbot-main/
│   ├── app.py              # FastAPI routes
│   ├── main.py             # App entry point
│   ├── utils.py            # Utility functions
│   ├── templates/
│   │   └── index.html      # Frontend layout
│   └── test*.jpg/png/webp  # Sample medical images
├── .env                    # API key file (git-ignored)
├── .gitignore              # Files to exclude from Git
├── requirements.txt        # Python dependencies
└── README.md               # Project overview
🖼 UI Preview


🔐 API Access
This app uses Groq's API for multimodal inference.
🔗 Get your API key: https://console.groq.com/keys

⚠️ Do not upload your API key to GitHub. Store it securely in a .env file or as an environment variable.

⚙️ Installation & Setup
Clone this Repository

bash
Copy
Edit
git clone https://github.com/k1ransnair/ai-medical-chatbot-multimodal-groq-llama.git
cd ai-medical-chatbot-multimodal-groq-llama
Set Up a Virtual Environment

bash
Copy
Edit
python -m venv .venv
.venv\Scripts\activate    # For Windows
Install Required Packages

bash
Copy
Edit
pip install -r requirements.txt
Add Your API Key

Insert it in .env or directly into main.py (not recommended)

Run the App

bash
Copy
Edit
uvicorn main:app --reload
Access in Browser

Open http://127.0.0.1:8000

👥 Contributors
Project developed as a collaborative academic initiative by:

Kiran S Nair

Kushal S

Asritha Y

Prajwal V

📄 License
This project is intended for academic and demonstrative use.
You're welcome to fork, enhance, or reuse—just remember to credit the authors.

📚 Citation
Published in the International Journal of Research Publication and Reviews (IJRPR)
🗓 May 2025 | Volume 6, Issue 5 | Pages 1259–1263
ISSN: 2582-7421

💬 Feedback & Contributions
Found an issue? Have ideas for improvement?
Feel free to open an issue or submit a pull request — all contributions are appreciated!
