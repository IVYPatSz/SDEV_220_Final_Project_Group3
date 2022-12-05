
btn1 = tk.Button(root, text="Add", font=('Arial',10), command=AddContact)
btn1.place(x=10, y=250)

btn2 = tk.Button(root, text="Remove", font=('Arial',10), command=remove )
btn2.place(x=60, y=250)

btn2 = tk.Button(root, text="Edit", font=('Arial',10), )
btn2.place(x=130, y=250)

btn2 = tk.Button(root, text="Show", font=('Arial',10), command = something)
btn2.place(x=181, y=250)

btn2 = tk.Button(root, text="Reset", font=('Arial',10), command=Reset)
btn2.place(x=240, y=250)

scroll_bar = Scrollbar(root, orient=VERTICAL)
select = Listbox(root, yscrollcommand=scroll_bar.set, height=12)
scroll_bar.config (command=select.yview)