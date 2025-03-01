from PIL import Image
import os
from tqdm import tqdm

def convert_images_to_webp(input_path):
    output_path = os.path.join(input_path, 'webp_converted')
    os.makedirs(output_path, exist_ok=True)
    
    if os.path.isdir(input_path):
        files = [os.path.join(input_path, f) for f in os.listdir(input_path) if os.path.isfile(os.path.join(input_path, f))]
    else:
        files = [input_path]
    
    for file in tqdm(files, desc="Converting images"):
        try:
            img = Image.open(file)
            base_name = os.path.basename(file).split('.')[0]
            output_file = os.path.join(output_path, f"{base_name}.webp")
            img.save(output_file, 'webp')
        except Exception as e:
            print(f"Failed to convert {file}: {e}")
    
    return output_path
