from PIL import Image
import os

# Files to convert
workspace_root = os.path.dirname(os.path.dirname(__file__))
files = [
    os.path.join(workspace_root, 'logo.png'),
    os.path.join(workspace_root, 'giftcard.jpg'),
]

output_names = [
    os.path.join(workspace_root, 'logo.jpg'),
    os.path.join(workspace_root, 'giftcard.jpg'),
]

for src, dst in zip(files, output_names):
    if not os.path.exists(src):
        print(f"Source not found: {src}")
        continue

    print(f"Converting: {src} -> {dst}")
    with Image.open(src) as im:
        # If the image has an alpha channel, paste over a white background
        if im.mode in ('RGBA', 'LA') or (im.mode == 'P' and 'transparency' in im.info):
            background = Image.new('RGB', im.size, (255, 255, 255))
            background.paste(im.convert('RGBA'), mask=im.convert('RGBA').split()[3])
            im_rgb = background
        else:
            im_rgb = im.convert('RGB')

        im_rgb.save(dst, 'JPEG', quality=95)

print('Done')
