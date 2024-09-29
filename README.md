# Smart Extract

Smart Extract is a document processing and question-answering application that supports both English and Hindi documents. It allows users to extract text from uploaded documents and ask questions based on the extracted content.

## Features

- Text extraction from English and Hindi documents
- Question-answering capability for extracted text
- User-friendly interface built with Gradio

## Live Demo

You can try out Smart Extract using our live demo hosted on Hugging Face Spaces:

[Smart Extract Demo](https://huggingface.co/spaces/codhash/Smart-Extract)

This demo allows you to experience the features of Smart Extract without having to install it locally. Simply visit the link and start extracting text and asking questions about your documents!

## Local Installation

If you want to run Smart Extract locally, follow these steps:

### Prerequisites

Before running this project, make sure you have the following installed:

- Python 3.9+
- pip (Python package manager)
- Tesseract OCR

### Installation Steps

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
   git clone https://github.com/ihashirjadoon/Smart-Extract
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

To run Smart Extract locally:

1. Ensure you're in the project directory and your virtual environment is activated.
2. Run the application:
   ```
   python app.py
   ```
3. Open your web browser and navigate to the URL provided in the console output (typically http://localhost:7860).


## Project Structure

The Smart Extract project is organized with the following folder structure:

- `app/`: Contains the main application code.
- `model/`: Stores the pre-trained models and any other model files.
- `README.md`: This file.
- `requirements.txt`: Lists the dependencies required for the project.

## Contributing

Contributions to Smart Extract are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
