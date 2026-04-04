from ultralytics import YOLO

model = YOLO("runs/classify/clasificador_animales/weights/best.pt")

results = model("media/caballo.jpg")

clase = results[0].names[results[0].probs.top1]
precision = results[0].probs.top1conf

print(f"Predicción: {clase}")
print(f"Precisión: {precision:.4f}") 