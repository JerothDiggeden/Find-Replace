import customtkinter as ctk



def find():
    find_data = box_find.get("1.0", "end-1c")
    rep_data = box_replace.get("1.0", "end-1c")
    data = box_code.get("1.0", "end-1c")
    data_split = data.split(" ")
    print(data_split)
    for f in data_split:
        if f == find_data:
            f.replace(find_data, rep_data)
            data_join = rep_data.join(data_split)
    print(data_join)

# ITTERATE OVER EACH LETTER IN WORD, COUNT, AND SLICE WORD TO HAVE A SPACE AT THE END

root = ctk.CTk()
root.geometry('1000x750')
root.title('Find and Replace')

lbl_title = ctk.CTkLabel(master=root, text='Find-Replace', height=50, font=('Verdana Bold', 60))
lbl_title.pack(padx=1, pady=1)
# FIND
lbl_find = ctk.CTkLabel(master=root, text='FIND...', height=50, width=900, font=('Verdana Bold', 20), anchor="w")
lbl_find.pack(padx=1, pady=1)
box_find = ctk.CTkTextbox(master=root, width=900, height=25)
box_find.pack()
# REPLACE
lbl_replace = ctk.CTkLabel(master=root, text='REPLACE...', height=50, width=900, font=('Verdana Bold', 20), anchor="w")
lbl_replace.pack(padx=1, pady=1)
box_replace = ctk.CTkTextbox(master=root, width=900, height=25)
box_replace.pack()
# CODE
lbl_code = ctk.CTkLabel(master=root, text='CODE...', height=50, width=900, font=('Verdana Bold', 20), anchor="w")
lbl_code.pack(padx=1, pady=1)
box_code = ctk.CTkTextbox(master=root, width=900, height=400)
box_code.pack()
# BUTTON
btn_fr = ctk.CTkButton(master=root, text="Find & Replace", width=900, command=find)
btn_fr.pack(padx=1, pady=1)

root.mainloop()

