import React, { useState } from "react";
import "./FAQ.css";

const faqs = [
  {
    question: "What is BitfuryTech?",
    answer:
      "BitfuryTech is an investment platform that provides access to investment opportunities across stocks, cryptocurrency, real estate, and agriculture through a user-friendly digital experience."
  },
  {
    question: "What is the minimum investment?",
    answer:
      "The minimum investment on BitfuryTech is $200."
  },
  {
    question: "What is the maximum investment?",
    answer:
      "The maximum investment available on the platform is $5,000,000, depending on the investment plan selected."
  },
  {
    question: "Which investment plans are available?",
    answer:
      "BitfuryTech offers Stock, Cryptocurrency, Real Estate, and Agricultural investment plans. Each investment category includes Beginner, Prime, Master, and Executive tiers."
  },
  {
    question: "How do I start investing?",
    answer:
      "Create an account, complete any required verification, fund your wallet, choose an investment category and plan, then monitor your portfolio through your dashboard."
  },
  {
    question: "How can I contact customer support?",
    answer:
      "Customer support can be reached through the live chat, contact form, or official support email available on the website."
  }
];

export default function FAQ() {
  const [active, setActive] = useState<number | null>(null);

  return (
    <section className="faq">

      <h2>Frequently Asked Questions</h2>

      <p className="faq-subtitle">
        Find answers to some of the most common questions about BitfuryTech.
      </p>

      {faqs.map((item, index) => (
        <div className="faq-item" key={index}>

          <button
            className="faq-question"
            onClick={() =>
              setActive(active === index ? null : index)
            }
          >
            {item.question}
          </button>

          {active === index && (
            <div className="faq-answer">
              {item.answer}
            </div>
          )}

        </div>
      ))}

    </section>
  );
}
