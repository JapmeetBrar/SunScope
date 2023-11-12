import { Link } from "react-router-dom";

function NavBar() {
  return (
    <div className="h-20 flex items-center px-10 py-6 shadow-lg rounded-b-lg">
      <a
        href="/home"
        className="title text-4xl font-bold text-orange-500 cursor-pointer"
      >
        SunScope
      </a>
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
        </ul>
      </div>
    </div>
  );
}

export default NavBar;
