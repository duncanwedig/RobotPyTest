import wpilib, ctre
from robot.constants import robotmap


class Drive(object):

    def __init__(self):

        self.left_master = ctre.WPI_TalonSRX(robotmap.left_master_talon_id)
        self.right_master = ctre.WPI_TalonSRX(robotmap.right_master_talon_id)

        self.left_slave = ctre.WPI_VictorSPX(robotmap.left_slave_victor_id)
        self.right_slave = ctre.WPI_VictorSPX(robotmap.right_slave_victor_id)

        self.left_slave.follow(self.left_master)
        self.right_slave.follow(self.right_master)

    def get_left_velocity(self):
        return self.left_master.getSelectedSensorVelocity(0)

    def get_right_velocity(self):
        return self.right_master.getSelectedSensorVelocity(0)

