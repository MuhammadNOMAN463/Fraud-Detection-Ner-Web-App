# 🕵️ Fraud Detection NER App

This is a simple Named Entity Recognition (NER) web app built using **FastAPI** and **spaCy**. It detects potentially suspicious entities such as names, organizations, dates, money, and locations in financial text — useful for basic fraud detection tasks.

### 🚀 Live Demo
Deployed on [Vercel](https://vercel.com) (link will be added after deployment)

---

## 📌 Features

- 🧠 Named Entity Recognition (NER) with spaCy
- 🧾 Detects PERSON, ORG, GPE, DATE, and MONEY entities
- 🌐 Web-based interface (HTML + JavaScript)
- ⚙️ FastAPI backend
- ☁️ Serverless deployment on Vercel

---

## 🧪 Example Input

```
John Smith transferred $50,000 to a Swiss bank account via ShellCorp Inc. on March 12, 2024.
```

### ✅ Output
- **John Smith** → PERSON  
- **$50,000** → MONEY  
- **Swiss** → GPE  
- **ShellCorp Inc.** → ORG  
- **March 12, 2024** → DATE  

---

## 💻 How to Run Locally

1. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   python -m spacy download en_core_web_sm
   ```

2. **Start the server**
   ```bash
   uvicorn api.ner:app --reload
   ```

3. Open `index.html` in your browser and test it out!

---

## 🌍 Deploy on Vercel

1. Push this project to a GitHub repo
2. Connect the repo to your [Vercel](https://vercel.com) account
3. Vercel will auto-deploy it using `vercel.json`

> After deployment, update the **Live Demo** link above.

---

## 📂 Project Structure

```
fraud-ner-vercel/
├── api/
│   └── ner.py         # FastAPI backend
├── index.html         # Frontend interface
├── vercel.json        # Vercel config
└── requirements.txt   # Python dependencies
```

---

## 📜 License
This project is open-source and free to use.

---

## 👨‍💻 Author
**Noman** — aspiring AI Engineer | [LinkedIn](https://linkedin.com)