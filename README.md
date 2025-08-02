# 🌍 GEO_RAG – Geographic Information Retrieval-Augmented Generation System

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Status](https://img.shields.io/badge/status-Active-brightgreen)

> A powerful Retrieval-Augmented Generation (RAG) system that integrates geographic data, satellite imagery, and location-specific context to deliver intelligent spatial query responses.

---

## 🚀 Deployment

🌐 **Live Demo**: [Click here to try it out]([https://your-deployment-link.com](https://georag-geazkvkcfd59vznr34mvcb.streamlit.app/))

> Replace the above link with your actual deployment URL once it's live.

---

## 🧠 Features

- 🔍 **Natural Language Geographic Query Support**
- 🗺️ **Integration with Satellite Imagery**
- 📚 **Vector Store using FAISS**
- 🧾 **Document Retrieval from GeoJSON / CSV / External Sources**
- 🤖 **RAG-powered Answer Generation using OpenAI/GPT**
- 📍 **Geospatial Reasoning and Contextual Answers**
- 🖼️ **Image and Map Embedding with Results**

---

## 🛠️ Technologies Used

- Python 3.10+
- **LangChain**, **FAISS**, **OpenAI GPT**
- **Streamlit** for UI
- **Geopandas**, **Shapely**, **Folium** for geospatial operations
- **Matplotlib**, **Pillow**, **OpenCV** for image visualization
- Git + GitHub for version control

---

## 📁 Project Structure

geo_rag/
├── app.py # Main Streamlit app
├── geo_utils.py # Geospatial processing functions
├── rag_engine.py # Core RAG pipeline
├── embeddings/ # Embedding generation & FAISS index
├── satellite_images/ # Satellite data preprocessing
├── data/ # GeoJSON/CSV files
├── requirements.txt
└── README.md

yaml
Copy
Edit

---

## 🧪 Setup Instructions

```bash
# Clone the repository
git clone https://github.com/prakashgurudoddi1612/GEO_RAG.git
cd GEO_RAG

# Create virtual environment
python -m venv venv
venv\Scripts\activate    # On Windows

# Install dependencies
pip install -r requirements.txt

# Run the application
streamlit run app.py
⚠️ Notes
Do NOT commit the venv/ folder or large model binaries (e.g., .dll, .lib, .pt files).

If needed, configure .gitignore like:

bash
Copy
Edit
venv/
__pycache__/
*.dll
*.lib
*.pt
*.ckpt
*.h5
🙋‍♂️ Author
👤 Guru Prakash

GitHub: @prakashgurudoddi1612

LinkedIn: LinkedIn Profile

📄 License
This project is licensed under the MIT License. See the LICENSE file for more details.

yaml
Copy
Edit

---

Let me know if you want me to include badges for build, deployment status, or if you're deploying via

