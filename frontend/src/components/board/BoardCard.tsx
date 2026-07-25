import React from "react";

export interface BoardMember {
  id: number;
  name: string;
  position: string;
  image: string;
}

interface Props {
  member: BoardMember;
  onViewProfile: (id: number) => void;
}

export default function BoardCard({ member, onViewProfile }: Props) {
  return (
    <div className="board-card">
      <img
        className="board-photo"
        src={member.image}
        alt={member.name}
      />

      <h3>{member.name}</h3>

      <p className="board-position">
        {member.position}
      </p>

      <button
        className="board-btn"
        onClick={() => onViewProfile(member.id)}
      >
        View Profile
      </button>
    </div>
  );
}
