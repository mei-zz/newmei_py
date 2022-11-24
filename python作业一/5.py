#第21题
import math
horizontal=0    #水平方向
vertical=0      #垂直方向
class Robot():
    def __init__(self,UP,DOWN,LEFT,RIGHT):
        super(Robot, self).__init__()
        self.UP = UP
        self.DOWN = DOWN
        self.LEFT = LEFT
        self.RIGHT = RIGHT
    def move_horizontal(self):
        horizontal=abs(self.RIGHT-self.LEFT)
        return horizontal
    def move_vertical(self):
        vertical = abs(self.UP - self.DOWN)
        return vertical
    def distance(self,horizontal,vertical):
        print(round(math.sqrt(horizontal*horizontal+vertical*vertical)))
if __name__ == '__main__':
    UP, DOWN, LEFT, RIGHT=input().split(" ")
    robot=Robot(int(UP), int(DOWN), int(LEFT), int(RIGHT))
    robot.distance(robot.move_horizontal(),robot.move_vertical())