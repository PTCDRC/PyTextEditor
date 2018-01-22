#PyTextEdit.py Simple text editor
#Python2.7

import os
from Tkinter import *
import Tkinter, tkFileDialog, ttk, tkMessageBox


#editor
class editor():

    #All basic functions
    #initiate window GUI
    def window_init(self):
        self.root=Tk()
        self.root.wm_state('normal')
        self.root.title('PyTextEditor')

        #contains the actions
        self.text_write()
        self.text_label()

    #write text
    def text_write(self):
        self.editor = Text(self.root)
        self.editor.config(bg='#eeefff', fg='#411d47', width=100,wrap=WORD,padx=5,pady=5, insertbackground='#eeefff')
        self.editor.pack(fill=Y, expand=1)

    def text_label(self):
        self.status = Label(self.root)
        self.status.config(text='New File', anchor=W)
        self.status.pack(expand=0, fill=X)


    #Initiate a menu and its functions: Open, Save, Save as, New
    def menu_init(self):
        self.menu_bar=Menu(self.root)
        self.menu_bar.config(bg='#eeefff', borderwidth=1)

        def menu_init(label, layout):
            menu = Menu(self.menu_bar, tearoff=0)
            self.menu_bar.add_cascade(label=label, menu=menu)

            for i in layout:
                sub_label = i[0]
                command = i[1]

                menu.add_command(label=sub_label, command=command)

        #Define list of functions in menu
        menu_init("File", [["New", self.new_file],
                            ["Open", self.open_file],
                            ["Save", self.save_file],
                            ["Save as..", self.save_file_as],
                            ["Exit", self.root.quit]])

        self.root.config(menu=self.menu_bar)

    #Menu functions
    def open_file(self):
        path = tkFileDialog.askopenfilename()
        the_file = open(path, 'r')
        content = str(the_file.read())
        the_file.close()

        self.path = path
        self.status.config(text=path)
        self.root.update_idletasks()
        self.editor.delete('1.0', 'end')
        self.editor.insert('1.0', content)

    def save_file(self):
        the_file = open(self.path, 'w')
        the_file.write(self.editor.get('1.0', 'end'))
        the_file.close()

    def save_file_as(self):
        path = tkFileDialog.asksaveasfilename()
        the_file = open(path, 'w')
        the_file.write(self.editor.get('1.0', 'end'))
        the_file.close()

    def new_file(self):
        editor = self.editor.get('1.0', 'end')
        print(len(editor))
        if len(editor) > 1:
            answer = tkFileDialog.askokcancel('Are you sure?', 'Discard current changes?')
        if answer == True:
            self.editor.delete('1.0', 'end')
            self.status.config(text = 'New File')

    def __init__(self):

        self.path = None

        self.window_init()
        self.menu_init()




app = editor()

if __name__ == '__main__':
    app.root.mainloop()
