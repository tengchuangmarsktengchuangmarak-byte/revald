from PIL import Image
import os
import colorsys

workspace_root = os.path.dirname(os.path.dirname(__file__))
files = [
    os.path.join(workspace_root, 'logo.jpg'),
    os.path.join(workspace_root, 'giftcard.jpg'),
]
output_names = [
    os.path.join(workspace_root, 'logo_blue.jpg'),
    os.path.join(workspace_root, 'giftcard_blue.jpg'),
]

# Aldi blue hue (in 0..1); equivalent to about #003087
target_hex = (0, 48, 135)
target_hue = colorsys.rgb_to_hsv(target_hex[0]/255.0, target_hex[1]/255.0, target_hex[2]/255.0)[0]

def rgb_to_hsv_pixel(r, g, b):
    return colorsys.rgb_to_hsv(r/255.0, g/255.0, b/255.0)

def hsv_to_rgb_pixel(h, s, v):
    rgb = colorsys.hsv_to_rgb(h, s, v)
    return (int(rgb[0]*255), int(rgb[1]*255), int(rgb[2]*255))

for src, dst in zip(files, output_names):
    if not os.path.exists(src):
        print(f"Source not found: {src}")
        continue

    print(f"Recoloring: {src} -> {dst}")
    with Image.open(src) as im:
        im = im.convert('RGB')
        w, h = im.size
        pixels = im.load()

        for y in range(h):
            for x in range(w):
                r, g, b = pixels[x, y]
                hsv = rgb_to_hsv_pixel(r, g, b)
                hue, sat, val = hsv
                # Detect red-ish hues near 0 (or near 1 due to circular hue)
                is_red = (hue < 0.07 or hue > 0.93) and sat > 0.15 and val > 0.08
                if is_red:
                    # Replace hue with target blue, keep saturation and value
                    nh = target_hue
                    ns = min(1.0, sat * 1.05)
                    nv = val
                    nr, ng, nb = hsv_to_rgb_pixel(nh, ns, nv)
                    pixels[x, y] = (nr, ng, nb)

        im.save(dst, 'JPEG', quality=95)

print('Done')
