from game import Game
if __name__ == "__main__":
    game = Game()
    while True:
        game.handle_events()
        game.update()
        game.draw()

#This allows us to loop through the game class
#The game class serves as the backbone to the game as it creates and runs the game window
#This allows for the program to first recieve all the player input , then update all the affect methods / objects and finall display for the player