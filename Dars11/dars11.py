from tkinter import *
from tkinter.messagebox import *

oyna=Tk()
oyna.geometry("500x100")


python_list=('bool','int','float','complex','str','if','for','while','match','bool','int','float','complex','str','if','for','while','match','bool','int','float','bool','int','float','complex','str','if','for','while','match','bool','int','float','complex','str','if','for','while','match','bool','int','float','complex','str','if','complex','str','if','for','while','match','bool','int','float','complex','str','if','for','while','match')

var=Variable(value=python_list)

listbox=Listbox(oyna,height=200,listvariable=var,selectmode=SINGLE)


scrollv=Scrollbar(oyna,orient=VERTICAL,command=listbox.yview)

listbox['yscrollcommand']=scrollv.set

scrollv.pack(side=LEFT,fill=Y)

listbox.pack(fill=BOTH)



def item_select(args):
    selected=listbox.curselection()
    t="\n".join([listbox.get(i) for i in selected])
    print(t)
    match t:
        case 'if':
            oyna2=Toplevel()
            oyna2.geometry("400x400")


listbox.bind("<<ListboxSelect>>",item_select)


oyna.mainloop()