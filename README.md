# 🚗 Vehicle License Plate Recognition (VLPR)

A Python-based application that detects and recognizes Vietnamese vehicle license plates from images using OpenCV and Tesseract OCR.

![Demo](https://github.com/Loitranph/VehicleLicensePlateRecognition/assets/your-demo.gif)

---

## 📌 Features

- 🔍 Detects and extracts license plates from input images
- 🔠 Recognizes plate characters using Tesseract OCR
- 🇻🇳 Supports Vietnamese-style plates
- 🖼️ Visual display of bounding boxes and recognized text

---

## 🛠️ Tech Stack

- **Python 3.x**
- **OpenCV** – for image processing & contour detection
- **Pytesseract** – Python wrapper for Tesseract OCR
- **NumPy**, **Matplotlib** – for visualization & data handling

---

## 📂 Folder Structure
VehicleLicensePlateRecognition/
│
├── input_images/ # Folder for testing images
├── output_images/ # Folder to save annotated images
├── main.py # Main detection and OCR script
├── utils.py # Image preprocessing functions
├── README.md # Project documentation
└── requirements.txt # Required libraries
