import os
import urllib.request
from uuid import uuid4


def download_face_data(data, path):
    try:
        print("🟢 Downloading face data... 📥")
        image_path_and_label_pair = []
        known_faces = data['known']
        unknown_face = data['unknown']
        image_urls = [item["image_url"] for item in known_faces]
        labels = [item["label"] for item in known_faces]

        for i, url in enumerate(image_urls):
            path_to_image = os.path.join(path, f"{uuid4()}.jpg")
            urllib.request.urlretrieve(url, path_to_image)
            image_path_and_label_pair.append(
                {'image_path': path_to_image, 'label': labels[i]})

        path_to_unknown_image = os.path.join(path, f"{uuid4()}.jpg")
        urllib.request.urlretrieve(unknown_face, path_to_unknown_image)

        return image_path_and_label_pair, path_to_unknown_image

    except Exception as e:
        print(e)
        print("Error: Could not download face data")
        return None, None
