import tkinter
from tkinter import Tk,Button, filedialog, Radiobutton
from ErrorWindow import ErrorWindows
import config
from CommonUtils import CommonUtils

import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import ( FigureCanvasTkAgg, NavigationToolbar2Tk)
import pandas as pd
@add_settings("Анализ стоимости")
class MainApp(Tk):
    def __init__(self, *arg, **kwarg):
        super().__init__(*arg, **kwarg)
        self.result_dict={}
        self.ax = None
        self.canvas= None
        self.tk_widget= None
        self.toolbar= None
        self.draw =False
        self.line=True
        self.var.set(0)
        self.button_load= Button(self,text="Выбрать файл",padx=150,pady=10, command=lambda: self.load_file())
        self.button_visual = Button(self, text="Отобразить", padx=150, pady=10, command=lambda: self.create_visualization())
        position ={"relx":0.6,"rely":0.01}
        self.button_load.place(relx=0.1,rely=0.01)
        self.button_visual.place(relx=0.1, rely=0.11)
        item=0
        for graphic_type in config.types_of_graphic:
            lang_btn = Radiobutton(text=graphic_type,value=item,variable=self.var)
            lang_btn.place(**position)
            position["rely"]=0.11
            item+=1
        self.graph()
    def load_file(self):
        filepath = filedialog.askopenfilename()
        if filepath !="":
            self.draw,self.result_dict=CommonUtils.load_txt(filepath)
    def create_visualization(self):
        if len(self.result_dict)>0
            self.graph()
        else:
            ErrorWindows(self,config.errorTextImport)
    def graph(self):
        if  (self.tk_widget != None):
            try:
                self.ax.clear()
            except:
                print("Нет объекта")
            self.tk_widget.place_forget()
            self.toolbar.place_forget()
        fig=Figure(figsize=(9,5),dpi=100)
        if(self.draw):
            self.ax =fig.add_subplot(111)
            self.ax.grid(lw=0.5,ls='--')
        xdata = np.array(self.result_dict['date'],dtype='datetime64')
        if self.var.get()==0:
            self.ax.plot(xdata,self.result_dict['close'])
        else:
            dates =pd.DatetimeIndex(self.result_dict['date'])
            t=dates.month
            start=1
            index=0
            new_dict={'open': [], 'close': [], 'high':[], 'low':[],'date': [dates[0]]}
            open=[]
            close=[]
            high=[]
            low=[]
            for item in t:
                if(item==start):
                    open.append(self.result_dict['open'][index])
                    close.append(self.result_dict['close'][index])
                    high.append(self.result_dict['high'][index])
                    low.append(self.result_dict['low'][index])
                else:
                    new_dict['open'].append(open[0])
                    new_dict['close'].append(close[-1])
                    new_dict['high'].append(np.max(np.array(high)))
                    new_dict['low'].append(np.max(np.array(low)))
                    new_dict['date'].append(dates[index])
                    open=[]
                    close=[]
                    high=[]
                    low=[]
                    open.append(self.result_dict['open'][index])
                    close.append(self.result_dict['close'][index])
                    high.append(self.result_dict['high'][index])
                    low.append(self.result_dict['low'][index])
                    start+=1
                index+=1
                if(start==13):
                    start-=1
                pass
            new_dict['open'].append(open[0])
            new_dict['close'].append(close[-1])
            new_dict['high'].append(np.max(np.array(high)))
            new_dict['low'].append(np.max(np.array(low)))

            prices=pd.DataFrame({'open': new_dict['open'],'close': new_dict['close'],'high': new_dict['high'],'low': new_dict['low']},index=new_dict['date'])
            print(prices)
            