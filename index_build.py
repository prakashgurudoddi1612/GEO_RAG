import os
from modules.data_loader import load_geo_features
from modules.embedder import embed_text
import faiss
import numpy as np

os.makedirs("db", exist_ok=True)
gdf = load_geo_features()
descs = list(gdf['description'])
embeddings = np.array([embed_text(t) for t in descs]).astype('float32')
index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(embeddings)
faiss.write_index(index, 'db/faiss_index.idx')
print("FAISS index built and saved to db/faiss_index.idx")
