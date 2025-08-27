# src/api.py
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import FileResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import cv2
import numpy as np
import os
import uuid
from datetime import datetime

# Import our damage detector
from .damage_detector import DamageDetector

# Initialize FastAPI app
app = FastAPI(title="AutoGrade AI API", version="1.0.0")

# Add CORS middleware to allow frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize the damage detector
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(PROJECT_ROOT, 'models', 'car_damage_v1', 'weights', 'best.pt')
detector = DamageDetector(model_path=MODEL_PATH)

# Create directories for uploads and results
UPLOAD_DIR = os.path.join(PROJECT_ROOT, "data", "uploads")
RESULTS_DIR = os.path.join(PROJECT_ROOT, "data", "api_results")
os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(RESULTS_DIR, exist_ok=True)

@app.get("/")
async def root():
    return {"message": "Midzar AutoGrade AI API", "status": "active", "version": "1.0.0"}

@app.post("/analyze-vehicle/")
async def analyze_vehicle(file: UploadFile = File(...)):
    """
    Analyze a vehicle image for damage detection.
    Accepts an image file and returns analysis results.
    """
    try:
        # Validate file type
        if not file.content_type.startswith('image/'):
            raise HTTPException(status_code=400, detail="File must be an image")
        
        # Generate unique filename
        file_extension = os.path.splitext(file.filename)[1]
        unique_id = str(uuid.uuid4())
        input_filename = f"upload_{unique_id}{file_extension}"
        output_filename = f"result_{unique_id}.jpg"
        
        # Save uploaded file
        input_path = os.path.join(UPLOAD_DIR, input_filename)
        output_path = os.path.join(RESULTS_DIR, output_filename)
        
        # Read and save the uploaded image
        contents = await file.read()
        nparr = np.frombuffer(contents, np.uint8)
        image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        
        if image is None:
            raise HTTPException(status_code=400, detail="Invalid image file")
        
        cv2.imwrite(input_path, image)
        
        # Perform damage detection
        results, annotated_image = detector.analyze_image(input_path)
        
        # Process results
        detections = []
        for result in results:
            for box in result.boxes:
                class_id = int(box.cls)
                confidence = float(box.conf)
                label = result.names[class_id]
                
                # Get bounding box coordinates (x1, y1, x2, y2)
                x1, y1, x2, y2 = box.xyxy[0].tolist()
                
                detections.append({
                    "label": label,
                    "confidence": round(confidence, 3),
                    "bbox": [round(x1, 1), round(y1, 1), round(x2, 1), round(y2, 1)]
                })
        
        # Save annotated result
        cv2.imwrite(output_path, annotated_image)
        
        # Prepare response
        response = {
            "success": True,
            "request_id": unique_id,
            "timestamp": datetime.now().isoformat(),
            "detections": detections,
            "summary": {
                "total_damage_found": len(detections),
                "damage_types": list(set([d["label"] for d in detections]))
            },
            "results": {
                "annotated_image_url": f"/results/{output_filename}",
                "original_image_url": f"/uploads/{input_filename}"
            }
        }
        
        return JSONResponse(content=response)
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Processing error: {str(e)}")

@app.get("/results/{filename}")
async def get_result(filename: str):
    """Serve annotated result images"""
    file_path = os.path.join(RESULTS_DIR, filename)
    if os.path.exists(file_path):
        return FileResponse(file_path)
    raise HTTPException(status_code=404, detail="File not found")

@app.get("/uploads/{filename}")
async def get_upload(filename: str):
    """Serve original uploaded images"""
    file_path = os.path.join(UPLOAD_DIR, filename)
    if os.path.exists(file_path):
        return FileResponse(file_path)
    raise HTTPException(status_code=404, detail="File not found")

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "timestamp": datetime.now().isoformat()}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)