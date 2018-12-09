import Bang

"""
- 최초 작성자 : 박근태
- 최초 작성일 : 2018.12.05
- 최초 변경일 : 2018.12.05
- 목적 : 로그인 내부 처리 및 professor의 방 관련 기능 수행
- 개정 이력 : 박근태, 2018.12.05
"""

class InitializeManager:

    def __init__(self,profListfile):
        self.bang = {}
        self.prof = {}
        self.__listInitialize(profListfile)

    """
        - 목적 : 새로운 방을 생성
        - 매개변수 : fileAddress(학생 정보 파일 위치): String, bangName(생성할 방 이름): String, who(호출자): Integer
        - 반환 값 : 없음
        - 변경 이력 : 박근태, 2018.12.05
        """
    def makeNew(self, file, bangName, who, disobj):
        print("makenew")
        f = open(file, "r", encoding="utf-8-sig")
        teamNo = 1
        #읽은 파일을 변환
        higher = 0
        for b in self.bang:
            if higher < b:
                higher = b
        bangNo = higher + 1
        bangOwnerID = who
        subjName = bangName
        inputs = []
        while True:
            entry = f.readline()
            if not entry:
                break
            data = entry.split()
            #studenNo, studentName, studentPhone
            inputList = [data[0], data[1], data[2], str(teamNo), str(teamNo)]
            inputs.append(inputList)
            teamNo += 1
        nbang = Bang.Bang(str(bangNo), bangOwnerID, subjName, inputs)
        print(nbang.studentInfoList)
        self.bang[bangNo] = nbang
        self.saveList(disobj)

    """
        - 목적 : 객체 초기화
        - 매개변수 : profListfile (교수 명단 파일주소): String
        - 반환 값 : 없음
        - 변경 이력 : 박근태, 2018.12.05
        """
    def __listInitialize(self, profListfile):
        f = open(profListfile, "r", encoding="utf-8-sig")
        inputList = []
        while True:
            proflist = f.readline()
            if not proflist:
                break
            spprof = proflist.split()
            self.prof[spprof[0]] = spprof[1]
        f.close()
        f= open("Bang List.txt", "r", encoding="utf-8-sig")
        while True:
            blist = f.readline()
            if not blist:
                break
            b = blist.split()
            b = b[1]
            bf = open(b, "r", encoding="utf-8-sig")
            bangNo = bf.readline()
            bangNo = bangNo.strip('\n')
            bangOwnerID = bf.readline()
            bangOwnerID = bangOwnerID.strip('\n')
            subjName = bf.readline()
            subjName = subjName.strip('\n')
            inputList = []
            while True:
                be = bf.readline()
                if not be:
                    break
                be = be.split()
                inputList.append(be)
            bang = Bang.Bang(bangNo,bangOwnerID,subjName,inputList)
            bangNo = int(bangNo)
            self.bang[bangNo] = bang
            bf.close()
        f.close()

    """
        - 목적 : 입력 받은 번호가 입력 받은 방 번호에 해당하는 class에 존재하는가 확인
        - 매개변수 : id(자신 학번): Integer, name(자신 이름): String, bang(방 번호): Integer
        - 반환 값 : Bool(일치 = True, 불일치 = False)
        - 변경 이력 : 박근태, 2018.12.05 
        """
    def studCheck(self,id, name, bang):
        for bangs in self.bang:
            if self.bang[bangs].bangNo == bang:
                stdlist = self.bang[bangs].getAll4Display()
                for std in stdlist:
                    if stdlist[std].studentName == name:
                        if stdlist[std].studentNo == id:
                            return 0
                        else:
                            #메세지 보내기 - id 틀림
                            return 1
                #메세지 보내기 - 리스트에 이름 존재 안함
                return 2
        #메세지 보내기 - 방이 존재하지 않음
        return 3

    """
        - 목적 : 교수 명단 확인
        - 매개변수 : id(번호): Integer, name(이름): String
        - 반환 값 : Bool(일치 = True, 불일치 = False)
        - 변경 이력 : 박근태, 2018.12.05 
        """
    def profCheck(self, id, name):
        # prof 찾기
        print(self.prof)
        for profs in self.prof:
            if self.prof[profs] == name:
                if profs == id:
                    return 0
                #메세지 보내기 - id 이름 불일치
                else:
                    return 1
        #메세지 보내기 - 이름 존재 안 함
        return 2

    """
        - 목적 : 방 객체 얻기
        - 매개변수 : bangIndex(방 번호): , id(): , display():
        - 반환 값 : 해당 방 객체
        - 변경 이력 : 박근태, 2018.12.05 
        """
    def getBang(self, bangIndex):
        bangobj = self.bang[bangIndex]
        return bangobj

    """
        - 목적 : 방 리스트 저장
        - 매개변수 : 없음
        - 반환 값 : 없음
        - 변경 이력 : 박근태, 2018.12.05 
        """
    def saveList(self,disobj):
        f = open("Bang List.txt", "w", encoding="utf-8-sig")
        for bang in self.bang:
            writeString = str(bang) + " bang" + str(bang) + ".txt\n"
            f.write(writeString)
            self.bang[bang].save(0)
        f.close()
        bangs = []
        bangi = []
        for bange in self.bang:
            print("wer",str(bange))
            bangi.append(str(bange))
            bangs.append(self.bang[bange])
        disobj.refreshBangList(bangs, bangi)


    """
        - 목적 : 방 리스트 전달
        - 매개변수 : id(교수 id): Integer
        - 반환 값 : Index_List(교수가 owner인 방 리스트 index)
        - 변경 이력 : 박근태, 2018.12.05 
        """
    def throwBangList(self,id):
        bangList = []
        for bangs in self.bang:
            if self.bang[bangs].getOwnerID() == id:
                bangList.append([int(bangs), self.bang[bangs]])
        return bangList