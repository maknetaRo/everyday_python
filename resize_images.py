# python resize_images.py --input_dir=path/to/the/folder/with/pictures --output_dir=path/to/the/new/folder If folder is not specified the script will create the resized folder next to resize_image.py script.

# DEFAULT size is width=1024 and height=768, if the width is shorter than height the width=768 and height=1024

# but the size of resized images can be changed in command line python resize_image.py --width=320 --height=180

import os 
import argparse
from PIL import Image 

DEFAULT_SIZE = (1024, 768)


def resize_image(input_dir, infile, output_dir='resized', size=DEFAULT_SIZE):
    outfile = os.path.splitext(infile)[0] + '_resized'
    extension = os.path.splitext(infile)[1]

    try:
        img = Image.open(input_dir + '/' + infile)
        w,h = img.size

        if w >= h:
            if int(h) / int(w) == 0.75 :        
                img = img.resize((size[0], size[1]), Image.LANCZOS)
            else: 
                proportion = int(h) / int(w)
                new_h = int(size[0] * proportion)
                size = (1024, new_h)
                img = img.resize((size[0], size[1]), Image.LANCZOS)
        elif w < h: 
            if int(h) / int(w) ==0.75:
                img = img.resize((size[1], size[0]), Image.LANCZOS)
            else: 
                proportion = int(h) / int(w)
                new_w = int(size[1] * proportion)
                size = (new_w, 768)
                img = img.resize((size[1], size[0]), Image.LANCZOS)
        else: 
            print("I don't know what to do!")
        new_file = output_dir + '/' + outfile + extension
        img.save(new_file)       

    except IOError:
        print('unable to resize image {}'.format(infile))


if __name__ == '__main__':
    dir = os.getcwd()

    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input_dir', help='Full Input Path')
    parser.add_argument('-o', '--output_dir', help='Full Output Path')

    parser.add_argument('-w', '--width', help='Resized Width')
    parser.add_argument('-t', '--height', help='Resized Height')
    args = parser.parse_args()

    print(args)

    if args.input_dir:
        input_dir = args.input_dir 
    else: 
        input_dir = dir + '/images'

    if args.output_dir:
        output_dir = args.output_dir
    else:
        output_dir = dir + '/resized'

    if args.width and args.height:
        size = (int(args.width), int(args.height))
    else:
        size = DEFAULT_SIZE

       
    if not os.path.exists(os.path.join(dir, output_dir)):
        os.mkdir(output_dir)

    try:
        for file in os.listdir(input_dir):
            resize_image(input_dir, file, output_dir, size=size)
    except OSError:
        print('file not found')