import json
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from mpl_toolkits.axes_grid1 import host_subplot
from mpl_toolkits.axisartist.parasite_axes import HostAxes
import mpl_toolkits.axisartist as AA
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
    def panel_energy_graph(self, file_path, cost_per_panel, rate_per_kwh, yearly_bill):
        panels = []
        energy_production = []
        totalcost = []
        profits = []
        data = import_json(file_path)
        for key, energy_kwh in data.items():
            panels_count = int(key.replace('yearlyEnergyDcKwh', ''))  # Extracting the number of panels
            panels.append(panels_count)
            energy_production.append(energy_kwh)
            totalcost.append(cost_per_panel*panels_count)
            reveune = self.calculate_revenue(panels_count, rate_per_kwh)
            profits.append(reveune-yearly_bill)
        buffer = BytesIO()


        fig = plt.figure()

        host = fig.add_axes([0.15, 0.1, 0.65, 0.8], axes_class=HostAxes)
        par1 = host.get_aux_axes(viewlim_mode=None, sharex=host)
        par2 = host.get_aux_axes(viewlim_mode=None, sharex=host)

        host.axis["right"].set_visible(False)

        par1.axis["right"].set_visible(True)
        par1.axis["right"].major_ticklabels.set_visible(True)
        par1.axis["right"].label.set_visible(True)



        par2.axis["right2"] = par2.new_fixed_axis(loc="right", offset=(60, 0))

        par2.axis["right"].toggle(all=True)
        host.set_xlim(0, max(panels))
        host.set_ylim(0, max(energy_production))

        host.set_xlabel("Number of Panels")
        host.set_ylabel("Yearly Energy Production (Kwh)")
        par1.set_ylabel("Total Installation Cost ($)")
        par2.set_ylabel("Yearly Net Profits/Savings ($)")
        
        p1, = host.plot(panels, energy_production, label="Yearly Energy Production")
        p2, = par1.plot(panels, totalcost, label="Total Installation Cost")
        p3, = par2.plot(panels, profits, label="Net Profits/Savings")
        par1.set_ylim(0, max(totalcost))
        par2.set_ylim(min(profits), max(profits))
        host.legend()
        
        host.axis["left"].label.set_color(p1.get_color())
        par1.axis["right"].label.set_color(p2.get_color())
        par2.axis["right"].label.set_color(p3.get_color())
        plt.plot()
        plt.savefig(buffer, dpi = 500, format='png', bbox_inches = "tight", pad_inches = 0.4)
        img = PIL.Image.open(buffer)
        saved = img.save('sunscope/BE/data/PanelEnergyProduction.png')
        return img
    

def import_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data




if __name__ == '__main__':
    # Path to the uploaded JSON file
    file_path = 'sunscope/BE/data/get_solar_data_example_CAN_couple.json'

    # Importing data from the JSON file
    data = import_json(file_path)

    # Creating an instance of FinancialEngineering with the imported data
    fe = FinancialEngineering(data)

    # Example rate per kWh and cost per panel for calculations
    rate_per_kwh = 0.10  # This can be adjusted as needed
    cost_per_panel = 500  # Example: $1000 per panel

    # Iterating through each configuration and performing calculations
    fe.panel_energy_graph(file_path, cost_per_panel, rate_per_kwh, 2400)


