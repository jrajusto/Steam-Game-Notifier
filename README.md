# Steam-Game-Notifier
Project for CPE106l

# Description
This program allows the user to browse games and see which games have discounts on certain stores. The user can store their wanted games in a bookmark list and be notified when discounts are available. The application keeps track of the games and prices through a database that is updated by accessing the Steam and IsThereAnyDeal's API.



# How to Use
To use this application, you must first have Kivy installed.

Although the program does not require any specific version, the Kivy version that it is using is 2.0.0.

To install Kivy, follow the steps indicated for your operating system on Kivy's official documentation: https://kivy.org/doc/stable/gettingstarted/installation.html#

It is also recommended to install kivy on a virtual environment to keep things clean and tidy.

To start the console application, go to the Console folder and run the Steam_games_notifier.py. As soon as you start the program, you will be asked to login, for now you can input jrajusto as the username and pass123 as the password. The program will then show your notificaions list and the different choices that you could do in the program. 

If you enter 0, the program will quit.
If you enter 1, you will be able to search the database for its games by name, you dont need to input all the words as long as you input the letters that includes the name but it is recommended to enter the whole name for better filtering. After searching, you will be prompted if you want to add any of the games to you bookmarks list, if you enter y, then you need to enter the game number which is shown on the screen that is associated to the game that you want to add to your bookmarks.
If you enter 2, the games wilth 100% discount according to the database will be shown.
If you enter 3, the games and their associated prices in your bookmarks list will be shown.
If you enter 4, your notifications will be shown. It will be displayed with the format of  "The game TEKKEN 7 now has a 27% discount on Steam!"
If you enter 5, the database will be updated with new games from steam and the prices and discounts of the existing games. 

