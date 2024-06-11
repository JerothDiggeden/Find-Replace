import customtkinter as ctk
import pyperclip


# ITTERATE OVER EACH LETTER IN WORD, COUNT, AND SLICE WORD TO HAVE A SPACE AT THE END
def find():
    find_data = box_find.get("1.0", "end-1c")
    rep_data = box_replace.get("1.0", "end-1c")
    data = box_txt_f.get("1.0", "end-1c")
    data_split = data.split(" ")
    data_split_copy = data_split.copy()
    # REMOVE WORD/S
    for f in range(len(data_split_copy)):
        if find_data in data_split_copy[f]:
            data_split.remove(data_split_copy[f])
    # JOIN WORDS INTO STRING
    for s in range(len(data_split)):
        data_split[s] = data_split[s] + " "
    result = ""
    # CREATE STRING
    for j in range(len(data_split)):
        result += data_split[j]
    frame1.pack_forget()
    frame2.pack(fill=ctk.BOTH, expand=True)
    return result




def copy():
    pyperclip.copy(box_txt_n.get("1.0", "end-1c"))


def insert():
    result_copy = find()
    box_txt_n.insert("1.0", result_copy)


def first():
    frame2.pack_forget()
    frame1.pack(fill=ctk.BOTH, expand=True)


root = ctk.CTk()
root.geometry('900x775')
root.title('Find and Replace')
ctk.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"

result = ""


#FRAME 1
frame1 = ctk.CTkFrame(root)
frame1.pack(side=ctk.LEFT)
lbl_title = ctk.CTkLabel(master=frame1, text='Find-Replace', height=50, font=('Verdana Bold', 60))
lbl_title.pack(padx=1, pady=1)
# FIND
lbl_find = ctk.CTkLabel(master=frame1, text='FIND...', height=50, width=900, font=('Verdana Bold', 20), anchor="w")
lbl_find.pack(padx=1, pady=1)
box_find = ctk.CTkTextbox(master=frame1, width=900, height=25)
box_find.pack()
# REPLACE
lbl_replace = ctk.CTkLabel(master=frame1, text='REPLACE...', height=50, width=900, font=('Verdana Bold', 20), anchor="w")
lbl_replace.pack(padx=1, pady=1)
box_replace = ctk.CTkTextbox(master=frame1, width=900, height=25)
box_replace.pack()
# TEXT
lbl_txt_f = ctk.CTkLabel(master=frame1, text='TEXT...', height=50, width=900, font=('Verdana Bold', 20), anchor="w")
lbl_txt_f.pack(padx=1, pady=1)
box_txt_f = ctk.CTkTextbox(master=frame1, width=900, height=400)
box_txt_f.pack()
# BUTTON
btn_fr = ctk.CTkButton(master=frame1, text="FIND & REPLACE", width=900, command=insert)
btn_fr.pack(padx=1, pady=1)

#FRAME 2
frame2 = ctk.CTkFrame(root)
lbl_title = ctk.CTkLabel(master=frame2, text='Find-Replace', height=50, font=('Verdana Bold', 60))
lbl_title.pack(padx=1, pady=1)
# TEXT
lbl_txt_n = ctk.CTkLabel(master=frame2, text='NEW TEXT...', height=50, width=900, font=('Verdana Bold', 20), anchor="w")
lbl_txt_n.pack(padx=1, pady=1)
box_txt_n = ctk.CTkTextbox(master=frame2, width=900, height=580)
box_txt_n.pack()
# BUTTONS
btn_cp = ctk.CTkButton(master=frame2, text="COPY", width=900, command=copy)
btn_cp.pack(padx=1, pady=1)
btn_cp = ctk.CTkButton(master=frame2, text="BACK", width=900, command=first)
btn_cp.pack(padx=1, pady=1)

root.mainloop()
