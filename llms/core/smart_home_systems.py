from .noa_rose_ring import AI_Nose_Ring
class SmartHomeSystem:
    def __init__(self):
        self.devices = {}
    
    def add_device(self, name, device):
        self.devices[name] = device
        print(f"{name} added to the smart home system.")
    
    def remove_device(self, name):
        if name in self.devices:
            del self.devices[name]
            print(f"{name} removed from the smart home system.")
        else:
            print(f"Error: {name} not found in the smart home system.")
    
    def analyze_environment_all_devices(self):
        print("Analyzing environment for all devices in the smart home system:")
        for name, device in self.devices.items():
            print(f"Analyzing environment for {name}...")
            device.analyze_environment()
            print()
    
    def get_recommendations_all_devices(self):
        print("Getting recommendations for all devices in the smart home system:")
        for name, device in self.devices.items():
            print(f"Getting recommendations for {name}...")
            device.get_recommendations()
            print()

# Instantiate the SmartHomeSystem
smart_home = SmartHomeSystem()

# Add AI Nose Ring device to the smart home system
nose_ring = AI_Nose_Ring()
smart_home.add_device("AI Nose Ring", nose_ring)

# Analyze environment for all devices
smart_home.analyze_environment_all_devices()

# Get recommendations for all devices
smart_home.get_recommendations_all_devices()

# Adjust sensitivity of the AI Nose Ring
nose_ring.adjust_sensitivity(8)

# Remove AI Nose Ring device from the smart home system
smart_home.remove_device("AI Nose Ring")

