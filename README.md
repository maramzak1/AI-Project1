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
Milo Vet Care is a **mobile application** that leverages advanced AI to deliver **personalized pet care**. By combining breed classification, health monitoring, and explainable recommendations, it helps users make informed decisions for their pets’ well-being.  

---  

## ✨ Key Features  

### 🐶 **Breed Classification**  
Pretrained deep learning models for accurate dog/cat breed identification.  

### 🧠 **General Recommendation System (RAG-based)**  
A **Retrieval-Augmented Generation (RAG)** pipeline that provides **evidence-backed health advice** tailored to your pet’s breed.  
- **🔍 Retrieval**: Uses **BGE-small-en-v1.5** embeddings (normalized to unit length) with **cosine similarity** for precise document matching *(1.0 = identical, 0.0 = unrelated)*.  
- **📜 Context Handling**: Processes long documents (128K tokens) with **Gemma-3-4B-IT**, optimized for efficiency on consumer hardware.  
- **🎛️ Generation Control**: Balances creativity and reliability via:  
  - `temperature=0.7` *(deterministic but adaptable)*  
  - `top_p=0.85` *(filters low-probability nonsense)*  
- **📊 Confidence Scoring**: Ranks sources by relevance (e.g., *90% for peer-reviewed papers vs. 78% for guides*).  

> **Example**: Search for *“Golden Retriever hip dysplasia prevention”* to retrieve FDA reports, AKC guides, and research papers—then receive summarized advice with source ratings.  

### ⚠️ **Anomaly Detection**  
Flags unusual health patterns (e.g., lethargy, appetite changes) for early intervention.  

### 🌿 **Natural Remedies Recommendation**  
Semantic search powered by:  
- **✅ SentenceTransformers** for multilingual query understanding.  
- **⚡ FAISS** for fast similarity search.  
- **🧠 Ollama + LLaMA3** for context-aware answers.  
- **🧪 LIME** to explain which query terms influenced results *(e.g., highlights “joint pain” in a French query)*.  
- **💾 Diskcache** to avoid redundant computations.  

### 🩻 **X-ray Cardiac Analysis**  
AI-driven diagnostics for detecting heart conditions from X-rays.  

---  

## 🛠️ Tech Stack  

| Category                | Technologies                                                                 |  
|-------------------------|------------------------------------------------------------------------------|  
| **Mobile**              | Flutter / FlutterFlow                                                        |  
| **Deep Learning**       | TensorFlow / PyTorch                                                         |  
| **RAG Pipeline**        | FAISS, LangChain, BGE-small-en-v1.5, Gemma-3-4B-IT                          |  
| **NLP Tools**           | Sentence Transformers, LangDetect, LIME                                     |  
| **Caching**             | Diskcache                                                                    |  

---  

## 📂 Project Structure  


