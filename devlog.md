5:54 PM, 3/1/2025
I set up the project including taking the python files from the given zip file. This project involves me building a system using three seperate files.
Those include a logger, an encryption program, and a driver program.
I will be doing this project in python, so I will utilize the subprocess module that is available. I will start my session on working the project.

Session ended at 6:30, 3/1/2025
So I mainly spent time really understanding the flow of the project and getting a feel of how I should structure the files and such. I accomplished my goal, so for the next session, I will focus on how the encryption and decryption process works.

1:37 PM, 3/6/2025
I am looking through the files right now. I have understood how to encrypt and decrypt the program and I will setup those functions.
Session ended at 2:15 3/6/2025
During this work session, I made sure to setup the encrypt and decrypt programs and the formula for those programs. I also spent more time really understanding the flow between how the files should interact with each other along with how the user should interact with the program. Next session, I will focus more on the logger file and then start working on the driver file.

7:51 PM, 3/9/2025
So far, I understand how the project is supposed to run. Main file which makes subprocesses where one is the logger file and the other is with the encryption file. I haven't had any new thoughts since the last session. I plan to further finish the logger and then work on the driver file. My goal is to finish the logger, and then maybe start with the driver.

8:30 PM 3/9/2025
So from this work session, I finished setting up the logger file and then began working on the driver. I didn't encounter any problems so far this session as it was mainly just following the pdf instructions that were given about this project. Next session, I hope to finish the driver file and then setup everything and test.

1:40 PM, 3/11/2025
I got a better understanding of the flow between the driver file to the encryption and logger. I need to rechange the scheme in driver and encryption to better send instructions from driver to those subprocesses. My goal is to setup the connection between the logger and the driver properly this work session.

Work Session ended at 2:15 3/11/2025
I wasn't able to get much done this work session, mainly because my environment was rather loud and I had a lot of distractions, so I decided to get work done later, which is why this session wasn't very productive. My next session, I plan to finish the goals I had previously set in my last session.

3:09 pm 3/18/2025
Current thoughts - Nothing new so far, I have not touched the project in some days but I have a clearer idea on what I have to do, and the flow of my project from the driver file to the other two files that are present.
Current session goals - This session, I plan to fix the flow between the files, something that I wasn't able to finish during my last sesssion, so I want to make sure the driver calls the encryption and the logger with proper subprocesses and set those up properly.

8:03 pm 3/18/2025
Session Reflection: So I managed to finish the driver file, and also adjust the connection between the driver and the encryption file and the logger file. I still need to tweak the logger file so that every action is logged better. I didn't encounter any new problems so that was good. I accomplished my goal for this session, so for next session, I want to make sure every connection and logic is sound, then test the code more and make sure it is working properly.

3:56 pm 3/19/2025
Current thoughts - Haven't had any new thoughts.
Current session goals - I plan to do testing to see if my program works the way it is intented to. I originally did testing only for the encryption file to make sure the encrypt and decrypt methods were working properly and they were. I plan to really go through the project and ensure various test cases are working and that the project meets the instructions.

6:30 3/19/2025
Session reflection - I encounted some new problems, mainly the flow between the menus, or going from the seperate history menu back to the main menu, or the encrypted value and decrypted value not being stored in the result properly. I did accomplish part of my goal which was to do testing and see if my project runs so far and if there were any errors. Initially there were some minor error due to me calling the subprocess module directly along with certain type mismatches during input and such, but I managed to address those issues.
Next session - I plan to further test out all the commands and essentially try as many combinations of passwords, encryptions, and decryptions along with further fixing the format the logger.py logs in.

2:45 PM 3/20/2025
Current throughts - Haven't had any new thoughts when it comes to testing and such.
Current session goals - I want to further check all the functionality of the project, and fix some formatting and test various passwords, encryptions, and decryptions. I will then also test it on the cs1 server to make sure my project is functioning properly.

3:16 PM 3/20/2025
Session reflection - Identified two issues that I need to fix. I will do that after attending to another matter that I have which is why this session is cut short.
Next session - I plan to fix the issues I identified and I will elaborate on those issues during my next log when I will say in more detail the issues that I found and that I needed to fix.

3:51 PM 3/20/2025
Current thoughts - Nothing new.
Current session goals - I identified two new issues my last session related to how the user uses the program so I will fix those this session. Those issues are mainly the word RESULT not being printed when the password is set and the history menu displaying 0 to go back, when that shouldn't be there. I will fix those this session along with overall checking if everything is right.

6:29 PM 3/20/2025
Session reflection- So when I ran it on the cs1 server, I encountered problems with the python version I have as I am using python version 3+ and the server has python version 2.7.5, so I had to change a lot of the commands I used, mainly the f" and replaced it with .format() or using sys.stdout.write for the encryption file, along with having to use raw_input() instead of input(), so I had to address those issues. Rerunning it on the server helped me find these issues, so those were the main problems. I was able to fix the UI issues that I had before that I wanted to fix at the start of my session so that was good. I am able to get my project running on the cs1 server so now I am able to do that which is great.
Next session - I am close to finishing the project, I will probably run through all the menus and cases I have and recheck the instructions before submitting, and that will be my goal for next session.

1:39 PM 3/21/2025
Current thoughts - I realized that python3 works on the server.
Current session goals - I am going to revert everything back so it can work on python3. I did not realize the UTD servers has python3 so I will change everything back. I will also just make sure everything works.

1:48 PM 3/21/2025
Session reflection - I think I am going to keep it as I do not know whether testing is going to be done on python or python3.
Next session - I will double check everything and I will probably submit.

1:35 PM 3/24/2025
Current thoughts - I feel good about this project yet I want to make sure there are no errors that pop up.
Current session goals - I will go through my entire project, check every possible user interaction so I can see the areas I need to change. These are minute tweaks so I do not think I should be worried and I can still get the project submitted by tonight.

3:35 PM 3/24/2025
Session reflection: I was able to edit some parts of my program when it comes to error handling and messages that needed to be displayed along with fixing some issues in my program including being able to go back to the main menu from the history menu. I also fixed how the program checks if history is empty or not and the appropriate errors that need to be displayed as such.
Next session goals - I will probably double check all the requirements and submit the project.
