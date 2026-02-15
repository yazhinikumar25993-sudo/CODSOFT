import torch
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import os
import sys

def load_model():
    try:
        print("Loading image captioning model...")
        processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
        model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
        print("Model loaded successfully.\n")
        return processor, model
    except Exception as e:
        print("Error loading model:", e)
        sys.exit(1)

def load_image(image_path):
    if not os.path.exists(image_path):
        print("Error: File does not exist.")
        sys.exit(1)
    try:
        image = Image.open(image_path).convert("RGB")
        return image
    except Exception as e:
        print("Error opening image:", e)
        sys.exit(1)

def generate_caption(processor, model, image):
    try:
        inputs = processor(image, return_tensors="pt")
        with torch.no_grad():
            output = model.generate(**inputs)
        caption = processor.decode(output[0], skip_special_tokens=True)
        return caption
    except Exception as e:
        print("Error generating caption:C:\\Users\\adminS\\Desktop\\cap\\images.jpg", e)
        sys.exit(1)

def main():
    processor, model = load_model()
    image_path = input("Enter image path: ").strip()
    image = load_image(image_path)
    caption = generate_caption(processor, model, image)
    print("\nGenerated Caption:")
    print(caption)

if __name__ == "__main__":
    main()
