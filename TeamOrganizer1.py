'''
activityQ
team
organizeSwitch
teamLimit
'''

class TeamActivity:
	def __init__(self, i_from, i_to, i_type):
		self._from = i_from
		self._to = i_to
		self._type = i_type

	

class Team:
	def __init__(self. i_leaderNo, i_number_o_Person, i_teamMemberNo, i_teamNo)
		self._leaderNo = i_leaderNo
		self._number_o_Person = i_number_o_Person
		self._teamMemberNo = i_teamMemberNo
		self._teamNo = i_teamNo


class TeamOrganizer:
	def __init__(self):
		self._team = []
		self._activityQ = [] 	
                self._organizeSwitch = True
                self._teamLimit = 3
                
	def storeCommand(self, i_fromm, i_to, i_type):
		#find(from) find(to)
                tmpTeamActivity = TeamActivity(i_fromm, i_to, i_type)
               ''' if i_type == 0:
                        
                        self._activityQ.append(tmpTeamActivity)

                if i_type == 1:
                        executeAcitvity(tmpTeamActivity)

                if i_type == 2:
                        if len(self._activityQ)!= 0:
                                self._activityQ.remove(self._activityQ[0])
                if i_type == 3:
                        executeAcitvity(tmpTeamActivity)

                '''
		
		
	
	def loadTeam(self, i_idd, i_teamNo, i_uniqueNo):
		
		state = True
		for team in self._team:
			if team._teamNo==i_teamNo:
				state = False 
		
		if state == False:
			print("can not creat  the new team "+str(i_teamNo))
			print("this team has been created already")
			return False
		
		tmpMember=(i_idd, i_uniqueNo)		
		tmpMemberList = [tmpMember]
		tmpTeam = Team(i_idd, 0, tmpMemberList , i_teamNo)
		self._team.append(tmpTeam)
		print("success creat a new team: t_No:"+str(i_teamNo))
		return True

	def findTeamNo(self, idd):
		state = False
		for team in self._team:
                        for member in team._teamMember
                        
                                if member[0] == idd:
                                        state = True
                                        return team.teamNo
                if state = False
                        print("error, Not found this student in team")
                                
			

	def findLeaderNo(teamNo):
		if(team[teamNo-1] != None):
			return team[teamNo-1].leaderNo 
		else:
			print("error! Not find team")

	def executeAcitvity(self, command):
                # this function execute the input command
                # send message using Bang.sentMessage, the argument message =  command.type
                

                
                view = View();
		Bang.sentMessage(command._type, view)

		
                if command._type == 0:
                        self._activityQ.append(command)
                        
                if command._type == 1:
                        for tmp in self._activityQ:
                                if tmp._to = command._from and tmp._from = command._to:
                                        tmpTeamNo = findTeamNo(command._to)
                                        for team in self._team:
                                                if team._teamNo = tmpTeamNo
                                                        team._teamMemberNo.append(command._to)
                        for tmp in self.activityQ:
                                if tmp.to = command._to and tmp._from = command._from and tmp._type = command._type:
                                        self.activityQ.remove(tmp)
                                                        
                if command._type == 2:
                        for tmp in self._activityQ:
                                if tmp.to = command._to and tmp._from = command._from and tmp._type = command._type:
                                        self.activityQ.remove(tmp) 
                        
                if command._type == 3:
                        tmpTeamNo = findTeamNo(command._to)
                        for team in self._team:
                                if team._teamNo = tmpTeamNo
                                        team._teamMemberNo.remove(command._to)


	def deleteTeam(teamNo):
		_team.remove(team[teamNo-1])

	def getSwitch():
		return _organizeSwitch
	
	def getLimit():
		return _teamLimit

	def setSwitch():
		_organizeSwitch = !_organizeSwitch
			return _organizeSwitch

	def setLimit(limit):
		if(_organizeSwitch == False):
			_teamLimit = limit

	def cleanQ():
		if(_organizeSwitch == False):
			del _activityQ
	




