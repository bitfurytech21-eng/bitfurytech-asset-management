import { useState } from "react";

function Login() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [message, setMessage] = useState("");
  
  const handleLogin = async (e:React.FormEvent<HTMLFormElement>)=> {e.preventDefault();//your login code};
    
   try {
      const response = await fetch(`https//:bitfurytech-asset-management-5.onrender.com/api/auth/login`, {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({ email, password })
});
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

        // Optional: go to dashboard
        window.location.href = "https://bitfurytech-asset-management-5.onrender.com/api/dashboard";
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
