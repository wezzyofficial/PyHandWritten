import os, textwrap, random, pathlib, platform
from PIL import Image, ImageDraw, ImageFont


class TextToPicture:
    def __init__(self, text: str = '', hash_d: str = ''):
        self.text = text
        self.__hash = hash_d

    __color = (47, 79, 159)
    __max_char = 47
    __max_lines = 21
    __indent = 49.5
    __font_size = 50
    __n_pictures = ['exel1', 'exel2']
    __font_name = 'font4.otf'

    def __wrap(self, text: str = '') -> list:
        return textwrap.wrap(text, self.__max_char)

    def word_processing(self) -> list:
        files_list = []
        page, tw = 1, self.__wrap(text=self.text)

        for cl in range(0, len(tw), self.__max_lines):
            part = tw[cl:cl + self.__max_lines]

            x, y, pic_name = 15, -47, self.__n_pictures[1]
            if page % 2 == 0:
                x, y, pic_name = 155, -47, self.__n_pictures[0]

            path_ff = pathlib.Path(__file__).parent
            path_fonts_folder = f'{path_ff}/fonts/'
            if platform.system() == 'Windows':
                path_fonts_folder = f'{path_ff}\\fonts\\'

            lf = ImageFont.truetype(font=f'{path_fonts_folder}{self.__font_name}', size=self.__font_size)

            path_pf = pathlib.Path(__file__).parent
            path_photo_folder = f'{path_pf}/photo/{pic_name}.jpg'
            if platform.system() == 'Windows':
                path_photo_folder = f'{path_pf}\\photo\\{pic_name}.jpg'

            open_n_pic = Image.open(fp=path_photo_folder)
            draw_n_pic = ImageDraw.Draw(im=open_n_pic)

            y_indent = y
            for t in part:
                y_indent += self.__indent
                x_random = x - random.randint(-2, 2)

                if x_random <= 0: x_random = 1
                draw_n_pic.text(xy=(x_random, int(y_indent)), text=t, fill=self.__color, font=lf)

            path_sf = pathlib.Path(__file__).parent.parent.parent
            path_save_folder = f'{path_sf}/pictures/out{self.__hash}_{page}.jpg'
            if platform.system() == 'Windows':
                path_save_folder = f'{path_sf}\\pictures\\out{self.__hash}_{page}.jpg'

            open_n_pic.save(fp=path_save_folder)
            files_list.append(path_save_folder)
            page += 1

        return files_list