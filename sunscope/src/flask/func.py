import flask

def annualUtilityBillEstimate(yearlyKWhEnergyConsumption, initialAcKwhPerYear, efficiencyDepreciationFactor, year, costIncreaseFactor, discountRate):
    def annualProduction(initialAcKwh, efficiencyFactor, year):
        return initialAcKwh * pow(efficiencyFactor, year)

    cost_per_kwh = 0.258  # average cost per kWh in Alberta

    def billCostModel(consumption):
      return consumption * cost_per_kwh


    return (
        billCostModel(
            yearlyKWhEnergyConsumption -
            annualProduction(initialAcKwhPerYear, efficiencyDepreciationFactor, year)
        ) * pow(costIncreaseFactor, year) / pow(discountRate, year)
    )

def lifetimeUtilityBill(yearlyKWhEnergyConsumption, initialAcKwhPerYear, efficiencyDepreciationFactor, installationLifeSpan, costIncreaseFactor, discountRate):
    bill = [0] * installationLifeSpan
    for year in range(installationLifeSpan):
        bill[year] = annualUtilityBillEstimate(
            yearlyKWhEnergyConsumption,
            initialAcKwhPerYear,
            efficiencyDepreciationFactor,
            year,
            costIncreaseFactor,
            discountRate
        )
    return bill

# Example usage:
# Define constants like cost_per_kwh, efficiencyDepreciationFactor, etc. as per your data.
# Then call the functions with appropriate arguments.
