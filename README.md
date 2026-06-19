# 🎯 Projet-FaceMeter

## 📌 Objectif
FaceMeter est une application basée sur **UniFace** qui permet d’estimer en temps réel l’**âge** et le **genre** d’un visage capturé par webcam ou via une photo uploadée.

---

## 🛠️ Technologies
- Python 3.10+
- [Streamlit](https://streamlit.io/) → interface web interactive
- [OpenCV](https://opencv.org/) → traitement d’images
- [UniFace](https://github.com/serengil/uniface) → analyse faciale (RetinaFace + AgeGender)
- NumPy, Pandas, Scikit-learn

---

## 🚀 Installation locale

1. **Cloner le dépôt**
   ```bash
   git clone https://github.com/Emmanuel-Kouassi-Esse/Projet-FaceMeter.git
   cd Projet-FaceMeter
Créer un environnement virtuel

bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
Installer les dépendances

bash
pip install -r requirements.txt
Lancer l’application

bash
streamlit run app.py
👉 L’interface s’ouvre dans ton navigateur à l’adresse : http://localhost:8501

📂 Structure du projet
core.py → script d’analyse faciale (validation sur dataset)

app.py → interface Streamlit (upload photo + webcam)

requirements.txt → dépendances

README.md → documentation

🌐 Déploiement sur Streamlit Cloud
Pousser le projet sur GitHub

bash
git add .
git commit -m "Initialisation du projet FaceMeter"
git push origin main
Aller sur Streamlit Cloud

Cliquer sur New app

Sélectionner ton dépôt Emmanuel-Kouassi-Esse/Projet-FaceMeter

Choisir la branche main et le fichier app.py

Cliquer sur Deploy

URL publique générée automatiquement  
Exemple :

Code
https://emmanuel-kouassi-esse-projet-facemeter.streamlit.app