import wpilib
from robot.systems import drive


class MyRobot(wpilib.TimedRobot):

    def robotInit(self):
        self.drivetrain = drive.Drive()

