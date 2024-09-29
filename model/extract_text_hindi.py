import pytesseract
import fitz
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_text_from_file_hindi(file_path, lang ='hin'):
    extracted_text_hin = ""
    
    if file_path.endswith('.pdf'):
        try:
            pdf_document = fitz.open(file_path)
            
            for page_num in range(len(pdf_document)):
                page = pdf_document.load_page(page_num)
                pix = page.get_pixmap()
                image = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
                text = pytesseract.image_to_string(image, lang=lang)
                extracted_text_hin += text +"\n"
                
        except Exception as e:
            return f"Error processing PDF: {str(e)}"
        
    elif file_path.lower().endswith(('.png', '.jpg', 'jpeg', '.gif', '.bmp')):
        try:
            image = Image.open(file_path)
            text = pytesseract.image_to_string(image, lang = lang)
            extracted_text_hin += text + "\n"
            
        except Exception as e:
            return f"Error processing image: {str(e)}"
        
    else: 
        return "Unsupported file format."
    
    return extracted_text_hin.strip()
        
    
    # elif file_path.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
    #     try:
    #         image = Image.open(file_path)
    #         text = pytesseract.image_to_string(image, lang=lang)
    #         extracted_text += text + "\n"

    #     except Exception as e:
    #         return f"Error processing image: {str(e)}"

    # else:
    #     return "Unsupported file format."

    # return extracted_text.strip()
    
            