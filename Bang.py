import TeamOrganizer
import random
import operator

"""
- 최초 작성자 : 박근태
- 최초 작성일 : 2018.12.05
- 최초 변경일 : 2018.12.05
- 목적 : 데이터 관리 및 변경 내용 전파
- 개정 이력 : 박근태, 2018.12.05
"""

class Bang:
    bangNo = 0
    studentInfoList = {}
    bangOwnerID = 0
    subjName = ""
    logInQ = []
    switchStat = False
    displayObj = {}

    def __init__(self, bangNo, bangOwnerID, subjName, inputList):
        self.bangNo = bangNo
        self.bangOwnerID = bangOwnerID
        self.subjName = subjName
        self.teamorg = TeamOrganizer.TeamOrganizer(self)
        for input in inputList:
            stud = StudentInfo(input[0],input[1],input[2],input[3],input[4])
            self.studentInfoList[input[0]] = stud

    """
        - 목적 : 방 Owner ID를 반환
        - 매개변수 : 없음
        - 반환 값 : Integer(방 Owner ID)
        - 변경 이력 : 박근태, 2018.12.05
        """
    def getOwnerID(self):
        return self.bangOwnerID

    """
        - 목적 : 학생 entry 삭제
        - 매개변수 : id(대상 id) : Integer, me(수행자 id) : Integer
        - 반환 값 : 없음
        - 변경 이력 : 박근태, 2018.12.05
        """
    def delete(self,id, me):
        if id in self.studentInfoList:
            del self.studentInfoList[id]
        else:
            #return을 넣어 오류 발생을 알리던지 함수에서 실행자 정보를 받아 display로 오류를 바로 보내던지
            self.displayObj[id].messageSend()
            #오류(존재하지 않는 학생)

    """
    - 목적 : 새 항목 추가
    - 매개변수 : studNo(학생 학번): Integer, studName(학생 이름): String, studPhone(연락처): Integer, me(수행자 id): Integer
    - 반환 값 : 없음
    - 변경 이력 : 박근태, 2018.12.05
    """
    def newDataInput(self,studNo,studName,studPhone, me):
        if studNo in self.studentInfoList:
            #오류(이미 등록되어 있는 학생)
            self.displayObj[me].messageSend()
        else:
            highVal = 0
            for id in self.studentInfoList:
                if highVal < self.studentInfoList[id].studentUniqueNo:
                    highVal = self.studentInfoList[id].studentUniqueNo
            newUniqueVal = highVal + 1
            newStd = StudentInfo(studNo,studName,studPhone,newUniqueVal,newUniqueVal)
            self.studentInfoList[studNo] = newStd
            disp = self.__ordering()
            for dis in self.displayObj:
                self.displayObj[dis].refreshBang(disp)
            self.teamorg.removeTeam()
            for id in self.studentInfoList:
                self.teamorg.loadTeam(self.studentInfoList)

    """
        - 목적 : 정보 수정
        - 매개변수 : studNo(학번): Integer, studName(이름): String, studPhone(연락처): Integer, studTeamNo(팀 번호): Integer, me(수행자 id): integer
        - 반환 값 : 없음
        - 변경 이력 : 박근태, 2018.12.05
        """
    def updateList(self,studNo, studName, studPhone, studTeamNo, me):
        if not (studNo in self.studentInfoList):
            # return을 넣어 오류 발생을 알리던지 함수에서 실행자 정보를 받아 display로 오류를 바로 보내던지
            #오류(등록 되지 않은 학생)
            self.displayObj[me].messageSend()
        else:
            self.studentInfoList[studNo].studentName = studName
            self.studentInfoList[studNo].studentPhone = studPhone
            if studTeamNo >= 1:
                self.studentInfoList[studNo] = studTeamNo
            disp = self.__ordering()
            for dis in self.displayObj:
                self.displayObj[dis].refreshBang(disp)

    """
        - 목적 : 학생 팀 정보 변경
        - 매개변수 : studNo(학번): Integer, studTeamNo(팀 번호): Integer
        - 반환 값 : 없음
        - 변경 이력 : 박근태, 2018.12.05
        """
    def updateTeam(self,studNo, studTeamNo):
        if studTeamNo != 0:
            self.studentInfoList[studNo].studentTeamNo = studTeamNo
        else:
            self.studentInfoList[studNo].studentTeamNo = self.studentInfoList[studNo].studentUniqueNo
        disp = self.__ordering()
        for dis in self.displayObj:
            self.displayObj[dis].refreshBang(disp)

    """
        - 목적 : 팀 구성 on/off 및 현재 switch상태 확인
        - 매개변수 : me(id번호) : Iteger
        - 반환 값 : 없음
        - 변경 이력 : 박근태, 2018.12.05
        """
    def switchOnOff(self, me):
        self.switchStat = self.teamorg.setSwitch()
        self.displayObj[me].refreshBang()
    """
        - 목적 : 팀 구성 limit 설정
        - 매개변수 : limit(제한 인원 수): Integer
        - 반환 값 : 없음
        - 변경 이력 : 박근태, 2018.12.05
        """
    def setLimit(self,limit, me):
        self.teamorg.setLimit(limit, me)

    """
        - 목적 : 학생 정보 List 반환
        - 매개변수 : 없음
        - 반환 값 : studentInfoList(학생정보 list): studentInfo_List
        - 변경 이력 : 박근태, 2018.12.05
        """
    def getAll4Display(self):
        return self.studentInfoList

    """
        - 목적 : SubjName 반환
        - 매개변수 : 없음
        - 반환 값 : subjName(과목 이름): String
        - 변경 이력 : 박근태, 2018.12.05
        """
    def getSubjName(self):
        return self.subjName

    """
        - 목적 : bangNo 반환
        - 매개변수 : 없음
        - 반환 값 : bangNo(방번호): Integer
        - 변경 이력 : 박근태, 2018.12.06
        """
    def getBangNo(self):
        return self.bangNo

    """
        - 목적 : 로그인, 방 입장 처리
        - 매개변수 : id(id 번호): Integer, display(Display 객체): Display
        - 반환 값 : 없음
        - 변경 이력 : 박근태, 2018.12.05
        """
    def logIn(self, id, display):
        if id in self.displayObj:
            #오류(이미 로그인 되어 있음)
            self.displayObj[id].messageSend()
        else:
            self.displayObj[id] = display
            self.logInQ.append(id)
            disp = self.__ordering()
            self.displayObj[id].refreshBang(disp)
            for message in self.studentInfoList[id].messages:
                self.sendMessage(message.message, id, message.froms)

    """
        - 목적 : 로그 아웃 처리
        - 매개변수 : id(id): Integer, meDisplay(수행자 display 객체): Display
        - 반환 값 : 없음
        - 변경 이력 : 박근태, 2018.12.05
        """
    def logOut(self,id, meDisplay):
        if not (id in self.displayObj):
            #오류(처음부터 로그인 되어 있지 않았음)
            meDisplay.messageSend()
        else:
            del self.displayObj[id]
            self.logInQ.pop(id)
            if len(self.logInQ) <= 0:
                self.__save()

    """
        - 목적 : 대상에게 메세지 보내기
        - 매개변수 : message(message 종류): Integer, to(수신자 id): Integer, froms(송신자 id): Integer
        - 반환 값 : 없음
        - 변경 이력 : 박근태, 2018.12.05
        """
    def sendMessage(self,message, to, froms):
        if to in self.displayObj:
            #가입신청 메시지
            if message == 1:
                self.displayObj[to].messageSend(1, froms)
            #거절 메시지
            elif message == 3:
                self.displayObj[to].messageSend(3, froms)
            #신청 불가 메시지
            elif message == 101:
                self.displayObj[froms].messageSend(101, froms)
            #수락 불가 메시지
            elif message == 102:
                self.displayObj[froms].messageSend(102, froms)
            #탈퇴 불가 메시지
            elif message == 104:
                self.displayObj[froms].messageSend(104, froms)
        else:
            self.__addMessage(message, to, froms)

    """
        - 목적 : 무작위 팀 생성
        - 매개변수 : 없음
        - 반환 값 : 없음
        - 변경 이력 : 박근태, 2018.12.05
        """
    def randomTeamMake(self):
        limit = self.teamorg.getLimit()
        cap = len(self.studentInfoList)
        if cap % limit == 0:
            teamcap = int(cap / limit)
        else:
            teamcap = int(cap / limit) + 1
        tempdict = {}
        #teamentry = []
        #팀 번호 랜덤 생성(팀장 랜덤 생성)
        for i in range(teamcap + 1):
            while True:
                rand = random.randrange(1, len(self.studentInfoList) + 1)
                if not (rand in tempdict):
                    tempdict[rand] = 1
                    #teamentry.append(rand)
                    break
        #생성된 랜덤 팀에 팀원 배치
        for id in self.studentInfoList:
            if not (self.studentInfoList[id].studentTeamNo in tempdict):
                while True:
                    tno = random.choice(tempdict)
                    if tempdict[tno] < limit:
                        tempdict[tno] = tempdict[tno] + 1
                        self.studentInfoList[id].studentTeamNo = tno
                        break
                if tempdict[tno] == limit:
                    del tempdict[tno]

    """
        - 목적 : 메세지 덧붙이기
        - 매개변수 : message(message 종류): Integer, to(수신자 id): Integer, froms(송신자 id): Integer
        - 반환 값 : 없음
        - 변경 이력 : 박근태, 2018.12.05
        """
    def __addMessage(self, message, to, froms):
        newMessage = Message(froms,message)
        self.studentInfoList[to].messages.append(newMessage)

    """
        - 목적 : 방 파일에 변경 내용 저장
        - 매개변수 : 없음
        - 반환 값 : 없음
        - 변경 이력 : 박근태, 2018.12.05
        """
    def __save(self):
        filename = "bang " + self.bangNo + ".txt"
        f = open(filename,'w')
        f.writelines(self.bangNo)
        f.writelines(self.bangOwnerID)
        f.writelines(self.subjName)
        #학생 정보 list 저장
        for id in self.studentInfoList:
            writestring = self.studentInfoList[id].studentNo + " " + self.studentInfoList[id].studentName\
                          + " " + self.studentInfoList[id].studentPhone + " " + self.studentInfoList[id].studentTeamNo\
                          + " " + self.studentInfoList[id].studentUniqueNo + "\n"
            f.writelines(writestring)

        f.close()
    """
        - 목적 : dictionary형태의 data를 정렬된 list형태로 반환
        - 매개변수 : 없음
        - 반환 값 : StudentInfo_List
        - 변경 이력 : 박근태, 2018.12.05
        """
    def __ordering(self):
        stdlist = []
        for id in self.studentInfoList:
            stdlist.append(self.studentInfoList[id])
        #정렬
        stdlist = sorted(self.studentInfoList.items(), key=operator.itemgetter(1).studentTeamNo)
        return stdlist

"""
- 최초 작성자 : 박근태
- 최초 작성일 : 2018.12.05
- 최초 변경일 : 2018.12.05
- 목적 : 학생 정보 저장 구조체 대용 클래스
- 개정 이력 : 박근태, 2018.12.05
"""

class StudentInfo:
    studentNo = -1
    studentName = ""
    studentPhone = -1
    studentTeamNo = -1
    studentUniqueNo = -1
    messages = []
    isLogin = False

    def __init__(self, studentNo, studentName, studentPhone, studentTeamNo, studnetUniqueNo):
        self.studentNo = studentNo
        self.studentName = studentName
        self.studentPhone = studentPhone
        self.studentUniqueNo = studnetUniqueNo
        self.studentTeamNo = studentTeamNo

"""
- 최초 작성자 : 박근태
- 최초 작성일 : 2018.12.05
- 최초 변경일 : 2018.12.05
- 목적 : 메시지 내용 저장 구조체 대용 클래스
- 개정 이력 : 박근태, 2018.12.05
"""

class Message:
    froms = -1
    message = -1
    def __init__(self, froms, message):
        self.froms = froms
        self.message = message