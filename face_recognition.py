import face_recognition
import os
import shutil

# Specify the folder path
folder_path = 'C:\\Users\\mdasi\\Pictures\\Iqoo\\TheFolder\\Image'
no_face_folder_path = 'C:\\Users\\mdasi\\Pictures\\Iqoo\\TheFolder\\NoFace'

# Create the no face folder if it doesn't exist
if not os.path.exists(no_face_folder_path):
    os.makedirs(no_face_folder_path)
    
# Load all images from the folder
image_paths = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith(('.jpg', '.jpeg', '.png', '.bmp'))]

# Create a dictionary to store the face encodings
face_encodings = {}

# Process each image
for image_path in image_paths:
    # Load the image
    image = face_recognition.load_image_file(image_path)

    # Extract the face encoding
    face_encoding = face_recognition.face_encodings(image)
    if len(face_encoding) > 0:
        face_encoding = face_encoding[0]
    else:
        # Move the image to the no face folder
        shutil.move(image_path, no_face_folder_path)
        print(f"Moved {image_path} to {no_face_folder_path} as it contains no face.")

    # Add the face encoding to the dictionary
    face_encodings[image_path] = face_encoding

# Group similar faces together
clusters = {}
for image_path, face_encoding in face_encodings.items():
    # Compare the face encoding with existing clusters
    for cluster, cluster_encoding in clusters.items():
        if face_recognition.compare_faces([cluster_encoding], face_encoding, tolerance=0.5):
            # Add the image to the existing cluster
            clusters[cluster].append(image_path)
            break
    else:
        # Create a new cluster
        clusters[image_path] = [image_path]

# Create folders for each cluster
cluster_folder_path = 'C:\\Users\\mdasi\\Pictures\\Iqoo\\TheFolder\\Clusters'
os.makedirs(cluster_folder_path, exist_ok=True)
cluster_id = 1
for cluster, image_paths in clusters.items():
    cluster_folder = os.path.join(cluster_folder_path, f'Cluster_{cluster_id}')
    os.makedirs(cluster_folder, exist_ok=True)
    for image_path in image_paths:
        # Move the image to the corresponding cluster folder
        shutil.move(image_path, os.path.join(cluster_folder, os.path.basename(image_path)))
    cluster_id += 1