import os
import sys
import json

ScriptName = "Emote Pyramid"
Website = "https://github.com/aseroff/pyramid/"
Description = "congratulation completion of emote pyramids for Streamlabs Bot"
Creator = "rvaen17"
Version = "0.0.1"

configFile = "config.json"
settings = {}

def ScriptToggled(state):
	return

def Init():
	global settings

	path = os.path.dirname(__file__)
	try:
		with codecs.open(os.path.join(path, configFile), encoding='utf-8-sig', mode='r') as file:
			settings = json.load(file, encoding='utf-8-sig')
	except:
		settings = {
			"liveOnly": True,
			"responseThreeWide": "/me $user just finished a 3-$emote pyramid! Nice SeemsGood",
		}
	msg = ""
	user = ""
	i = 0
	max = 0

def Execute(data):
	if ((settings["liveOnly"] and Parent.IsLive()) or (not settings["liveOnly"])) and data.IsChatMessage():
		if (i is 0) and (data.GetParamCount() is 1):
			user = data.UserName
			msg = data.getParam(0)
			i += 1
		elif (i > 0) and (data.UserName == user):
			if (data.GetParamCount() is (i + 1)) and (data.getParam(0) == msg) and (len(list(set(data.Message.split(" ")))) == 1):
				i += 1
				max = i
			elif (data.GetParamCount() is (i - 1)) and (data.getParam(0) == msg) and (len(list(set(data.Message.split(" ")))) == 1):
    				i -= 1
				if i == 1:
					if max == 3:
						outputMessage = settings["responseThreeWide"]
						outputMessage.replace("$user", username)
						outputMessage.replace("$emote", msg)
						Parent.SendStreamMessage(outputMessage)
		else:
			i = 0
			max = 0
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
