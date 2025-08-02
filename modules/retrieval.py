import faiss
import numpy as np
from .embedder import embed_text
from .spatial_index import filter_by_radius
from .llm_utils import compose_generation

def search_faiss(query, index, texts, k=5):
    q_emb = embed_text(query).astype('float32')
    D, I = index.search(np.array([q_emb]), k)
    return [texts[i] for i in I[0]]

def spatial_rag_query(gdf, query, location, radius_km, index, texts):
    spatial_df = filter_by_radius(gdf, location[0], location[1], radius_km)
    spatial_texts = list(spatial_df['description'])
    if not spatial_texts:
        return {"response": "No features found in this area.", "context": [], "fallback": "spatial"}
    semantic_matches = search_faiss(query, index, texts)
    hybrid = [t for t in semantic_matches if t in spatial_texts]
    # fallback to spatial or semantic only if hybrid fails
    if not hybrid:
        hybrid = spatial_texts[:3] if spatial_texts else semantic_matches[:3]
        fallback = "semantic" if semantic_matches else "spatial"
    else:
        fallback = None
    answer = compose_generation(hybrid, query)
    return {"response": answer, "context": hybrid, "fallback": fallback, "spatial_features": spatial_df}

