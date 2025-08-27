# src/train_model.py
from ultralytics import YOLO
import os

# Get the absolute path to the project root
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def train_damage_detector():
    # Load a pre-trained YOLO model (using a larger 'small' model for better accuracy)
    model = YOLO('yolov8s.pt')
    
    # Path to the data configuration file from the downloaded dataset
    data_config_path = os.path.join(PROJECT_ROOT, 'data', 'car-damage-dataset', 'data.yaml')
    
    # Check if the data.yaml file exists
    if not os.path.exists(data_config_path):
        print(f"❌ ERROR: Data config file not found at {data_config_path}")
        print("Please make sure you've downloaded and placed the dataset correctly.")
        return
    
    # Train the model
    results = model.train(
        data=data_config_path,  # path to the data.yaml file
        epochs=50,              # number of training epochs
        imgsz=640,              # image size
        batch=8,                # batch size (reduce if you run out of GPU memory)
        device=0,
        name='car_damage_v1',   # name of the training run
        project=os.path.join(PROJECT_ROOT, 'models'),  # save location
    )
    
    print("✅ Training completed!")

if __name__ == '__main__':
    train_damage_detector()