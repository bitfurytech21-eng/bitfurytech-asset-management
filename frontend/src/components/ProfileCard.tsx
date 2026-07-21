import "./ProfileCard.css";

interface ProfileCardProps {
  name: string;
  email: string;
  role: string;
  photo: string;
}

function ProfileCard({
  name,
  email,
  role,
  photo,
}: ProfileCardProps) {
  return (
    <div className="profile-card">

      <img
        src={photo}
        alt={name}
        className="profile-photo"
      />

      <h2>{name}</h2>

      <p>{email}</p>

      <span className="badge">
        {role.toUpperCase()}
      </span>

      <hr />

      <div className="profile-info">

        <p>
          <strong>Status:</strong> Verified
        </p>

        <p>
          <strong>KYC:</strong> Completed
        </p>

        <p>
          <strong>Member Since:</strong> 2026
        </p>

      </div>

    </div>
  );
}

export default ProfileCard;
