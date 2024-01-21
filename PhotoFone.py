from rembg import remove
from PIL import Image
from pathlib import Path
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def bg_remover():
    list_of_extensions=["*.png", "*.jpg", "*.jpeg"]
    all_files=[]

    for ext in list_of_extensions:
        all_files.extend(Path('input_img').glob(ext))

    for i in all_files:
        input_path=Path(i)
        file_name = input_path.stem
        output_path=f'output_img/{file_name}_bgremoved.png'
        input_img=Image.open(input_path)
        output_img=(remove(input_img)).save(output_path)

def main():
    bg_remover()
if __name__=='__main__':
    main()
##CUBRIKK##