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


    def __init__(self, bangNo, bangOwnerID, subjName, inputList):
        self.bangNo = 0
        self.studentInfoList = {}
        self.bangOwnerID = 0
        self.subjName = ""
        self.logInQ = []
        self.switchStat = False
        self.displayObj = {}
        self.stdlist = []
        self.bangNo = bangNo
        self.bangOwnerID = bangOwnerID
        self.subjName = subjName
        #self.teamorg = TeamOrganizer.TeamOrganizer(self)
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
        - 목적 : TeamOrganizer 객체 ref 반환
        - 매개변수 : 없음
        - 반환 값 : TeamOrganizer object
        - 변경 이력 : 박근태, 2018.12.08
    """
    def getOrg(self):
        return self.teamorg

    """
        - 목적 : 학생 entry 삭제
        - 매개변수 : id(대상 id) : Integer, me(수행자 id) : Integer
        - 반환 값 : 없음
        - 변경 이력 : 박근태, 2018.12.05
        """
    def delete(self,id, me):
        if id in self.studentInfoList:
            del self.studentInfoList[id]
            self.__ordering()
            for dis in self.displayObj:
                self.displayObj[dis].refreshBang(self.stdlist,self.switchStat)

    """
    - 목적 : 새 항목 추가
    - 매개변수 : studNo(학생 학번): Integer, studName(학생 이름): String, studPhone(연락처): Integer, me(수행자 id): Integer
    - 반환 값 : 없음
    - 변경 이력 : 박근태, 2018.12.05
    """
    def newDataInput(self,studNo,studName,studPhone, me):
        if studNo in self.studentInfoList:
            ...
        else:
            highVal = 0
            for id in self.studentInfoList:
                if highVal < int(self.studentInfoList[id].studentTeamNo):
                    highVal = int(self.studentInfoList[id].studentTeamNo)
            newUniqueVal = highVal + 1
            newUniqueVal = str(newUniqueVal)
            newStd = StudentInfo(studNo,studName,studPhone,newUniqueVal,newUniqueVal)
            self.studentInfoList[studNo] = newStd
            self.__ordering()
            for dis in self.displayObj:
                self.displayObj[dis].refreshBang(self.stdlist,self.switchStat)
            #self.teamorg.removeTeam()
            #for id in self.studentInfoList:
            #    self.teamorg.loadTeam(self.studentInfoList)

    """
        - 목적 : 정보 수정
        - 매개변수 : studNo(학번): Integer, studName(이름): String, studPhone(연락처): Integer, studTeamNo(팀 번호): Integer, me(수행자 id): integer
        - 반환 값 : 없음
        - 변경 이력 : 박근태, 2018.12.05
        """
    def updateList(self,studNo, studName, studPhone, studTeamNo, me):
        print(type(studNo))
        if not (studNo in self.studentInfoList):
            # return을 넣어 오류 발생을 알리던지 함수에서 실행자 정보를 받아 display로 오류를 바로 보내던지
            #오류(등록 되지 않은 학생)
            self.displayObj[me].messageSend()
        else:
                self.studentInfoList[studNo].studentName = studName
                self.studentInfoList[studNo].studentPhone = studPhone
                if studTeamNo >= 1:
                    self.studentInfoList[studNo].studentTeamNo = str(studTeamNo)
                elif studTeamNo == -1:
                    # 학생이 정보 수정
                    self.save(me)
                self.__ordering()
                for dis in self.displayObj:
                    self.displayObj[dis].refreshBang(self.stdlist, self.switchStat)

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
        self.__ordering()
        for dis in self.displayObj:
            self.displayObj[dis].refreshBang(self.stdlist)

    """
        - 목적 : 팀 구성 on/off 및 현재 switch상태 확인
        - 매개변수 : me(id번호) : Iteger
        - 반환 값 : 없음
        - 변경 이력 : 박근태, 2018.12.05
        """
    def switchOnOff(self, me):
        self.switchStat = self.teamorg.setSwitch()
        self.displayObj[me].refreshBang(self.stdlist,self.switchStat)
    """
        - 목적 : 팀 구성 limit 설정
        - 매개변수 : limit(제한 인원 수): Integer
        - 반환 값 : 없음
        - 변경 이력 : 박근태, 2018.12.05
        """
    def setLimit(self, limit, me):
        self.limit = limit
        self.randomTeamMake()
        self.__ordering()
        for dis in self.displayObj:
            self.displayObj[dis].refreshBang(self.stdlist, self.switchStat)
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
            self.__ordering()
            if id in self.studentInfoList:
                for message in self.studentInfoList[id].messages:
                    self.sendMessage(message.message, id, message.froms)
            self.displayObj[id].refreshBang(self.stdlist, self.switchStat)



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
                self.save()

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
        limit = self.limit
        cap = len(self.studentInfoList)
        if cap % limit == 0:
            teamcap = int(cap / limit)
        else:
            teamcap = int(cap / limit) + 1
        tempdict = {}
        print(teamcap)
        templist = []
        for std in self.studentInfoList:
            templist.append(self.studentInfoList[std])
        for i in range(1, teamcap + 1):
            tempdict[i] = []
        for i in range(1, teamcap + 1):
            a = 0
            while a < self.limit and a < len(templist):
                rand = random.choice(templist)
                templist.remove(rand)
                tempdict[i].append(rand)

                a += 1
            print(tempdict)

        for list in tempdict:
            for std in tempdict[list]:
                self.studentInfoList[std.studentNo].studentTeamNo = str(list)


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
    def save(self, me):
        print(self.bangNo)
        filename = "bang" + self.bangNo + ".txt"
        f = open(filename,'w', encoding='utf-8-sig')
        f.writelines(self.bangNo + '\n')
        f.writelines(self.bangOwnerID + '\n')
        f.writelines(self.subjName + '\n')
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
        self.stdlist = []
        for id in self.studentInfoList:
            self.stdlist.append(self.studentInfoList[id])
        #정렬
        i = 0
        inx = 0
        lowest = self.stdlist[0]
        while True:
            for a in range(i,len(self.stdlist)):
                if int(lowest.studentTeamNo) > int(self.stdlist[a].studentTeamNo):
                    lowest = self.stdlist[a]
                    inx = a
            print(i , inx)
            self.stdlist[inx] = self.stdlist[i]
            self.stdlist[i] = lowest

            i += 1
            if i >= len(self.stdlist):
                break
            inx = i
            lowest = self.stdlist[i]
        for i in range(len(self.stdlist)):
            print(self.stdlist[i].studentName, " / ", self.stdlist[i].studentTeamNo)

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