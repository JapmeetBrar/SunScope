const Home = () => {
    return (
      <div className="min-h-screen bg-light-blue-50 font-modern-sans">
        <header className="bg-gradient-to-r from-cyan-500 to-blue-500 h-96 flex items-center justify-center">
          <div className="text-center">
            <h1 className="text-6xl font-extrabold mb-4 text-white">SunScope</h1>
            <p className="text-2xl text-gray-100">Empowering your solar potential</p>
          </div>
        </header>
  
        <div className="grid md:grid-cols-2 gap-10 p-10">
          <section className="bg-white p-8 rounded-2xl shadow-md hover:shadow-lg transition duration-500">
            <h2 className="text-4xl font-bold mb-4 text-gray-800">Google's Solar API Integration</h2>
            <p className="text-gray-600">Lorem ipsum dolor sit amet consectetur adipisicing elit. Dolores, suscipit.</p>
          </section>
  
          <section className="bg-gray-50 p-8 rounded-2xl shadow-md hover:shadow-lg transition duration-500">
            <h2 className="text-4xl font-bold mb-4 text-gray-800">Solar Data Retrieval</h2>
            <p className="text-gray-600">Lorem ipsum dolor sit amet consectetur adipisicing elit. Optio, totam?</p>
          </section>
  
          <section className="bg-white p-8 rounded-2xl shadow-md hover:shadow-lg transition duration-500">
            <h2 className="text-4xl font-bold mb-4 text-gray-800">Weather API Integration</h2>
            <p className="text-gray-600">Lorem ipsum dolor sit amet consectetur adipisicing elit. Alias, recusandae.</p>
          </section>
  
          <section className="bg-gray-50 p-8 rounded-2xl shadow-md hover:shadow-lg transition duration-500">
            <h2 className="text-4xl font-bold mb-4 text-gray-800">Custom Solar Panel Options</h2>
            <p className="text-gray-600">Lorem ipsum dolor sit, amet consectetur adipisicing elit. Magni, nostrum.</p>
          </section>
        </div>
  
        <section className="p-10 bg-gray-200">
        <h2 className="text-4xl font-bold mb-5 text-gray-800">Government Incentives and Subsidies</h2>
        <p className="text-gray-700">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Praesentium, consequuntur.</p>
        </section>


  
        <footer className="bg-gray-800 text-white text-center p-6">
          <p>FOOTER - ADD</p>
        </footer>
      </div>
    );
  };
  
  export default Home;
  