const Home = () => {
    return (
        <div className="min-h-screen bg-light-blue-50 font-modern-sans">

<div style={{ backgroundColor: 'rgb(225 245 254 / var(1)', paddingTop: '50px', marginBottom: '2.5%' }}> 
        <header className="bg-gradient-to-r from-cyan-500 to-blue-500 h-[26rem] flex items-center justify-between rounded-xl" style={{ width: '80%', margin: 'auto', borderRadius: '20px' }}>

          <div className="flex items-center" style={{ backgroundColor: 'white', borderRadius: '20px', padding: '10px 20px', marginLeft: '100px' }}>
            <div>
              <h1 className="text-6xl font-extrabold mb-4" style={{ color: '#333' }}>SunScope</h1>
              <p className="text-2xl" style={{ color: '#555' }}>Empowering your solar potential</p>
            </div>
          </div>
          <img src={"/house_image.png"} alt="House showcasing solar panels" style={{ height: '120%', maxWidth: '100%', marginTop: '-10%', marginBottom: '-10%' }} />
        </header>
      </div>








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
  