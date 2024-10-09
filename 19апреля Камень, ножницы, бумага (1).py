from tkinter import *
from random import *

window = Tk()
window.title("Камень, ножницы, бумага")
window.geometry("600x400+950+10")
window.resizable(False, False)
window['bg'] = 'Lime'
count1 = 0
count2 = 0
count3 = 0
global x
global comp


def vqxod():
    print("Игра закончена!")
    exit()


def stonee():
    global x
    stone.config(bg="#FF8C00", activebackground="#f5f75c")
    scissors.config(bg="#00FF7F")
    paper.config(bg="#00FF7F")
    x = "Камень"
    Vknb()


def sscissors():
    global x
    stone.config(bg="#00FF7F")
    scissors.config(bg="#FF8C00", activebackground="#f5f75c")
    paper.config(bg="#00FF7F")
    x = "Ножницы"
    Vknb()


def papier():
    global x
    stone.config(bg="#00FF7F")
    scissors.config(bg="#00FF7F")
    paper.config(bg="#FF8C00", activebackground="#f5f75c")
    x = "Бумага"
    Vknb()


def schet():
    labeltext2.config(text="")
    label12.config(text="")
    if count1 == 1:
        label5.config(bg="blue")
    if count2 == 1:
        label9.config(bg="red")
    if count1 == 2:
        label4.config(bg="blue")
    if count2 == 2:
        label10.config(bg="red")
    if count1 == 3:
        label.config(bg="blue")
    if count2 == 3:
        label11.config(bg="red")
    if count1 == 4:
        label8.config(bg="blue")
    if count2 == 4:
        label6.config(bg="red")
    if count1 == 5:
        label7.config(bg="blue")
        labeltext2.config(text="   ПОБЕДА!", fg="blue")
        label12.config(text="\t  Ещё партию ? Жми старт!", fg="black")
        stone.config(state=DISABLED)
        paper.config(state=DISABLED)
        scissors.config(state=DISABLED)
    if count2 == 5:
        label7.config(bg="red")
        labeltext2.config(text="   ПРОИГРАЛ!", fg="red")
        label12.config(text="\t  Ещё партию ? Жми старт!", fg="black")
        stone.config(state=DISABLED)
        paper.config(state=DISABLED)
        scissors.config(state=DISABLED)


def start():
    global count1
    global count2
    global count3
    label12.config(text="")
    label.config(bg="white")
    label4.config(bg="white")
    label5.config(bg="white")
    label6.config(bg="white")
    label7.config(bg="yellow")
    label8.config(bg="white")
    label9.config(bg="white")
    label10.config(bg="white")
    label11.config(bg="white")
    label4.config(bg="white")

    count1 = 0
    count2 = 0
    count3 = 0

    scissors.config(state=NORMAL)
    stone.config(state=NORMAL)
    paper.config(state=NORMAL)

    label1.config(text="Победы: ",  bg="lime", fg="blue")
    label2.config(text="Проигрыши: ",  bg="lime", fg="red")
    label3.config(text="Ничьи: ",  bg="lime", fg="#808000")

    labeltext.config(text="Готов ?", fg="#4169E1", font=("Arial", 20), bg='lime')

    stone.config(text="Камень", font=("Helvetica", 20), bg="white", fg="black")
    scissors.config(text="Ножницы", font=("Helvetica", 20), bg="white", fg="black")
    paper.config(text="Бумага", font=("Helvetica", 20), bg="white", fg="black")

    labeltext2.config(text="  Делай выбор!", fg="#4169E1", font=("Arial", 20), bg='lime', anchor="center")


def Vknb():
    global x
    global count1
    global count2
    global count3
    knb = ["Камень", "Ножницы", "Бумага"]
    comp = choice(knb)
    color = ["#f0t513", "#15f511", "#11f5f1", "#1120f5", "#11f5", "#f51170"]
    labeltext.config(text=comp, foreground="#1120f5")
    if x == "Бумага" and comp == "Бумага":
        count3 += 1
        label3.config(text="Ничьи: " + str(int(count3)))
    elif x == "Ножницы" and comp == "Ножницы":
        count3 += 1
        label3.config(text="Ничьи: " + str(count3))
    elif x == "Камень" and comp == "Камень":
        count3 += 1
        label3.config(text="Ничьи: " + str(count3))
    elif x == "Бумага" and comp == "Ножницы":
        count2 += 1
        label2.config(text="Проигрыши: " + str(count2))
    elif x == "Бумага" and comp == "Камень":
        count1 += 1
        label1.config(text="Победы: " + str(count1))
    elif x == "Камень" and comp == "Ножницы":
        count1 += 1
        label1.config(text="Победы: " + str(count1))
    elif x == "Камень" and comp == "Бумага":
        count2 += 1
        label2.config(text="Проигрыши: " + str(count2))
    elif x == "Ножницы" and comp == "Камень":
        count2 += 1
        label2.config(text="Проигрыши: " + str(count2))
    elif x == "Ножницы" and comp == "Бумага":
        count1 += 1
        label1.config(text="Победы: " + str(count1))
    schet()


labeltext = Label(window, text="Сыграем?", fg="black", font=("Arial", 20), bg='lime')
labeltext.place(x=230, y=100)

stone = Button(window, text="Камень", font=("Helvetica", 20), bg="white", fg="black", command=stonee)
stone.place(x=50, y=300)

scissors = Button(window, text="Ножницы", font=("Helvetica", 20), bg="white", fg="black", command=sscissors)
scissors.place(x=220, y=300)

paper = Button(window, text="Бумага", font=("Helvetica", 20), bg="white", fg="black", command=papier)
paper.place(x=420, y=300)


label1 = Label(text="Победы: ",  bg="lime", fg="blue")
label1.place(x=20, y=20)

label2 = Label(text="Проигрыши: ",  bg="lime", fg="red")
label2.place(x=20, y=50)

label3 = Label(text="Ничьи: ",  bg="lime", fg="#808000")
label3.place(x=20, y=80)


label = Label(window, text="   ", bg="white")
label.place(x=500, y=20)

label4 = Label(window, text="   ", bg="white")
label4.place(x=475, y=20)

label5 = Label(window, text="   ", bg="white")
label5.place(x=450, y=20)

label6 = Label(window, text="   ", bg="white")
label6.place(x=500, y=50)

label7 = Label(window, text="   ", bg="#ffd700")
label7.place(x=475, y=50)

label8 = Label(window, text="   ", bg="white")
label8.place(x=450, y=50)

label9 = Label(window, text="   ", bg="white")
label9.place(x=500, y=80)

label10 = Label(window, text="   ", bg="white")
label10.place(x=475, y=80)

label11 = Label(window, text="   ", bg="white")
label11.place(x=450, y=80)

labeltext2 = Label(window, text="Делай свой выбор.", fg="black", font=("Arial", 20), bg='lime', anchor="center")
labeltext2.place(x=200, y=200)

exit1 = Button(window, text="Выход", font=("Helvetica", 10), bg="#ADFF2F", activebackground="yellow", command=vqxod)
exit1.place(x=470, y=140)

start1 = Button(window, text="Старт", font=("Helvetica", 10), bg="#ADFF2F", activebackground="yellow", command=start)
start1.place(x=20, y=140)

label12 = Label(window, text="Постарайся закрасить золотой квадрат первым!", fg="black", bg="lime",
                font=("Arial", 17), anchor="center")
label12.place(x=40, y=250)

window.mainloop()
