import React from "react";

interface BoardMember {
  name: string;
  position: string;
  image: string;
  bio: string;
}

interface BoardCardProps {
  member: BoardMember;
  onClick: () => void;
}

const BoardCard: React.FC<BoardCardProps> = ({ member, onClick }) => {
  return (
    <div className="board-card" onClick={onClick}>
      <img
        src={member.image}
        alt={member.name}
        className="board-card-image"
      />

      <div className="board-card-content">
        <h3>{member.name}</h3>
        <p>{member.position}</p>

        <button className="board-btn">
          View Profile
        </button>
      </div>
    </div>
  );
};

export default BoardCard;
