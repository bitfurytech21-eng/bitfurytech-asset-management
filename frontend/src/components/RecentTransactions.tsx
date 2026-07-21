interface Transaction {
  id: number;
  type: string;
  amount: string;
  status: string;
}

const transactions: Transaction[] = [
  {
    id: 1,
    type: "Deposit",
    amount: "$5,000",
    status: "Completed",
  },
  {
    id: 2,
    type: "Investment",
    amount: "$2,500",
    status: "Active",
  },
  {
    id: 3,
    type: "Withdrawal",
    amount: "$1,000",
    status: "Pending",
  },
];

function RecentTransactions() {
  return (
    <div className="transactions-card">
      <h3>Recent Transactions</h3>

      <table>
        <thead>
          <tr>
            <th>Type</th>
            <th>Amount</th>
            <th>Status</th>
          </tr>
        </thead>

        <tbody>
          {transactions.map((transaction) => (
            <tr key={transaction.id}>
              <td>{transaction.type}</td>
              <td>{transaction.amount}</td>
              <td>{transaction.status}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default RecentTransactions;
