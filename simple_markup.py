import sys, re
from util import *
OUT_FILE = 'D:\\用户目录\\Documents\\Python\\即时标记\\out.html'
IN_FILE = 'D:\\用户目录\\Documents\\Python\\即时标记\\text_input.txt'
IN = open(IN_FILE)
with open(OUT_FILE, 'w+') as OUT:
    print('<html><head><title>...</title><body>', file = OUT)
    title = True
    for block in blocks(IN):
        block = re.sub(r'\*(.+?)\*', r'<em>\1</em>', block)
        if title:
            print('<h1>', file = OUT)
            print(block, file = OUT)
            print('</h1>', file = OUT)
            title = False
        else:
            print('<p>', file = OUT)
            print(block, file = OUT)
            print('</p>', file = OUT)

    print('</body></html>', file = OUT)
IN.close()
