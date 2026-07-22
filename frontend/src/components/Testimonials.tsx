import React from "react";
import "./Testimonials.css";

const testimonials = [
  {
    name: "Michael A.",
    country: "United Kingdom",
    plan: "Stock Plan",
    message:
      "The platform is easy to use, and the investment dashboard makes it simple to monitor my portfolio.",
  },
  {
    name: "Sophia L.",
    country: "Canada",
    plan: "Real Estate Plan",
    message:
      "I appreciate the clear investment information and the professional presentation of every plan.",
  },
  {
    name: "Daniel K.",
    country: "Australia",
    plan: "Crypto Plan",
    message:
      "The investment options are well organized, and customer support has been responsive whenever I had questions.",
  },
];

const Testimonials = () => {
  return (
    <section className="testimonials">
      <div className="section-title">
        <h2>What Investors Say</h2>
        <p>
          Hear what users appreciate about the BitfuryTech investment platform.
        </p>
      </div>

      <div className="testimonial-grid">
        {testimonials.map((item, index) => (
          <div className="testimonial-card" key={index}>
            <p>"{item.message}"</p>

            <h3>{item.name}</h3>

            <span>
              {item.country} • {item.plan}
            </span>
          </div>
        ))}
      </div>
    </section>
  );
};

export default Testimonials;
