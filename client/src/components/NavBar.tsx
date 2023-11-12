import { Link } from "react-router-dom";

function NavBar() {
  return (
    <div className="h-20 flex items-center px-10 py-6 shadow-lg rounded-b-lg">
      <div className="flex justify-center content-center h-1/1">
        <a
          href="/home"
          className="title pt-6 text-4xl font-bold text-orange-500 cursor-pointer"
        >
          SunScope
        </a>
        <img
              src={"../src/assets/logo.png"}
              alt="logo"
              style={{
                width: '80px',
                height: "80px",
              }}
            />
      </div>
      <div className="flex-grow">
        <ul className="flex justify-end gap-6 font-bold text-xl">
          <li>
            <Link to="/home" className="hover:text-orange-500">
              Home
            </Link>
          </li>
          <li>
            <Link to="/estimate" className="hover:text-orange-500">
              Estimate
            </Link>
          </li>
          <li>
            <Link to="/contact" className="hover:text-orange-500">
              Contact Us
            </Link>
          </li>
        </ul>
      </div>
    </div>
  );
}

export default NavBar;