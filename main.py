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
#setting up config variables to change game play options

blank = '-'


def main():
    #setting up our screen buffer
    #we will use a 500 character array
    #to give us a 10hx50w psuedo screen
    #we also set up a blank space character so we

    sb =  [blank for i in range(500)]
    
    for count,character in enumerate(sb):
        print(sb[count],end="")
        if count%50 == 49:
            print("\n")
    
    return 0

if __name__ == "__main__":
    main()

