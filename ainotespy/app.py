from flask import Flask, render_template, request
from docx import Document
import re
import PyPDF2
import pytesseract
from PIL import Image

app = Flask(__name__)

def analyze_text(text, topics, total_papers):
    text = text.lower()
    results = []

    for topic in topics:
        safe_topic = re.escape(topic.lower())
        count = len(re.findall(safe_topic, text))

        score = (count / total_papers) * 100 if total_papers > 0 else 0

        if score >= 70:
            priority = "Most Important 🔥"
        elif score >= 40:
            priority = "Important ✅"
        elif score >= 20:
            priority = "Moderate ⚡"
        else:
            priority = "Low Priority 📘"

        results.append({
            "topic": topic,
            "count": count,
            "score": round(score, 2),
            "priority": priority
        })

    return sorted(results, key=lambda x: x["score"], reverse=True)


@app.route("/", methods=["GET", "POST"])
def index():
    results = None
    error = None

    if request.method == "POST":
        syllabus = request.form.get("syllabus", "").strip()
        text_input = request.form.get("text_input", "").strip()
        paper_count = request.form.get("paper_count", "").strip()

        if not syllabus or not paper_count:
            error = "Syllabus and Paper Count are required!"
            return render_template("index.html", results=None, error=error)

        try:
            paper_count = int(paper_count)
        except:
            error = "Paper Count must be a number!"
            return render_template("index.html", results=None, error=error)

        topics = [t.strip() for t in syllabus.split(",") if t.strip()]

        combined_text = ""

        # Multiple file support
        files = request.files.getlist("files")

        for file in files:
            if file and file.filename:
                filename = file.filename.lower()

                if filename.endswith(".pdf"):
                    try:
                        reader = PyPDF2.PdfReader(file)
                        for page in reader.pages:
                            page_text = page.extract_text()
                            if page_text:
                                combined_text += page_text
                    except:
                        error = "Error reading PDF file."

                elif filename.endswith(".txt"):
                    try:
                        combined_text += file.read().decode("utf-8")
                    except:
                        error = "Error reading TXT file."

                elif filename.endswith(".docx"):
                    try:
                        document = Document(file)
                        for para in document.paragraphs:
                            combined_text += para.text
                    except Exception as e:
                        print("DOCX Error:", e)
                elif filename.endswith((".png", ".jpg", ".jpeg")):
                    try:
                        image = Image.open(file)
                        text_from_image = pytesseract.image_to_string(image)
                        combined_text += text_from_image
                    except Exception as e:
                        print("Image OCR Error:", e)

        combined_text += text_input

        if combined_text.strip() == "":
            error = "Please upload file or enter text."
            return render_template("index.html", results=None, error=error)

        results = analyze_text(combined_text, topics, paper_count)

    return render_template("index.html", results=results, error=error)


if __name__ == "__main__":
    app.run(debug=True)