import Professor
import Student
import Display

"""
- 최초 작성자 : 박근태
- 최초 작성일 : 2018.12.05
- 최초 변경일 : 2018.12.05
- 목적 : client 로그인 처리 및 사용자에 맞는 객체 생성
- 개정 이력 : 박근태, 2018.12.05
"""

class Client:
    def __init__(self,managerObj):
        self.obj = managerObj
        self.display = Display.Display()

    """
    - 목적 : 로그인 수행
    - 매개변수 : id(id 번호) : Integer, name(이름) : String, bang(방 번호) : Integer
    - 반환 값 : 없음
    - 변경 이력 : 박근태, 2018.12.05
    """
    def logIn(self,id, name, bang):
        # 학생 로그인
        if bang != None:
            isRight = self.obj.studCheck(id, name, bang)
            if isRight == True:
                #생성자 변동 -> self.display를 parameter로 받음 추가
                student = Student.Student(id, bang, self.display, self.obj)
                self.me = student
            else:
                self.display.messageSend(0,0)
        # 교수 로그인
        else:
            isRight = self.obj.profCheck(id, name)
            if isRight == True:
                # 생성자 변동 -> self.display를 parameter로 받음 추가
                professor = Professor.Professor(id, self.display, self.obj)
                self.me = professor
            else:
                self.display.messageSend(0, 0)
