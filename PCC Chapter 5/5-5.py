# 5-5. Alien Colors #3: Turn your if-else chain from Exercise 5-4 into an if-elifelse
# chain.
# • If the alien is green, print a message that the player earned 5 points.
# • If the alien is yellow, print a message that the player earned 10 points.
# • If the alien is red, print a message that the player earned 15 points.
# • Write three versions of this program, making sure each message is printed
# for the appropriate color alien.

def test_color(color):
    if color=='green':
        print("You earned 5 points")
    elif color=='yellow':
        print("You earned 10 points")
    else:
        print("You earned 15 points")

alien_color= 'green'
test_color(alien_color)

alien_color = 'yellow'
test_color(alien_color)

alien_color = 'red'
test_color(alien_color)