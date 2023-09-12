# LicencePy-Verify 🚗

| ![ Python]( https://img.shields.io/badge/python-3.x-blue.svg ) | ![ OpenCV]( https://img.shields.io/badge/OpenCV-4.x-green.svg ) | ![ SQLite]( https://img.shields.io/badge/SQLite-3.x-orange.svg ) | ![ Tesseract]( https://img.shields.io/badge/Tesseract-4.x-red.svg ) |
|----------------------------------------------------------------|-----------------------------------------------------------------|------------------------------------------------------------------|---------------------------------------------------------------------|
## 🌟 Overview

This project aims to recognize and verify license plate numbers from an image 📷. It utilizes OpenCV for image processing and Tesseract for Optical Character Recognition (OCR). The license plate numbers are verified against an SQLite database 🛡.

## 🛠 Requirements

- Python 3.x
- OpenCV (`cv2`)
- Tesseract (`pytesseract`)
- SQLite (`pysqlite3`)

👇 Install these Python packages if you haven't already:

```bash
pip install opencv-python
pip install pytesseract
pip install pysqlite3
```

### 📘 Tesseract Installation

Make sure to [download and install Tesseract](https://github.com/tesseract-ocr/tesseract) and specify the path in the script.

## 📂 File Structure

- `plate_recognition.py`: Contains functions for license plate recognition 📸.
- `sqlicense_plates.py`: Contains functions for SQLite database operations 🗄.
- `main.py`: The main script that ties everything together 🧠.
- `license_plates.db`: SQLite database file (automatically created) 💽.

## 🚀 How To Use

1️⃣ Run `sqlicense_plates.py` to initialize the SQLite database:

```bash
python sqlicense_plates.py
```

2️⃣ Optionally, add some sample license plates to the database:

```bash
python -c 'import sqlicense_plates; sqlicense_plates.add_license_plate("ABC123")'
```

3️⃣ Run `main.py` to process an image for license plate recognition and verification:

```bash
python main.py
```

## 💡 Code Snippets

### 🖼 Image to Text Conversion (`plate_recognition.py`)

Here, we use OpenCV for image processing and Tesseract for OCR 📝.

```python
import cv2
import pytesseract

def img_to_text(image_path):
    # ... (as in your code)
    return license_texts
```

### 📚 SQLite Database Operations (`sqlicense_plates.py`)

We use SQLite to maintain a list of valid license plates 🗒.

```python
import pysqlite3  # Make sure to install pysqlite3

def create_database():
    # ... (as in your code)
```

### 🎛 Main Program (`main.py`)

This script performs the recognition and verification 🔍.

```python
import sys
import sqlicense_plates as sqlicenses
import plate_recognition as pr

# ... (as in your code)
```

## 🛠 Troubleshooting

- 📌 Make sure that Tesseract is properly installed and the path is correctly specified.
- 📌 Check if the SQLite database is properly initialized and populated.

**Note**: For complete functionality, refer to the source code and comments within 📄.