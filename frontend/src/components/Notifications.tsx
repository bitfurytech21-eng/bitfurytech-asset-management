import "./Notifications.css";

interface Notification {
  id: number;
  title: string;
  message: string;
}

const notifications: Notification[] = [
  {
    id: 1,
    title: "Deposit Confirmed",
    message: "Your recent deposit has been successfully confirmed."
  },
  {
    id: 2,
    title: "Investment Update",
    message: "Your Real Estate investment earned today's ROI."
  },
  {
    id: 3,
    title: "Security",
    message: "Keep your password secure and enable 2FA when available."
  }
];

function Notifications() {
  return (
    <div className="notifications">
      <h2>Notifications</h2>

      {notifications.map((item) => (
        <div className="notification-card" key={item.id}>
          <h4>{item.title}</h4>
          <p>{item.message}</p>
        </div>
      ))}
    </div>
  );
}

export default Notifications;
