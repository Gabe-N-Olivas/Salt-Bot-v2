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
### PD
- [x] Command Executed
- [x] Empty argument
- [x] Using arg 'list'
- [x] Specific file (Changed so the input is no longer case sensitive)
- [x] Overall Pass

## createcredit
Removed because credit can now create a credit file

## credit
### PD
- [x] Command executed
- [x] Authorized role can execute
- [x] Non-member used (Bad argument reported)
- [x] Non-integer used (Bad argument reported)
- [x] Non-logged member used (Bad argument reported)
- [x] Overall Pass

## devmode (oh boy)
- [x] Command Executed
- [x] Only authorized role can access
- [x] Applies globally
- [x] No args parsed (Added a line where if no arguments are given it shows the status of devmode)
- [x] Overall Pass

## forcetraceback
### NA
- [ ] Command executed (This by nature does not crash safely which is the point.)
- [x] Overall Pass

## 