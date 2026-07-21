import TransactionTable from "../components/TransactionTable";
import { useEffect, useState } from "react";

interface Transaction {
  id: number;
  type: string;
  amount: number;
  status: string;
  date: string;
}

export default function TransactionTable() {
  const [transactions, setTransactions] = useState<Transaction[]>([]);

  useEffect(() => {
    fetch("http://127.0.0.1:5000/api/transactions")
      .then((res) => res.json())
      .then((data) => setTransactions(data))
      .catch((err) => console.error(err));
  }, []);

  return (
    <div className="transaction-table">
      <h2>Recent Transactions</h2>

      <table>
        <thead>
          <tr>
            <th>ID</th>
            <th>Type</th>
            <th>Amount</th>
            <th>Status</th>
            <th>Date</th>
          </tr>
        </thead>

        <tbody>
          {transactions.map((tx) => (
            <tr key={tx.id}>
              <td>{tx.id}</td>
              <td>{tx.type}</td>
              <td>${tx.amount}</td>
              <td>{tx.status}</td>
              <td>{tx.date}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
