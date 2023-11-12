const Home = () => {
  return (
    <div className="min-h-screen bg-gradient-to-r from-cyan-500 to-blue-500 font-modern-sans">
      <div
        style={{
          backgroundColor: "rgb(225 245 254) / var(1)",
          paddingTop: "50px",
          marginBottom: "2.5%",
        }}
      >
        <header
          className="bg-light-blue-50 h-[28rem] flex items-center justify-between rounded-xl"
          style={{ width: "86%", margin: "auto", borderRadius: "20px" }}
        >
          <div
            className="flex items-center bg-gradient-to-r from-cyan-500 to-blue-500"
            style={{
              backgroundColor: "white",
              borderRadius: "20px",
              padding: "36px 60px",
              marginLeft: "75px",
            }}
          >
            <div className="text-orange-500">
              <h1
                className="text-6xl font-extrabold mb-4"
                style={{ color: "#333" }}
              >
                SunScope
              </h1>
              <p className="text-2xl" style={{ color: "#555" }}>
                  Illuminate Your Home with Solar Brilliance
              </p>
            </div>
          </div>
          <img
            src={"/house_image.png"}
            alt="House showcasing solar panels"
            style={{
              height: "120%",
              maxWidth: "100%",
              marginTop: "-10%",
              marginBottom: "-10%",
              marginRight: "0px",
            }}
          />
        </header>
      </div>

      <section className="flex justify-center p-10">
        <div className="bg-white p-8 rounded-2xl shadow-md">
          <h2 className="text-4xl font-bold mb-4 ">
            Our Mission
          </h2>
          <p className="text-xl">
          At SunScope, our mission is to empower homeowners with the tools to harness the sun's energy,<br />driving forward a future where clean and renewable solar power is at the heart of every community.
          </p>
        </div>
      </section>

      <div className="grid md:grid-cols-2 gap-10 p-10">
        <section className="bg-white p-8 rounded-2xl shadow-md hover:shadow-lg transition duration-500">
          <h2 className="text-4xl font-bold mb-4 text-gray-800">
            Google's Solar API Integration
          </h2>
          <p className="text-xl">
          SunScope seamlessly integrates with Google's Solar API to provide precise, location-based solar potential assessments, enabling users to make informed decisions about solar installations with the latest in geospatial technology.
          </p>
        </section>

        <section className="bg-gray-50 p-8 rounded-2xl shadow-md hover:shadow-lg transition duration-500">
          <h2 className="text-4xl font-bold mb-4 text-gray-800">
            Solar Data Retrieval
          </h2>
          <p className="text-xl">
            SunScope's Solar Data Retrieval system offers real-time, accurate solar production data, empowering you with the insights needed to optimize your energy usage and savings.
          </p>
        </section>

        <section className="bg-white p-8 rounded-2xl shadow-md hover:shadow-lg transition duration-500">
          <h2 className="text-4xl font-bold mb-4 text-gray-800">
            Weather API Integration
          </h2>
          <p className="text-xl">
            SunScope enhances your solar strategy by integrating with leading Weather APIs, delivering forecasts to help maximize energy generation tailored to local weather patterns.
          </p>
        </section>

        <section className="bg-gray-50 p-8 rounded-2xl shadow-md hover:shadow-lg transition duration-500">
          <h2 className="text-4xl font-bold mb-4 text-gray-800">
            Custom Solar Panel Options
          </h2>
          <p className="text-xl">
            SunScope offers customizable solar panel options, allowing you to tailor your setup for optimal performance and aesthetics suited to your unique home and lifestyle.
          </p>
        </section>
      </div>

      <section className="p-10 bg-gray-200">
        <h2 className="text-4xl font-bold mb-5 text-gray-800">
          Government Incentives and Subsidies
        </h2>
        <p className="text-xl">
        SunScope navigates the complex landscape of government incentives and subsidies for you, ensuring you benefit from all available financial support for your solar investment.
        </p>
      </section>

      <footer className="bg-gray-800 text-white text-center p-6">
        <p>Created as a project for HackTheChange2023</p>
      </footer>
    </div>
  );
};

export default Home;
