import os

from fitz import fitz

latin_to_cyrillic_map = {
    'a': 'а', 'b': 'б', 'c': 'ц', 'č': 'ч', 'ć': 'ћ', 'd': 'д', 'đ': 'ђ',
    'e': 'е', 'f': 'ф', 'g': 'г', 'h': 'х', 'i': 'и', 'j': 'ј', 'k': 'к',
    'l': 'л', 'lj': 'љ', 'm': 'м', 'n': 'н', 'nj': 'њ', 'o': 'о', 'p': 'п',
    'r': 'р', 's': 'с', 'š': 'ш', 't': 'т', 'u': 'у', 'v': 'в', 'z': 'з',
    'ž': 'ж', 'A': 'А', 'B': 'Б', 'C': 'Ц', 'Č': 'Ч', 'Ć': 'Ћ', 'D': 'Д',
    'Đ': 'Ђ', 'E': 'Е', 'F': 'Ф', 'G': 'Г', 'H': 'Х', 'I': 'И', 'J': 'Ј',
    'K': 'К', 'L': 'Л', 'Lj': 'Љ', 'M': 'М', 'N': 'Н', 'Nj': 'Њ', 'O': 'О',
    'P': 'П', 'R': 'Р', 'S': 'С', 'Š': 'Ш', 'T': 'Т', 'U': 'У', 'V': 'В',
    'Z': 'З', 'Ž': 'Ж'
}


def transliterate_pdf(file):
    file_path = os.path.join("uploads", file.filename)
    file.save(file_path)

    pdf_document = fitz.Document("uploads" + os.sep + file.filename, filetype="pdf")

    # This is a horrible approach that should be changed but it works
    # Despite numerous attempts & hours wasted I could not find a way to directly change the text of the pdf
    # page.get_text("blocks") returns blocks but changing them has no effect on the pdf.
    # page.set_text does not exist
    # TODO: figure out why cyrillic letters sometimes get put in the wrong place (higher & smaller than others)

    for key, val in {"nj": "њ", "lj": "љ", "NJ": "Њ", "LJ": "Љ"}.items():
        find_char = key
        replacement_char = val
        for page_number in range(pdf_document.page_count):
            page = pdf_document[page_number]
            hits = page.search_for(find_char)
            for rect in hits:
                page.add_redact_annot(rect, replacement_char, fontname="figo", fontsize=12,
                                      align=fitz.TEXT_ALIGN_LEFT, cross_out=False)
            page.apply_redactions(images=fitz.PDF_REDACT_IMAGE_NONE)

    for key, val in latin_to_cyrillic_map.items():
        find_char = key
        replacement_char = val
        for page_number in range(pdf_document.page_count):
            page = pdf_document[page_number]
            hits = page.search_for(find_char)
            for rect in hits:
                page.add_redact_annot(rect, replacement_char, fontname="figo", fontsize=12,
                                      align=fitz.TEXT_ALIGN_LEFT, cross_out=False)
            page.apply_redactions(images=fitz.PDF_REDACT_IMAGE_NONE)

    pdf_document.save("uploads" + os.sep + "edited_file.pdf")
    return "uploads" + os.sep + "edited_file.pdf"


def transliterate_txt(file):
    original_text = file.read().decode('utf-8')

    transliterated_text = transliterate_text(original_text)

    edited_file_path = save_transliterated_text(transliterated_text)

    return edited_file_path


def transliterate_text(text):
    for key, val in latin_to_cyrillic_map.items():
        text = text.replace(key, val)
    return text


def save_transliterated_text(transliterated_text):
    edited_file_path = os.path.join("uploads", "edited_file.txt")
    with open(edited_file_path, 'w', encoding='utf-8') as edited_file:
        edited_file.write(transliterated_text)

    return edited_file_path
