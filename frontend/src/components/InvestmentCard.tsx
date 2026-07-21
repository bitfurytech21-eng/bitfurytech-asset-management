import "./InvestmentCard.css";

interface InvestmentCardProps {
  title: string;
  amount: string;
  roi: string;
  status: string;
}

function InvestmentCard({
  title,
  amount,
  roi,
  status,
}: InvestmentCardProps) {
  return (
    <div className="investment-card">
      <h3>{title}</h3>

      <p>
        <strong>Investment:</strong> {amount}
      </p>

      <p>
        <strong>ROI:</strong> {roi}
      </p>

      <p>
        <strong>Status:</strong> {status}
      </p>

      <div className="progress">
        <div className="progress-fill"></div>
      </div>
    </div>
  );
}

export default InvestmentCard;
