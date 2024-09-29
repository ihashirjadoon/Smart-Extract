# Smart Extract

Smart Extract is a document processing and question-answering application that supports both English and Hindi documents. It allows users to extract text from uploaded documents and ask questions based on the extracted content.

## Features

- Text extraction from English and Hindi documents
- Question-answering capability for extracted text
- User-friendly interface built with Gradio

## Prerequisites

Before running this project, make sure you have the following installed:

- Python 3.7+
- pip (Python package manager)
- Tesseract OCR

## Installation

1. Install Tesseract OCR:
   - On Windows:
     - Download and install Tesseract from https://github.com/UB-Mannheim/tesseract/wiki
     - Add the Tesseract installation directory to your system PATH
   - On macOS:
     ```
     brew install tesseract
     ```
   - On Linux:
     ```
     sudo apt-get install tesseract-ocr
     ```

2. Clone the repository:
   ```
   git clone https://github.com/your-username/smart-extract.git
   cd smart-extract
   ```

3. Create a virtual environment:
   ```
   python -m venv env
   ```

4. Activate the virtual environment:
   - On Windows:
     ```
     .\env\Scripts\activate
     ```
   - On macOS and Linux:
     ```
     source env/bin/activate
     ```

5. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:
   ```
   python app.py
   ```

2. Open your web browser and go to the URL displayed in the terminal (usually `http://127.0.0.1:7860`).

3. Use the interface to upload documents, extract text, and ask questions.

## Project Structure

- `app.py`: Main application file containing the Gradio interface and core functionality.
- `model/qa_model.py`: Question-answering model implementation.
- `model/extract_text.py`: Text extraction for English documents.
- `model/extract_text_hindi.py`: Text extraction for Hindi documents.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).

<!-- Add your live link here when available -->
<!-- ## Live Demo -->
<!-- The project is live at: [https://your-project-url.com](https://your-project-url.com) -->

