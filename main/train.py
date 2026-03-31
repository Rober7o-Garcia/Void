from ultralytics import YOLO

model = YOLO("yolov8n-cls.pt")

model.train(
    data="dataset",  # carpeta raíz
    epochs=50,
    imgsz=224,
    name="clasificador_animales"
)

model = YOLO("runs/classify/clasificador_animales/weights/best.pt")

results = model("imagen.jpg")
print(results[0].probs)