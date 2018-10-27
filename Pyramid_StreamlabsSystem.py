import os
import sys
import json
import codecs

ScriptName = "Emote Pyramid"
Website = "https://github.com/aseroff/pyramid/"
Description = "Congratulate users on completion of emote pyramids"
Creator = "rvaen17"
Version = "1.1.0"

configFile = "config.json"
settings = {}
msg = ""
user = ""
count = 0
width = 0
desc = 0

def ScriptToggled(state):
	return

def Init():
	global configFile, settings

	path = os.path.dirname(__file__)
	try:
		with codecs.open(os.path.join(path, configFile), encoding='utf-8-sig', mode='r') as file:
			settings = json.load(file, encoding='utf-8-sig')
	except:
		settings = {
			"liveOnly": False,
			"responseThreeWide": "/me $user just finished a 3-wide $emote pyramid! Pretty good TPFufun",
                        "responseFourWide": "/me $user just finished a 4-wide $emote pyramid! Nice LUL",
                        "responseFiveWide": "/me $user just finished a 5-wide $emote pyramid! Very nice MVGame",
                        "responseSixWide": "/me $user just finished a 6-wide $emote pyramid! Wow PogChamp",
                        "responseSevenWide": "/me $user just finished a 7-wide $emote pyramid! Incredible KAPOW",
                        "responseEightWide": "/me $user just finished a 8-wide $emote pyramid! Crazy OhMyDog",
                        "responseNineWide": "/me $user just finished a 9-wide $emote pyramid! Insane SwiftRage",
                        "responseTenPlusWide": "/me $user just finished a 10+ $emote pyramid! Impossible Kreygasm",
			"rewardThreeWide": 0,
                        "rewardFourWide": 0,
                        "rewardFiveWide": 5,
                        "rewardSixWide": 6,
                        "rewardSevenWide": 7,
                        "rewardEightWide": 8,
                        "rewardNineWide": 9,
                        "rewardTenPlusWide": 10,
		}
		
def Execute(data):
	global msg, user, count, width, desc, settings
	if ((settings["liveOnly"] and Parent.IsLive()) or (not settings["liveOnly"])) and data.IsChatMessage():
		if ((count == 0) and (data.GetParamCount() == 1)):
			user = data.UserName
			msg = data.Message
			count += 1
			desc = 0
		elif (count > 0) and (data.UserName == user):
			if (desc == 0) and (data.GetParamCount() == (count + 1)) and (data.Message.split(" ")[0] == msg) and (len(list(set(data.Message.split(" ")))) == 1):
				count += 1
				width = count
			elif (data.GetParamCount() == (count - 1)) and (data.Message.split(" ")[0] == msg) and (len(list(set(data.Message.split(" ")))) == 1):
    				count -= 1
    				desc = 1
				if count == 1:
					if width == 3:
						outputMessage = settings["responseThreeWide"]
						reward = settings["rewardThreeWide"]
					elif width == 4:
						outputMessage = settings["responseFourWide"]
						reward = settings["rewardFourWide"]
					elif width == 5:
						outputMessage = settings["responseFiveWide"]
						reward = settings["rewardFiveWide"]
					elif width == 6:
						outputMessage = settings["responseSixWide"]
						reward = settings["rewardSixWide"]
					elif width == 7:
						outputMessage = settings["responseSevenWide"]
						reward = settings["rewardSevenWide"]
					elif width == 8:
						outputMessage = settings["responseEightWide"]
						reward = settings["rewardEightWide"]
					elif width == 9:
						outputMessage = settings["responseNineWide"]
						reward = settings["rewardNineWide"]
					elif width > 9:
						outputMessage = settings["responseTenPlusWide"]
						reward = settings["rewardTenPlusWide"]
					if width > 2:
                                                outputMessage = outputMessage.replace("$user", user)
                                                outputMessage = outputMessage.replace("$emote", msg)
                                                Parent.SendStreamMessage(outputMessage)
                                                Parent.AddPoints(data.User,data.UserName,reward)
                                                count = 0
                                        width = 0
					desc = 0
			elif (data.GetParamCount() == 1):
                                msg = data.Message
                                count = 1
                                desc = 0
                        else:
                                count = 0
                                width = 0
                                desc = 0
		else:
			count = 0
			width = 0
                        desc = 0
	return

def ReloadSettings(jsonData):
        Init()
	return

def OpenReadMe():
	location = os.path.join(os.path.dirname(__file__), "README.txt")
	os.startfile(location)
	return

def Tick():
	return
