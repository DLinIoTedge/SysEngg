

import matplotlib.pyplot as plt

# CubeSat components
components = {
    "Payload": "Capture Data",
    "Power System": "Generate Power",
    "Communication System": "Transmit Data",
    "Orbit Control System": "Adjust Orbit",
}

# Create a diagram
fig, ax = plt.subplots(figsize=(6, 4))

# Draw CubeSat structure
ax.add_patch(plt.Rectangle((0, 0), 1, 1, fill=None, edgecolor='black', linewidth=2, label='CubeSat'))

# Draw components
for i, (component, action) in enumerate(components.items()):
    x_position = 0.5
    y_position = 0.8 - i * 0.2
    ax.text(x_position, y_position, component, ha='center', va='center', fontsize=10, fontweight='bold')
    ax.text(x_position, y_position - 0.05, action, ha='center', va='center', fontsize=8)

# Customize plot
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')
ax.legend(loc='upper right', bbox_to_anchor=(1, 1))

# Show the diagram
plt.title("CubeSat Mission Architecture")
plt.show()

