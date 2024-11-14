import os
from rembg import remove
from PIL import Image
import io

# Directorio de imágenes de entrada y salida
input_dir = 'carpetaEntrada'
output_dir = 'carpetaSalida'

# Asegúrate de que la carpeta de salida exista
os.makedirs(output_dir, exist_ok=True)

# Procesa cada imagen en la carpeta de entrada
for filename in os.listdir(input_dir):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
        input_path = os.path.join(input_dir, filename)
        output_path = os.path.join(output_dir, f"sin_fondo_{os.path.splitext(filename)[0]}.png")  # Guarda como PNG
        
        with open(input_path, 'rb') as input_file:
            image_data = input_file.read()
            output_data = remove(image_data)  # Elimina el fondo
            
            # Convierte los datos de la imagen sin fondo a formato PNG y guarda
            output_image = Image.open(io.BytesIO(output_data)).convert("RGBA")
            output_image.save(output_path, format="PNG")

print("¡Proceso completo! Las imágenes sin fondo están en la carpeta de salida.")
