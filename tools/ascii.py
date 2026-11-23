from ascii_magic import AsciiArt # pip install ascii-magic | https://pypi.org/project/ascii-magic/

img = AsciiArt.from_image("image.png")

img.to_image_file(
    path="ascii.png",
    monochrome=True,
    stroke_width=1,
    columns=50
)