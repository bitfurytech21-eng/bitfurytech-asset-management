import "./App.css";

import Hero from "./components/Hero";
import About from "./components/About";
import CompanyVideo from "./components/CompanyVideo";
import WhyChooseUs from "./components/WhyChooseUs";
import MarketOverview from "./components/MarketOverview";
import Plans from "./components/Plans";
import Payments from "./components/Payments";
import BoardSection from "./components/board/BoardSection";
import Footer from "./components/Footer";

function App() {
  return (
    <div className="App">
      {/* Hero */}
      <Hero />

      {/* About Us */}
      <About />

      {/* Company Introduction Video */}
      <CompanyVideo />

      {/* Why Choose Us */}
      <WhyChooseUs />

      {/* Market Overview */}
      <MarketOverview />

      {/* Investment Plans */}
      <Plans />

      {/* Payment Methods */}
      <Payments />

      {/* Board of Directors */}
      <BoardSection />

      {/* Footer */}
      <Footer />
    </div>
  );
}

export default App;
