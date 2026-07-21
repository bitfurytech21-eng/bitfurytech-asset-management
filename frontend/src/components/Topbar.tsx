import "./Topbar.css";import defaultAvatar from "../assets/images/default-avatar.png";

function Topbar() {
  return (
    <header className="topbar">

      <div className="brand">
        <h2>Bitfury Tech Investment</h2>
      </div>

      <div className="search">
        <input
          type="text"
          placeholder="Search..."
        />
      </div>

      <div className="topbar-right">

        <button className="icon-btn">🔔</button>

        <button className="icon-btn">💬</button>

        <img
  src={defaultAvatar}
  alt="profile-photo"
  className="profile-photo"
/>

        <button className="logout-btn">
          Logout
        </button>

      </div>

    </header>
  );
}

export default Topbar;