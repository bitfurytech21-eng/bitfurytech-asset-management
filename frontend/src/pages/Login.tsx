import { useState } from "react";

function Login() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [message, setMessage] = useState("");
  
  const handleLogin = async (e:React.FormEvent<HTMLFormElement>)=> {e.preventDefault();//your login code};
    
   try {
      const response = await fetch(
        "http://127.0.0.1:5000/api/login",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          credentials: "include",
          body: JSON.stringify({
            email: email,
            password: password,
          }),
        }
      );

      const data = await response.json();

      if (response.ok) {
        setMessage("Login successful");

        // Optional: go to dashboard
        window.location.href = "/dashboard";
      } else {
        setMessage(data.message);
      }

    } catch (error) {
      console.log(error);
      setMessage("Backend connection failed");
    }
  };

  return (
    <div>
      <h1>Investor Login</h1>

      <form onSubmit={handleLogin}>

        <div>
          <label>Email</label>
          <input
            type="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            placeholder="Enter email"
            required
          />
        </div>

        <div>
          <label>Password</label>
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            placeholder="Enter password"
            required
          />
        </div>


        <button type="submit">
          Sign In
        </button>

      </form>

      <p>{message}</p>

    </div>
  );
}

export default Login;