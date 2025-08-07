# 🚗 Vehicle License Plate Recognition (VLPR)

A Python-based application that detects and recognizes Vietnamese vehicle license plates from images using OpenCV and Tesseract OCR.

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

```
VehicleLicensePlateRecognition/
│
├── main.py                 # Main detection and OCR script
└── README.md               # Project documentation
```

---

## ⚙️ Installation

1. Clone the repository:

```bash
git clone https://github.com/Loitranph/VehicleLicensePlateRecognition.git
cd VehicleLicensePlateRecognition
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. (Windows only) Download and install [Tesseract OCR](https://github.com/tesseract-ocr/tesseract), then add it to system PATH.

---

## 🚀 Usage

Run the main script:

```bash
python main.py
```

Results (with bounding boxes and text) will be saved to `output_images/`.

---

## 🧑‍💻 Author

- **Phuoc Loi Tran** – [GitHub](https://github.com/Loitranph)

---
