# Stable Release Testing
This is to test a stable release of SaltBot and showing what was done

Guide
NA - No Arguments

PD - Pulls from a local directory

PI - Pulls content from the internet

RA - Response needed after command

If a report has () next to it it means that it failed but it had a safe way of taking care of the error
## about 
#### NA
- [x] Command Executed
- [x] Overall Pass

## avatar 
#### PI
- [x] Command Executed
- [x] Non-Member used (Bad Argument Reported)
- [x] Non-User used (Bad Argument Reported)
- [x] Overall Pass

## big 
#### PI
- [x] Command Executed
- [x] Default Emojis
- [x] Server Emojis
- [x] Animated Server Emoji
- [x] Nitro Emoji (Bad Argument Reported)
- [x] Non-Emoji (Bad Argument Reported)
- [x] Overall Pass

## copypasta
#### PD
- [x] Command Executed
- [x] Empty argument
- [x] Using arg 'list'
- [x] Specific file (Changed so the input is no longer case sensitive)
- [x] Overall Pass

## createcredit
Removed because credit can now create a credit file

## credit
#### PD
- [x] Command executed
- [x] Authorized role can execute
- [x] Non-member used (Bad argument reported)
- [x] Non-integer used (Bad argument reported)
- [x] Non-logged member used (A new key is created for that member)
- [x] Overall Pass

## devmode
- [x] Command Executed
- [x] Only authorized role can access
- [x] Applies globally
- [x] No args parsed (Added a line where if no arguments are given it shows the status of devmode)
- [x] Overall Pass

## forcetraceback
#### NA
- [ ] Command executed (This by nature does not crash safely which is the point.)
- [x] Only authorized role can access
- [x] Overall Pass

## gato
#### NA PD
- [x] Command executed
- [x] Overall Pass

## mememe
#### NA PD
- [x] Command executed
- [x] Handles large files (Reports the file chosen was too large)
- [x] Overall Pass

## mute & unmute
- [x] Command executed
- [x] Only authorized role can access
- [x] No Muted role in server (Reported back there is no muted role)
- [x] Non-member used (Bad argument reported)
- [x] Non-User used (Bad Argument Reported)
- [x] Overall Pass

## pingmod
#### NA
- [x] Command executed
- [x] Overall Pass

## prfxchng
- [x] Command executed
- [x] Only authorized role can access
- [x] Prefix with space used (Reported back the prefix was rejected)
- [x] Overall Pass

## privacypolicy
#### NA
- [x] Command executed
- [x] Overall Pass

## purge
- [x] Command executed
- [x] Only authorized role can access
- [x] Over 20 messages deleted (Reports amount not supported)
- [x] Non-int used (Reports invalid number used)
- [x] Overall Pass

## randmath
#### RA
- [x] Command executed
- [x] Non-existent difficulty used (Defaults to hard)
- [x] First stage timeout (Timeout error given)
- [x] Second stage timeout (Gives the correct answer)
- [x] Wrong answer given (Gives correct answer)
- [x] Correct answer given
- [x] Overall Pass

## refresh
#### NA
- [x] Command executed
- [x] Only authorized role can access
- [x] Overall Pass

## rps
#### RA
- [x] Command executed
- [x] Time out (Timeout error given)
- [x] Non option used (Bad argument reported)
- [x] Overall Pass

## sh
- [x] Command executed
- [x] Only authorized role can access
- [x] Overall Pass

## slap
- [x] Command executed
- [x] Non-Member used (Bad argument reported)
- [x] Non-user used (Bad argument reported)
- [x] Overall Pass

## test
#### NA
- [x] Command executed
- [x] Overall Pass

## testlog
#### NA PD
- [x] Command executed
- [x] Only authorized role can access
- [x] Overall Pass

## toggle
- [x] Command executed
- [x] Only authorized role can access
- [x] Toggle used as arg (Reports that toggle can not be used)
- [x] Overall Pass