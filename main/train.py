from ultralytics import YOLO
import torch

def main():
    print(torch.cuda.is_available())

    model = YOLO("yolov8n-cls.pt")

    model.train(
        data="dataset",
        epochs=30,
        imgsz=224,
        name="clasificador_animales"
    )

    model = YOLO("runs/classify/clasificador_animales2/weights/best.pt")

if __name__ == "__main__":
    main()