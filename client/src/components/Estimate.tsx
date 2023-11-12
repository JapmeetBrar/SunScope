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
      const response = await axios.get('https://sunscope-latest-gtpsnz34ja-uc.a.run.app/get_solar_financial_data', { params: { address } });
      console.log('API Response:', response.data);
      const { maxSunshineHoursPerYear, maxArrayAreaMeters2} = response.data.processed_data;
      const financial_analysis = response.data.financial_analysis

      setResults({
        sunlightHours: parseInt(maxSunshineHoursPerYear).toFixed(),
        availableArea: parseInt(maxArrayAreaMeters2).toFixed(),
        revenue: parseFloat(financial_analysis.revenue).toFixed(2),
        paybackPeriod: parseFloat(financial_analysis.payback_period).toFixed(2)
      });
    } catch (error) {
      console.error('Error during analysis:', error);
    }
    setIsAnalyzing(false);
  };

  return (
    <div className="min-h-screen bg-gradient-to-r from-cyan-500 to-blue-500 font-sans text-gray-800">
      <div className="container mx-auto py-12 px-6 md:px-0">
  
        <div className="bg-gray-100 p-8 rounded-xl shadow-md">
        <h1 className="text-5xl font-bold mb-2 text-center">Estimate Your Solar Potential 🌞🔍</h1>

        <p className='text-lg'>Gain a clear understanding of what solar power could mean for your home with SunScope's precise estimate page. Simply enter your address and let our advanced algorithms provide you with an accurate solar potential estimate, including expected energy output and financial benefits.</p>
          <div className="">
            <label htmlFor="address" className="block text-2xl font-semibold mb-3">
              Your Address
            </label>
            <div className='flex flex-col justify-center items-center'>
              <input
                type="text"
                className="form-input w-1/2 p-4 rounded-xl bg-gray-50 border border-gray-300 focus:border-blue-300 focus:ring-1 focus:ring-blue-300 transition duration-200 ease-in-out"
                id="address"
                placeholder="Enter your address"
                value={address}
                onChange={(e) => setAddress(e.target.value)}
              />
              <img src="./src/assets/roof.png" alt="" className='rotate-90 text-center -my-20'/>
            </div>
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

        <div className='flex justify-center content-center '>
          <div className="mt-12 bg-gray-100 p-8 rounded-xl text-left">
            <h2 className="text-2xl font-semibold ">Annual Solar Output</h2>
            <p className="text-xl mt-4">Usable Sunlight per Year: <b>{results.sunlightHours} Hours</b></p>
            <p className="text-xl">Space Available for Panels: <b>{results.availableArea} m<sup>2</sup></b></p>
            <p className="text-xl">Estimated Revenue: <b>${results.revenue}</b></p>
            <p className="text-xl">Payback Period: <b>{results.paybackPeriod} Years</b></p>
          </div>
          <img src="./src/assets/graph.png" alt="" className='w-1/2 mt-10' />
        </div>
        </div>
      </div>
    </div>
  );
};

export default EstimatePage;
