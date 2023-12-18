
class CubeSatMissionRequirements:
    def __init__(self):
        self.payload_requirements = []
        self.power_requirements = {}
        self.communication_requirements = {}
        self.orbit_requirements = {}

    def add_payload_requirement(self, payload_type, data_resolution, data_transfer_rate):
        requirement = {
            'payload_type': payload_type,
            'data_resolution': data_resolution,
            'data_transfer_rate': data_transfer_rate
        }
        self.payload_requirements.append(requirement)

    def set_power_requirements(self, average_power, peak_power):
        self.power_requirements['average_power'] = average_power
        self.power_requirements['peak_power'] = peak_power

    def set_communication_requirements(self, data_rate, frequency_band):
        self.communication_requirements['data_rate'] = data_rate
        self.communication_requirements['frequency_band'] = frequency_band

    def set_orbit_requirements(self, altitude, inclination, orbital_period):
        self.orbit_requirements['altitude'] = altitude
        self.orbit_requirements['inclination'] = inclination
        self.orbit_requirements['orbital_period'] = orbital_period

# Example usage
cube_sat_requirements = CubeSatMissionRequirements()

# Payload Requirements
cube_sat_requirements.add_payload_requirement('Imaging', 'High', '1 Mbps')
cube_sat_requirements.add_payload_requirement('Spectroscopy', 'Medium', '500 Kbps')

# Power Requirements
cube_sat_requirements.set_power_requirements(2.5, 5.0)  # in Watts

# Communication Requirements
cube_sat_requirements.set_communication_requirements('1 Mbps', 'UHF')

# Orbit Requirements
cube_sat_requirements.set_orbit_requirements(500, 45, 90)  # in kilometers, degrees, minutes

# Display the requirements
print("CubeSat Mission Requirements:")
print("Payload Requirements:", cube_sat_requirements.payload_requirements)
print("Power Requirements:", cube_sat_requirements.power_requirements)
print("Communication Requirements:", cube_sat_requirements.communication_requirements)
print("Orbit Requirements:", cube_sat_requirements.orbit_requirements)

