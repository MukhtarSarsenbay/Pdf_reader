import fitz  # PyMuPDF
from gtts import gTTS
import os

def pdf_to_speech(pdf_path, output_audio_path='output.mp3', language='en'):
    # Open the PDF file
    doc = fitz.open(pdf_path)

    # Extract text from the first page to the last page
    text = ''
    for page in doc:
        text += page.get_text()

    # Close the document
    doc.close()

    # Convert text to speech
    tts = gTTS(text=text, lang=language, slow=False)
    tts.save(output_audio_path)
    print(f"Audio file saved as: {output_audio_path}")

# Example usage
pdf_path = 'example.pdf'  # Replace with your PDF file path
pdf_to_speech(pdf_path)
