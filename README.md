
# 🐶 Milo Vet Care - AI-Powered Veterinary Assistant  
*Computer Vision & NLP for Animal Healthcare - Disease Detection, Diagnosis Support & Treatment Recommendations*

<p align="center">
  <img alt="AI" src="https://img.shields.io/badge/AI-Computer_Vision_|_NLP_|_RAG-blueviolet">
  <img alt="Accuracy" src="https://img.shields.io/badge/Top_Accuracy-97%25-brightgreen">
  <img alt="SDGs" src="https://img.shields.io/badge/UN_SDGs-3_9_15_17-green">
</p>

---

## 📌 Overview  
**Problem**:  
- 40% veterinary shortage in rural Tunisia  
- 70% delayed care until emergencies  

**AI Solution**:  
Mobile app featuring:  
- **Computer Vision**: Species classification (37 classes) & disease detection (97% accuracy)  
- **NLP**: Symptom checker & RAG systems for evidence-based recommendations  
- **Edge Optimization**: Works with limited internet connectivity  

---

## ✨ Key Features  

### **1. Computer Vision for Animal Health**  
| Feature | Technology | Performance |  
|---------|------------|-------------|  
| Species Classification | Custom CNN, ResNet50 | 89.9% F1-Score |  
| Dog Skin Disease Detection | ResNet50 + LogSoftmax | 97% Accuracy |  
| X-Ray Cardiac Analysis | EfficientNet_B0 | 87% AUC |  

### **2. NLP & Diagnostic Support**  
- **Symptom Checker**: Llama3 + MiniLM-L6-v2 embeddings  
- **RAG Systems**:  
  - Breed-specific advice (Gemma-3-4B + FAISS)  
  - Treatment plans (FDA/clinical guidelines retrieval)  

### **3. Explainable AI (XAI)**  
- Grad-CAM heatmaps for vision models  
- LIME explanations for NLP outputs  
- Confidence scoring (0-1 scale)  

---

## 🛠️ Tech Stack  

### **Frontend**  
`Flutter` | `Dart` | XAI Visualization | PWA Support  

### **Backend**  
| Component | Technology |  
|-----------|------------|  
| **Vision Models** | PyTorch, ONNX Runtime |  
| **NLP Pipelines** | Hugging Face Transformers, LangChain |  
| **Vector Database** | FAISS, Sentence-Transformers |  
| **API** | FastAPI, Swagger UI |  

### **DevOps & ML Tools**  
- **MLOps**: MLflow, DVC  
- **Data Processing**: OpenCV, Albumentations  
- **Deployment**: Docker, Kubernetes  

---

## 📂 Project Structure  
```
milovetcare/
├── frontend/               # Flutter app (Dart)
├── ml/                     # Machine Learning
│   ├── vision/             # 7 CNN models
│   └── nlp/                # RAG & Llama3
├── api/                    # FastAPI endpoints
└── datasets/               # Structured data
    ├── dog_xrays/          # 1,200 annotated images
    └── clinical_guides/    # Labeled PDFs
```

---

## 🚀 Getting Started  

### **Prerequisites**  
```bash
Python 3.10+ (PyTorch 2.0+)  
Flutter 3.13+  
Ollama (for local Llama3)  
NVIDIA GPU (CUDA 12.1 recommended)  
```

### **Installation**  
1. Clone the repository:  
   ```bash
   git clone https://github.com/yourrepo/milovetcare
   cd milovetcare
   ```
2. Set up environment:  
   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r backend/requirements.txt
   ```
3. Launch API:  
   ```bash
   uvicorn api.main:app --reload
   ```

### **Demo**  
```bash
python ml/predict.py --image=dog.jpg --task=skin_disease
```

---

## 🙏 Acknowledgments  
- **Ariana Veterinary Clinic** for clinical validation (95% accuracy)  
- **Mendeley Dataset** for cardiac X-rays  
- **Team Neuronix**:
  - Maram Zakraoui(**)
  - Dorra Soud (**)
  - Souleima Gharbi (**)
  - Farah Hassen (**)  
  - Emna Nkhili (**)  
  - Amir Staxi (**)  
<p align="center">
  <b>Developed by Team Neuronix</b><br>
  Souleima Gharbi • Maram Zakraoui • Emna Nkhili<br>
  Farah Hassen • Dorra Sioud • Amir Staxi  
</p>
<p align="center">
  <i>🚀 Open-source project advancing SDG 3 (Health) & 9 (Innovation)</i>
</p>
```





