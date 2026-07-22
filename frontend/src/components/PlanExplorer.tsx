import PlanTierCard from "./PlanTierCard";

interface Props {
  plan:any;
  close:()=>void;
}


export default function PlanExplorer({plan, close}:Props){

return (

<div className="plan-explorer">

<button onClick={close}>
Close
</button>


<img 
src={plan.image}
alt={plan.title}
/>


<h2>
BitfuryTech {plan.title}
</h2>


<p>

BitfuryTech identifies market opportunities,
analyses performance, manages strategies,
and provides investors access to structured
investment opportunities.

</p>


<h3>
Choose Your Investment Level
</h3>


<PlanTierCard sector={plan.title}/>


</div>

);

}