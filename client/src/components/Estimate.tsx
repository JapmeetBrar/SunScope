import { useState } from 'react';
import axios from 'axios';

const EstimatePage = () => {
  const [address, setAddress] = useState('');
  const [isAnalyzing, setIsAnalyzing] = useState(false);
  const [results, setResults] = useState({
    sunlightHours: '___',
    availableArea: '___',
    revenue: '___',
    paybackPeriod: '___'
  });

  const handleAnalysis = async () => {
    setIsAnalyzing(true);
    try {
      // NEED TO CHANGE THE URL
      const response = await axios.get(`http://127.0.0.1:5000/get_solar_financial_data`, { params: { address } });
      console.log('API Response:', response.data);
      const { maxSunshineHoursPerYear, maxArrayAreaMeters2} = response.data.processed_data;
      const financial_analysis = response.data.financial_analysis

      setResults({
        sunlightHours: maxSunshineHoursPerYear,
        availableArea: maxArrayAreaMeters2,
        revenue: financial_analysis.revenue,
        paybackPeriod: financial_analysis.payback_period
      });
    } catch (error) {
      console.error('Error during analysis:', error);
    }
    setIsAnalyzing(false);
  };

  return (
    <div className="min-h-screen bg-white font-sans text-gray-800">
      <div className="container mx-auto py-12 px-6 md:px-0">
        <h1 className="text-5xl font-bold mb-12 text-center">Solar Potential Estimate</h1>

        <div className="bg-gray-100 p-8 rounded-xl shadow-md">
          <div className="mb-8">
            <label htmlFor="address" className="block text-xl font-semibold mb-3">
              Your Address
            </label>
            <input
              type="text"
              className="form-input w-full p-4 rounded-xl bg-gray-50 border border-gray-300 focus:border-blue-300 focus:ring-1 focus:ring-blue-300 transition duration-200 ease-in-out"
              id="address"
              placeholder="Enter your address"
              value={address}
              onChange={(e) => setAddress(e.target.value)}
            />
          </div>

          <div className="text-center">
            <button
              className="bg-blue-600 hover:bg-blue-700 text-white font-bold py-3 px-8 rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2 transition duration-200 ease-in-out"
              type="button"
              onClick={handleAnalysis}
              disabled={isAnalyzing}
            >
              {isAnalyzing ? 'Analyzing...' : 'Analyze'}
            </button>
          </div>
        </div>

        <div className="mt-12 bg-gray-100 p-8 rounded-xl shadow-md">
          <h2 className="text-2xl font-semibold">Results:</h2>
          <p className="text-xl mt-4">{results.sunlightHours} hours of usable sunlight per year</p>
          <p className="text-xl">{results.availableArea} sqft available for solar panels</p>
          <p className="text-xl">Estimated Revenue: ${results.revenue}</p>
          <p className="text-xl">Payback Period: {results.paybackPeriod} years</p>
        </div>
      </div>
    </div>
  );
};

export default EstimatePage;
