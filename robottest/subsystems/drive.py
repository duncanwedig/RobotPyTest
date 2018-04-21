import wpilib, ctre
from robottest.constants import robotmap
from wpilib.command import Subsystem
from robotpy_ext.common_drivers import navx


class Drive(Subsystem):

    def __init__(self):

        super().__init__('Drive')

        self.gyro = navx.AHRS.create_spi()

        self.left_master = ctre.WPI_TalonSRX(robotmap.left_master_talon_id)
        self.left_slave = ctre.WPI_VictorSPX(robotmap.left_slave_victor_id)
        # self.left = wpilib.SpeedControllerGroup(self.left_master, self.left_slave)

        self.right_master = ctre.WPI_TalonSRX(robotmap.right_master_talon_id)
        self.right_slave = ctre.WPI_VictorSPX(robotmap.right_slave_victor_id)
        # self.right_side = wpilib.SpeedControllerGroup(self.left_master, self.left_slave)

        self.left_slave.follow(self.left_master)
        self.right_slave.follow(self.right_master)

    def set_percent_output(self, left_power : float, right_power : float):
        self.right_master.set(ctre.ControlMode.PercentOutput, right_power)
        self.left_master.set(ctre.ControlMode.PercentOutput, left_power)

        self.right_slave.set(ctre.ControlMode.PercentOutput, right_power)
        self.left_slave.set(ctre.ControlMode.PercentOutput, left_power)


    def get_left_velocity(self):
        return self.left_master.getSelectedSensorVelocity(0)

    def get_right_velocity(self):
        return self.right_master.getSelectedSensorVelocity(0)

    def get_left_position(self):
        return self.left_master.getSelectedSensorPosition(0)

    def get_right_position(self):
        return self.right_master.getSelectedSensorPosition(0)

    def get_avg_position(self):
        return (self.get_left_position() + self.get_right_position()) / 2

    def get_motor_currents(self):
        left_currents = [self.left_master.getOutputCurrent(), self.left_slave.getOutputCurrent()]
        right_currents = [self.right_master.getOutputCurrent(), self.right_slave.getOutputCurrent()]
        return left_currents + right_currents

    def get_motor_voltages(self):
        left_voltages = [self.left_master.getBusVoltage(), self.left_slave.getBusVoltage()]
        right_voltages = [self.right_master.getBusVoltage(), self.right_slave.getBusVoltage()]
        return left_voltages + right_voltages

    def report_data(self):
        wpilib.SmartDashboard.putNumber('Left speed', self.get_left_velocity())
        wpilib.SmartDashboard.putNumber('Right speed', self.get_right_velocity())
        wpilib.SmartDashboard.putNumber('Left position', self.get_left_position())
        wpilib.SmartDashboard.putNumber('Right position', self.get_right_position())

