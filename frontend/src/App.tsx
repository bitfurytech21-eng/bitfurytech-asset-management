function App() {
  return (
    <div>

      {/* Hero Section */}
      <section style={{ padding: "60px", textAlign: "center" }}>
        <h1>Bitfury Tech Investment</h1>
        <p>Building Wealth, Securing Futures</p>

        <button>Start Investing</button>
      </section>

      {/* About Us */}
      <section style={{ padding: "40px" }}>
        <h2>About Us</h2>

        <p>
          Bitfury Tech Investment is a global investment platform focused on
          Real Estate, Agriculture, Stocks and Digital Assets.
        </p>
      </section>

      {/* Company Video */}
      <section style={{ padding: "40px" }}>
        <h2>Company Introduction</h2>

        <p>
          Company introduction video will appear here.
        </p>
      </section>

      {/* Why Choose Us */}
      <section style={{ padding: "40px" }}>
        <h2>Why Choose Us</h2>

        <ul>
          <li>Secure Investments</li>
          <li>Professional Management</li>
          <li>Global Portfolio</li>
          <li>24/7 Customer Support</li>
        </ul>
      </section>

      {/* Board of Directors */}
      <section style={{ padding: "40px" }}>
        <h2>Board of Directors</h2>

        <p>
          React will load the board members from the Flask backend here.
        </p>
      </section>

    </div>
  );
}

export default App;