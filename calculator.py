import tkinter as t
def press(num):
    T.insert(t.END,str(num))
def equal():
    try:
        result=eval(T.get())
        T.delete(0,t.END)
        T.insert(t.END,str(result))
    except:
        T.delete(0,t.END)
        T.insert(t.END,"ERROR")
def clear():
    T.delete(0,t.END)
root=t.Tk()
root.title("Calculator")
root.geometry("300x400")
T=t.Entry(root,font=("Arial",18),bd=10,insertwidth=2,width=14,borderwidth=4,justify='right')
T.grid(row=0,column=0,columnspan=4,padx=10,pady=10)
btn=[('7',1,0),('8',1,1),('9',1,2),('/',1,3),
('4',2,0),('5',2,1),('6',2,2),('*',2,3),
('1',3,0),('2',3,1),('3',3,2),('-',3,3),
('0',4,0),('.',4,1),('=',4,2),('+',4,3)]
for(txt,row,col) in btn:
    if txt == '=' :
        btn=t.Button(root,text=txt,padx=20,pady=20,font=("Arial",12),command=equal)
    else:
        btn=t.Button(root,text=txt,padx=20,pady=20,font=("Arial",12),command=lambda t=txt : press(t))
    btn.grid(row=row,column=col)
clear_btn=t.Button(root,text="Clear",padx=20,pady=20,font=("Arial",12),command=clear)
clear_btn.grid(row=5,column=0,columnspan=4)
root.mainloop()