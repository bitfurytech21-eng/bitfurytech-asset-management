export default function PlanDetails({sector,tier}:any){

return(

<div className="details-card">

<h2>
BitfuryTech {sector}
</h2>


<h3>
{tier.name}
</h3>


<p>

This plan allows investors to participate
in BitfuryTech's {sector.toLowerCase()} 
investment opportunities with structured
portfolio management and reporting.

</p>


<h4>
Investment Range
</h4>

<p>
{tier.range}
</p>


<h4>
Includes
</h4>

<ul>

<li>Portfolio monitoring</li>

<li>Investment reports</li>

<li>Market insights</li>

<li>Customer support</li>

</ul>


<button>
Start Investing
</button>


</div>

)

}