import tkinter as tk
from tkinter import font
import requests
import random
from gtts import gTTS
import os

language = 'ru'

HEIGHT = 300
WIDTH = 700
rech = ['Товарищи! ', 'С другой стороны ', 'Равным образом ', 'Не следует, однако, забывать, что ', 'Таким образом ', 'Повседневная практика показывает, что '] 
rech1 = ['реализация намеченных плановых заданий ', 'рамки и место обучения кадров ', '\nпостоянный количественный рост и сфера нашей активности ', 'сложившаяся структура организации ', '\nновая модель организационной деятельности ', 'дальнейшее развитие различных форм деятельности ']
rech2 = ['\nиграет важную роль в формировании ', '\nтребуют от нас анализа ', '\nтребуют определения и уточнения ', '\nспособствует подготовке и реализации ', '\nобеспечивает широкому кругу трудящихся участие в формировании ', '\nразвитие позволяет выполнить важные заданния по разработке ']
rech3 = ['\nсущественных финансовых и административных условий ', '\nдальнейших направлений развития ', '\nсистемы массового участия ', '\nпозиций, занимаемых участниками в отношении поставленных задач ', '\nновых предложений ', '\nнаправлений прогрессивного развития ']



#print(pick + pick1)
#print(pick2 + pick3)

    
def finaltext():

    pick = random.choice(rech)
    pick1 = random.choice(rech1)
    pick2 = random.choice(rech2)
    pick3 = random.choice(rech3)
    label['text'] = (pick + pick1 + pick2 + pick3)
    output = gTTS(text=pick + pick1 + pick2 + pick3, lang=language, slow=False)
    output.save('output.mp3')
    os.system('start output.mp3')
    
root = tk.Tk()

canvas = tk.Canvas (root, height = HEIGHT, width = WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file='1222.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)


frame = tk.Frame(root, bg='red')
frame.place(relx=0.5, rely=0.65, relwidth=0.2, relheight=0.2, anchor='n')


button = tk.Button(frame, fg='red', text = 'РЕЧЬ', font = ('courier', 12,), command=finaltext)
button.place(relx=0.5, rely=0.2, relheight=0.6, relwidth=0.6, anchor = 'n')

upframe = tk.Frame(root, bg='red', bd=5)
upframe.place(relx=0.5, rely=0.1, relwidth=1, relheight=0.3, anchor='n')

label = tk.Label(upframe, font=('Sitkatext',12), anchor='n', bd=1)
label.place(relx=0.5, relwidth=1, relheight=1, anchor='n')               #dont type bd=_ in lower line. i dont know
                                                                         #why but it has fucked everything up




#lower_frame = tk.Frame(root, bg='#508fbf', bd=10)
#lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

#label = tk.Label(lower_frame, font=('Sitkatext', 18), anchor='nw', justify='left', bd=4)
#label.place(relwidth=1, relheight=1)




root.mainloop()

#import random

#rech = ['Товарищи! ', 'С другой стороны ', 'Равным образом ', 'Не следует, однако, забывать, что ', 'Таким образом ', 'Повседневная практика показывает, что '] 
#rech1 = ['реализация намеченных плановых заданий ', 'рамки и место обучения кадров ', 'постоянный количественный рост и сфера нашей активности ', 'сложившаяся структура организаци ', 'новая модель организационной деятельности ', 'дальнейшее развитие различных форм деятельности ']
#rech2 = ['играет важную роль в формировании ', 'требуют от нас анализа ', 'требуют определения и уточнения ', 'способствует подготовке и реализации ', 'обеспечивает широкому кругу трудящихся участие в формировании ', 'развитие позволяет выполнить важные заданния по разработке ']
#rech3 = ['существенных финансовых и административных условий ', 'дальнейших направлений развития ', 'системы массового участия ', 'позиций, занимаемых участниками в отношении поставленных задач ', 'новых предложений ', 'направлений прогрессивного развития ']

#pick = random.choice(rech)
#pick1 = random.choice(rech1)
#pick2 = random.choice(rech2)
#pick3 = random.choice(rech3)

#print(pick + pick1)
#print(pick2 + pick3)
