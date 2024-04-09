'''
Plan to create a bracket typing game in the game bracket characters
will fall load into a buffer at a random speed this is just a project 
for fun lets see how it goes

needs
1. Character array Buffer to act as a game screen
2. Likely going to use a character loop
3. A secondary buffer to grab target characters positions
4. kill logic to delete character from buffer
'''
#imports
import time, random, sys

#setting up config variables to change game play options


def draw_buffer(screen_buffer):
    for count,character in enumerate(screen_buffer):
        sys.stdout.write(screen_buffer[count])
        sys.stdout.flush()
        if count%50 == 49:
            print("\n")
    return 0

def main():
    #basic game settings
    blank = '-'
    bracket_characters="(){}[]#_,=+/%"
    game_speed = 10
    player_lives = 1
    
    #setting up our screen buffer
    #we will use a 500 character array
    #to give us a 10hx50w psuedo screen
    #we also set up a blank space character so we
    screen_buffer =  [blank for i in range(500)]
    game_ticker=0
    while player_lives > 0:
        game_ticker+=1
        time.sleep(0.1)
                
        #print(screen_buffer.pop(),end='',flush=True)
        if game_ticker % game_speed == 0:
            #print(random.choice(bracket_characters),end="")
            screen_buffer.append(random.choice(bracket_characters))
        else: 
            screen_buffer.append(blank)
        draw_buffer(screen_buffer)
        if game_ticker % 50 ==0:
            print(":", end="\n")
        if game_ticker > 300:
            player_lives=player_lives-1
    return 0

if __name__ == "__main__":
    main()

