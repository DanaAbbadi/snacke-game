import random
import curses
import time

# Part 1: Initialize the screen size
sc = curses.initscr()  
h, w = sc.getmaxyx()   
win = curses.newwin(h, w, 0, 0) 

win.keypad(1)  
curses.curs_set(0)  

# Part 2: Initialize snake and apple initial positions

snake_head = [10,15]
snake_position = [[15,10],[14,10],[13,10]]
apple_position = [20,20]
score = 0

win.addch(apple_position[0], apple_position[1], curses.ACS_DIAMOND)

prev_button_direction = 1
button_direction = 1
key = curses.KEY_RIGHT


# Part 3: Specifying Game Over Conditions and Scoring

def collision_with_boundaries(snake_head):
    """
     Game will end if the snake crosses the boarder of the screen
    """

    if snake_head[0]>=h-1 or snake_head[0]<=0 or snake_head[1]>=w-1 or snake_head[1]<=0 :
        return 1
    else:
        return 0

def collision_with_self(snack_position):
    """
    Game ends if snake collides with itself
    """
    snake_head = snake_position[0]
    if snake_head in snake_position[1:]:
        return 1
    else:
        return 0

def collision_with_apple(score):
    apple_position = [random.randint(1,h-2),random.randint(1,w-2)]
    score += 1
    return apple_position, score

# Part 4: Playing the Game
a = []
while True:

    win.border(0) 
    win.timeout(100) 
    next_key = win.getch() 

    if next_key == -1:
        key = key
    else:
        key = next_key



    if key == curses.KEY_LEFT and prev_button_direction != 1:
        button_direction = 0
    elif key == curses.KEY_RIGHT and prev_button_direction != 0:
        button_direction = 1
    elif key == curses.KEY_UP and prev_button_direction != 2:
        button_direction = 3
    elif key == curses.KEY_DOWN and prev_button_direction != 3:
        button_direction = 2
    else:
        pass

    prev_button_direction = button_direction

    # Move snake

    if button_direction == 1:
        snake_head[1] += 1

    elif button_direction == 0:
        snake_head[1] -= 1

    elif button_direction == 2:
        snake_head[0] += 1

    elif button_direction == 3:
        snake_head[0] -= 1



    if snake_head == apple_position:
        apple_position, score = collision_with_apple(score) 
        snake_position.insert(0, list(snake_head))
        a.append(apple_position)
        win.addch(apple_position[0], apple_position[1], curses.ACS_DIAMOND)

    # snake didn't eat the apple, but is just moving
    else:
        snake_position.insert(0,list(snake_head))
        last = snake_position.pop()
        win.addch(last[0], last[1], ' ') 

    # ending the game
    if collision_with_boundaries(snake_head) == 1 or collision_with_self(snake_position) == 1:
            break
    # Display the snake
    win.addch(snake_position[0][0], snake_position[0][1], '#')


#print score
sc.addstr(10, 30, 'Your Score is:  '+str(score))
sc.refresh()
time.sleep(2)
curses.endwin()
print(a)
print(w,h)