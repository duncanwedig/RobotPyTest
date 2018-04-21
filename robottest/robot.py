import wpilib
from robottest.subsystems import drive
from wpilib.command import Command
from commandbased import CommandBasedRobot
from robottest.commands.drive import drivetime


class Robot(CommandBasedRobot):

    drivetrain = drive.Drive()

    def robotInit(self):
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
        autonomous_command = drivetime.DriveTime(5, 0.5)
        autonomous_command.start()

    def autonomousPeriodic(self):
        self.scheduler.getInstance().run()



if __name__ == "__main__":
    wpilib.run(Robot)

