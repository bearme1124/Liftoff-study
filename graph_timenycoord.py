import pyautogui
from tkinter import *
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
import pandas as pd

# 스코프 클래스 정의
class Scope(object):
    # 초기 설정
    def __init__(self, ax, fn, xmax, ymax, xstart, ystart, title_name = 'Mouse Pointer', xlabel = 'Time', ylabel = 'Y_coordinate'):
        self.xmax = xmax #x축 길이
        self.xstart = xstart #x축 시작점
        self.ymax = ymax #y축 길이
        self.ystart = ystart #y축 시작점

        # 그래프 설정
        self.ax = ax 
        self.ax.set_xlim((self.xstart,self.xmax))
        self.ax.set_ylim((self.ystart,self.ymax))
        self.ax.set_title(title_name)
        self.ax.set_xlabel(xlabel)
        self.ax.set_ylabel(ylabel)

        # dataFrame 설정
        self.df = pd.DataFrame(columns = ['time', 'value'])

        self.x = [0] # x축 초기값 
        self.y = [540] # y축 초기값
        self.value = 0
        self.df = self.df.append({'time' : 0, 'value' : 540}, ignore_index = True)
        self.fn = fn
        self.line, = ax.plot([],[])

        self.ti = time.time() #현재시각
        print("초기화 완료")

    # 그래프 업데이트 설정
    def update(self, i):
        # 시간차
        tempo = time.time()-self.ti
        self.ti = time.time() #시간 업데이트
        
        # 값 넣기
        self.value = self.fn()# y값 함수 불러오기
        self.y.append(self.value) #y값 넣기
        self.x.append(tempo + self.x[-1]) #x값 넣기
        self.line.set_data(self.x,self.y)
        
        # csv 파일 업데이트
        new_data = {'time' : tempo + self.x[-1], 'value' : self.value}
        self.df = self.df.append(new_data, ignore_index = True)

        if self.x[-1] >= self.xstart + self.xmax:
            plt.savefig('savefig_default.png') #png 파일 추출
            self.df.to_csv('savecsv_default.csv')#csv 파일 추출
            return True
            
        """
        # 화면에 나타낼 x축 범위 업데이트
        if self.x[-1] >= self.xstart + self.xmax :
            #전체 x값중 반을 화면 옆으로 밀기
            self.xstart = self.xstart + self.xmax/2
            self.ax.set_xlim(self.xstart,self.xstart + self.xmax)

            self.ax.figure.canvas.draw()
        """
        
        return (self.line, )

# y축에 표현할 값을 반환해야하고 scope 객체 선언 전 선언해야함.
def insert():
    x, y = pyautogui.position()
    value = 1080 - y
    return value 

# Start 버튼 클릭 시 (960, 540)으로 이동 후, 그래프 그리기 시작
def btn_click(event):
    pyautogui.moveTo(960, 540)

    #그래프 설정
    fig, ax = plt.subplots()
    #Full Screen 설정
    manager = plt.get_current_fig_manager()
    manager.full_screen_toggle()
    ax.grid(True)

    # 객체 생성
    scope = Scope(ax, insert, xmax=100, xstart=0, ymax=1080, ystart=0)
    
    # update 매소드 호출
    ani = animation.FuncAnimation(fig, scope.update, frames=200, interval=10, blit=True)
    
    plt.show()

#Start 버튼 생성
root = Tk()
b1 = Button(root, text='Start')
b1.pack()

b1.bind('<ButtonRelease-1>', btn_click)
root.mainloop()