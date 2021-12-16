from pathlib import WindowsPath
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import sys

def resize_image(image: Image.Image, new_max_sidelength):
    size = image.size 
    bigger_side_length = max(size)
    new_size = (new_max_sidelength*size[0]/bigger_side_length, new_max_sidelength*size[1]/bigger_side_length)
    new_size = tuple(map(int, new_size))
    image = image.resize(new_size)
    return image, new_size



def main():
    if len(sys.argv) <= 1:
        print("enter at least one argument - the image name")
        return 1

    image_filename = sys.argv[1]    
    image_PIL = Image.open(image_filename) 
    image_PIL, new_size = resize_image(image_PIL, 950)

    output_filename = "output_file.csv"
    if len(sys.argv) == 3:
        output_filename = sys.argv[2]
        

    window = tk.Tk()

    image_tk = ImageTk.PhotoImage(image_PIL)
    window.geometry("1000x1000")

    canvas = tk.Canvas(window, width=new_size[0], height=new_size[1], background="blue") 

    canvas.create_image(0, 0, image=image_tk, anchor=tk.NW)

    canvas.place(x=(1000 - new_size[0])/2, y=(1000 - new_size[1])/2)

    def on_click(event, list_of_coords):
        print(event.x, event.y)
        list_of_coords.append((event.x, event.y))

    list_of_coords = []
    canvas.bind("<Button-1>", lambda event: on_click(event, list_of_coords))

    def on_undo(event, list_of_coords):
        list_of_coords.pop(-1)
    
    window.bind("<U>", lambda event: on_undo(event, list_of_coords))

    def on_closing():
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            # write to file
            with open(output_filename, "w") as f:
                f.truncate(0)
                for x, y in list_of_coords:
                    f.write(f"{x}, {y}\n")

            window.destroy()

    window.protocol("WM_DELETE_WINDOW", on_closing)

    window.mainloop()

if __name__ == "__main__":
    main()