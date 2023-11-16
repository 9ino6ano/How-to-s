from PIL import Image, ImageFont, ImageDraw

my_image=Image.open("textimage2.jpg")
title_font=ImageFont.truetype("arial.ttf",150)
title_text="9ino6ano Productions"
image_editable=ImageDraw.Draw(my_image)
image_editable.text((300,300),title_text,("red"),font=title_font)
my_image.save("text_result.jpg")

