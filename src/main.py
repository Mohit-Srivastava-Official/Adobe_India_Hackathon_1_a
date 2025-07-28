import os
import json
from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer, LTChar
import fitz  # PyMuPDF

def extract_title_and_headings(pdf_path):
    doc = fitz.open(pdf_path)
    title = doc.metadata.get('title') or os.path.splitext(os.path.basename(pdf_path))[0]
    outline = []
    for page_num, page in enumerate(doc, 1):
        blocks = page.get_text("dict")['blocks']
        for block in blocks:
            if block['type'] == 0:  # text block
                for line in block['lines']:
                    text = ''.join([span['text'] for span in line['spans']]).strip()
                    if not text or len(text) < 3:
                        continue
                    font_sizes = [span['size'] for span in line['spans']]
                    max_size = max(font_sizes)
                    # Heuristic: largest font on first page is title
                    if page_num == 1 and max_size > 16 and len(text.split()) > 2:
                        title = text
                    # Heuristic: heading detection
                    if max_size > 14:
                        level = 'H1'
                    elif max_size > 12:
                        level = 'H2'
                    elif max_size > 10:
                        level = 'H3'
                    else:
                        continue
                    outline.append({
                        'level': level,
                        'text': text,
                        'page': page_num
                    })
    return title, outline

def process_pdfs(input_dir, output_dir):
    for filename in os.listdir(input_dir):
        if filename.lower().endswith('.pdf'):
            pdf_path = os.path.join(input_dir, filename)
            title, outline = extract_title_and_headings(pdf_path)
            output = {
                'title': title,
                'outline': outline
            }
            outname = os.path.splitext(filename)[0] + '.json'
            with open(os.path.join(output_dir, outname), 'w', encoding='utf-8') as f:
                json.dump(output, f, ensure_ascii=False, indent=2)

def main():
    input_dir = '/app/input'
    output_dir = '/app/output'
    os.makedirs(output_dir, exist_ok=True)
    process_pdfs(input_dir, output_dir)

if __name__ == '__main__':
    main()
