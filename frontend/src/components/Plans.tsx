import PlanExplorer from "./PlanExplorer";
import PlanTierCard from "./PlanTierCard";
import PlanDetails from "./PlanDetails";
export React, { useState } from "react";

const investmentPlans = [
  {
    title: "Stock Plan",
    image: "/Images/Plans/stock.png",
    description:
      "Access global stock market opportunities through BitfuryTech managed strategies.",
  },
  {
    title: "Crypto Plan",
    image: "/Images/Plans/crypto.png",
    description:
      "Explore digital asset opportunities with professional market analysis.",
  },
  {
    title: "Real Estate Plan",
    image: "/Images/Plans/real-estate.png",
    description:
      "Participate in property investment opportunities managed by BitfuryTech.",
  },
  {
    title: "Agriculture plan",
    image: "/Images/plans/agricuture",

export default function Plans() {
  const [selectedPlan, setSelectedPlan] = useState<any>(null);

  return (
    <section className="plans-section">

      <h2>Investment Plans</h2>

      <div className="plans-grid">

        {investmentPlans.map((plan) => (
          <div className="plan-card" key={plan.title}>

            <img src={plan.image} alt={plan.title}/>

            <h3>{plan.title}</h3>

            <p>{plan.description}</p>

            <button
              onClick={() => setSelectedPlan(plan)}
            >
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

    </section>
  );
}
                                                                        