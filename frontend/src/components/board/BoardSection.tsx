import { useEffect, useState } from "react";
import BoardModal from "./BoardModal";
import BoardCard from "./BoardCard";
import "./Board.css";

interface BoardMember {
  id: number;
  name: string;
  position: string;
  image: string;
  bio: string;
}

function BoardSection() {
  const [selectedMember, setSelectedMember] = useState<BoardMember | null>(null);
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [members, setMembers] = useState<BoardMember[]>([]);

  useEffect(() => {
    fetch("/api/board-members")
      .then((response) => response.json())
      .then((data) => setMembers(data.members ?? []))
      .catch((error) => console.error(error));
  }, []);

  return (
    <section style={{ padding: "60px" }}>
      <h2 style={{ textAlign: "center" }}>Board of Directors</h2> 

      <section className="board-section">

  <div className="board-header">

    <span>OUR EXPERTS</span>

    <h2>WE ARE FRIENDLY & PROFESSIONAL</h2>

    <p>
      BitfuryTech Investment was founded in 2017 by a group of
      skilled financial analysts, fund managers, and research
      scientists with the mission of delivering disciplined
      investment strategies while managing risk responsibly.
    </p>

  </div>

  <div className="board-grid">

    {members.map((member) => (
      <BoardCard
        key={member.id}
        member={member}
        onClick={() => {
          setSelectedMember(member);
          setIsModalOpen(true);
        }}
      />
    ))}

  </div>
{selectedMember && isModalOpen && (
  <BoardModal
    member={selectedMember}
    onClose={() => setIsModalOpen(false)}
  />
)}

</section>
    </section>
  );
}

export default BoardSection;
