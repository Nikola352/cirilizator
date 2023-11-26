import os
import random
import numpy as np

from fonts.font_parser import Font


FONTS_DIR = os.path.join(os.getcwd(), 'resources', 'fonts')


def load_fonts():
    fonts = []
    for filename in os.listdir(FONTS_DIR):
        filepath = os.path.join(FONTS_DIR, filename)
        font = Font(filepath).set_category()
        fonts.append(font)
    return fonts


def cosine_similarity(vector1, vector2):
    return np.dot(vector1, vector2) / (np.linalg.norm(vector1) * np.linalg.norm(vector2))



def match_fonts(font_service):
    fonts = load_fonts()
    print(len(fonts))

    serif_fonts = [font for font in fonts if font.category == 'serif']
    other_fonts = [font for font in fonts if font.category != 'serif']

    print(len(serif_fonts), len(other_fonts))
    print(set([font.category for font in other_fonts]))

    for font in other_fonts:
        similarities = []
        for i, serif_font in enumerate(serif_fonts):
            similarities.append((cosine_similarity(font.as_vector(), serif_font.as_vector()), i))
        
        sorted_similarities = sorted(similarities, key=lambda x: x[0], reverse=True)
        idx = random.randint(0, np.min([len(sorted_similarities), 10]))
        print('Found best match: ', font.font_family, '-', serif_fonts[sorted_similarities[idx][1]].font_family, sorted_similarities[idx][0])
        font_service.new_match(font.font_family, serif_fonts[sorted_similarities[idx][1]].font_family, sorted_similarities[idx][0])

if __name__ == "__main__":
    fonts = load_fonts()
    match_fonts(fonts)