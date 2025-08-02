from sentence_transformers import SentenceTransformer
from transformers import CLIPProcessor, CLIPModel
import torch

text_model = SentenceTransformer('all-MiniLM-L6-v2')
clip_model = CLIPModel.from_pretrained("openai/clip-vit-base-patch16")
clip_processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch16")

def embed_text(text):
    return text_model.encode([text])[0]

def embed_image(image):
    inputs = clip_processor(images=image, return_tensors="pt")
    with torch.no_grad():
        outputs = clip_model.get_image_features(**inputs)
    return outputs[0].cpu().numpy()
