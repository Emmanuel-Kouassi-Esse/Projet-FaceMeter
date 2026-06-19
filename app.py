import streamlit as st
import cv2
import numpy as np
from uniface import FaceAnalyzer, RetinaFace, AgeGender

# Initialisation
analyzer = FaceAnalyzer(detector=RetinaFace(), attributes=[AgeGender()])

st.title("FaceMeter - Estimation Âge & Genre")

# Upload d'une photo
uploaded = st.file_uploader("Choisissez une photo")
if uploaded:
    file_bytes = np.asarray(bytearray(uploaded.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, 1)
    faces = analyzer.analyze(image)
    for face in faces:
        st.write(f"Genre : {face.sex}, Âge : {face.age} ans")

# Capture en temps réel avec webcam
camera_photo = st.camera_input("📸 Prendre une photo en direct")
if camera_photo:
    file_bytes = np.asarray(bytearray(camera_photo.getvalue()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, 1)
    faces = analyzer.analyze(image)
    for face in faces:
        st.write(f"Genre : {face.sex}, Âge : {face.age} ans")
