<<<<<<< HEAD
# 🚗 AutoGrade AI - Vehicle Damage Detection System

A production-ready AI system for automated vehicle damage detection, built for Webxloo's automotive auction platform.

## ✨ Features
=======
# AutoGrade AI - Vehicle Damage Detection System

A production-ready AI system for automated vehicle damage detection, built for Webxloo's automotive auction platform.

## Features
>>>>>>> 1a924624204542848505d3c1f0ae3f21edcb9101

- **AI-Powered Damage Detection**: YOLOv8 model trained to identify dents, scratches, and other vehicle damage
- **RESTful API**: FastAPI backend with comprehensive endpoints for image analysis
- **Modern Web Interface**: Responsive frontend with drag-and-drop upload and real-time results
- **Dockerized**: Complete containerization for easy deployment
- **Production Ready**: Built with scalability, monitoring, and cloud deployment in mind

<<<<<<< HEAD
## 🏗️ Architecture
=======
## Architecture
>>>>>>> 1a924624204542848505d3c1f0ae3f21edcb9101
autograde-ai/
├── src/ # FastAPI backend
│ ├── api.py # Main API endpoints
│ ├── damage_detector.py # YOLOv8 model integration
│ └── train_model.py # Model training scripts
├── webapp/ # Frontend web application
│ ├── index.html
│ ├── style.css
│ └── script.js
├── models/ # Trained AI models
├── data/ # Datasets and processing directories
├── Dockerfile # Container configuration
└── requirements.txt # Python dependencies


<<<<<<< HEAD
## 🚀 Quick Start
=======
## Quick Start
>>>>>>> 1a924624204542848505d3c1f0ae3f21edcb9101

### Prerequisites
- Python 3.11+
- Docker
- Git

### Local Development

<<<<<<< HEAD
1. **Clone the repository**
   ```bash
=======
1. Clone the repository
>>>>>>> 1a924624204542848505d3c1f0ae3f21edcb9101
   git clone https://github.com/your-username/autograde-ai.git
   cd autograde-ai

2. Install dependencies   
pip install -r requirements.txt

3. Run the API server
python src/api.py

4. Run the web interface
cd webapp
python -m http.server 3000

5. Open in browser: http://localhost:3000

Docker Deployment
# Build the image
docker build -t autograde-ai .

# Run the container
docker run -p 8000:8000 autograde-ai

<<<<<<< HEAD
# 📚 API Documentation
=======
# API Documentation
>>>>>>> 1a924624204542848505d3c1f0ae3f21edcb9101
Once running, access the interactive API docs at: http://localhost:8000/docs

# Endpoints
POST /analyze-vehicle/ - Analyze vehicle images for damage
GET /health - Health check endpoint
GET /results/{filename} - Retrieve analyzed images
GET /uploads/{filename} - Retrieve original uploads

<<<<<<< HEAD
# 🛠️ Technologies Used
=======
# 🛠Technologies Used
>>>>>>> 1a924624204542848505d3c1f0ae3f21edcb9101
Backend: FastAPI, Python, Uvicorn
AI/ML: PyTorch, YOLOv8, Ultralytics
Computer Vision: OpenCV, Pillow
Frontend: HTML5, CSS3, JavaScript (ES6+)
Deployment: Docker, AWS ECR/ECS ready
Monitoring: Built-in FastAPI metrics, ready for Prometheus/Grafana

<<<<<<< HEAD
# 📊 Model Performance
=======
# Model Performance
>>>>>>> 1a924624204542848505d3c1f0ae3f21edcb9101
mAP50: 0.408
Precision: 0.513
Recall: 0.421
Inference Speed: ~29ms per image (on RTX 4090)

<<<<<<< HEAD
Built with ❤️ for the automotive industry

=======
>>>>>>> 1a924624204542848505d3c1f0ae3f21edcb9101
### **Step 6: Final Push to GitHub**

# Add the README
git add README.md

# Commit and push
git commit -m "Add comprehensive README with documentation"
git push

Step 7: Add Deployment Instructions (Optional but Recommended)
Create a DEPLOYMENT.md file:

<<<<<<< HEAD
markdown
# 🚀 Deployment Guide
=======
# Deployment Guide
>>>>>>> 1a924624204542848505d3c1f0ae3f21edcb9101

## AWS ECS Deployment

1. **Build and push to ECR**:
  
   aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin YOUR_ACCOUNT_ID.dkr.ecr.us-east-1.amazonaws.com
   docker build -t autograde-ai .
   docker tag autograde-ai:latest YOUR_ACCOUNT_ID.dkr.ecr.us-east-1.amazonaws.com/autograde-ai:latest
   docker push YOUR_ACCOUNT_ID.dkr.ecr.us-east-1.amazonaws.com/autograde-ai:latest

2. Create ECS Task Definition referencing your ECR image
<<<<<<< HEAD

3. Create ECS Service with load balancer

=======
3. Create ECS Service with load balancer
>>>>>>> 1a924624204542848505d3c1f0ae3f21edcb9101
4. Configure DNS with Route 53

# Environment Variables
PYTHONPATH=/app/src
MODEL_PATH=/app/models/car_damage_v12/weights/best.pt

# Monitoring Setup
CloudWatch for logs and metrics
Prometheus/Grafana for detailed monitoring
Health checks at /health endpoint
