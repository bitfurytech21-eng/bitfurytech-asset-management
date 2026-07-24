const advantages = [
  {
    number: "01",
    title: "Research-led decisions",
    description:
      "Market data and disciplined analysis guide every portfolio allocation.",
  },
  {
    number: "02",
    title: "Risk-conscious strategy",
    description:
      "Diversification and active oversight keep capital protection central to the process.",
  },
  {
    number: "03",
    title: "Clear portfolio access",
    description:
      "A streamlined dashboard keeps investment activity and performance easy to follow.",
  },
];

function WhyChooseUs() {
  return (
    <section className="why-choose-us" aria-labelledby="why-choose-us-title">
      <div className="container why-choose-us-grid">
        <div className="why-choose-us-intro">
          <p className="eyebrow">Why choose us</p>
          <h2 id="why-choose-us-title">
            A measured approach for changing markets.
          </h2>
          <p>
            Bitfury Tech Investment combines market intelligence, portfolio
            discipline, and accessible tools to help investors make informed
            decisions with confidence.
          </p>

          <div className="why-choose-us-signal" aria-hidden="true">
            <span />
            <span />
            <span />
            <span />
            <span />
          </div>
        </div>

        <div className="advantage-list">
          {advantages.map((advantage) => (
            <article className="advantage-item" key={advantage.number}>
              <span className="advantage-number">{advantage.number}</span>
              <div>
                <h3>{advantage.title}</h3>
                <p>{advantage.description}</p>
              </div>
            </article>
          ))}
        </div>
      </div>
    </section>
  );
}

export default WhyChooseUs;
