# 🐾 Milo Vet Care - AI-Powered Veterinary Assistance

<p align="center">
  <b>Bridging the veterinary care gap in rural Tunisia with AI</b><br>
  <i>Neuronix Team Project | Partnered with Ariana Veterinary Clinic</i>
</p>

<p align="center">
  <img alt="AI Accuracy" src="https://img.shields.io/badge/Disease_Detection-97%25_Accuracy-brightgreen">
  <img alt="SDGs" src="https://img.shields.io/badge/SDGs-3%2C9%2C15%2C17-blue">
  <img alt="XAI" src="https://img.shields.io/badge/Explainability-Grad--CAM%2C_LIME-success">
  <img alt="Data" src="https://img.shields.io/badge/Datasets-7.8K_Images-orange">
</p>

---

## 📌 Project Overview
**Problem:** 40% vet coverage in rural Tunisia, with 70% of pet owners delaying care until emergencies.

**Solution:** Mobile AI application providing:
- Breed classification (37 species)
- Disease detection (95% accuracy on X-rays)
- Symptom-to-diagnosis assistance
- Treatment recommendations via RAG
- X-ray cardiac analysis (87% accuracy)

---

## ✨ Core Modules

### 1. Animal Species Classification
- **Models:** Custom CNN (71% accuracy), ResNet50 (89.9%), EfficientNet (74%)
- **Pipeline:**
  ```python
  Conv → BatchNorm → ReLU → MaxPooling → [512 FC + Dropout] → [256 FC] → Softmax
Optimizer: Adam with LR scheduler

Hardware: GPU accelerated

2. Symptom-to-Diagnosis Assistant
Tech Stack:

Embeddings: MiniLM-L6-v2 (lightweight, efficient)

Retrieval: FAISS similarity search

LLM: Llama3 via Ollama (local deployment)

Sample Output:

plaintext
Symptoms: Vomiting + Diarrhea → Probable Diagnosis: Parasitic infection
Urgency Level: High (risk of dehydration)
3. Breed-Specific Recommendations (RAG System)
Data: 209 breeds with health profiles

Pipeline:

PDFs/HTML → RecursiveCharacterTextSplitter → bge-small-en-v1.5 → FAISS → Gemma-3-4B-IT
Confidence Scoring:

plaintext
Golden Retriever Results:
[90%] AKC Breeding Guidelines 
[81%] Veterinary Dermatology Study
4. Animal Disease Detection
Performance:

Dog skin diseases: 97% test accuracy (7 classes, 4.6K images)

Cat skin diseases: 95% accuracy (8 classes, 3.2K images)

Model: ResNet50 → 256 FC → LogSoftmax

Loss: NLLLoss

Optimizer: Adam (LR=0.001)

5. X-Ray Heart Disease Detection
Datasets:

Veterinary partnership X-rays

Mendeley cardiac dataset

Best Model: EfficientNet_B0 (87% val accuracy)

Output Example:

plaintext
Grad-CAM Detection: Cardiomegaly → Recommendation: 
"Start ACE inhibitors. Refer for echocardiography."
🛠️ Technical Implementation
Key Architectural Choices
Component	Selection	Rationale
Embeddings	MiniLM-L6-v2 vs BGE-small	Balance of speed (91MB) & accuracy
LLM	Llama3/Gemma-3	Local deployability & multilingual support
Retrieval	FAISS	Fast similarity search for embeddings
XAI	Grad-CAM + LIME	Model interpretability for vet trust
Performance Metrics
Species Classification: EfficientNet achieved 74% with Grad-CAM explainability

Disease Detection: ResNet50 reached 97% accuracy (dogs)

Cardiac Analysis: EfficientNet_B0 - 87% validation accuracy

🌍 Impact on SDGs
SDG 3: Improved animal health → reduced zoonotic diseases

SDG 9: Tech innovation in veterinary care

SDG 15: Better domestic animal welfare

SDG 17: Partnership with Ariana Veterinary Clinic

📂 Repository Structure
milovetcare/
├── /models/               # Pretrained model weights
│   ├── species_classifier/
│   ├── disease_detection/
│   └── cardiac_analysis/
├── /data/                 # Sample datasets
├── /src/                  # Core application code
│   ├── rag_pipeline.py    # Recommendation system
│   ├── grad_cam.py        # XAI visualization
│   └── mobile_app/        # Flutter implementation
└── /partnerships/         # Veterinary collaboration docs
🚀 Getting Started
Prerequisites:

bash
Python 3.8+, Ollama, GPU-enabled environment
Install dependencies:

bash
pip install -r requirements.txt
Run demo:

bash
python src/demo_pipeline.py --image_path="sample_xray.jpg"
<p align="center"> <b>Developed with ❤️ by Team Neuronix</b><br> Farah | Souleima | Emna | Maram  | Dorra | Amir </p> ```
