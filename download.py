from ftplib import FTP
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askdirectory

class downBody:
    def __init__(self):
        self.cnt = 0
        self.root = Tk()
        self.root.title('다운로드')
        self.root.geometry('505x385')  # window 크기조정
        self.root.resizable(0, 0)
        mycolor='#%02x%02x%02x' % (163, 204, 163)
        self.root.config(bg=mycolor)
        self.root.protocol("WM_DELETE_WINDOW", self.close)

        self.fList = Listbox(self.root,width=69,height=20,bg='white') # width ==> 한 줄에 들어갈 '문자 수', height==> 줄 수
        self.fList.grid(padx=9,pady=5,row=0,column=0,columnspan=3,sticky=E+W) # colmnspan 가로로 덮을 공간 따라서 0~3만큼의 공간을 덮는다.
        self.fList.config(selectmode='multiple')

        self.loadBtn = Button(self.root, text="파일 목록 불러오기", width=32, height=2,command=self.getList)
        self.loadBtn.grid(padx=10,pady=5,row=1,column=0)

        self.downBtn = Button(self.root, text="파일 다운", width=32, height=2,command=self.download)
        self.downBtn.grid(padx=5,pady=5,row=1,column=1)

    def start(self):
        self.ftp = FTP()
        self.ftp.encoding='utf-8'
        self.root.mainloop()

    def close(self):
        self.ftp.close()
        self.root.destroy()

    def isEmpty(self): # 파일 리스트가 비워지지 않았는지 체크
        if self.fList.index("end") != 0: return True
        return False

    def getList(self):
        files = self.ftp.nlst()
        files.remove('html')
        self.fList.delete(0,'end')
        for file in files:
            self.fList.insert(0, file)

    def download(self):
        fnum = self.fList.curselection()
        if len(fnum) != 0 and self.isEmpty():  # 마지막 index가 0이 아니라면
            for num in fnum:
                file = self.fList.get(num)
                #print('Downloading.....', file)
                dirName = askdirectory()
                self.ftp.retrbinary('RETR ' + file, open(dirName+"\\"+file, 'wb').write)
            #print('Done')
            messagebox.showinfo('완료!', '다운로드가 완료 되었습니다.')