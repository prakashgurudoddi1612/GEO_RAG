import geopandas as gpd
import os
from PIL import Image

def load_geo_features(path='data/geo_features.geojson'):
    return gpd.read_file(path)

def load_sat_images(directory='data/satellite/'):
    images = {}
    for fname in os.listdir(directory):
        if fname.endswith(('.png', '.jpg', '.jpeg', '.tif')):
            images[fname] = Image.open(os.path.join(directory, fname))
    return images
