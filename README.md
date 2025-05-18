

---

# 🐶 Milo Vet Care – AI-Powered Veterinary Assistant

*Computer Vision, NLP & RAG for Animal Healthcare – Disease Detection, Diagnosis Support & Treatment Recommendations*

<p align="center">
  <img alt="AI" src="https://img.shields.io/badge/AI-Computer_Vision_|_NLP_|_RAG-blueviolet">
  <img alt="Accuracy" src="https://img.shields.io/badge/Top_Accuracy-97%25-brightgreen">
  <img alt="SDGs" src="https://img.shields.io/badge/UN_SDGs-3_9_15_17-green">
</p>

---

## 📌 Overview

**Problem Addressed**:

* Severe **veterinary shortage** (40%) in rural Tunisia
* 70% of animal care is **delayed** until emergencies

**AI-Driven Solution**:
Milo Vet Care is a **mobile AI-powered veterinary assistant** that leverages:

* ✅ **Computer Vision models** for species and disease recognition
* ✅ **Natural Language Processing (NLP)** for symptom checking & medical advice
* ✅ **Retrieval-Augmented Generation (RAG)** for treatment suggestions
* ✅ **Edge computing optimization** for offline & low-connectivity use cases

---

## ✨ Features

### 🐾 **1. Computer Vision for Animal Health**

| Feature                         | Technology Stack      | Performance    |
| ------------------------------- | --------------------- | -------------- |
| Multi-Species Classification    | Custom CNN, ResNet50  | 89.9% F1-Score |
| Skin Disease Detection (Dogs)   | ResNet50 + LogSoftmax | 97% Accuracy   |
| X-Ray Cardiac Anomaly Detection | EfficientNet\_B0      | 87% AUC        |

### 🧠 **2. NLP for Symptom Analysis & Diagnosis Support**

* Interactive **symptom checker chatbot** using Llama3 + MiniLM-L6-v2
* Dual-stage **RAG system** for:

  * Breed-specific recommendations (Gemma 3B + FAISS)
  * FDA-aligned treatment plans

### 🧬 **3. Explainable AI (XAI)**

* Visual insights via Grad-CAM for CNN predictions
* NLP interpretability via LIME
* Output confidence levels (scale: 0–1)

---

## 🛠️ Tech Stack

### ⚙️ Frontend

`FlutterFlow` | `Dart` | Custom **GUI** for veterinarians & pet owners

### ⚙️ Backend

| Component                  | Technologies Used                       |
| -------------------------- | --------------------------------------- |
| **Computer Vision Models** | PyTorch, TorchVision, ONNX Runtime      |
| **NLP & RAG Pipelines**    | Hugging Face Transformers, LangChain    |
| **Vector Search**          | FAISS, SentenceTransformers             |
| **API Layer**              | FastAPI, Swagger UI (API Documentation) |

---

## 📁 Directory Structure

```
milovetcare/
├── frontend/               # Flutter app (cross-platform GUI)
├── ml/                     # AI & ML modules
│   ├── vision/             # CNNs, XAI, model training scripts
│   └── nlp/                # LLMs, RAG pipelines, embeddings
├── api/                    # FastAPI routes & inference APIs
└── datasets/               # Training data & annotated files
    ├── dog_xrays/          # 1,200 annotated X-ray images
    └── clinical_guides/    # Labeled PDF medical documents
```

---

## 🚀 Getting Started

### ✅ Prerequisites

```bash
Python 3.10+  
PyTorch 2.0+  
Flutter 3.13+  
Ollama (for local inference of Llama3)  
NVIDIA GPU (CUDA 12.1 recommended)  
```

### 🔧 Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourrepo/milovetcare
   cd milovetcare
   ```
2. Set up your Python environment:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r backend/requirements.txt
   ```
3. Launch the API server:

   ```bash
   uvicorn api.main:app --reload
   ```

### 🧪 Demo Command (Skin Disease Prediction)

```bash
python ml/predict.py --image=dog.jpg --task=skin_disease
```

---

## 🎯 Use Cases & Keywords

* AI for veterinary care
* Animal disease detection
* Edge AI healthcare solutions
* NLP in medical diagnostics
* GUI for veterinary diagnosis
* XAI for healthcare transparency
* API for AI-based diagnosis
* Mobile veterinary assistant
* TensorFlow / PyTorch models
* FastAPI for ML deployments

---

## 🙏 Acknowledgments

* **Ariana Veterinary Clinic** for clinical validation (95% model agreement)
* **Mendeley** dataset for cardiac X-ray benchmarking
* **Team Neuronix** – Core developers:

  * Souleima Gharbi
  * Maram Zakraoui
  * Emna Nkhili
  * Farah Hassen
  * Dorra Sioud
  * Amir Staxi

<p align="center">
  <b>Made with 💙 by Team Neuronix</b><br>
  Souleima Gharbi • Maram Zakraoui • Emna Nkhili<br>
  Farah Hassen • Dorra Sioud • Amir Staxi  
</p>

<p align="center">
  <i>🚀 Open-source project advancing UN SDG 3 (Health), SDG 9 (Innovation), SDG 15 (Life on Land), and SDG 17 (Partnerships)</i>
</p>


