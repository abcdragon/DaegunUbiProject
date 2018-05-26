from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilenames
import upload
import download

class body:
    def __init__(self): # 각종 컴포넌트 등을 초기화
        self.active=False

        self.root = Tk();self.root.title("FTP 파일 공유 시스템") # GUI 초기화와 타이틀 지정
        self.root.geometry('505x385') # window 크기조정
        mycolor='#%02x%02x%02x' % (163, 204, 163)
        self.root.config(bg=mycolor)
        self.root.resizable(0,0) # x와 y 축으로 window 크기를 늘이는 것을 못하게 막음
        self.root.protocol("WM_DELETE_WINDOW", self.close)

        self.menu = Menu(self.root)
        self.root.config(menu=self.menu)
        file = Menu(self.menu)
        file.add_command(label='Download', command=self.showDownloadWindow)
        file.add_command(label='Exit', command=self.close)
        self.menu.add_cascade(label='File', menu=file)

        self.fList = Listbox(self.root,width=69,height=20,bg='white') # width ==> 한 줄에 들어갈 '문자 수', height==> 줄 수
        self.fList.grid(padx=9,pady=5,row=0,column=0,columnspan=3,sticky=E+W) # colmnspan 가로로 덮을 공간 따라서 0~3만큼의 공간을 덮는다.
        self.fList.config(selectmode='multiple')

        self.insBtn = Button(self.root, text="파일 등록", width=20, height=2, command=self.ins)
        self.insBtn.grid(pady=5,row=1,column=0)

        self.delBtn = Button(self.root, text="목록에서 삭제", width=20, height=2, command=self.delList)
        self.delBtn.grid(pady=5,row=1,column=1)

        self.regBtn = Button(self.root, text="업로드", width=20, height=2, command=self.reg)
        self.regBtn.grid(pady=5,row=1,column=2)

    def showDownloadWindow(self):
        self.skeleton=download.downBody()
        self.skeleton.start()

    def start(self): # 프로그램 시작
        self.root.mainloop()

    def close(self):
        if self.active:
            self.skeleton.close()
        self.root.destroy()
        exit(0)

    def isEmpty(self): # 파일 리스트가 비워지지 않았는지 체크
        if self.fList.index("end") != 0: return True
        messagebox.showwarning('경고', '파일을 등록하지 않았습니다.\n왼쪽 하단의 \'파일 등록\' 버튼을 눌러 파일을 등록해주세요')
        return False
    
    def ins(self):  # ins ==> insert
        files = askopenfilenames( # 파일 다중 선택
            title='파일 선택하기',
            filetypes=( ('All files', '*.*') ,
                        ('Text files', '*.txt'),
                        ('JPEG files', '*.jpg') ))
        if files:
            for file in files: self.fList.insert(END, file)  # 리스트에 파일 경로를 저장
        else:
            messagebox.showwarning("경고", "파일을 선택하지 않았습니다.")
            return
    def delList(self): # delList ==> delete List
        if self.isEmpty(): # 마지막 index가 0이 아니라면
            getItems = self.fList.curselection()
            # 리스트의 인덱스 순서대로 삭제되는데,
            # 이 때 먼저 번의 데이터가 지워지면, 그 갯수만큼 앞으로 당겨야 하므로
            # i를 index를 조정한다.
            i = 0
            for pos in getItems:
                self.fList.delete(int(pos) - i)
                i += 1
            # print(index) # Debug 용
    def reg(self):  # reg ==> registration
        if self.isEmpty(): # 마지막 index가 0이 아니라면
            fName = self.fList.get(0)
            self.fList.delete(0)
            upload.upload(fName)
