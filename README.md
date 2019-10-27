# everyday_python
Learning Python day by day. 

## How to use resize_images.py script 
`python resize_images.py --input_dir=path/to/the/folder/with/pictures --output_dir=path/to/the/new/folder `
If folder is not specified the script will create the resized folder next to resize_image.py script.

DEFAULT size is width=1024 and height=768, if the width is shorter than height the width=768 and height=1024

but the size of resized images can be changed in command line
`python resize_image.py --width=320 --height=180`