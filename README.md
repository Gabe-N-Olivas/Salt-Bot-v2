
# Salt Bot Version 2

A discord bot used by me and my friends feel free to fork and use on your server! This is a bot mean't to do everything!* It includes some basic bot functions, administration tools, games, and much more!

*By everything I mean what ever I put into it
## Installation

This is a pure python project which means there's no way to "install" it but you can run it and here's how

```bash
  git clone https://github.com/Gabe-N-Olivas/Salt-Bot-v2
  cd Salt-Bot-V2
  python3 bot.py
```
If you want to run this in the background do the following (This is assuming this script is job #1 to be sure run ```jobs``` to see which job this script this is):

Do the key combo 'Ctrl+Z'
Then enter the following commands
```bash
  bg
  disown %1
```


After that you may also want to customize it a little. Some ways you can do this is by replacing images in the ```./Frontend/RandMeme``` folder with your own fun images and fill in ./Frontend/txt/pasta with your own funny messages (so long as they're under 4000 characters).

Another thing you may want to do is change the default dev password (root) using the the makehash.py file.

## Roadmap

Right now I'm the only one who's running this project and between school, and work I may not have a ton of time to work on this project. That being said here's what I plan for the future of this bot in order of priority:

1. Implement Embeds. This will make the output of the bot look a lot cleaner and more organized
2. Add a .conf file for global customization. This will allow for greater customization for bot hosters as well as reducing the risk of a user ruining smooth operation of the bot.
3. Add a console for direct access to the bot. I admit this will most likely cause instability but I think it would be a good option for bot hosters.
4. Switch the bot from using prefixes to discords new "/" commands.


## Used By

This project is used by the following servers:

- The Salt Locker
- Mr.BlueSky's House
- Maybe Your Server!


## License

This project is licensed under the GPL V2. I recommend you read the full license at the end of this file but for those who wont here's the TL;DR:

Also this is not legal advice I'm just a novice programmer not a fully trained lawyer!

- What you *CAN* do: This license allows **Modification**, **Distribution**, **Commercial Usage**, and **Placement of Warranty** 
- What you *CANNOT*: This license does not allow **Sublicensing**, and **Holding The Developer Liable**
- what I *MUST* do: This license requires me to **Include Original Code**, **Disclose Source Code**, **Include License**, and **State Changes To Source Code**

  [Read Full License Here](https://www.gnu.org/licenses/old-licenses/gpl-2.0.html)

