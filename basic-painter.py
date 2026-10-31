import tkinter as tk
from tkinter import colorchooser

root = tk.Tk()
colorCode = "#000000"
clearAlert = None

#event handlers
    #canvas painting
def paintCanvas(event):
    # print(f"painting on coord ({event.x}, {event.y})")
    cc = colorCode
    bs = brushSizeScale.get()
    canvas.create_oval(event.x-bs,event.y-bs,event.x+bs,event.y+bs, fill=cc, outline=cc)

def chooseColor():
    global colorCode
    selectedColor = colorchooser.askcolor(title="Choose color")[1]
    # print(colorCode)
    if(selectedColor is not None):
        colorCode = selectedColor
        colorLabel.config(bg=colorCode)

def clearCanvas():
    global canvas
    global clearAlert
    canvas.delete("all")
    clearAlert.destroy()

def clearPopup():
    global clearAlert
    clearAlert = tk.Toplevel(root)
    clearAlert.geometry("300x200")
    clearAlert.attributes('-topmost', True)
    tk.Label(clearAlert, text="Are you sure you want to clear the canvas?").grid(row=0, columnspan=2)
    tk.Button(clearAlert, text="Cancel", command=clearAlert.destroy).grid(row=1, column=0)
    tk.Button(clearAlert, text="Clear", command=clearCanvas).grid(row=1, column=1)

# Widgets
title = tk.Label(root, text="Basic Painter").grid(row=0, columnspan=2)

firstColumn = tk.PanedWindow(root, width=240, height=510, orient="horizontal")
controls = tk.Frame(firstColumn)
firstColumn.add(controls)

colorLabel = tk.Label(controls, bg=colorCode)
colorLabel.grid(row=0, column=0)
colorButton = tk.Button(controls, text="Select Color", command=chooseColor)
colorButton.grid(row=0, column=1)
brushSizeScale = tk.Scale(controls, from_=1, to=50, orient="horizontal")
brushSizeScale.set(10)
brushSizeScale.grid(row=1, columnspan=2)
clearButton = tk.Button(controls, text="Clear Canvas", command=clearPopup)
clearButton.grid(row=2, columnspan=2)


secondColumn = tk.PanedWindow(root, width=760, height=510, orient="horizontal")
canvas = tk.Canvas(secondColumn, width=750, height=500, bg="white")
canvas.bind("<B1-Motion>", paintCanvas)
secondColumn.add(canvas)


firstColumn.grid(row=1, column=0)
secondColumn.grid(row=1, column=1)

#main loop
root.mainloop()