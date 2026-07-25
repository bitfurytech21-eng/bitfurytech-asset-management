import { useState } from "react";
import BoardCard, { BoardMember } from "./BoardCard";
import BoardModal from "./BoardModal";

const members: BoardMember[] = [
  {
    id: 1,
    name: "John Smith",
    position: "Chairman",
    image: "/Images/Board/chairman.jpg",
  },
  {
    id: 2,
    name: "Sarah Williams",
    position: "Chief Executive Officer",
    image: "/Images/Board/ceo.jpg",
  },
  {
    id: 3,
    name: "Michael Johnson",
    position: "Chief Financial Officer",
    image: "/Images/Board/cfo.jpg",
  },
];

export default function BoardSection() {
  const [profile, setProfile] = useState<any>(null);

  async function openProfile(id: number) {
    try {
      const response = await fetch(`/api/board-members/${id}`);

      if (!response.ok) {
        throw new Error("Unable to load biography.");
      }

      const data = await response.json();
      setProfile(data);
    } catch (error) {
      console.error(error);
    }
  }

  return (
    <section className="board-section">
      <h2>Board of Directors</h2>

      <div className="board-grid">
        {members.map((member) => (
          <BoardCard
            key={member.id}
            member={member}
            onViewProfile={openProfile}
          />
        ))}
      </div>

      {profile && (
        <Boardmodal
          profile={profile}
          onClose={() => setProfile(null)}
        />
      )}
    </section>
  );
}
