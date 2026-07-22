import React from "react";

interface BoardMember {
  name: string;
  position: string;
  image: string;
  bio: string;
}

interface BoardModalProps {
  member: BoardMember | null;
  onClose: () => void;
}

const BoardModal: React.FC<BoardModalProps> = ({ member, onClose }) => {
  if (!member) return null;

  return (
    <div className="board-modal-overlay">
      <div className="board-modal">
        <button className="close-btn" onClick={onClose}>
          ×
        </button>

        <img
          src={member.image}
          alt={member.name}
          className="board-image"
        />

        <h2>{member.name}</h2>
        <h4>{member.position}</h4>
        <p>{member.bio}</p>
      </div>
    </div>
  );
};

export default BoardModal;
