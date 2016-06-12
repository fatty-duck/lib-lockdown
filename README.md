# lib-lockdown

This rather simple script was used for Library Lockdown, a  program at Morton-James Public Library in Nebraska City, NE where children built an escape room.

The program has a command line interface and prompts for 'passcodes', which players find by solving puzzles in the room. Once they enter enough passcodes, the program provides the final code--the PIN number for the safe, in our case. 

The program includes 3 levels of 'winning'. To get the passcode, only 8 of the 10 puzzles must be solved. Solving the 9th and 10th allows players to achieve Silver and Gold status, respectively. 

Codes can be entered in in any order and are not case sensitive. 

The configuration file, passcodes.cfg, can be used to modify the program. You can determine the passcode values, as well as the number of codes required to retrieve the final code. You can modify or remove the text excerpts, as well. 

The release includes the Python source code, as well as an executable created for Windows. 

# Windows

To run the program, double click on passcodes.exe in the dist folder. The default passcodes are a, b, c, d, e, f, g, h, i, j.

To tailor the program for your own purposes (for example, choosing the passcodes), open passcodes.cfg in a text editor (e.g. Notepad), make any changes and save.
