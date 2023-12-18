pip install control

import numpy as np
import control as ctrl
import matplotlib.pyplot as plt
from scipy.integrate import odeint



# Quadcopter dynamics model
def quadcopter_dynamics(state, t, u, params):
    """
    Quadcopter dynamics model.
    state: [phi, theta, psi, p, q, r]
    u: [phi_cmd, theta_cmd, psi_cmd]
    params: [Jx, Jy, Jz, Jr, l, m, g]
    """
    phi, theta, psi, p, q, r = state
    phi_cmd, theta_cmd, psi_cmd = u
    Jx, Jy, Jz, Jr, l, m, g = params

    # Attitude dynamics
    phi_dot = p + (q * np.sin(phi) + r * np.cos(phi)) * np.tan(theta)
    theta_dot = q * np.cos(phi) - r * np.sin(phi)
    psi_dot = (q * np.sin(phi) + r * np.cos(phi)) / np.cos(theta)

    # Angular velocity dynamics
    p_dot = (Jy - Jz) / Jx * q * r + Jr / Jx * l * (theta_cmd - theta)
    q_dot = (Jz - Jx) / Jy * p * r + Jr / Jy * l * (phi_cmd - phi)
    r_dot = (Jx - Jy) / Jz * p * q + (Jr / Jz) * (psi_cmd - psi)

    return [phi_dot, theta_dot, psi_dot, p_dot, q_dot, r_dot]

# PID controller
class PIDController:
    def __init__(self, Kp, Ki, Kd):
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd
        self.prev_error = 0
        self.integral = 0

    def update(self, error, dt):
        self.integral += error * dt
        derivative = (error - self.prev_error) / dt
        output = self.Kp * error + self.Ki * self.integral + self.Kd * derivative
        self.prev_error = error
        return output

# Simulation parameters
dt = 0.01
t_sim = np.arange(0, 10, dt)

# Quadcopter parameters
quad_params = [0.1, 0.1, 0.1, 0.01, 0.2, 0.5, 9.8]

# Desired attitude angles (roll, pitch, yaw)
phi_cmd = np.zeros_like(t_sim)
theta_cmd = np.zeros_like(t_sim)
psi_cmd = np.zeros_like(t_sim)

# PID controller gains
Kp = 2.0
Ki = 0.1
Kd = 0.5

# Create PID controllers for roll, pitch, and yaw
pid_roll = PIDController(Kp, Ki, Kd)
pid_pitch = PIDController(Kp, Ki, Kd)
pid_yaw = PIDController(Kp, Ki, Kd)

# Initial conditions
initial_state = [0, 0, 0, 0, 0, 0]

# Simulation loop
states = np.zeros((len(t_sim), len(initial_state)))
states[0, :] = initial_state

for i in range(1, len(t_sim)):
    time = [t_sim[i - 1], t_sim[i]]
    control_input = [phi_cmd[i], theta_cmd[i], psi_cmd[i]]
    ode_output = odeint(quadcopter_dynamics, states[i - 1, :], time, args=(control_input, quad_params))
    states[i, :] = ode_output[-1, :]

# Plot the results
plt.figure(figsize=(12, 8))

plt.subplot(3, 1, 1)
plt.plot(t_sim, states[:, 0], label='Roll')
plt.legend()
plt.grid(True)
plt.xlabel('Time (s)')
plt.ylabel('Angle (rad)')

plt.subplot(3, 1, 2)
plt.plot(t_sim, states[:, 1], label='Pitch')
plt.legend()
plt.grid(True)
plt.xlabel('Time (s)')
plt.ylabel('Angle (rad)')

plt.subplot(3, 1, 3)
plt.plot(t_sim, states[:, 2], label='Yaw')
plt.legend()
plt.grid(True)
plt.xlabel('Time (s)')
plt.ylabel('Angle (rad)')

plt.show()


# Generate dynamic control inputs
phi_cmd = np.sin(0.1 * t_sim)
theta_cmd = np.cos(0.05 * t_sim)
psi_cmd = np.zeros_like(t_sim)

# Simulation loop
states = np.zeros((len(t_sim), len(initial_state)))
states[0, :] = initial_state

for i in range(1, len(t_sim)):
    time = [t_sim[i - 1], t_sim[i]]
    control_input = [phi_cmd[i], theta_cmd[i], psi_cmd[i]]
    ode_output = odeint(quadcopter_dynamics, states[i - 1, :], time, args=(control_input, quad_params))
    states[i, :] = ode_output[-1, :]

# Plot the results
plt.figure(figsize=(12, 8))

plt.subplot(3, 1, 1)
plt.plot(t_sim, np.degrees(states[:, 0]), label='Roll')  # Convert to degrees for better readability
plt.plot(t_sim, np.degrees(phi_cmd), '--', label='Desired Roll', color='red')
plt.legend()
plt.grid(True)
plt.xlabel('Time (s)')
plt.ylabel('Angle (degrees)')

plt.subplot(3, 1, 2)
plt.plot(t_sim, np.degrees(states[:, 1]), label='Pitch')  # Convert to degrees for better readability
plt.plot(t_sim, np.degrees(theta_cmd), '--', label='Desired Pitch', color='red')
plt.legend()
plt.grid(True)
plt.xlabel('Time (s)')
plt.ylabel('Angle (degrees)')

plt.subplot(3, 1, 3)
plt.plot(t_sim, np.degrees(states[:, 2]), label='Yaw')  # Convert to degrees for better readability
plt.plot(t_sim, np.degrees(psi_cmd), '--', label='Desired Yaw', color='red')
plt.legend()
plt.grid(True)
plt.xlabel('Time (s)')
plt.ylabel('Angle (degrees)')

plt.show()



