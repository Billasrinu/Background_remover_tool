from rembg  import remove
from PIL import Image
input_path= 'PHOTO2.webp' # Mention the photo path
output_path= 'removed.png' # Mention the path and the name of the new edited photo
input=Image.opern(input_path)
output = remove(input)
output.save(output_path)
