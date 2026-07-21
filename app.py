from flask import Flask, render_template_string, request, redirect, url_for, session, jsonify
from flask_cors import CORS

def create_app():
    app = Flask(__name__, static_folder='.', static_url_path='')
    app.secret_key = 'bitfury-tech-investment-secret'
    CORS(app)

    users = {
        'admin@bitfurytechinvestment.com': {'password': 'Admin123!', 'name': 'Admin Team', 'role': 'admin'},
        'investor@bitfurytechinvestment.com': {'password': 'Investor123!', 'name': 'Alex Morgan', 'role': 'user'},
    }

    def require_login():
        if 'user' not in session:
            return redirect(url_for('login'))
        return None

    def require_admin():
        if 'user' not in session or session['user']['role'] != 'admin':
            return redirect(url_for('dashboard'))
        return None

    @app.route('/')
    def home():
        return app.send_static_file('index.html')    
    @app.route('/api/test', methods=['GET'])
    def api_test():
        return jsonify({
            "message": "Flask API connected successfully"
        })


    @app.route('/api/login', methods=['POST'])
    def api_login():

        data = request.get_json()

        email = data.get('email', '').strip().lower()
        password = data.get('password', '')

        user = users.get(email)

        if user and user['password'] == password:

            session['user'] = {
                'email': email,
                'name': user['name'],
                'role': user['role']
            }

            return jsonify({
                "status": "success",
                "message": "Login successful",
                "user": session['user']
            })

        return jsonify({
            "status": "failed",
            "message": "Invalid email or password"
        }), 401

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            email = request.form.get('email', '').strip().lower()
            password = request.form.get('password', '')
            user = users.get(email)
            if user and user['password'] == password:
                session['user'] = {'email': email, 'name': user['name'], 'role': user['role']}
                if user['role'] == 'admin':
                    return redirect(url_for('admin'))
                return redirect(url_for('dashboard'))
            return render_template_string('''
            <!doctype html>
            <html lang="en">
              <head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Investor Login</title>
              <style>body{font-family:Arial,sans-serif;margin:0;background:#07111f;color:#f5f7fb} .wrap{max-width:520px;margin:2rem auto;padding:1rem} .card{background:rgba(255,255,255,.08);padding:2rem;border-radius:24px;border:1px solid rgba(255,255,255,.16)} .field{display:flex;flex-direction:column;gap:.35rem;margin-bottom:1rem} input{padding:.8rem 1rem;border-radius:12px;border:1px solid rgba(255,255,255,.16);background:#0b1730;color:#fff} button{border:0;border-radius:999px;padding:.8rem 1.1rem;font-weight:700;background:linear-gradient(135deg,#f2c94c,#ffd970);color:#07111f} a{color:#f2c94c;text-decoration:none}.error{color:#ffd970;margin-bottom:1rem}</style></head>
              <body><div class="wrap"><div class="card"><h1>Investor Login</h1><p class="error">Invalid email or password. Please try again.</p><form method="post"><div class="field"><label>Email</label><input name="email" type="email" required></div><div class="field"><label>Password</label><input name="password" type="password" required></div><button type="submit">Sign in</button></form><p><a href="/register">Create account</a></p><p><a href="/">Back to home</a></p></div></div></body></html>
            ''')
        return render_template_string('''
        <!doctype html>
        <html lang="en">
          <head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Investor Login</title>
          <style>body{font-family:Arial,sans-serif;margin:0;background:#07111f;color:#f5f7fb} .wrap{max-width:520px;margin:2rem auto;padding:1rem} .card{background:rgba(255,255,255,.08);padding:2rem;border-radius:24px;border:1px solid rgba(255,255,255,.16)} .field{display:flex;flex-direction:column;gap:.35rem;margin-bottom:1rem} input{padding:.8rem 1rem;border-radius:12px;border:1px solid rgba(255,255,255,.16);background:#0b1730;color:#fff} button{border:0;border-radius:999px;padding:.8rem 1.1rem;font-weight:700;background:linear-gradient(135deg,#f2c94c,#ffd970);color:#07111f} a{color:#f2c94c;text-decoration:none}</style></head>
          <body><div class="wrap"><div class="card"><h1>Investor Login</h1><p>Access your secure account and manage your portfolio with confidence.</p><form method="post"><div class="field"><label>Email</label><input name="email" type="email" required></div><div class="field"><label>Password</label><input name="password" type="password" required></div><button type="submit">Sign in</button></form><p><a href="/register">Create account</a></p><p><a href="/">Back to home</a></p></div></div></body></html>
        ''')

    @app.route('/register', methods=['GET', 'POST'])
    def register():
        if request.method == 'POST':
            email = request.form.get('email', '').strip().lower()
            name = request.form.get('name', '').strip()
            password = request.form.get('password', '')
            if '@' not in email or not password:
                return render_template_string('''
                <!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Create Account</title><style>body{font-family:Arial,sans-serif;margin:0;background:#07111f;color:#f5f7fb} .wrap{max-width:560px;margin:2rem auto;padding:1rem} .card{background:rgba(255,255,255,.08);padding:2rem;border-radius:24px;border:1px solid rgba(255,255,255,.16)} .field{display:flex;flex-direction:column;gap:.35rem;margin-bottom:1rem} input,select{padding:.8rem 1rem;border-radius:12px;border:1px solid rgba(255,255,255,.16);background:#0b1730;color:#fff} button{border:0;border-radius:999px;padding:.8rem 1.1rem;font-weight:700;background:linear-gradient(135deg,#f2c94c,#ffd970);color:#07111f} a{color:#f2c94c;text-decoration:none}.error{color:#ffd970}</style></head><body><div class="wrap"><div class="card"><h1>Create Investor Account</h1><p class="error">Please provide a valid email and password.</p><form method="post"><div class="field"><label>Full name</label><input name="name" required></div><div class="field"><label>Email</label><input name="email" type="email" required></div><div class="field"><label>Preferred plan</label><select name="plan"><option>Conservative</option><option selected>Balanced</option><option>Growth</option></select></div><div class="field"><label>Password</label><input name="password" type="password" required></div><button type="submit">Create account</button></form><p><a href="/login">Log in</a></p></div></div></body></html>
                ''')
            users[email] = {'password': password, 'name': name, 'role': 'user'}
            session['user'] = {'email': email, 'name': name, 'role': 'user'}
            return redirect(url_for('dashboard'))
        return render_template_string('''
        <!doctype html>
        <html lang="en">
          <head><metacharset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Create Account</title>
          <style>body{font-family:Arial,sans-serif;margin:0;background:#07111f;color:#f5f7fb} .wrap{max-width:560px;margin:2rem auto;padding:1rem} .card{background:rgba(255,255,255,.08);padding:2rem;border-radius:24px;border:1px solid rgba(255,255,255,.16)} .field{display:flex;flex-direction:column;gap:.35rem;margin-bottom:1rem} input,select{padding:.8rem 1rem;border-radius:12px;border:1px solid rgba(255,255,255,.16);background:#0b1730;color:#fff} button{border:0;border-radius:999px;padding:.8rem 1.1rem;font-weight:700;background:linear-gradient(135deg,#f2c94c,#ffd970);color:#07111f} a{color:#f2c94c;text-decoration:none}</style></head>
          <body><div class="wrap"><div class="card"><h1>Create Investor Account</h1><p>Join Bitfury Tech Investment and gain access to portfolio insights, investment plans, and dedicated support.</p><form method="post"><div class="field"><label>Full name</label><input name="name" required></div><div class="field"><label>Email</label><input name="email" type="email" required></div><div class="field"><label>Preferred plan</label><select name="plan"><option>Conservative</option><option selected>Balanced</option><option>Growth</option></select></div><div class="field"><label>Password</label><input name="password" type="password" required></div><button type="submit">Create account</button></form><p><a href="/login">Log in</a></p></div></div></body></html>
        ''')

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
        "photo": "/images/default-avatar.png"})
    
    
    @app.route("/profile")
    def profile():
        if "user" not in session:
            return redirect(url_for("login"))
    user = session["user"]

    return render_template_string("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>User Profile</title>

        <style>
            body{
                margin:0;
                font-family:Arial,sans-serif;
                background:#07111f;
                color:white;
            }

            .container{
                max-width:800px;
                margin:40px auto;
                padding:20px;
            }

            .card{
                background:#101d34;
                border-radius:18px;
                padding:30px;
                text-align:center;
            }

            img{
                width:120px;
                height:120px;
                border-radius:50%;
                border:4px solid #f2c94c;
                margin-bottom:20px;
            }

            h1{
                margin-bottom:10px;
            }

            p{
                font-size:18px;
                margin:8px 0;
            }

            a{
                display:inline-block;
                margin-top:20px;
                text-decoration:none;
                background:#f2c94c;
                color:#07111f;
                padding:12px 24px;
                border-radius:10px;
                font-weight:bold;
            }
        </style>

    </head>

    <body>

        <div class="container">

            <div class="card">
                                  
                <img src="/images/default-avatar.png">

                <h1>{{ name }}</h1>

                <p><strong>Email:</strong> {{ email }}</p>

                <p><strong>Role:</strong> {{ role }}</p>

                <p><strong>Status:</strong> Verified Investor</p>

                <a href="/dashboard">Back to Dashboard</a>

            </div>

        </div>

    </body>

    </html>
    """,
    name=user["name"],
    email=user["email"],
    role=user["role"])

    @app.route('/admin')
    def admin():
        redirect_result = require_admin()
        if redirect_result:
            return redirect_result
        return render_template_string('''
        <!doctype html>
        <html lang="en">
          <head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Admin Panel</title>
          <style>body{font-family:Arial,sans-serif;background:#07111f;color:#f5f7fb;margin:0} .wrap{max-width:1000px;margin:0 auto;padding:2rem} .grid{display:grid;grid-template-columns:repeat(2,1fr);gap:1rem}.card{background:rgba(255,255,255,.07);padding:1.5rem;border-radius:20px;border:1px solid rgba(255,255,255,.12)} a{color:#f2c94c} li{line-height:1.8}</style></head>
          <body>
            <div class="wrap">
              <h1>Admin Panel</h1>
              <p>Administrative controls for portfolio allocation, compliance, and reporting.</p>
              <div class="grid">
                <div class="card"><h3>Portfolio Allocation</h3><ul><li>Real estate: 40%</li><li>Stocks: 35%</li><li>Precision metals: 25%</li></ul></div>
                <div class="card"><h3>Admin Actions</h3><ul><li>Approve investor requests</li><li>Monitor performance reports</li><li>Configure risk thresholds</li></ul></div>
              </div>
              <p><a href="/dashboard">Back to dashboard</a> · <a href="/logout">Logout</a></p>
            </div>
          </body>
        </html>
        ''')
        
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
    @app.route('/logout')
    def logout():
        session.pop('user', None)
        return redirect(url_for('home'))
        
    return app

app = create_app()


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
