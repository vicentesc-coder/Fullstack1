from PIL import Image
import os
from pathlib import Path

# Carpeta con las imágenes
carpeta_imagenes = r"C:\Users\sando\Documents\carpetita\tickets\IMAGENES POSTMAN"

# Obtener lista de imágenes ordenadas por fecha
imagenes = sorted([f for f in os.listdir(carpeta_imagenes) if f.endswith('.png')])

if not imagenes:
    print("No se encontraron imágenes PNG")
    exit(1)

# Convertir a rutas completas
rutas_imagenes = [os.path.join(carpeta_imagenes, img) for img in imagenes]

# Abrir todas las imágenes como PIL Image
pil_imagenes = []
for ruta in rutas_imagenes:
    img = Image.open(ruta).convert('RGB')
    pil_imagenes.append(img)
    print(f"Cargada: {os.path.basename(ruta)}")

# Crear PDF
ruta_pdf = os.path.join(carpeta_imagenes, "Postman_Screenshots.pdf")
pil_imagenes[0].save(
    ruta_pdf,
    save_all=True,
    append_images=pil_imagenes[1:],
    optimize=False
)

print(f"\n✓ PDF generado exitosamente: {ruta_pdf}")
print(f"  Total de imágenes: {len(pil_imagenes)}")
