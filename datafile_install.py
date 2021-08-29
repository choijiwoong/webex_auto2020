from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
directory=''
infor=[]
subject_num=int(input("수강하실 과목의 개수를 입력해주세요: "))

def search():
    global directory
    directory=askopenfilename()
    print(directory+'로 경로설정되었습니다.')
    

def make_txt():
    outfile=open("Webex_datafile.txt","w")
    outfile.write(user_id.get()+" ")
    outfile.write(user_pass.get()+' ')
    outfile.write(directory+"\n")

    for i in range(subject_num):
        for m in range(4):
            if infor[i][m].get()=='':
                outfile.write('-1 ')
            outfile.write(infor[i][m].get()+' ')
        outfile.write("\n")
    outfile.close()
    window.quit()
    print("정보가 저장되었습니다!")

window=Tk()

Label(window,text="시간란에 24시간형식 사용").grid(row=0,column=0,pady=5)
Label(window,text="ex)월 7or 월 7 화 14").grid(row=0,column=1)
Label(window,text="띄어쓰기로 정보를 구분하니").grid(row=0,column=2)
Label(window,text="시간형식에 유의해주세요").grid(row=0,column=3)

Label(window,text="싸캠 아이디").grid(row=1,column=0)
user_id=Entry(window)
user_id.grid(row=1,column=1)
Label(window,text="싸캠 비밀번호").grid(row=1,column=2,pady=5)
user_pass=Entry(window)
user_pass.grid(row=1,column=3)

Label(window,text="강의명").grid(row=2,column=0)
Label(window,text="Webex링크").grid(row=2,column=1)
Label(window,text="싸캠링크").grid(row=2,column=2)
Label(window,text="시간정보").grid(row=2,column=3,pady=5)

infor=[]
for i in range(subject_num):
    infor.append([0,0,0,0])
    
for i in range(subject_num):
    for m in range(4):
        infor[i][m]=Entry(window)
        infor[i][m].grid(row=3+i,column=m,padx=5,pady=5)

Label(window,text="시간 외에").grid(row=subject_num+3,column=0)
Label(window,text="띄어쓰기를 넣지 마세요").grid(row=subject_num+3,column=1)
search_file=Button(window,text="크롬드라이버 위치설정",command=search).grid(row=subject_num+3,column=2)

button=Button(window,text="저장",command=make_txt).grid(row=subject_num+3,column=3,pady=5)
