import wpilib
from robottest.systems import drive
from wpilib.command import Command
from commandbased import CommandBasedRobot


class MyRobot(CommandBasedRobot):

    def robotInit(self):
        # self.drivetrain = drive.Drive()
        pass

    def disabledInit(self):
        pass

    def disabledPeriodic(self):
        self.scheduler.getInstance().removeAll()

    def teleopInit(self):
        pass

    def teleopPeriodic(self):
        self.scheduler.getInstance().run()

    def autonomousInit(self):
        pass

    def autonomousPeriodic(self):
        self.scheduler.getInstance().run()



if __name__ == "__main__":
    wpilib.run(MyRobot)

