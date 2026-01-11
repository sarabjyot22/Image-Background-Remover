## 🖼️ AI Background Remover

A lightweight AI-powered background removal tool built in Python using the rembg library.
This project removes image backgrounds automatically and saves the output as a transparent PNG.

## 🔍 Project Overview

This tool uses a pre-trained deep learning model to separate the foreground from the background in an image.

*It is useful for:*

- Profile pictures

- Product images

- Design assets

- Image preprocessing for ML projects

The project demonstrates practical AI usage with minimal code.

## ✨ Features

*🧠 AI-based background removal*

*🖼️ Supports common image formats (JPG, PNG)*

*🎯 Produces transparent background output (PNG)*

*⚡ Simple and fast execution*

*🧩 Minimal dependencies*

## 🛠️ Technologies Used

- Python

- rembg – AI background removal

- Pillow (PIL) – image processing

- IO Bytes handling

## 📁 Project Structure
ai-background-remover-python/
├── background_remover.py
├── requirements.txt
└── README.md

## ⚙️ How It Works

- Reads an input image as bytes

- Passes the image to rembg’s AI model

- Separates the foreground from the background

- Saves the output as a transparent PNG

- Input Image → AI Model → Background Removed → Output Image

## ▶️ How to Run

*1️⃣ Install Dependencies*

pip install -r requirements.txt

*2️⃣ Run the Script*

python background_remover.py

## Make sure to update the input image path inside the script.

The AI model automatically detects the subject and removes the background.

## 📷 Example Output
Background removed successfully. Saved to output.png

*Output image contains an image without a background*
