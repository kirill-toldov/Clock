import tkinter as tk
import tkinter.messagebox as mb
import time
import pygame

class Clock:
    def __init__(self):
        self.time_mode=True
        self.alarm_time=None
        
        self.window=tk.Tk()
        self.window.title=('Часы')

        #время
        self.label=tk.Label(self.window,text=self.get_time())
        self.label.pack(side='top')

        #кнопки управления
        self.h_button=tk.Button(self.window,text='H',command=self.h_up,bg = "white")
        self.h_button.pack(side='left')
        
        self.m_button=tk.Button(self.window,text='M',command=self.m_up,bg = "white")
        self.m_button.pack(side='left')

        self.a_button=tk.Button(self.window,text='A',command=self.alarm_set,bg = "white")
        self.a_button.pack(side='left')

        self.exit_button=tk.Button(self.window, text='Выйти', command=self.window.destroy,bg = "white")
        self.exit_button.pack(side='bottom')
        
        self.refresh()
        
        self.window.mainloop()

    #перевод часов, минут и секунд в формат времени вида h:m:s
    def to_time_format(self,h,m,s):
        return h+":"+m+":"+s

    #получение текущего времени
    def get_time(self):
        t=time.asctime()[11:19]
        self.h=t[0:2]
        self.m=t[3:5]
        self.s=t[6:8]
        return self.to_time_format(self.h,self.m,self.s)

    #обновление часов на экране
    def refresh(self):
        if self.time_mode:
            self.label['text'] = text=self.get_time()
        if self.label['text'] == self.alarm_time:
            self.alarm()
        self.label.after(250, self.refresh)

    #пока бесполезно
    def renum(self):
        None

    #функции установки времени будильника
    def h_up(self):
        if self.alarm_time==None:
            self.time_mode=False
            self.label['text']=str(int(self.label['text'][0:2])+1).zfill(2)+self.label['text'][2:6]+"00"
            if self.label['text'][0:2]=='25':
                self.label['text']='00'+self.label['text'][2:8]
            
    def m_up(self):
        if self.alarm_time==None:
            self.time_mode=False
            self.label['text']=self.label['text'][0:3]+str(int(self.label['text'][3:5])+1).zfill(2)+self.label['text'][5:6]+"00"
            if self.label['text'][3:5]=='60':
                self.h_up()
                self.label['text']=self.label['text'][0:3]+'00'+self.label['text'][5:8]
        
    def alarm_set(self):
        if self.alarm_time==None:
            self.a_button.config(bg = "red")
            self.alarm_time=self.label['text']
            self.time_mode=True
        else:
            self.alarm_time=None
            self.a_button.config(bg = "white")
            self.time_mode=True
            
    #непосредственно сам будильник
    def alarm(self):
        pygame.mixer.init()
        pygame.mixer.music.load('alarm.mp3')
        pygame.mixer.music.play()
        ans = mb.askyesno("Будильник", "Перенести на пять минут?")
        if ans:
            m=int(self.m)+5
            if m>=60:
                h=int(self.h)+1
                m-=60
            else:
                h=int(self.h)
            self.alarm_time=self.to_time_format(str(h),str(m),"00")               
        else:
            self.a_button.config(bg = "white")
            self.alarm_time=None

#запуск программы
Clock()







