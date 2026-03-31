from django.shortcuts import render
from ultralytics import YOLO
import os

model = YOLO("yolov8n.pt")

def detectar(request):
    if request.method == "POST" and request.FILES.get("imagen"):
        imagen = request.FILES["imagen"]

        ruta = os.path.join("media", imagen.name)

        with open(ruta, "wb+") as f:
            for chunk in imagen.chunks():
                f.write(chunk)

        results = model(ruta)
        results[0].save(filename=ruta)

        return render(request, "resultado.html", {"imagen": ruta})

    return render(request, "subir.html")