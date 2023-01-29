from PIL import Image
import pandas as pd

df = pd.read_excel('colors.xlsx', index_col=None, na_values=['NA'])
sw_code = df['COLOR #'].values.tolist()
color_names = df['COLOR NAME'].values.tolist()
hex_list = df['HEX'].values.tolist()

def hex_to_rgb(value):
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

def blend_color(color, coeff):
    return tuple([int(color[i] * coeff) for i in range(3)])

im_msk = Image.open('furniture.png').convert('L')
im_msk_px = im_msk.load()

im_target = Image.open('bg.jpeg').convert('RGB')
im_target_l = im_target.convert('L')
im_target_px = im_target.load()

for color in hex_list:
    print("Processing color: " + color + "...")
    for w in range(im_msk.width):
        for h in range(im_msk.height):
            if im_msk_px[w, h] != 0:
                im_target_px[w, h] = blend_color(hex_to_rgb(color), im_target_l.getpixel((w, h)) / 255)
        c_index = hex_list.index(color)
    im_target.save('./out/bg_' + sw_code[c_index] +
                   '_' + color_names[c_index] + '_' + color + '.png')
