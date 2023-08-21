import PIL.Image
import customtkinter as ctk
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageFont


def open_image():
    file_path = filedialog.askopenfilename()
    if file_path:
        global original_image
        image_label.configure(text=file_path)
        original_image = Image.open(file_path)
        image_label.img = ctk.CTkImage(original_image, size=(500, 500))
        image_display.configure(image=image_label.img)

def new_name():
    new_name = new_name_entry.get()
    return new_name

def add_watermark():
    if original_image:
        watermark = watermark_entry.get()
        if watermark:
            img_with_watermark = original_image.copy()
            draw = ImageDraw.Draw(img_with_watermark)
            width, height = img_with_watermark.size
            font = ImageFont.load_default()
            text_width, text_height = draw.textsize(watermark, font=font)
            position = (width - text_width, height - text_height)
            draw.text(position, watermark, fill=(255, 255, 255, 128), font=font)
            image_label.img_with_watermark = ctk.CTkImage(img_with_watermark, size=(500, 500))
            image_display.configure(image=image_label.img_with_watermark)
            name = new_name()
            img_with_watermark.save(fp=f'{name}.jpg')

# GUI

root = ctk.CTk()
root.geometry('800x700')
root.title("Image Watermarking Tool")


image_label = ctk.CTkLabel(root, text="No image selected")
image_label.pack()

open_button = ctk.CTkButton(root, text="Open Image", command=open_image)
open_button.pack()

wmk_label = ctk.CTkLabel(root, text="Enter desired text watermark")
wmk_label.pack()

watermark_entry = ctk.CTkEntry(root, width=300)
watermark_entry.pack()

file_name_label = ctk.CTkLabel(root, text="What name should the new image be saved as:")
file_name_label.pack()

new_name_entry = ctk.CTkEntry(root, width=300)
new_name_entry.pack()

add_watermark_button = ctk.CTkButton(root, text="Add Watermark", command=add_watermark)
add_watermark_button.pack()

image_frame = ctk.CTkFrame(master=root, width=500, height=500)
image_frame.pack()

image_display = ctk.CTkLabel(image_frame, text='')
image_display.pack()


root.mainloop()
