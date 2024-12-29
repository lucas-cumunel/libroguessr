import os
import s3fs

fs = s3fs.S3FileSystem(client_kwargs={"endpoint_url": "https://minio.lab.sspcloud.fr"})

# Variables
MY_BUCKET = "arnaudbrrt"  
LOCAL_FOLDER = "libroguessr/Data" 
S3_FOLDER = f"{MY_BUCKET}/Data"  

# Parcourir tous les fichiers du dossier local
for root, dirs, files in os.walk(LOCAL_FOLDER):
    for file in files:
        # Construire les chemins local et S3
        local_path = os.path.join(root, file)  # Chemin complet du fichier local
        relative_path = os.path.relpath(local_path, LOCAL_FOLDER)  # Chemin relatif au dossier local
        s3_path = f"{S3_FOLDER}/{relative_path}"  # Chemin complet dans S3

        # Upload du fichier vers S3
        with fs.open(s3_path, "w") as file_out:
            with open(local_path, "rb") as file_in:  # Lire en mode binaire pour tout type de fichier
                file_out.write(file_in.read())
        print(f"Fichier {file} uploadé vers {s3_path}.")
