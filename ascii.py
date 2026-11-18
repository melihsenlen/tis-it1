from ascii_magic import AsciiArt # pip install ascii-magic | https://pypi.org/project/ascii-magic/

img = AsciiArt.from_image("media/background.png")

img.to_image_file(
    "ascii_image.png",
    monochrome=True,
    stroke_width=1,
    columns=250
)