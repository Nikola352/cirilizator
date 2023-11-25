from fontTools.ttLib import TTFont


ALLOWED_FONT_TYPES = ["woff", "woff2", "ttf", "otf"]


class Font:
    def __init__(self, font_file):
        self.font_file = font_file
        self.all_files = [font_file]
        self = set_from_file(self, font_file)

    def add_file(self, font_file):
        self.all_files.append(font_file)


def set_from_file(font, font_file) -> Font:
    font.type = font_file.split(".")[-1]
    if font.type not in ALLOWED_FONT_TYPES:
        raise ValueError(f"Font type {font.type} is not supported")
    font.font = TTFont(font_file)
    font.font_family = font.font["name"].names[1].string.decode("utf-8")
    font.font_subfamily = font.font["name"].names[2].string.decode("utf-8")
    font.font_full_name = font.font["name"].names[4].string.decode("utf-8")
    font.font_postscript_name = font.font["name"].names[6].string.decode("utf-8")
    font.font_weight = font.font["OS/2"].usWeightClass
    font.font_width = font.font["OS/2"].usWidthClass
    font.font_italic = font.font["post"].italicAngle
    font.font_ascent = font.font["hhea"].ascent
    font.font_descent = font.font["hhea"].descent
    font.font_line_gap = font.font["hhea"].lineGap
    font.font_cap_height = font.font["OS/2"].sCapHeight
    font.font_x_height = font.font["OS/2"].sxHeight
    font.font_stem_v = font.font["post"].underlineThickness
    return font
        
    
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
