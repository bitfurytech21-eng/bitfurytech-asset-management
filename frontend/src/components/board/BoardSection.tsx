import { useEffect, useState } from "react";

interface BoardMember {
  id: number;
  name: string;
  position: string;
  image: string;
  bio: string;
}

function BoardSection() {
  const [members, setMembers] = useState<BoardMember[]>([]);

  useEffect(() => {
    fetch("/api/board-members")
      .then((response) => response.json())
      .then((data) => setMembers(data))
      .catch((error) => console.error(error));
  }, []);

  return (
    <section style={{ padding: "60px" }}>
      <h2 style={{ textAlign: "center" }}>Board of Directors</h2>

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
              onClick={() => alert(member.bio)}
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
