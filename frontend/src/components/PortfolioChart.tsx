type PortfolioChartProps = {
  portfolio: number;
};

function PortfolioChart({ portfolio }: PortfolioChartProps) {
  return (
    <div className="card">
      <h3>Portfolio Growth</h3>

      <div
        style={{
          height: "180px",
          display: "flex",
          alignItems: "flex-end",
          gap: "10px",
          marginTop: "20px",
        }}
      >
        {[35, 55, 70, 90, 65, 100, 85].map((height, index) => (
          <div
            key={index}
            style={{
              flex: 1,
              height: `${height}%`,
              background: "#00b894",
              borderRadius: "6px 6px 0 0",
            }}
          />
        ))}
      </div>

      <h2 style={{ marginTop: "20px" }}>
        ${portfolio.toLocaleString()}
      </h2>
    </div>
  );
}

export default PortfolioChart;
