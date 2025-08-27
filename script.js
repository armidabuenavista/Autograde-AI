class VehicleAnalyzer {
    constructor() {
        this.apiBaseUrl = 'http://localhost:8000';
        this.initializeEventListeners();
    }

    initializeEventListeners() {
        const uploadBox = document.getElementById('uploadBox');
        const fileInput = document.getElementById('fileInput');
        const browseLink = uploadBox.querySelector('.browse-link');

        // Click to select file
        uploadBox.addEventListener('click', () => fileInput.click());
        browseLink.addEventListener('click', (e) => {
            e.stopPropagation();
            fileInput.click();
        });

        // Drag and drop
        uploadBox.addEventListener('dragover', (e) => {
            e.preventDefault();
            uploadBox.classList.add('dragover');
        });

        uploadBox.addEventListener('dragleave', () => {
            uploadBox.classList.remove('dragover');
        });

        uploadBox.addEventListener('drop', (e) => {
            e.preventDefault();
            uploadBox.classList.remove('dragover');
            const files = e.dataTransfer.files;
            if (files.length > 0) {
                this.handleFileSelect(files[0]);
            }
        });

        // File input change
        fileInput.addEventListener('change', (e) => {
            if (e.target.files.length > 0) {
                this.handleFileSelect(e.target.files[0]);
            }
        });
    }

    async handleFileSelect(file) {
        if (!file.type.startsWith('image/')) {
            this.showError('Please select an image file');
            return;
        }

        this.showLoading();
        this.hideError();
        this.hideResults();

        try {
            const formData = new FormData();
            formData.append('file', file);

            const response = await fetch(`${this.apiBaseUrl}/analyze-vehicle/`, {
                method: 'POST',
                body: formData
            });

            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }

            const results = await response.json();
            this.displayResults(results, file);

        } catch (error) {
            console.error('Error:', error);
            this.showError('Failed to analyze image. Please make sure the API server is running.');
        } finally {
            this.hideLoading();
        }
    }

    displayResults(results, originalFile) {
        const resultsSection = document.getElementById('resultsSection');
        const damageList = document.getElementById('damageList');
        const originalImage = document.getElementById('originalImage');
        const annotatedImage = document.getElementById('annotatedImage');

        // Display original image
        const originalUrl = URL.createObjectURL(originalFile);
        originalImage.src = originalUrl;

        // Display annotated image
        annotatedImage.src = `${this.apiBaseUrl}${results.results.annotated_image_url}`;

        // Display damage details
        damageList.innerHTML = '';

        if (results.detections.length === 0) {
            damageList.innerHTML = '<div class="damage-item">No damage detected</div>';
        } else {
            results.detections.forEach(damage => {
                const damageItem = document.createElement('div');
                damageItem.className = 'damage-item';
                damageItem.innerHTML = `
                    <div class="damage-type">${damage.label}</div>
                    <div class="damage-confidence">Confidence: ${(damage.confidence * 100).toFixed(1)}%</div>
                    <div class="damage-bbox">Location: [${damage.bbox.map(c => c.toFixed(1)).join(', ')}]</div>
                `;
                damageList.appendChild(damageItem);
            });
        }

        this.showResults();
    }

    showLoading() {
        document.getElementById('loading').style.display = 'block';
    }

    hideLoading() {
        document.getElementById('loading').style.display = 'none';
    }

    showResults() {
        document.getElementById('resultsSection').style.display = 'block';
    }

    hideResults() {
        document.getElementById('resultsSection').style.display = 'none';
    }

    showError(message) {
        const errorDiv = document.getElementById('error');
        errorDiv.querySelector('p').textContent = message;
        errorDiv.style.display = 'block';
    }

    hideError() {
        document.getElementById('error').style.display = 'none';
    }
}

// Initialize the application when the page loads
document.addEventListener('DOMContentLoaded', () => {
    new VehicleAnalyzer();
});