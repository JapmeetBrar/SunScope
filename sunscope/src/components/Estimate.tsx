import { useState } from 'react';
import axios from 'axios';

const EstimatePage = () => {
  const [address, setAddress] = useState('');
  const [monthlyBill, setMonthlyBill] = useState('');
  const [sunlightHours, setSunlightHours] = useState('___');
  const [availableArea, setAvailableArea] = useState('___');
  const [isAnalyzing, setIsAnalyzing] = useState(false);

  const handleAnalysis = async () => {
    setIsAnalyzing(true);
    try {
      // Replace with Flask API endpoint
      const response = await axios.post('http://localhost:5000/api/analyze', {
        address,
        monthlyBill
      });
      setSunlightHours(response.data.sunlightHours);
      setAvailableArea(response.data.availableArea);
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

          <div className="mb-8">
            <label htmlFor="monthly-bill" className="block text-xl font-semibold mb-3">
              Your Average Monthly Electric Bill
            </label>
            <input
              type="text"
              className="form-input w-full p-4 rounded-xl bg-gray-50 border border-gray-300 focus:border-blue-300 focus:ring-1 focus:ring-blue-300 transition duration-200 ease-in-out"
              id="monthly-bill"
              placeholder="Enter your average monthly electric bill"
              value={monthlyBill}
              onChange={(e) => setMonthlyBill(e.target.value)}
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
          <p className="text-xl mt-4">{sunlightHours} hours of usable sunlight per year</p>
          <p className="text-xl">{availableArea} sqft available for solar panels</p>
        </div>
      </div>
    </div>
  );
};

export default EstimatePage;