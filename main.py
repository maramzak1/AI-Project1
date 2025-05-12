import io  # <--- Ce module est utilisé pour lire le fichier image en mémoire

from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import torch
from torchvision import transforms
from PIL import Image
import io

# Charger le modèle
model = torch.jit.load("efficientnet_b0_traced.pt")
model.eval()

# Prétraitement
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
])

# FastAPI app
app = FastAPI()

# Autoriser FlutterFlow (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # remplace par ton domaine FlutterFlow si tu veux
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Route pour prédiction
@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    contents = await file.read()
    image = Image.open(io.BytesIO(contents)).convert("RGB")
    input_tensor = transform(image).unsqueeze(0)  # (1, 3, 224, 224)

    with torch.no_grad():
        output = model(input_tensor)
        pred_class = output.argmax(dim=1).item()

    return {"prediction": int(pred_class)}
