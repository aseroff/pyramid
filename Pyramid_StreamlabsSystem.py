import os
import sys
import json
import codecs

ScriptName = "Emote Pyramid"
Website = "https://github.com/aseroff/pyramid/"
Description = "Congratulate users on completion of emote pyramids"
Creator = "rvaen17"
Version = "1.2.1"

CONFIG = "config.json"
SETTINGS = {}
MSG = ""
USER = ""
COUNT = 0
WIDTH = 0
MAXIMUM = 0
DESC = False


def ScriptToggled(state):
    return


def Init():
    global CONFIG, SETTINGS

    path = os.path.dirname(__file__)
    try:
        with codecs.open(os.path.join(path, CONFIG), encoding='utf-8-sig', mode='r') as file:
            SETTINGS = json.load(file, encoding='utf-8-sig')
    except:
        SETTINGS = {
            "liveOnly": False,
            "multiUser": False,
            "responseBlocked": "/me $user with the block! Kappa",
            "responseChoked": "/me $user managed to mess up their own pyramid. NotLikeThis",
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
    global MSG, USER, COUNT, WIDTH, MAXIMUM, DESC, SETTINGS
    if ((SETTINGS["liveOnly"] and Parent.IsLive()) or (not SETTINGS["liveOnly"])) and data.IsChatMessage():
        if WIDTH > 0:
            if ((data.UserName == USER) or SETTINGS["multiUser"]):
                set_count(data.Message, data.UserName)
                if (DESC == False) and (COUNT == (WIDTH + 1)):
                    WIDTH = COUNT
                    MAXIMUM = WIDTH
                elif COUNT == (WIDTH - 1):
                    WIDTH -= 1
                    DESC = True
                    if WIDTH == 1:
                        if MAXIMUM > 2:
                            Parent.SendStreamMessage(complete_message(MAXIMUM).replace("$user", USER).replace("$emote", MSG))
                            Parent.AddPoints(data.User, data.UserName, complete_reward(MAXIMUM))
                        reset()
                else:
                    if data.UserName == USER:
                        Parent.SendStreamMessage(SETTINGS["responseChoked"].replace("$user", data.UserName))
                    else:
                        Parent.SendStreamMessage(SETTINGS["responseBlocked"].replace("$user", data.UserName))
                    reset()
            elif (WIDTH > 1 or ((WIDTH == 1) and DESC)):
                Parent.SendStreamMessage(SETTINGS["responseBlocked"].replace("$user", data.UserName))
                reset()
        else:
            reset(data.Message, data.UserName)
    return


def set_count(message, username):
    global MSG, COUNT
    split = message.strip().split(" ")
    if (len(list(set(split))) == 1) and (split[0] == MSG) and (split[0] != ""):
        COUNT = len(split)
    else:
        reset(message, username)
    return


def reset(message="", username=""):
    global MSG, USER, COUNT, WIDTH, DESC
    if message != "":
        split = message.strip().split(" ")
        if len(split) == 1:
            MSG = split[0]
            USER = username
            COUNT = 1
            WIDTH = 1
            DESC = False
    else:
        MSG = ""
        USER = ""
        COUNT = 0
        WIDTH = 0
        DESC = False
    return


def complete_message(pyramid_width):
    global SETTINGS
    message = ""
    if pyramid_width >= 3:
        switcher = {
            3: SETTINGS["responseThreeWide"],
            4: SETTINGS["responseFourWide"],
            5: SETTINGS["responseFiveWide"],
            6: SETTINGS["responseSixWide"],
            7: SETTINGS["responseSevenWide"],
            8: SETTINGS["responseEightWide"],
            9: SETTINGS["responseNineWide"]
        }
        message = switcher.get(pyramid_width) or SETTINGS["responseTenPlusWide"]
    return message


def complete_reward(pyramid_width):
    global SETTINGS
    value = 0
    if pyramid_width >= 3:
        switcher = {
            3: SETTINGS["rewardThreeWide"],
            4: SETTINGS["rewardFourWide"],
            5: SETTINGS["rewardFiveWide"],
            6: SETTINGS["rewardSixWide"],
            7: SETTINGS["rewardSevenWide"],
            8: SETTINGS["rewardEightWide"],
            9: SETTINGS["rewardNineWide"]
        }
        value = switcher.get(pyramid_width) or SETTINGS["rewardTenPlusWide"]
    return value


def ReloadSettings(jsonData):
    Init()
    return


def OpenReadMe():
    location = os.path.join(os.path.dirname(__file__), "README.txt")
    os.startfile(location)
    return


def Tick():
    return
