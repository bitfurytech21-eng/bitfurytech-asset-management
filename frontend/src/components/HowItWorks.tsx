import React from "react";
import "./HowItWorks.css";

const steps = [
  {
    number: "01",
    title: "Create Your Account",
    description:
      "Sign up for a BitfuryTech account and complete the registration process to begin your investment journey.",
    icon: "👤",
  },
  {
    number: "02",
    title: "Verify Your Identity",
    description:
      "Complete identity verification to help keep your account secure and enable full access to platform features.",
    icon: "🛡️",
  },
  {
    number: "03",
    title: "Fund Your Wallet",
    description:
      "Deposit funds into your BitfuryTech wallet using one of the supported payment methods.",
    icon: "💳",
  },
  {
    number: "04",
    title: "Choose an Investment Plan",
    description:
      "Select from Stock, Crypto, Real Estate, or Agricultural investments, then choose Beginner, Prime, Master, or Executive.",
    icon: "📊",
  },
  {
    number: "05",
    title: "Track Your Portfolio",
    description:
      "Monitor your investments, portfolio performance, and transaction history from your personal dashboard.",
    icon: "📈",
  },
  {
    number: "06",
    title: "Manage Your Investments",
    description:
      "Review your investment activity, reinvest when appropriate, or submit withdrawal requests according to your selected plan.",
    icon: "💰",
  },
];

const HowItWorks = () => {
  return (
    <section className="how-it-works">
      <div className="section-header">
        <h2>How BitfuryTech Works</h2>
        <p>
          Follow these simple steps to begin your investment journey with
          BitfuryTech.
        </p>
      </div>

      <div className="steps-grid">
        {steps.map((step) => (
          <div className="step-card" key={step.number}>
            <div className="step-icon">{step.icon}</div>

            <span className="step-number">{step.number}</span>

            <h3>{step.title}</h3>

            <p>{step.description}</p>
          </div>
        ))}
      </div>

      <div className="how-buttons">
        <button className="primary-btn">Create Account</button>

        <button className="secondary-btn">
          Explore Investment Plans
        </button>
      </div>
    </section>
  );
};

export default HowItWorks;
