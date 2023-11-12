import json
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import PIL
from io import BytesIO
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
    def panel_energy_graph(self, file_path):
        panels = []
        energy_production = []
        data = import_json(file_path)
        for key, energy_kwh in data.items():
            panels_count = int(key.replace('yearlyEnergyDcKwh', ''))  # Extracting the number of panels
            panels.append(panels_count)
            energy_production.append(energy_kwh)

        buffer = BytesIO()
        plt.xlabel('Number of Panels')
        plt.ylabel('Energy Production (kWh)')
        plt.plot(panels, energy_production)
        plt.savefig(buffer, format='png')
        img = PIL.Image.open(buffer)
        saved = img.save('sunscope/_backend/data/PanelEnergyProduction.png')
        return img


def import_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data




if __name__ == '__main__':
    # Path to the uploaded JSON file
    file_path = 'sunscope/_backend/data/get_solar_data_example_CAN_couple.json'

    # Importing data from the JSON file
    data = import_json(file_path)

    # Creating an instance of FinancialEngineering with the imported data
    fe = FinancialEngineering(data)

    # Example rate per kWh and cost per panel for calculations
    rate_per_kwh = 0.10  # This can be adjusted as needed
    cost_per_panel = 1000  # Example: $1000 per panel

    # Iterating through each configuration and performing calculations
    fe.panel_energy_graph(file_path)


