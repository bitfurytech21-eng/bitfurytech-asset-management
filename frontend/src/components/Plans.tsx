import { useState } from "react";
import PlanExplorer from "./PlanExplorer";
import PlanTierCard from "./PlanTierCard";
import PlanDetails from "./PlanDetails";

const investmentPlans = [
  {
    title: "Stock Plan",
    image: "/images/plans/stock.png",
    description:
      "Access global stock market opportunities through BitfuryTech managed strategies.",
  },
  {
    title: "Crypto Plan",
    image: "/images/plans/crypto.png",
    description:
      "Explore digital asset opportunities with professional market analysis.",
  },
  {
    title: "Real Estate Plan",
    image: "/images/plans/real-estate.png",
    description:
      "Participate in property investment opportunities managed by BitfuryTech.",
  },
  {
    title: "Agriculture Plan",
    image: "/images/plans/agriculture.png",
    description:
      "Invest in modern agricultural opportunities with sustainable returns.",
  },
];

export default function Plans() {
  const [selectedPlan, setSelectedPlan] = useState<any>(null);

  return (
    <section className="plans-section">
      <h2>Investment Plans</h2>

      <div className="plans-grid">
        {investmentPlans.map((plan) => (
          <div key={plan.title} className="plan-card">
            <img src={plan.image} alt={plan.title} />

            <h3>{plan.title}</h3>

            <p>{plan.description}</p>

            <button onClick={() => setSelectedPlan(plan)}>
              Explore Plan
            </button>
          </div>
        ))}
      </div>

      {selectedPlan && (
        <PlanExplorer
          plan={selectedPlan}
          close={() => setSelectedPlan(null)}
        />
      )}

      <PlanTierCard />
      <PlanDetails />
    </section>
  );
}
