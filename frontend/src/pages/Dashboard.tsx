import Notifications from "../components/Notifications";
import QuickActions from "../components/QuickActions";
import InvestmentCard from "../components/InvestmentCard";
import RecentTransactions from "../components/RecentTransactions";
import PortfolioChart from "../components/PortfolioChart";
import { useEffect, useState } from "react";
import "../components/Dashboard.css";
import WelcomeCard from "../components/WelcomeCard";
import StatCard from "../components/StatCard";
import Sidebar from "../components/Sidebar";
import Topbar from "../components/Topbar";

interface DashboardData {
    name: string;
    email: string;
    role: string;
    portfolio: number;
    balance: number;
    investments: number;
    profit: number;
    risk_level: string;
    photo: string;
}

function Dashboard(){const [data, setData] = useState<DashboardData | null>(null);

useEffect(() => {
  fetch("http://127.0.0.1:5000/api/dashboard", {
    credentials: "include",
  })
    .then((res) => res.json())
    .then((result) => setData(result))
    .catch((err) => console.error(err));
}, []);if (!data) {
  return <h2>Loading Dashboard...</h2>;
}

return(

<div className="dashboard">

<Sidebar/>

<div className="dashboard content">

      <Topbar
          name={data.name}
          photo={data.photo}
          />
    
      <WelcomeCard 
          name={data.name} />
    
      <div className="stats-grid">

    <StatCard
  title="Portfolio Value"
  value={`$${data.portfolio.toLocaleString()}`}
/>

<StatCard
  title="Available Balance"
  value={`$${data.balance.toLocaleString()}`}
/>

<StatCard
  title="Active Investments"
  value={data.investments.toString()}
/>

<StatCard
  title="Today's Profit"
  value={`+$${data.profit.toLocaleString()}`}
/>
</div>
 <PortfolioChart portfolio={data.portfolio} />
  <import RecentTransactions/>
  <h2 style={{ color: "#F2C94C", marginTop: "40px" }}>
  Active Investments
</h2>

<InvestmentCard
  title="Real Estate"
  amount="$10,000"
  roi="12.4%"
  status="Running"
/>

<InvestmentCard
  title="Agriculture"
  amount="$6,500"
  roi="8.2%"
  status="Running"
/>

<InvestmentCard
  title="Cryptocurrency"
  amount="$4,200"
  roi="15.8%"
  status="Running"
/>

<InvestmentCard
  title="Stocks"
  amount="$3,100"
  roi="7.4%"
  status="Running"
/>
<QuickActions />
<Notifications />
</main>
</div>
);
