# AI-Notes-Analyzer
AI-based Multi-Format Exam Paper Analyzer built using Flask. Supports PDF, DOCX, TXT, and Image (OCR) files to analyze syllabus topics and classify them into Most Important, Important, Moderate, and Low Priority based on frequency analysis.

🚀 Overview

AI-based Multi-Format Exam Paper Analyzer built using Flask.  
This application analyzes Previous Year Question Papers (PYQs) and classifies syllabus topics based on importance using frequency-based analysis.

✨ Features

- 📄 Supports PDF files
- 📝 Supports TXT files
- 📘 Supports DOCX files
- 🖼 Supports Image files (JPG, PNG) using OCR
- 🧠 Frequency-based topic importance analysis
- 📊 Priority classification:
  - 🔥 Most Important
  - ✅ Important
  - ⚡ Moderate
  - 📘 Low Priority
- 🎨 Professional styled UI
- 📂 Multiple file upload support

🛠 Technologies Used

- Python
- Flask
- PyPDF2
- python-docx
- pytesseract
- Pillow
- HTML
- CSS

📦 Installation

Install required libraries:

```bash

https://github.com/UB-Mannheim/tesseract/wiki download from link
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
&"C:\Program Files\Tesseract-OCR\tesseract.exe" --version

pip install python-docx
pip install flask nltk pytesseract pillow
pip install flask PyPDF2 python-docx pytesseract pillow
