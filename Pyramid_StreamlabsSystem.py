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
msg = ""
user = ""
count = 0
width = 0

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
			"liveOnly": False,
			"responseThreeWide": "/me $user just finished a 3 $emote pyramid! Nice SeemsGood",
		}
def Execute(data):
	global msg, user, count, width
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
