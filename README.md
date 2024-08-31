# KuraTica-Tac-Toe

--------------------- GAME OVERVIEW --------------------------
This is an innovative take on the old Tic-Tac-Toe game, complete with interactive visuals, adjustable music, and easy-to-use controls. The game is meant for two players, and each takes turns placing their markings (X or O) on a 3x3 hexagonal grid. To win the round, align three of your markers horizontally, vertically, or diagonally. The game is a best-of-five series, with the first player to win three rounds claiming the overall victory. The game also has a tie score tracker, soundtrack control, and a beginner's guide.


--------------------- SET-UP INSTRUCTIONS --------------------------

1. Install the latest python from the original website
   https://www.python.org/
2. Using your Visual Studio Code
   - Run new terminmal
   - Type python --version to make sure the python is installed and it's in the path
   - Type pip install pygame
   - Wait for a second to install the software
3. Download the ZIP File in this github repository
4. Extract the files in your designated path
5. Run the python file in your Visual Studio Code
DONE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

--------------------- TECHNICAL DEPENDENCIES --------------------------
1. Ensure that the Python 3.x is installed on your system
  To check type in the terminal/cmd python --version
2. Ensure that Pygame is installed on your system as this game relies on the pygame library for rendering the graphics
   To download pygame, just type in the terminal/cmd pip install pygame

--------------------- COMPATIBILITY --------------------------
1. The game is compatible with Windows, macOS, and Linux. However, this was tested and created using Windows 10
2. The game is designed to run on standard screen resolutions but to have optimal experience, 

add this code:
#This code sets the screen size based on the size of the start screen image
screen_size = start_screen_image.get_size()
screen = pygame.display.set_mode(screen_size)
#To modify the screen size
screen_size = ( , )  # Just input your desired screen size inside of the parentheses for example: (1920, 1080)
screen = pygame.display.set_mode(screen_size)

IF YOU MODIFY THE SCREEN SIZE, MAKE SURE TO POSITION YOUR GAME ELEMENTS (BUTTONS, GRID, TEXT) BASED ON THE SCREEN SIZE SO YOU MIGHT NEED TO ADJUST THE POSITION TO FIT THE NEW RESOLUTION!

THAT'S ALL!! BEST OF LUCK!!!!!!  


   
