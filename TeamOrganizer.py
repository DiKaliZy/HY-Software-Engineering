import Bang

class TeamActivity:
	def __init__(self, i_from, i_to, i_type):
		self._from = i_from
		self._to = i_to
		self._type = i_type

class Team:
	def __init__(self, i_leaderNo, i_number_o_Person, i_teamMemberNo, i_teamNo):
		self._leaderNo = i_leaderNo
		self._number_o_Person = i_number_o_Person
		self._teamMemberNo = i_teamMemberNo
		self._teamNo = i_teamNo

class TeamOrganizer:
	def __init__(self, bang):
		self._team = {}
		self._activityQ = [] 	
		self._organizeSwitch = False
		self._teamLimit = 1
		self.bangobj = bang
		stddict = self.bangobj.getAll4Display()
		self.loadTeam(stddict)

	def storeCommand(self, i_fromm, i_to, i_type):
		tmpTeamActivity = TeamActivity(i_fromm, i_to, i_type)
		self._activityQ.append(tmpTeamActivity)
		self.executeAcitvity(self._activityQ[0])
		self._activityQ.pop(0)

	def removeTeam(self):
		self._team = {}

	def loadTeam(self, stdlist):
		for key in stdlist:
			i_teamNo = stdlist[key].studentTeamNo
			i_idd = stdlist[key].studentNo
			i_uniqueNo = stdlist[key].studentUniqueNo
			if i_teamNo in self._team:
				self._team[i_teamNo].number_o_Person += 1
				self._team[i_teamNo].teamMemberNo.append(i_idd)
				if i_teamNo == i_uniqueNo:
					self._team[i_teamNo].leaderNo = i_idd
			else:
				self._team[i_teamNo] = Team(0,1,[i_idd],i_teamNo)
				if i_teamNo == i_uniqueNo:
					self._team[i_teamNo].leaderNo = i_idd
		for key in self._team:
			if self._team[key].leaderNo == 0:
				self._team[key].leaderNo = self._team[key].teamMemberNo[0]
				self._team[stdlist[self._team[key].leaderNo].studentUniqueNo] = self._team[key]
				for i in self._team[key].teamMemberNo:
					self.bangobj.updateList(i,stdlist[self._team[key].leaderNo].studentUniqueNo)
				del self._team[key]

	def findTeamNo(self, idd):
		for no in self._team:
			if idd in self._team[no].teamMemberNo:
				return no

	def findLeaderNo(self,teamNo):
		return self._team[teamNo]

	def executeAcitvity(self, command):
		myteamno = self.findTeamNo(command._from)
		teamno = self.findTeamNo(command._to)
		myteamlead = self.findLeaderNo(myteamno)
		teamlead = self.findLeaderNo(teamno)
		if command._type == 0:
			if self._team[teamno].number_o_Person + self._team[myteamno].number_o_Person > self._teamLimit:
				self.bangobj.sendMessage(101, command._to, command._from)
			elif self._team[myteamno].leaderNo != command._from:
				self.bangobj.sendMessage(101, command._to, command._from)
			else:
				self.bangobj.sendMessage(1, command._to, command._from)
		elif command._type == 1:
			if self._team[teamno].number_o_Person + self._team[myteamno].number_o_Person > self._teamLimit:
				self.bangobj.sendMessage(102, command._to, command._from)
			else:
				for id in self._team[teamno]._teamMemberNo:
					self.bangobj.updateTeam(command._to, myteamno)
				self.deleteTeam(teamno)
		elif command._type == 2:
			self.bangobj.sendMessage(command._type, command._to, command._from)
		elif command._type == 3:
			if self._team[myteamno].number_o_Person == 1:
				self.bangobj.sendMessage(104, command._to, command._from)
			else:
				self._team[myteamno].number_o_Person -=1
				self._team[myteamno].teamMemberNo.remove(command._from)
				self.bangobj.updateTeam(command._from, 0)

	def deleteTeam(self, teamNo):
		del self._team[teamNo]

	def getSwitch(self):
		return self._organizeSwitch
	
	def getLimit(self):
		return self._teamLimit

	def setSwitch(self):
		if self._organizeSwitch == True:
			self._organizeSwitch = False
			self.cleanQ()
		else:
			self._organizeSwitch = True
		return self._organizeSwitch

	def setLimit(self, limit, me):
		if(self._organizeSwitch == False):
			self._teamLimit = limit
		else:
			#limit 변환 불가 (switch가 On 상태임)
			self.bangobj.sendMessage(me,0,150)

	def cleanQ(self):
		self._activityQ = []

	




