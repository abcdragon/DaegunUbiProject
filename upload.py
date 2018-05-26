from tkinter import messagebox
import ftplib
import os

ftp = None
def upload(fName):
    file = open(fName, 'rb') # read binary 모드
    # <-----파일 이름만 추출
    tmp = fName.split('/')
    newFileName = tmp[len(tmp)-1] # 어짜피 파일명은 가장 끝에 있으므로 마지막 인덱스에서 가져온다.
    # 파일 이름만 추출----->
    #print(type(newFileName), newFileName) # Debug 용
    if os.path.exists(fName):
        ftp = ftplib.FTP() # FTP 로그인
        ftp.encoding='utf-8' # 파일을 utf-8 인코딩으로 바꾸어준다.
        ftp.storbinary('STOR ' + newFileName, file) # FTP Server에 파일 올리기
        ftp.close()
        messagebox.showinfo('업로드 성공', '파일이 성공적으로 업로드 되었습니다.')
        return
    else :
        messagebox.showerror('파일 에러', '파일이 존재하지 않습니다.')
        return