import face_recognition


def recognize_face_in_image(img_path_and_label_pairs, unknown_img_path):
    try:
        print("🟢 Recognizing face in image... 📷")
        # FACE ENCODINGS DE LAS IMAGENES CONOCIDAS
        known_faces = []

        for img_path_and_label_pair in img_path_and_label_pairs:
            img_path = img_path_and_label_pair["img_path"]
            known_img = face_recognition.load_image_file(img_path)
            known_face_encoding = face_recognition.face_encodings(known_img)[0]
            known_faces.append(known_face_encoding)

    # FACE ENCODING DE LA IMAGEN DESCONOCIDA
        unknown_img = face_recognition.load_image_file(unknown_img_path)
        unknown_face_encoding = face_recognition.face_encodings(unknown_img)[0]

    # COMPARACION DE LAS IMAGENES
        results = face_recognition.compare_faces(
            known_faces, unknown_face_encoding)

        for i in range(len(results)):
            if results[i]:
                return img_path_and_label_pairs[i]["label"]

        return None
    except Exception as e:
        print(e)
        return False
