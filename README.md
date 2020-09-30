# SquirrelXmas
This project is intended to serve as an enrichment activity for my Cyber Security class. It is written mainly in Python and runs on a Raspberry Pi running a LAMP server.

## Challenges:
0. This challenge must be completed to get into the game. The 4 lights on the front of the decoration are blinking a message in binary. The message tells the students to visit a URL.
1. WW91IGhhdmUgbWFkZS - The URL from Challenge 0 outlines the rules of the game and directs them to look around. The answer we are looking for is hidden in the source code of the web page. A simple "view-source" will reveal it.
2. BpdCB0aHJvdWdoIGFs - This challenge involves reading an ascii-art text image and realizing that it is an encoded message. Once you see the message, you can decode it with any of a number of Caesar Cipher solvers. It will direct you to the timallen directory. You also are given Item1.
3. bCBvZiB0aGUgY2hhbG - This challenge leads the students to use forceful browsing to find a file named XmasList.txt. GitHub will not copy empty directories so unfortunately, you will have to create 5 identical directories (door1-5), with 5 identical directories inside (cabinet1-5), each with 5 identical directories (drawer1-5). 
4. xlbmdlcyBleGNlcHQg - This one is specific to EOC Tech. The map leads you to a small picture of Secret Squirrel that has Item2 and the location of the next challenge on it.
5. b25lLiBHbyB0byB0aG - This one is a simple steganography challenge. There is a comment in this image that sends you to the next challenge. The image itself reveals Item3.
6. lzIFVSTCB0byBmaW5k - This challenge is really a grep problem. Can you figure out which day only had one event? Grepping makes this easy. The answer sends you to a directory with the next challenge in it and gives you Item4.
7. IG91dCBtb3JlOiBodH - This is a straight password cracking challenge. Using the RockYou list will yield Santa's password as christmastree. By visiting that directory, you are rewarded with the next challenge.
8. RwOi8vMTcyLjE2LjEy - Can you Google? This requires the student to realize that this is a Dell computer and that you can use the ST(Service Tag) number to lookup what the actual model and specs are. You will find that it is in need of part number Y48CM which leads to the next challenge and gives you Item5.
9. Mi4yMTUvVGhlRmluYW - This challenge forces you to send a custom header to get to the next challenge. You can do this with a browser extension or by using curl to send a header named cookies with a value of gingerbread.
10. xDaGFsbGVuZ2U - This is a check to make sure they've done all of the challenges. They can put them all in order and build a base64 encoded string that decodes into the location of the TheFinalChallenge.

The final challenge asks students to blink the light at the top of the Christmas Tree in yellow. They should be able to use the items they've collected as follows:
- Item 1: username of a user allowed to ssh into the raspberry pi
- Item 2: password for the user
- Item 3: port that ssh is running on
- Item 4: wiring diagram for the decoration to allow the student to see what pins are being used on the Pi.
- Item 5: sample code of how to blink a light on the Pi. 
With all of these items, the students will have enough information to remote into the Pi and write a small program that will blink the yellow star on the Christmas tree.
