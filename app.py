import streamlit as st
from modules.data_loader import load_geo_features
from modules.retrieval import spatial_rag_query
import faiss
import pandas as pd

st.set_page_config(layout="wide")
st.title("🗺️ Geographic RAG: Spatial & Semantic Retrieval Demo")

with st.sidebar:
    st.header("Query Parameters")
    lon = st.number_input("Longitude", value=77.5946, format="%.6f")
    lat = st.number_input("Latitude", value=12.9716, format="%.6f")
    radius = st.slider("Radius (km)", 1, 20, 3)

gdf = load_geo_features()
faiss_index = faiss.read_index('db/faiss_index.idx')
all_texts = list(gdf['description'])

st.markdown("**Example query:** `Find parks within 2km of city hall`")
query = st.text_input("Ask your spatial query:")

if st.button("Search") and query:
    result = spatial_rag_query(gdf, query, (lon, lat), radius, faiss_index, all_texts)
    st.markdown("### Response")
    st.write(result["response"])
    
    if result["context"]:
        st.markdown("**Relevant Context:**")
        for c in result["context"]:
            st.info(c)

    spatial_gdf = result.get("spatial_features")
    if spatial_gdf is not None and not spatial_gdf.empty:
        # Extract lon/lat from geometry column
        mapped_df = spatial_gdf.copy()
        mapped_df["lon"] = mapped_df.geometry.x
        mapped_df["lat"] = mapped_df.geometry.y

        # Streamlit map expects columns like 'lat' and 'lon'
        st.map(mapped_df[["lat", "lon"]])
    else:
        st.write("No spatial features to map.")

    if result.get("fallback"):
        st.warning(f"No hybrid spatial+semantic match, fallback used: {result['fallback']}.")
