function CompanyVideo() {
  return (
    <section style={{ padding: "60px", textAlign: "center" }}>
      <h2>Company Introduction</h2>

      <video
        controls
        width="800"
        style={{ maxWidth: "100%", borderRadius: "12px" }}
      >
        <source src="/videos/company.mp4" type="video/mp4" />
        Your browser does not support the video tag.
      </video>

      <p>
        Learn more about Bitfury Tech Investment, our mission, and our vision.
      </p>
    </section>
  );
}

export default CompanyVideo;