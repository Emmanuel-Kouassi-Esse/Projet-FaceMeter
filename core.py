import cv2
import pandas as pd
from sklearn.metrics import mean_absolute_error, accuracy_score
from uniface import FaceAnalyzer, RetinaFace, AgeGender

# Initialisation du modèle
analyzer = FaceAnalyzer(detector=RetinaFace(), attributes=[AgeGender()])

# Charger labels.csv
labels = pd.read_csv("labels.csv")

results = []

for _, row in labels.iterrows():
    image_path = f"dataset/{row['filename']}"
    image = cv2.imread(image_path)

    if image is None:
        print(f"⚠️ Erreur : impossible de charger {image_path}")
        continue

    faces = analyzer.analyze(image)
    if faces:
        face = faces[0]
        results.append({
            "filename": row['filename'],
            "true_age": row['age'],
            "pred_age": face.age,
            "true_gender": row['gender'],
            "pred_gender": face.sex
        })

# Vérifier si on a des résultats
if results:
    df = pd.DataFrame(results)
    df.to_csv("results.csv", index=False)

    mae = mean_absolute_error(df['true_age'], df['pred_age'])
    acc = accuracy_score(df['true_gender'], df['pred_gender'])

    print("📊 Résultats de validation")
    print("Erreur moyenne absolue (MAE) âge :", mae)
    print("Précision genre :", acc)
else:
    print("⚠️ Aucun visage analysé, vérifie tes fichiers dataset/ et labels.csv")
