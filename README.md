
# 🐾 Milo Vet Care - AI-Powered Veterinary Assistance  
*Bridging the veterinary care gap in rural Tunisia with AI*  

<p align="center">
  <img alt="Accuracy" src="https://img.shields.io/badge/Disease_Detection-97%25_Accuracy-brightgreen">
  <img alt="SDGs" src="https://img.shields.io/badge/SDGs-3%2C9%2C15%2C17-blue">
  <img alt="XAI" src="https://img.shields.io/badge/Explainability-Grad--CAM%2C_LIME-success">
  <img alt="Data" src="https://img.shields.io/badge/Datasets-7.8K_Images-orange">
</p>

## 📌 Problem Statement  
**"No pet should suffer just because a vet is too far away."**  
- 40% veterinary coverage in rural Tunisia  
- 70% of pet owners delay care until emergencies  
- 76% rural pet ownership with limited diagnostic access  

## ✨ Solution Overview  
**AI-Powered Mobile Application Featuring:**  

| Module | Technology | Accuracy |  
|--------|------------|----------|  
| **1. Species Classification** | Custom CNN/ResNet50 | 89.9% |  
| **2. Symptom Diagnosis** | Llama3 + FAISS | 95% (vet-validated) |  
| **3. Disease Detection** | ResNet50 | 97% (dog skin) |  
| **4. X-Ray Analysis** | EfficientNet_B0 | 87% (cardiac) |  
| **5. Treatment Recommendations** | Gemma-3 RAG | Confidence-scored |  

## 🛠️ Technical Deep Dive  

### 🔍 Core Architectures  
**1. Animal Classification**  
```python
# Custom CNN Architecture (VGG-inspired)
Conv(3x3) → BatchNorm → ReLU → MaxPool  
Flatten → FC512 (Dropout 30%) → FC256 → Softmax
```
- **Optimizer:** Adam with LR scheduler  
- **Best Model:** ResNet50 (89.9% test accuracy)  

**2. RAG Pipeline (Treatment Recommendations)**  
```
[PDFs/Web Data]  
↓  
RecursiveCharacterTextSplitter (1000 tokens)  
↓  
bge-small-en-v1.5 Embeddings  
↓  
FAISS Similarity Search (Cosine, k=3)  
↓  
Gemma-3-4B-IT Generation (temp=0.7)  
```
- **Confidence Thresholds:**  
  - ✅ >0.8: Peer-reviewed sources  
  - ⚠️ 0.4-0.8: Clinical guidelines  
  - ❌ <0.4: Filtered out  

### 📊 Performance Metrics  
| Task | Model | Metric |  
|------|-------|--------|  
| Species ID | EfficientNet | 74% acc |  
| Dog Skin Disease | ResNet50 | 97% acc |  
| Cardiac Analysis | EfficientNet_B0 | 87% val_acc |  
| Symptom QA | Llama3 | 95% vet-approved |  

## 🌍 Real-World Impact  
**Validated with Ariana Veterinary Clinic (Dr. Abid Olfa):**  
- 95% accurate disease detection on annotated X-rays  
- Clinical FAQ integration for rural vets  
- Supports 37 animal species  

**SDG Alignment:**  
- 🩺 **SDG 3:** Prevents zoonotic diseases  
- 💡 **SDG 9:** Tech innovation in animal healthcare  
- 🐕 **SDG 15:** Improves domestic animal welfare  
- 🤝 **SDG 17:** Clinic partnerships  

## 🚀 Getting Started  

### Prerequisites  
```bash
Python 3.8+  
Ollama (for local Llama3)  
GPU-enabled environment  
```

### Installation  
```bash
git clone https://github.com/yourrepo/milovetcare  
cd milovetcare  
pip install -r requirements.txt  
```

### Run Demo  
```python
python src/demo.py --image="pet_xray.jpg" --mode=cardiac
```

## 📂 Repository Structure  
```
milovetcare/  
├── models/               # Pretrained weights  
│   ├── species_classifier.h5  
│   └── cardiac_efficientnet.pt  
├── data/                 # Sample datasets  
│   ├── dog_skin/ (7 classes)  
│   └── xrays/ (cardiac)  
└── src/  
    ├── rag_pipeline.py   # Treatment recommendations  
    ├── grad_cam.py       # XAI visualization  
    └── mobile_app/       # Flutter interface  
```

## 💡 Why This Matters  
*"Our beta test showed 68% reduction in emergency visits through early AI detection."*  
- **Transparent AI:** Grad-CAM highlights decision regions  
- **Localized:** Optimized for Tunisian rural constraints  
- **Vet-Approved:** 95% clinical validation accuracy  

<p align="center">
  <b>Developed by Team Neuronix</b><br>
  Farah | Souleima | Emna | Maram | Dorra | Amir  
</p>
```

### Key Features:
1. **Clinical Validation Badges** - Immediate visibility of 97% accuracy
2. **Architecture Diagrams** - Clear code blocks showing model layers
3. **SDG Icons** - Visual UN goal alignment
4. **Structured Commands** - Ready-to-copy installation steps
5. **Confidence Thresholds** - Transparent scoring system for recommendations
6. **Team Recognition** - Proper contributor credits

