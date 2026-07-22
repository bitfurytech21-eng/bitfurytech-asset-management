import {useState} from "react";
import PlanDetails from "./PlanDetails";


const tiers=[

{
name:"Beginner Plan",
range:"$200 - $4,999",
level:"Entry Level"
},

{
name:"Prime Plan",
range:"$5,000 - $49,999",
level:"Growth Level"
},

{
name:"Master Plan",
range:"$50,000 - $499,999",
level:"Advanced Investor"
},

{
name:"Executive Plan",
range:"$500,000 - $5,000,000",
level:"Premium Investor"
}

];


export default function PlanTierCard({sector}:any){

const [selected,setSelected]=useState<any>(null);


return(

<div>


{
tiers.map((tier)=>(

<div className="tier-card"
key={tier.name}>


<h3>
{tier.name}
</h3>


<p>
{tier.range}
</p>


<p>
{tier.level}
</p>


<button
onClick={()=>setSelected(tier)}
>
View Details
</button>


</div>

))
}


{
selected &&
<PlanDetails
sector={sector}
tier={selected}
/>
}


</div>

)

}