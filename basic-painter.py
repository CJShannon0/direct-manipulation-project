import tkinter as tk
from tkinter import colorchooser

root = tk.Tk()
colorCode = "#000000"
clearAlert = None

root.title("Basic Painter")
root.geometry("1000x640")
root.minsize(640, 420)
root.configure(bg="#f4f5f6")

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
    clearAlert.title("Clear canvas")
    clearAlert.geometry("360x160")
    clearAlert.resizable(False, False)
    clearAlert.attributes('-topmost', True)
    clearAlert.configure(bg="#f4f5f6")

    popupContent = tk.Frame(clearAlert, bg="#f4f5f6", padx=24, pady=20)
    popupContent.pack(fill="both", expand=True)

    tk.Label(
        popupContent,
        text="Are you sure you want to clear the canvas?",
        bg="#f4f5f6",
        fg="#202124",
        font=("Segoe UI", 11),
    ).pack(anchor="w", pady=(0, 20))

    popupActions = tk.Frame(popupContent, bg="#f4f5f6")
    popupActions.pack(anchor="center")
    buttonStyle = {
        "relief": "flat",
        "bg": "#ffffff",
        "fg": "#202124",
        "activebackground": "#e9ebed",
        "padx": 12,
        "pady": 8,
    }
    tk.Button(
        popupActions,
        text="Cancel",
        command=clearAlert.destroy,
        **buttonStyle,
    ).pack(side="left", padx=(0, 8))
    tk.Button(
        popupActions,
        text="Clear",
        command=clearCanvas,
        **buttonStyle,
    ).pack(side="left")

# Widgets
header = tk.Frame(root, bg="#f4f5f6", padx=24, pady=18)
header.pack(fill="x")

title = tk.Label(
    header,
    text="Basic Painter",
    bg="#f4f5f6",
    fg="#202124",
    font=("Segoe UI", 18, "bold"),
)
title.pack(anchor="w")

workspace = tk.PanedWindow(
    root,
    orient="horizontal",
    bg="#f4f5f6",
    bd=0,
    sashwidth=5,
    sashrelief="flat",
)
workspace.pack(fill="both", expand=True, padx=16, pady=(0, 16))

controls = tk.Frame(workspace, bg="#f4f5f6", width=220, padx=12, pady=12)
controlGroup = tk.Frame(controls, bg="#f4f5f6")
canvasFrame = tk.Frame(workspace, bg="#ffffff")
workspace.add(controls, minsize=190, width=220, stretch="never")
workspace.add(canvasFrame, minsize=400, stretch="always")

controlGroup.pack(fill="x", expand=True)

colorControls = tk.Frame(controlGroup, bg="#f4f5f6")
colorControls.pack(anchor="center")

colorLabel = tk.Label(
    colorControls,
    bg=colorCode,
    width=4,
    height=2,
    relief="flat",
    highlightthickness=1,
    highlightbackground="#d9dcdf",
)
colorLabel.pack(side="left", padx=(0, 10))
colorButton = tk.Button(
    colorControls,
    text="Select color",
    command=chooseColor,
    relief="flat",
    bg="#ffffff",
    fg="#202124",
    activebackground="#e9ebed",
    padx=12,
    pady=8,
)
colorButton.pack(side="left")
brushSizeScale = tk.Scale(
    controlGroup,
    from_=1,
    to=50,
    orient="horizontal",
    label="Brush size",
    bg="#f4f5f6",
    fg="#5f6368",
    highlightthickness=0,
    troughcolor="#dfe2e5",
    activebackground="#5f6368",
    bd=0,
)
brushSizeScale.set(10)
brushSizeScale.pack(fill="x", pady=(20, 0))
clearButton = tk.Button(
    controlGroup,
    text="Clear canvas",
    command=clearPopup,
    relief="flat",
    bg="#ffffff",
    fg="#202124",
    activebackground="#e9ebed",
    padx=12,
    pady=8,
)
clearButton.pack(anchor="center", pady=(16, 0))

canvas = tk.Canvas(canvasFrame, bg="#ffffff", highlightthickness=0)
canvas.bind("<B1-Motion>", paintCanvas)
canvas.pack(fill="both", expand=True)

#main loop
root.mainloop()