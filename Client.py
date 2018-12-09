import ProfStuClass
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
        self.display = Display.Display(self)
        self.display.openView("LogIn")

    """
    - 목적 : 로그인 수행
    - 매개변수 : id(id 번호) : Integer, name(이름) : String, bang(방 번호) : Integer
    - 반환 값 : 없음
    - 변경 이력 : 박근태, 2018.12.05
    """
    def logIn(self, id, name, bang):
        # 학생 로그인
        if bang != -1:
            isRight = self.obj.studCheck(id, name, bang)
            if isRight == 0:
                self.display.closeView("Login")
                #생성자 변동 -> self.display를 parameter로 받음 추가
                ProfStuClass.Student(id, bang, self.display, self.obj)
            elif isRight == 1:
                self.display.messageSend(110, 0)
            elif isRight == 2:
                self.display.messageSend(111, 0)
            elif isRight == 3:
                self.display.messageSend(112, 0)
        # 교수 로그인

        elif bang == -1:
            isRight = self.obj.profCheck(id, name)
            if isRight == 0:
                banglist = []
                bangindex = []
                self.display.closeView("Login")
                # 생성자 변동 -> self.display를 parameter로 받음 추가
                professor = ProfStuClass.Professor(id, self.display, self.obj)
                self.me = professor
                rawbanglist = self.obj.throwBangList(id)
                for bangs in rawbanglist:
                    banglist.append(bangs[1])
                    bangindex.append(bangs[0])
                self.display.giveRef(self.me, "Professor")
                self.display.refreshBangList(bangindex,banglist)
            elif isRight == 1:
                self.display.messageSend(110, 0)
            elif isRight == 2:
                self.display.messageSend(111, 0)

        else:
            #잘못된 방 번호 입력
            self.display.messageSend(0, 999)

