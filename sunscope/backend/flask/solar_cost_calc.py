import json

def read_json(file_path):
    """ Reads a JSON file and returns the data. """
    with open(file_path, 'r') as file:
        return json.load(file)

def estimate_installation_area(bounding_box):
    """
    Estimates the installation area based on the bounding box.
    This is a simplified example and should be replaced with a more accurate calculation.
    """
    # Assuming each degree of latitude and longitude corresponds to a certain distance
    # This is a very rough estimate and should be replaced with a more accurate calculation
    lat_distance = 111  # km per degree of latitude
    lon_distance = 111  # km per degree of longitude
    lat_diff = abs(bounding_box['ne']['latitude'] - bounding_box['sw']['latitude'])
    lon_diff = abs(bounding_box['ne']['longitude'] - bounding_box['sw']['longitude'])
    area = lat_distance * lat_diff * lon_distance * lon_diff  # in square kilometers
    return area * 1e6  # Convert to square meters

def calculate_solar_potential(data):
    """ Calculates the solar potential based on the given data. """
    bounding_box = data['boundingBox']
    installation_area = estimate_installation_area(bounding_box)

    # Assuming average panel efficiency and solar irradiance
    avg_panel_efficiency = 0.2366  # Average from (https://www.greenmatch.co.uk/blog/2014/11/how-efficient-are-solar-panels)
    local_solar_irradiance = 1400  # kWh/kW/year - placeholder value
    estimated_capacity = installation_area * avg_panel_efficiency  # in kW

    annual_energy_production = estimated_capacity * local_solar_irradiance  # in kWh

    # Placeholder values for cost calculation
    electricity_rate = 0.12  # $/kWh - placeholder value
    installation_cost_per_kw = 1500  # $/kW - placeholder value
    initial_investment = estimated_capacity * installation_cost_per_kw  # Total installation cost

    annual_savings = annual_energy_production * electricity_rate  # Annual savings
    roi = annual_savings / initial_investment  # Return on Investment

    return {
        'Estimated Capacity (kW)': estimated_capacity,
        'Annual Energy Production (kWh)': annual_energy_production,
        'Annual Savings ($)': annual_savings,
        'ROI': roi,
        'Initial Investment ($)': initial_investment
    }

if __name__ == "__main__":
    file_path = 'sunscope\src\data\get_solar_data_example1.json'
    data = read_json(file_path)
    solar_potential = calculate_solar_potential(data)
    for key, value in solar_potential.items():
        print(f"{key}: {value:.2f}")
