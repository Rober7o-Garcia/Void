from django.shortcuts import render
from ultralytics import YOLO
import os
from django.core.files.storage import FileSystemStorage

model = YOLO("runs/classify/clasificador_animales/weights/best.pt")

def upload(request):
    if request.method == 'POST' and request.FILES.get('file'):
        uploaded_file = request.FILES['file']
        
        fs = FileSystemStorage()
        filename = fs.save(uploaded_file.name, uploaded_file)
        file_path = fs.path(filename)   # 👈 IMPORTANTE (ruta real)
        file_url = fs.url(filename)

        # 🔥 usar la imagen subida
        clase, precision = predecir_imagen(file_path)

        return render(request, 'main/upload.html', {
            'uploaded_file_url': file_url,
            'clase': clase,
            'precision': f"{precision:.4f}",
            'success': True
        })

    return render(request, 'main/upload.html')


def predecir_imagen(ruta_imagen):
    results = model(ruta_imagen)

    clase = results[0].names[results[0].probs.top1]
    precision = float(results[0].probs.top1conf)

    return clase, precision