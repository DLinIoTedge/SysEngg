

class CubeSatPayload:
    def __init__(self, payload_type):
        self.payload_type = payload_type

    def capture_data(self):
        print(f"Capturing {self.payload_type} data")


class PowerSystem:
    def __init__(self, average_power, peak_power):
        self.average_power = average_power
        self.peak_power = peak_power

    def generate_power(self):
        print(f"Generating power (Average: {self.average_power} W, Peak: {self.peak_power} W)")


class CommunicationSystem:
    def __init__(self, data_rate, frequency_band):
        self.data_rate = data_rate
        self.frequency_band = frequency_band

    def transmit_data(self):
        print(f"Transmitting data (Data rate: {self.data_rate}, Frequency band: {self.frequency_band})")


class OrbitControlSystem:
    def __init__(self, altitude, inclination, orbital_period):
        self.altitude = altitude
        self.inclination = inclination
        self.orbital_period = orbital_period

    def adjust_orbit(self):
        print(f"Adjusting orbit (Altitude: {self.altitude} km, Inclination: {self.inclination} deg, Orbital Period: {self.orbital_period} min)")


class CubeSatMission:
    def __init__(self):
        self.payload = None
        self.power_system = None
        self.communication_system = None
        self.orbit_control_system = None

    def set_payload(self, payload_type):
        self.payload = CubeSatPayload(payload_type)

    def set_power_system(self, average_power, peak_power):
        self.power_system = PowerSystem(average_power, peak_power)

    def set_communication_system(self, data_rate, frequency_band):
        self.communication_system = CommunicationSystem(data_rate, frequency_band)

    def set_orbit_control_system(self, altitude, inclination, orbital_period):
        self.orbit_control_system = OrbitControlSystem(altitude, inclination, orbital_period)

    def execute_mission(self):
        if self.payload:
            self.payload.capture_data()

        if self.power_system:
            self.power_system.generate_power()

        if self.communication_system:
            self.communication_system.transmit_data()

        if self.orbit_control_system:
            self.orbit_control_system.adjust_orbit()


# Example usage
cube_sat_mission = CubeSatMission()

# Set mission parameters
cube_sat_mission.set_payload('Imaging')
cube_sat_mission.set_power_system(2.5, 5.0)  # Average power, Peak power
cube_sat_mission.set_communication_system('1 Mbps', 'UHF')  # Data rate, Frequency band
cube_sat_mission.set_orbit_control_system(500, 45, 90)  # Altitude, Inclination, Orbital period

# Execute the mission
cube_sat_mission.execute_mission()

