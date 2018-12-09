import Bang, InitializeManager, TeamOrganizer

'''
    최초 작성자 : 이영찬
    최초 작성일 : 2018.11.29
    최초 변경일 : 2018.12.06
    목적 : 교수 클래스 생성
    개정 이력 : 이영찬 2018.12.06
'''
class Professor:
    #목적 : 교수 인스턴스 생성
    #매개변수 : 교수 리스트로부터 받은 id
    def __init__(self, id, display, IMobj):
        self.id = id
        self.display = display
        self.initializer = IMobj

    #목적 : 교수 방 입장
    #매개변수 : 방 번호
    def enterBang(self, bangIndex):
        self.bang = self.initializer.getBang(bangIndex)
        self.bang.logIn(self.id, self.display)

    #목적 : 학생 명단 제외
    #매개변수 : 학생 학번
    def deleteStud(self, id):

        self.bang.delete(id, self.id)
    #목적 : 학생 정보 추가
    #매개변수 : 학생번호, 학생이름, 학생번호
    def inputStud(self, studNo, studName, studPhone):
        self.bang.newDataInput(studNo, studName, studPhone, self.id)

    #목적 : 학생 정보 수정(교수권한)
    #매개변수 : 학번, 학생이름, 학생번호, 학생팀번호
    def modStudInform(self, studNo, studName, studPhone, studTeamNo):

        self.bang.updateList(studNo, studName, studPhone, studTeamNo, self.id)

    #목적 : 저장
    #매개변수 : 없음
    def saveOper(self):
        self.bang.save(self.id)

    #목적 : 팀 구성 인원 설정
    #매개변수 : 설정할 인원 수
    def setLimit(self, limit):
        self.bang.setLimit(limit, self.id)

    #목적 : 방 생성
    #매개변수 : 방 DB, 방 이름
    def makeBang(self, file, name):
        self.initializer.makeNew(file, name, self.id)


    #목적 : 시스템 로그아웃
    #매개변수 : 없음
    def logOut(self):
        self.bang.logOut()


    #목적 : 팀을 무작위로 구성
    #매개변수 : 없음
    def makeRandomTeam(self):
        self.bang.randomTeamMake()

'''
    최초 작성자 : 이영찬
    최초 작성일 : 2018.11.29
    최초 변경일 :
    목적 : 학생 클래스 생성
    개정 이력 :
'''

class Student:
    def __init__(self, id, bang, display, managerObj):

        self.id = id
        self.display = display
        self.display.giveRef(self, "Student")

        self.bang = managerObj.getBang(int(bang))
        self.teamOrg = self.bang.getOrg()
        self.bang.logIn(self.id, self.display)

    #목적 : 자신의 정보 수정
    #매개변수 : 이름, 연락처
    def modMyInform(self, name, phoneNo):
        self.bang.updateList(self.id, name, phoneNo,-1,self.id)

    #목적 : 원하는 사람에게 팀 가입을 신청한다
    #매개변수 : 원하는 사람의 학번
    def wantJoin(self, to):
        self.teamOrg.storeCommand(id ,to, 0)

    #목적 : 팀 가입을 요청한 사람의 제안을 승락하여 팀을 구성
    #매개변수 : 팀 가입을 원하는 사람의 학번
    def positive(self, to):
        self.teamOrg.storeCommand(id, to, 1)
        TeamOrganizer.TeamOrganizer.storeCommand(id, to, 1)

    #목적 : 팀 가입을 요청한 사람의 제안을 거절
    #매개변수 : 팀 가입을 원하는 사람의 학번
    def negative(self, to):
        self.teamOrg.storeCommand(id, to, 2)

    #목적 : 자신이 속한 팀에서 탈퇴
    #매개변수 : 팀장의 학번
    def quitTeam(self, to):
        self.teamOrg.storeCommand(id, to, 3)

    #목적 : 시스템에서 로그아웃
    #매개변수 : 없음
    def logOut(self):
        self.bang.logOut()

