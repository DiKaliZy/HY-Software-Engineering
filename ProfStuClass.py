'''
    최초 작성자 : 이영찬
    최초 작성일 : 2018.11.29
    최초 변경일 :
    목적 : 교수 클래스 생성
    개정 이력 :
'''

class Professor:
    #목적 : 교수 인스턴스 생성
    #매개변수 : 교수 리스트로부터 받은 id
    def __init__(self, id, display):
        self.id = id
        self.display = display

    #목적 : 교수 방 입장
    #매개변수 : 방 번호
    def enterBang(bangIndex):
        Initializer.getBang(bangIndex)

    #목적 : 학생 명단 제외
    #매개변수 : 학생 학번
    def deleteStud(id):
        Bang.delete(id)

    #목적 : 학생 정보 추가
    #매개변수 : 학생번호, 학생이름, 학생번호
    def inputStud(studNo, studName, studPhone):
        Bang.newDataInput(studNo, studName, studPhone)

    #목적 : 학생 정보 수정(교수권한)
    #매개변수 : 학번, 학생이름, 학생번호, 학생팀번호
    def modStudInform(studNo, studName, studPhone, studTeamNo):
        Bang.updateList(studNo, studName, studPhone, studTeamNo)

    #목적 : 팀 생성 가능 조건 설정
    #매개변수 : 없음
    def switchOper():
        Bang.swithOnOff()

    #목적 : 팀 구성 인원 설정
    #매개변수 : 설정할 인원 수
   def setLimit(limit):
        Bang.setLimit(limit)

    #목적 : 방 생성
    #매개변수 : 방 DB, 방 이름
    def makeBang(file, name):
        InitializeManager.makeNew(file, name)

    #목적 : 시스템 로그아웃
    #매개변수 : 없음
    def logOut():
        Bang.logOut()

    #목적 : 팀을 무작위로 구성
    #매개변수 : 없음
    def makeRandomTeam():
        Bang.randomTeamMake()

'''
    최초 작성자 : 이영찬
    최초 작성일 : 2018.11.29
    최초 변경일 :
    목적 : 학생 클래스 생성
    개정 이력 :
'''

class Student:
    def __init__(self, id, role, teamNo, managerObj, display):
        self.id = id
        self.role = role
        self.teamNo = teamNo
        self.managerObj = InitializeManager.getBang()
        self.display = display

    #목적 : 자신의 정보 수정
    #매개변수 : 이름, 연락처
    def modMyInform(name, phoneNo):
        Bang.updateList(id, name, phoneNo)

    #목적 : 원하는 사람에게 팀 가입을 신청한다
    #매개변수 : 원하는 사람의 학번
    def wantJoin(to):
        TeamOrganizer.storeCommand(id ,to, 0)

    #목적 : 팀 가입을 요청한 사람의 제안을 승락하여 팀을 구성
    #매개변수 : 팀 가입을 원하는 사람의 학번
    def positive(to):
        TeamOrganizer.storeCommand(id, to, 1)

    #목적 : 팀 가입을 요청한 사람의 제안을 거절
    #매개변수 : 팀 가입을 원하는 사람의 학번
    def negative(to):
        TeamOrganizer.storeCommand(id, to, 2)

    #목적 : 자신이 속한 팀에서 탈퇴
    #매개변수 : 팀장의 학번
    def quitTeam(to):
        TeamOrganizer.storeCommand(id, to, 3)

    #목적 : 시스템에서 로그아웃
    #매개변수 : 없음
    def logOut():
        Bang.logOut()