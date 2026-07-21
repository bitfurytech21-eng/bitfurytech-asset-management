import "./Sidebar.css";
function Sidebar() {
  return (
    <aside className="sidebar">

      <div className="logo">
        <h2>Bitfury Tech</h2>
      </div>

      <nav>

        <a href="/dashboard">🏠 Dashboard</a>

        <a href="#">💼 Portfolio</a>

        <a href="#">📈 Investments</a>

        <a href="#">💳 Deposit</a>

        <a href="#">💸 Withdraw</a>

        <a href="#">📄 Transactions</a>

        <a href="#">👥 Referrals</a>

        <a href="#">⚙ Settings</a>

        <a href="#">❓ Support</a>

        <a href="#">🚪 Logout</a>

      </nav>

    </aside>
  );
}

export default Sidebar;