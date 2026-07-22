import { useEffect, useState } from "react";
import BoardModal from "./BoardModal",
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

  useEffect(() => {
    fetch("/api/board-members")
      .then((response) => response.json())
      .then((data) => setMembers(data))
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

    <BoardCard />

    <BoardCard />

    <BoardCard />

    <BoardCard />

  </div>
{selectedMember && (
  <BoardModal
    member={selectedMember}
    isOpen={isModalOpen}
    onClose={() => setIsModalOpen(false)}
  />
)}
        
</section>
 
      <div
        style={{
          display: "grid",
          gridTemplateColumns: "repeat(auto-fit, minmax(250px,1fr))",
          gap: "20px",
          marginTop: "30px"
        }}
      >
        {members.map((member) => (
          <div
            key={member.id}
            style={{
              border: "1px solid #ddd",
              borderRadius: "12px",
              padding: "20px",
              textAlign: "center"
            }}
          >
            <img
              src={member.image}
              alt={member.name}
              width="150"
              height="150"
              style={{
                borderRadius: "50%",
                objectFit: "cover"
              }}
            />

            <h3>{member.name}</h3>

            <p>{member.position}</p>

            <button
           onClick={() => {
           setSelectedMember(member);
           setIsModalOpen(true);
           }}
        >
           View Biography
          </button>
          </div>
        ))}
      </div>
    </section>
  );
}

export default BoardSection;
