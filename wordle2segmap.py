import re
from PIL import Image
from PIL import ImageDraw

sky = '#9ceedd'
grass = '#7bc800'
plant = '#a8c832'
cloud = '#696969'
straw = '#a2a3eb'

# set =['🟨','⬜','⬛','🟩']
valid_chars = ['\N{Large Yellow Square}', '\N{White Large Square}',
       '\N{Black Large Square}', '\N{Large Green Square}']


def fill_rect(char, x, y):
    width = 1024/5
    height = 1024/6
    color = ''
    if char == '\N{Large Yellow Square}':
        color = cloud
    if char == '\N{White Large Square}' or char == '\N{Black Large Square}':
        color = sky
    if char == '\N{Large Green Square}':
        if y == 0:
            color = grass
        else:
            color = plant
    img1.rectangle([(x*width, (5-y)*height), (x*width+width,
                   (5-y+1)*height)], fill=color, outline=None)


strings = open('./samples/Wordle 211 5_6(1).txt').readlines()
strings = list(filter(lambda x: any(elem in x for elem in valid_chars), strings))

matrix = []
for i in strings:
    matrix.append(list(filter(lambda x: x in valid_chars, list(i))))

matrix = list(map(list, zip(*matrix)))

img = Image.new('RGB', (1024, 1024), color='#9ceedd')
img1 = ImageDraw.Draw(img)
for i, col in enumerate(matrix):
    for j, el in enumerate(reversed(col)):
        fill_rect(el, i, j)

img.save('segmentation.png')
