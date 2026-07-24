function CompanyVideo() {
  return (
    <section style={{ padding: "60px", textAlign: "center" }}>
      <h2>Company Introduction</h2>

      <iframe
    width="800"
    height="450"
    src="https://www.youtube.com/embed/QYE14pQ6NeQ"
    title="Bitfury Tech Investment Company Introduction"
    style={{
        maxWidth: "100%",
        borderRadius: "12px",
        border: "none"
    }}
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
    allowFullScreen
></iframe>

      <p>
        Learn more about Bitfury Tech Investment, our mission, and our vision.
      </p>
    </section>
  );
}

export default CompanyVideo;
