import json

class FinancialEngineering:
    def __init__(self, energy_data):
        self.energy_data = energy_data

    def get_yearly_energy(self, panels_count):
        key = f"yearlyEnergyDcKwh{panels_count}"
        return self.energy_data.get(key, 0)

    def calculate_revenue(self, panels_count, rate_per_kwh):
        yearly_energy = self.get_yearly_energy(panels_count)
        return yearly_energy * rate_per_kwh

    def calculate_payback_period(self, panels_count, rate_per_kwh, installation_cost):
        yearly_revenue = self.calculate_revenue(panels_count, rate_per_kwh)
        if yearly_revenue == 0:
            return float('inf')  # Infinite payback period if no revenue
        return installation_cost / yearly_revenue

def import_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

# Path to the uploaded JSON file
file_path = 'sunscope\_backend\data\get_solar_data_example_CAN_couple.json'

# Importing data from the JSON file
data = import_json(file_path)

# Creating an instance of FinancialEngineering with the imported data
fe = FinancialEngineering(data)

# Example rate per kWh and cost per panel for calculations
rate_per_kwh = 0.10  # This can be adjusted as needed
cost_per_panel = 1000  # Example: $1000 per panel

# Iterating through each configuration and performing calculations
for key, energy_kwh in data.items():
    panels_count = int(key.replace('yearlyEnergyDcKwh', ''))  # Extracting the number of panels
    revenue = fe.calculate_revenue(panels_count, rate_per_kwh)
    installation_cost = panels_count * cost_per_panel
    payback_period = fe.calculate_payback_period(panels_count, rate_per_kwh, installation_cost)
    
    print(f"Configuration: {panels_count} Panels")
    print(f"Yearly Energy Production: {energy_kwh} kWh")
    print(f"Yearly Revenue: ${revenue:.2f}")
    print(f"Payback Period: {payback_period:.2f} years")
    print("-----------------------------------------")
