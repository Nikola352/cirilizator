from fontTools.ttLib import TTFont
import numpy as np


ALLOWED_FONT_TYPES = ["woff", "woff2", "ttf", "otf"]


class Font:
    def __init__(self, font_file):
        self.font_file = font_file
        self.all_files = [font_file]
        self.set_from_file(font_file)

    def set_from_file(self, font_file):
        self.type = font_file.split(".")[-1]
        if self.type not in ALLOWED_FONT_TYPES:
            raise ValueError(f"Font type {self.type} is not supported")
        self.font = TTFont(font_file)
        self.font_family = self.font["name"].names[1].string.decode("utf-8")
        self.font_subfamily = self.font["name"].names[2].string.decode("utf-8")
        self.font_full_name = self.font["name"].names[4].string.decode("utf-8")
        self.font_postscript_name = self.font["name"].names[6].string.decode("utf-8")
        self.font_weight = self.font["OS/2"].usWeightClass
        self.font_width = self.font["OS/2"].usWidthClass
        self.font_italic = self.font["post"].italicAngle
        self.font_ascent = self.font["hhea"].ascent
        self.font_descent = self.font["hhea"].descent
        self.font_line_gap = self.font["hhea"].lineGap
        self.font_cap_height = self.font["OS/2"].sCapHeight if hasattr(self.font["OS/2"], "sCapHeight") else 0
        self.font_x_height = self.font["OS/2"].sxHeight if hasattr(self.font["OS/2"], "sxHeight") else 0
        self.font_stem_v = self.font["post"].underlineThickness
        return self

    def add_file(self, font_file):
        self.all_files.append(font_file)

    def as_vector(self):
        return np.array([
            self.font_weight,
            self.font_width,
            self.font_italic,
            self.font_ascent,
            self.font_descent,
            self.font_line_gap,
            self.font_cap_height,
            self.font_x_height,
            self.font_stem_v,
        ])
        
    
if __name__ == "__main__":
    font = Font("resources/fonts/EtarRNIDS-BoldItalic.woff2")
    print(font.font_family)
    print(font.font_subfamily)
    print(font.font_full_name)
    print(font.font_postscript_name)
    print(font.type)
    print(font.font_weight)
    print(font.font_width)
    print(font.font_italic)
    print(font.font_ascent)
    print(font.font_descent)
    print(font.font_line_gap)
    print(font.font_cap_height)
    print(font.font_x_height)
    print(font.font_stem_v)
