from .embedder import embed_image

def get_image_features(images):
    features = {}
    for name, img in images.items():
        features[name] = embed_image(img)
    return features
