from tkinter import *
root=Tk()
root.title("Multidimentional Arrays")

root.geometry("500x500")
label= Label(root)


array_1d = ["John", "James", "Thomsan"]
print(array_1d[0])

array_2d = [["john","A"], ["james","B"], ["Thomsan","C"]]
print(array_2d[0][1])

array_3d = [[["Jhon","A+","Excellent"],["James","A","Very Good"],["Thomsan","B","Good"]]]
print(array_3d[0][1][2])

def report():
    label["text"] = array_3d[0][1][0] + " got grade " + array_3d[0][1][1] +" and he is doing"
    +array_3d[0][1][2]
    
btn = Button(root, text= "show report", command = report)
btn.place(relx = 0.5, rely =0.5, anchor = CENTER)

label.place(relx = 0.5, rely =0.6, anchor = CENTER)

root.mainloop()    