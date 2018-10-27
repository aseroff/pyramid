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

def Execute(data):
  if ((settings["liveOnly"] and Parent.IsLive()) or (not settings["liveOnly"])):
	  if data.IsChatMessage() and data.GetParam(0)
    
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
