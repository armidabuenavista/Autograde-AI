# src/damage_detector.py
from ultralytics import YOLO
import cv2
import os

# Get the absolute path to the project root directory
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class DamageDetector:
    def __init__(self, model_path):
        # Load the specified model
        self.model = YOLO(model_path)
        print(f"✅ Loaded model: {model_path}")

    def analyze_image(self, image_path):
        """
        Runs prediction on a single image.
        Returns: results object, annotated image array
        """
        # Perform prediction
        results = self.model.predict(source=image_path, conf=0.3, save=False, verbose=False)  # Lower confidence threshold
        # Annotate the image with predictions
        annotated_frame = results[0].plot()
        return results, annotated_frame

    def save_annotated_image(self, annotated_array, output_path):
        """Saves an annotated image from an array to the specified path."""
        cv2.imwrite(output_path, annotated_array)

# Example usage for testing
if __name__ == "__main__":
    detector = DamageDetector()
    
    # Use absolute path to ensure we find the image
    test_image_path = os.path.join(PROJECT_ROOT, "data", "raw", "test_car.jpg")
    print(f"Looking for image at: {test_image_path}")
    
    # Check if test image exists
    if not os.path.exists(test_image_path):
        print(f"Test image not found at {test_image_path}. Please add a image first.")
        # Show what files are actually in the directory
        raw_dir = os.path.join(PROJECT_ROOT, "data", "raw")
        if os.path.exists(raw_dir):
            print(f"Files in {raw_dir}:")
            for file in os.listdir(raw_dir):
                print(f"  - {file}")
        else:
            print(f"Directory {raw_dir} does not exist!")
    else:
        results, annotated_img = detector.analyze_image(test_image_path)
        
        # Print results
        for result in results:
            print(f"Detected {len(result.boxes)} objects:")
            for box in result.boxes:
                class_id = int(box.cls)
                confidence = float(box.conf)
                label = result.names[class_id]
                print(f"- {label} with confidence {confidence:.2f}")
        
        # Save the annotated image
        output_path = os.path.join(PROJECT_ROOT, "data", "processed", "annotated_test.jpg")
        detector.save_annotated_image(annotated_img, output_path)
        print(f"Annotated image saved to {output_path}")