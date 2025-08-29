import os
from flask import Flask, request, jsonify
from google.cloud import vision

app = Flask(__name__)

# Initialize Google Cloud Vision API client
client = vision.ImageAnnotatorClient()

@app.route('/analyze', methods=['POST'])
def analyze_image():
    # If no image is uploaded, use the local image
    if 'image' in request.files:
        image_file = request.files['image']
        image_bytes = image_file.read()
        image = vision.Image(content=image_bytes)
    else:
        local_image_path = r"C:\Users\maina\Downloads\k8I1VTJ - Imgur.jpg"
        with open(local_image_path, "rb") as image_file:
            content = image_file.read()
        image = vision.Image(content=content)

    # Perform label detection
    response = client.label_detection(image=image)
    labels = [label.description for label in response.label_annotations]

    # Perform text detection (OCR)
    text_response = client.text_detection(image=image)
    texts = [text.description for text in text_response.text_annotations]

    return jsonify({
        "labels": labels,
        "texts": texts
    })

if __name__ == '__main__':
    app.run(debug=True)
