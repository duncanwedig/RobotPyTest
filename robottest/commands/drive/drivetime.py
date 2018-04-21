import wpilib, ctre
from robottest.subsystems.drive import Drive
from robottest.robot import Robot
from wpilib.command import Command


class DriveTime(Command):

    def __init__(self, timeout: float, power : float):
        self.requires(Robot.drivetrain)
        self.m_start_time = 0
        self.m_timeout = timeout
        self.m_power = power

    def initialize(self):
        self.m_start_time = wpilib.Timer.getFPGATimestamp()

    def execute(self):
        Robot.drivetrain.set_percent_output(self.m_power, self.m_power)

    def isFinished(self):
        return wpilib.Timer.getFPGATimestamp() - self.m_start_time >= self.m_timeout

    def end(self):
        Robot.drivetrain.set_percent_output(0, 0)

    def interrupted(self):
        self.end()