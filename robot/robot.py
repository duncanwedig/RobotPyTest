import wpilib

class MyRobot(wpilib.TimedRobot):

    def robotInit(self):
        self.motor = wpilib.Jaguar(1)