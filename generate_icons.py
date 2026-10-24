import os
import math
from PIL import Image, ImageDraw

def create_firefox_icon():
    sizes = [(256, 256), (128, 128), (64, 64), (48, 48), (32, 32), (16, 16)]
    images = []

    for w, h in sizes:
        img = Image.new("RGBA", (w, h), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)

        # Círculo base con degradado Firefox (naranja a fucsia a púrpura)
        center_x, center_y = w / 2, h / 2
        radius = min(w, h) * 0.44

        # Dibujar fuego / llama exterior
        for r in range(int(radius), 0, -1):
            ratio = r / radius
            red = int(255 * (1 - ratio * 0.3))
            green = int(113 * (1 - ratio * 0.5))
            blue = int(57 + (198 - 57) * (1 - ratio))
            alpha = int(255 * min(1.0, ratio * 1.5))
            draw.ellipse(
                [center_x - r, center_y - r, center_x + r, center_y + r],
                fill=(red, green, blue, alpha)
            )

        # Núcleo interior azul/cian (el planeta de Firefox)
        inner_r = radius * 0.58
        for r in range(int(inner_r), 0, -1):
            ratio = r / inner_r
            r_col = int(20 + 30 * ratio)
            g_col = int(100 + 80 * ratio)
            b_col = int(230 + 25 * ratio)
            draw.ellipse(
                [center_x - r + inner_r*0.15, center_y - r - inner_r*0.1,
                 center_x + r + inner_r*0.15, center_y + r - inner_r*0.1],
                fill=(r_col, g_col, b_col, 240)
            )

        images.append(img)

    assets_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "shared", "assets")
    os.makedirs(assets_dir, exist_ok=True)

    ico_path = os.path.join(assets_dir, "foxquantum.ico")
    png_path = os.path.join(assets_dir, "foxquantum.png")

    images[0].save(png_path, format="PNG")
    images[0].save(ico_path, format="ICO", sizes=[(s[0], s[1]) for s in sizes])
    print(f"Iconos generados exitosamente en:\n - {ico_path}\n - {png_path}")

if __name__ == "__main__":
    create_firefox_icon()
