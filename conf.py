### This file is not complete it the following sections
### - Some settings need to be made
### - All settings implemented

#! DO NOT EDIT UNLESS YOU KNOW WHAT YOU ARE DOING

v = "2.1"
creditPath = './Frontend/txt/credit.json'
hashPath = './Backend/hash'
tokenPath = 't0ken.secret'
tokenIntegrityCheck = True
modRole = 'BotAuth'
devRole = 'Dev'

### bot.py settings

devmodeOnByDefault = False
devmodeOnBeta = False
devmodeOnAlpha = True
prefix = '$'

### admin.py settings

maxPurge = 20
muteRole = 'Muted'
muteMessage = "you've been muted if you have any questions message the mods"
unmuteMessage = "you've been unmuted" 
banMessage = "you've been banned if you have any questions message the mods"

### base.py settings

newMemberMessage = "Have Fun!"
privacyPolicyURL = "https://github.com/Gabe-N-Olivas/Salt-Bot-v2/blob/main/privacyPolicy.md"
aboutMsg = f"This is SaltBOT {v}\nThis bot was created by Gabe-N-Olivas\nThis work is licensed under the GNU General Public License v2. \nThe official repository for SaltBOT is located at https://github.com/Gabe-N-Olivas/Salt-Bot-v2"
defaultEmojiImgURL = f'https://twemoji.maxcdn.com/v/latest/72x72/'

### define.py settings
commandCaseInsensitivity = True

### dev.py settings

requireHash = True
hashIntegrityCheck = True
testLogMessage = "𝔗 (Fancy T), 😊 (Emoji), ‱ (Special Math Symbol), ※ ௹ ⨌ (Unicode Symbols), Ὥ(Greek Symbol) This should have been saved perfectly with no boxes"

### fun.py settings

copypastaPath = "./Frontend/txt/pasta"
memeMePath = "./Frontend/img/memeMe"
gatoPath = "./Frontend/img/gato"

### game.py settings

### log.py settings
logSavePath = "log"
### loggedOnly.py settings

### custom settings & imports
### Only use your own custom settings if you know what you are doing