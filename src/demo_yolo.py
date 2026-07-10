from ultralytics import YOLO

project = "/home/student/k26/k268467/output"
name = "demo_yolo"  

# 2. モデル名を 正しく 'yolov8n.pt' に修正
model = YOLO("yolov8n.pt")  

# 訓練の実行
results = model.train(
    data="coco8.yaml", 
    epochs=100, 
    imgsz=640,
    project=project,
    name=name,        # 3. 上で定義した変数 name を使うように修正
    exist_ok=True     # 既存のフォルダに上書きする設定
)