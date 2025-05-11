# 🐾 Milo Vet Care

<p align="center">
  <b>AI-powered veterinary care in your pocket. 🐶🐱</b><br>
  <i>Breed classification, health monitoring, recommendations, and X-ray analysis — all in one app.</i>
</p>

<p align="center">
  <img alt="Built with Love" src="https://img.shields.io/badge/Built%20with-%E2%9D%A4-red">
  <img alt="AI Project" src="https://img.shields.io/badge/Powered%20by-AI%20%26%20Deep%20Learning-blueviolet">
  <img alt="Status" src="https://img.shields.io/badge/Status-Active-brightgreen">
</p>

---

## 📖 Overview

Milo Vet Care is a **mobile application** dedicated to improving the lives of animals by blending advanced **AI models** into a simple, user-friendly interface.  
It provides tools to **monitor pet health**, **recommend treatments**, and **assist with early detection** of health problems.

---

## ✨ Key Features

- **🐶 Breed Classification**  
  Deep learning pretrained models to recognize dog and cat breeds with high precision.

- **🧠 General Recommendation System (RAG-based)**  
  Using **FAISS**, **LangChain**, **Gemma 3** and **BGE-small v1.5** to provide customized daily care advice.

- **⚠️ Anomaly Detection in Health**  
  Detects unusual behaviors or health indicators to warn users early.

- **🌿 Natural Remedies Recommendation System**  
  A semantic search-based module that recommends natural remedies based on a user’s query.  
  It uses:
  - ✅ **SentenceTransformers** to embed both data and user queries.
  - ⚡ **FAISS** to find the most relevant content efficiently.
  - 🧠 **Ollama with LLaMA3** to generate personalized, context-aware answers.
  - 🧪 **LIME (Local Interpretable Model-agnostic Explanations)** to highlight which words in the question influenced the system's understanding.
  - 💾 **Diskcache** to optimize speed by avoiding recomputation.

  > 📌 *Example:* Ask “des traitements naturels pour les douleurs articulaires du chien âgé ?” and receive curated advice with a visual explanation of key query terms.

- **🩻 X-ray Cardiac Image Analysis**  
  AI-driven diagnostics to assist in interpreting X-ray images for heart issues.

---

## 🛠️ Tech Stack

| Category                | Technologies                                               |
|------------------------|------------------------------------------------------------|
| Mobile Development     | Flutter / FlutterFlow                                      |
| Deep Learning          | TensorFlow / PyTorch                                       |
| Recommendation Systems | FAISS, LangChain, Gemma 3, BGE-small-v1.5, LLaMA3 via Ollama|
| Natural Language Tools | Sentence Transformers, LangDetect, LIME                    |
| XAI & Visualization    | LIME, Matplotlib                                           |
| Caching                | Diskcache                                                  |

---

## 📂 Project Structure

