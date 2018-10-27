import os
import sys
import json
import codecs

ScriptName = "Emote Pyramid"
Website = "https://github.com/aseroff/pyramid/"
Description = "Congratulate users on completion of emote pyramids"
Creator = "rvaen17"
Version = "1.0.0"

configFile = "config.json"
settings = {}
msg = ""
user = ""
count = 0
width = 0

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
			"responseThreeWide": "/me $user just finished a 3-wide $emote pyramid! Nice SeemsGood",
                        "responseFourWide": "/me $user just finished a 4-wide $emote pyramid! Very nice LUL",
                        "responseFiveWide": "/me $user just finished a 5-wide $emote pyramid! Wow MVGame",
                        "responseSixWide": "/me $user just finished a 6-wide $emote pyramid! Incredible PogChamp",
		}
		
def Execute(data):
	global msg, user, count, width, settings
	if ((settings["liveOnly"] and Parent.IsLive()) or (not settings["liveOnly"])) and data.IsChatMessage():
		if ((count == 0) and (data.GetParamCount() == 1)):
			user = data.UserName
			msg = data.Message
			count += 1
		elif (count > 0) and (data.UserName == user):
			if (data.GetParamCount() == (count + 1)) and (data.Message.split(" ")[0] == msg) and (len(list(set(data.Message.split(" ")))) == 1):
				count += 1
				width = count
			elif (data.GetParamCount() == (count - 1)) and (data.Message.split(" ")[0] == msg) and (len(list(set(data.Message.split(" ")))) == 1):
    				count -= 1
				if count == 1:
					if width == 3:
						outputMessage = settings["responseThreeWide"]
					elif width == 4:
						outputMessage = settings["responseFourWide"]
					elif width == 5:
						outputMessage = settings["responseFiveWide"]
					elif width == 6:
						outputMessage = settings["responseSixWide"]
					outputMessage = outputMessage.replace("$user", user)
					outputMessage = outputMessage.replace("$emote", msg)
					Parent.SendStreamMessage(outputMessage)
		else:
			count = 0
			width = 0
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
