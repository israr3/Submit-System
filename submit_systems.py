from tkinter import *

def submit():
    submit = entry.get()
    print(submit)

def delete():
    entry.delete(0,END)

def backspace():
    entry.delete(len(entry.get())-1,END)
    
def exit_program():
    exit()

windows=Tk()
entry = Entry(windows,
               font=('sans-serif',50,'bold'),
              fg="#00FF00",
              bg="black",
              show='*'
              )
entry.insert(0,'Enter Text')
entry.pack(side=LEFT)

submit_button = Button(windows,text='submit',padx=10,pady=10 ,command=submit)
submit_button.pack(side=RIGHT)

delete_button = Button(windows,text='delete', padx=10,pady=10 ,command=delete)
delete_button.pack(side=RIGHT)


backspace_button = Button(windows,text='backspace', padx=10,pady=10 ,command=backspace)
backspace_button.pack(side=RIGHT)

exit_button = Button(windows,text='exit', padx=10,pady=10 ,command=exit_program)
exit_button.pack(side=RIGHT)



windows.mainloop()