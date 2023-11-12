import{ useState } from "react";
import { Link } from "react-router-dom";

enum navItemType {
  Home = "Home",
  Estimate = "Estimate",
}

function NavBar() {
  const [selected, setSelected] = useState(navItemType.Home);
  const navItemsArray = [
    navItemType.Home,
    navItemType.Estimate,
  ];

  return (
    <div className="h-20 flex gap-20 items-center px-10 py-6 shadow-lg rounded-b-lg">
      <div className="title text-4xl font-bold text-orange-500">SunScope</div>
      <div className="grow">
        <ul className="flex gap-3 font-bold justify-around text-xl">
          {navItemsArray.map((item) => {
            return (
              <Link
                to={"/" + item.toLowerCase()}
                className={
                  item === selected
                    ? "underline decoration-slate-800 underline-offset-8 text-orange-500"
                    : "hover:text-orange-500"
                }
                onClick={() => setSelected(item)}
              >
                {item}
              </Link>
            );
          })}
        </ul>
      </div>
    </div>
  );
}

export default NavBar;
