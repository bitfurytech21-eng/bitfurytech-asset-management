import Header from "../components/Header";
import Hero from "../components/Hero";
import About from "../components/About";
import Services from "../components/Services";
import Plans from "../components/Plans";
import Payments from "../components/Payments";
import Testimonials from "../components/Testimonials";
import Contact from "../components/Contact";
import Footer from "../components/Footer";
import CompanyVideo from "../components/CompanyVideo";
import BoardSection from "../components/BoardSection";
import HowItWorks from "../components/HowItWorks";
import FAQ from "../components/FAQ";

function Home() {
  return (
      <>
            <Header />
                  <Hero />
                        <About />

                        <CompanyVideo />  
                        <BoardSection />
                         <HowItWorks />
                              <Services />
                                    <Plans />
                                          <Payments />
                                                <Testimonials />
                                                      <Contact />
                                                       <FAQ />
                                                            <Footer />
                                                                </>
                                                                  );
                                                                  }

                                                                  export default Home; 
