"""_ Implement a class called player that represents a cricket player.
the player class should have a method called play() which prints "the player is playing cricket.
derive two classes , Batsman and bowler,from the player class.
override the play () method in each derived class to print"the batsman is batting" and "the bowler is bowling", respectively.
write a program to create objects of both the batsman and bowler classes and call the play () method for each object."""


#define the base class player
class player:
  def play (self):
    print("the player is playing cricket.")

#define the drived class batsman
class batsman(player):
  def play(self):
    print("the Batsman is sitting.")

#define the derived class bowler class
class bowler (player):
  def play (self):
    print("the bowler is bowling .")

#creat objects of batsman and bowler class
batsman = batsman()
bowler = bowler()

#call the play () method for each object
batsman.play()
bowler.play()

