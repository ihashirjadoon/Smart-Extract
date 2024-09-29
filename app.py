import gradio as gr
from model.qa_model import qa_model
from model.extract_text import extract_text_from_file
from model.extract_text_hindi import extract_text_from_file_hindi

def extract_english_text(file):
    file_path = file.name
    extracted_text = extract_text_from_file(file_path, lang='eng')
    return extracted_text

def answer_english_question(file, question):
    file_path = file.name
    extracted_text = extract_text_from_file(file_path, lang='eng')
    answer = qa_model(question=question, context=extracted_text)
    return answer['answer'] if 'answer' in answer else "No answer found."

def extract_hindi_text(file):
    file_path = file.name
    extracted_text = extract_text_from_file_hindi(file_path)
    return extracted_text

def answer_hindi_question(file, question):
    file_path = file.name
    extracted_text = extract_text_from_file_hindi(file_path)
    answer = qa_model(question=question, context=extracted_text)
    return answer['answer'] if 'answer' in answer else "No answer found."

ui = gr.Blocks()

with ui:
    gr.Markdown("# 📄 **Smart Extract**")
    
    with gr.Tab("English Document"):
        with gr.Column():
            english_file = gr.File(label="Upload English Document")
            english_extract_btn = gr.Button("Extract Text")
            english_extracted_text = gr.Textbox(label="Extracted Text", interactive=False, lines=15)
            english_extract_btn.click(extract_english_text, inputs=[english_file], outputs=[english_extracted_text])

        with gr.Column():
            english_question = gr.Textbox(label="Enter Question", placeholder="Ask a question based on the extracted text")
            english_answer = gr.Textbox(label="Answer", interactive=False, placeholder="The answer will appear here...")
            english_question_btn = gr.Button("Ask Question")
            english_question_btn.click(answer_english_question, inputs=[english_file, english_question], outputs=[english_answer])

    with gr.Tab("Hindi Document"):
        with gr.Column():
            hindi_file = gr.File(label="Upload Hindi Document")
            hindi_extract_btn = gr.Button("Extract Text")
            hindi_extracted_text = gr.Textbox(label="Extracted Text", interactive=False, lines=15)
            hindi_extract_btn.click(extract_hindi_text, inputs=[hindi_file], outputs=[hindi_extracted_text])

        with gr.Column():
            hindi_question = gr.Textbox(label="Enter Question", placeholder="Ask a question based on the extracted text")
            hindi_answer = gr.Textbox(label="Answer", interactive=False)
            hindi_question_btn = gr.Button("Ask Question")
            hindi_question_btn.click(answer_hindi_question, inputs=[hindi_file, hindi_question], outputs=[hindi_answer])

# CSS for better UI styling
ui.css = """
.gr-box {
    background-color: #f5f5f5;
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.1);
}
.gr-textbox, .gr-file, .gr-button {
    width: 100%;
    margin-top: 10px;
    margin-bottom: 10px;
}
.gr-button {
    background-color: #007bff;
    color: white;
    border: none;
    padding: 10px 20px;
    border-radius: 5px;
    cursor: pointer;
}
.gr-button:hover {
    background-color: #0056b3;
}
.gr-markdown h1 {
    font-size: 24px;
    font-weight: bold;
    color: #333;
    text-align: center;
    margin-bottom: 20px;
}
.gr-textbox textarea {
    height: 200px !important;
    font-size: 14px;
}
"""

if __name__ == "__main__":
    ui.launch()
