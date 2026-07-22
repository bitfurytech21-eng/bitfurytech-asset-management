from flask import (
    Flask,
    render_template_string,
    request,
    redirect,
    url_for,
    session,
    jsonify
)
from flask_cors import CORS


def create_app():
    app = Flask(
        __name__,
        static_folder=".",
        static_url_path=""
    )

    app.secret_key = "bitfury-tech-investment-secret"

    CORS(app)

    users = {
        "admin@bitfurytechinvestment.com": {
            "password": "Admin123!",
            "name": "Admin Team",
            "role": "admin"
        },
        "investor@bitfurytechinvestment.com": {
            "password": "Investor123!",
            "name": "Alex Morgan",
            "role": "user"
        }
    }

    def require_login():
        if "user" not in session:
            return redirect(url_for("login"))
        return None

    def require_admin():
        if (
            "user" not in session
            or session["user"]["role"] != "admin"
        ):
            return redirect(url_for("login"))
        return None


    @app.route("/")
    def home():
        return app.send_static_file("index.html")


    @app.route("/api/test")
    def api_test():
        return jsonify({
            "message": "Flask API connected successfully"
        })


    @app.route("/api/login", methods=["POST"])
    def api_login():

        data = request.get_json()

        email = data.get("email", "").strip().lower()
        password = data.get("password", "")

        user = users.get(email)

        if user and user["password"] == password:

            session["user"] = {
                "email": email,
                "name": user["name"],
                "role": user["role"]
            }

            return jsonify({
                "status": "success",
                "message": "Login successful",
                "user": session["user"]
            })

        return jsonify({
            "status": "failed",
            "message": "Invalid email or password"
        }), 401
        
    @app.route("/login", methods=["GET", "POST"])
     def login():

           if request.method == "POST":

            email = request.form.get("email", "").strip().lower()
            password = request.form.get("password", "")

            user = users.get(email)

            if user and user["password"] == password:

                session["user"] = {
                    "email": email,
                    "name": user["name"],
                    "role": user["role"]
                }

                if user["role"] == "admin":
                    return redirect(url_for("admin"))

                return redirect(url_for("profile"))

            return render_template_string("""
            <h2>Login Failed</h2>
            <p>Invalid email or password.</p>
            <a href="/login">Try Again</a>
            """)

        return render_template_string("""
        <!doctype html>

        <html>

        <head>
            <title>Investor Login</title>
        </head>

        <body>

            <h1>Investor Login</h1>

            <form method="POST">

                <p>
                    <input
                        type="email"
                        name="email"
                        placeholder="Email"
                        required>
                </p>

                <p>
                    <input
                        type="password"
                        name="password"
                        placeholder="Password"
                        required>
                </p>

                <button type="submit">
                    Login
                </button>

            </form>

            <p>
                <a href="/register">
                    Create Account
                </a>
            </p>

        </body>

        </html>
        """)


    @app.route("/register", methods=["GET", "POST"])
    def register():

        if request.method == "POST":

            name = request.form.get("name", "").strip()

            email = request.form.get("email", "").strip().lower()

            password = request.form.get("password", "")

            if not name or "@" not in email or not password:

                return render_template_string("""
                <h2>Registration Failed</h2>
                <p>Please complete every field.</p>
                <a href="/register">Back</a>
                """)

            users[email] = {
                "password": password,
                "name": name,
                "role": "user"
            }

            session["user"] = {
                "email": email,
                "name": name,
                "role": "user"
            }

            return redirect(url_for("profile"))

        return render_template_string("""
        <!doctype html>

        <html>

        <head>
            <title>Create Account</title>
        </head>

        <body>

            <h1>Create Investor Account</h1>

            <form method="POST">

                <p>
                    <input
                        name="name"
                        placeholder="Full Name"
                        required>
                </p>

                <p>
                    <input
                        type="email"
                        name="email"
                        placeholder="Email"
                        required>
                </p>

                <p>
                    <input
                        type="password"
                        name="password"
                        placeholder="Password"
                        required>
                </p>

                <button type="submit">
                    Register
                </button>

            </form>

            <p>
                <a href="/login">
                    Login
                </a>
            </p>

        </body>

        </html>
        """)
    @app.route("/api/dashboard", methods=["GET"])
    def api_dashboard():

             if "user" not in session:
                 return jsonify({
                  "success": False,
                  "message": "Unauthorized"
                   }), 401

        user = session["user"]

        return jsonify({
            "success": True,
            "name": user["name"],
            "email": user["email"],
            "role": user["role"],
            "portfolio": 25400,
            "balance": 8300,
            "investments": 12,
            "profit": 520,
            "risk_level": "Balanced",
            "photo": "/images/default-avatar.png"
        })


    @app.route("/profile")
    def profile():

        redirect_result = require_login()

        if redirect_result:
            return redirect_result

        user = session["user"]

        return render_template_string("""
        <!doctype html>

        <html>

        <head>

            <title>Investor Profile</title>

        </head>

        <body>

            <h1>{{ name }}</h1>

            <p><strong>Email:</strong> {{ email }}</p>

            <p><strong>Role:</strong> {{ role }}</p>

            <p>Status: Verified Investor</p>

            <p>

                <a href="/logout">
                    Logout
                </a>

            </p>

        </body>

        </html>
        """,
        name=user["name"],
        email=user["email"],
        role=user["role"])


    @app.route("/admin")
    def admin():

        redirect_result = require_admin()

        if redirect_result:
            return redirect_result

        return render_template_string("""
        <!doctype html>

        <html>

        <head>

            <title>Admin Dashboard</title>

        </head>

        <body>

            <h1>Bitfury Tech Investment Admin Panel</h1>

            <p>Welcome Administrator.</p>

            <a href="/logout">
                Logout
            </a>

        </body>

        </html>
        """)


    @app.route("/api/profile", methods=["GET"])
    def api_profile():

        if "user" not in session:

            return jsonify({
                "success": False,
                "message": "Unauthorized"
            }), 401

        user = session["user"]

        return jsonify({

            "success": True,
            "name": user["name"],
            "email": user["email"],
            "role": user["role"],
            "phone": "+1 000 000 0000",
            "country": "Australia",
            "photo": "/images/default-avatar.png",
            "status": "Verified",
            "kyc": "Completed"

        })
     @app.route("/api/transactions", methods=["GET"])
     def api_transactions():

          if "user" not in session:
            return jsonify([]), 401

        return jsonify([
            {
                "id": 1,
                "type": "Deposit",
                "amount": 5000,
                "status": "Completed",
                "date": "2026-07-20"
            },
            {
                "id": 2,
                "type": "Investment",
                "amount": 2500,
                "status": "Running",
                "date": "2026-07-19"
            },
            {
                "id": 3,
                "type": "Withdrawal",
                "amount": 1000,
                "status": "Pending",
                "date": "2026-07-18"
            }
        ])


    @app.route("/api/investments", methods=["GET"])
    def api_investments():

        if "user" not in session:
            return jsonify([]), 401

        return jsonify([
            {
                "title": "Real Estate",
                "amount": 10000,
                "roi": "12.4%",
                "status": "Running"
            },
            {
                "title": "Agriculture",
                "amount": 6500,
                "roi": "8.2%",
                "status": "Running"
            },
            {
                "title": "Cryptocurrency",
                "amount": 4200,
                "roi": "15.8%",
                "status": "Running"
            },
            {
                "title": "Stocks",
                "amount": 3100,
                "roi": "7.4%",
                "status": "Running"
            }
        ])


    @app.route("/api/notifications", methods=["GET"])
    def api_notifications():

        if "user" not in session:
            return jsonify([]), 401

        return jsonify([
            {
                "title": "Deposit Confirmed",
                "message": "Your deposit has been confirmed."
            },
            {
                "title": "Daily ROI",
                "message": "Today's earnings have been credited."
            },
            {
                "title": "Security",
                "message": "Your account is protected."
            }
        ])


    @app.route("/api/board-members", methods=["GET"])
    def board_members():

        return jsonify([
            {
                "id": 1,
                "name": "John Smith",
                "position": "Chief Executive Officer",
                "image": "/images/board/ceo.jpg",
                "bio": "John Smith has over 25 years of leadership experience in global investment management."
            },
            {
                "id": 2,
                "name": "Jane Williams",
                "position": "Chief Financial Officer",
                "image": "/images/board/cfo.jpg",
                "bio": "Jane Williams oversees financial strategy, risk management, and corporate governance."
            }
        ])


    @app.route("/logout")
    def logout():

        session.pop("user", None)

        return redirect(url_for("home"))


    return app


app = create_app()


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
