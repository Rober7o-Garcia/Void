from django.shortcuts import render
from ultralytics import YOLO
import os
from django.core.files.storage import FileSystemStorage

model = YOLO("yolov8n.pt")


def upload(request):
    if request.method == 'POST':
        print("--- Intento de POST detectado ---")
        print(f"Archivos recibidos: {request.FILES}") # Esto debe mostrar <MultiValueDict: {'file': [...]}>

        if request.FILES.get('file'):
            uploaded_file = request.FILES['file']
            
            # Guardamos
            fs = FileSystemStorage()
            filename = fs.save(uploaded_file.name, uploaded_file)
            uploaded_file_url = fs.url(filename)
            
            print(f"¡Archivo guardado en: {filename}!")
            
            # NOTA: Asegúrate de que la ruta del template sea la correcta (main/upload.html)
            return render(request, 'main/upload.html', {
                'uploaded_file_url': uploaded_file_url,
                'success': True
            })
        else:
            print("Error: No se encontró ningún archivo con la llave 'file'")

    return render(request, 'main/upload.html')


def detectar(request):
    pass