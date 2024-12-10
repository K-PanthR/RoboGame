import pgzrun
import random

WIDTH=600
HEIGHT=600
TITLE="Robo_Game"

bg=Actor("grass")
RoboIDLE=Actor("robot_idle")
Coin=Actor("coin_gold")
Bomb=Actor("bomb")

velocity=5
game_over=False
Timer=0

def Start():
    global velocity , game_over , Timer
    RoboIDLE.pos=WIDTH//2 , HEIGHT//2
    move_Coin()
    move_Bomb()

def move_Coin():
    Coin.x = random.randint(20 , WIDTH - 20)
    Coin.y = random.randint(20 , HEIGHT - 20)

    while Coin.colliderect(Bomb) or Coin.colliderect(RoboIDLE):
        Coin.x = random.randint(20 , WIDTH - 20)
        Coin.y = random.randint(20 , HEIGHT - 20)

def move_Bomb():
    Bomb.x = random.randint(20 , WIDTH - 20)
    Bomb.y = random.randint(20 , HEIGHT - 20)

    while Bomb.colliderect(Bomb) or Bomb.colliderect(RoboIDLE):
        Bomb.x = random.randint(20 , WIDTH - 20)
        Bomb.y = random.randint(20 , HEIGHT - 20)

def draw():
    screen.clear()
    bg.draw()
    Bomb.draw()
    Coin.draw()
    RoboIDLE.draw()

def update():
    if keyboard.left and RoboIDLE.left > 0:
        RoboIDLE.image="robot_left"
        RoboIDLE.x-=10

    if keyboard.right and RoboIDLE.right > 0:
        RoboIDLE.image="robot_right"
        RoboIDLE.x+=10

    if keyboard.down and RoboIDLE.bottom > 0:
        RoboIDLE.y+=10

    if keyboard.up and RoboIDLE.top > 0:
        RoboIDLE.y-=10

    if RoboIDLE.colliderect(Coin):
        #sounds.jump3.play()
        move_Coin()

    if RoboIDLE.colliderect(Bomb):
        #sounds.bomb_explosion.play()
        move_Bomb()

def on_key_up(key):
    if key==keys.left or key==keys.right:
        RoboIDLE.image="robot_idle"

Start()

pgzrun.go()