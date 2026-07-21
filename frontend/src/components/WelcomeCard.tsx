import "./WelcomeCard.css";

interface WelcomeCardProps {
  name: string;
}

function WelcomeCard({ name }: WelcomeCardProps) {
  return (
    <div className="welcome-card">
      <h1>Welcome Back 👋</h1>

      <h2>{name}</h2>

      <p>Verified Investor</p>

      <p>Your portfolio is ready.</p>
    </div>
  );
}

export default WelcomeCard;