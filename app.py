from flask import Flask, render_template_string, request, redirect, url_for, session


def create_app():
    app = Flask(__name__, static_folder='.', static_url_path='')
    app.secret_key = 'bitfury-tech-investment-secret'

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
          <head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Create Account</title>
          <style>body{font-family:Arial,sans-serif;margin:0;background:#07111f;color:#f5f7fb} .wrap{max-width:560px;margin:2rem auto;padding:1rem} .card{background:rgba(255,255,255,.08);padding:2rem;border-radius:24px;border:1px solid rgba(255,255,255,.16)} .field{display:flex;flex-direction:column;gap:.35rem;margin-bottom:1rem} input,select{padding:.8rem 1rem;border-radius:12px;border:1px solid rgba(255,255,255,.16);background:#0b1730;color:#fff} button{border:0;border-radius:999px;padding:.8rem 1.1rem;font-weight:700;background:linear-gradient(135deg,#f2c94c,#ffd970);color:#07111f} a{color:#f2c94c;text-decoration:none}</style></head>
          <body><div class="wrap"><div class="card"><h1>Create Investor Account</h1><p>Join Bitfury Tech Investment and gain access to portfolio insights, investment plans, and dedicated support.</p><form method="post"><div class="field"><label>Full name</label><input name="name" required></div><div class="field"><label>Email</label><input name="email" type="email" required></div><div class="field"><label>Preferred plan</label><select name="plan"><option>Conservative</option><option selected>Balanced</option><option>Growth</option></select></div><div class="field"><label>Password</label><input name="password" type="password" required></div><button type="submit">Create account</button></form><p><a href="/login">Log in</a></p></div></div></body></html>
        ''')

    @app.route('/dashboard')
    def dashboard():
        redirect_result = require_login()
        if redirect_result:
            return redirect_result
        user = session['user']
        return render_template_string('''
        <!doctype html>
        <html lang="en">
          <head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>User Dashboard</title>
          <style>body{font-family:Arial,sans-serif;background:#07111f;color:#f5f7fb;margin:0} .wrap{max-width:1100px;margin:0 auto;padding:2rem} .grid{display:grid;grid-template-columns:repeat(3,1fr);gap:1rem}.card{background:rgba(255,255,255,.07);padding:1.5rem;border-radius:20px;border:1px solid rgba(255,255,255,.12)} a{color:#f2c94c} .top{display:flex;justify-content:space-between;align-items:center;gap:1rem;margin-bottom:1.5rem}</style></head>
          <body>
            <div class="wrap">
              <div class="top"><h1>User Dashboard</h1><a href="/logout">Logout</a></div>
              <p>Welcome back, {{name}}. Your holdings and activity are up to date.</p>
              <div class="grid">
                <div class="card"><h3>Portfolio Value</h3><p>$1,248,000</p></div>
                <div class="card"><h3>Monthly Return</h3><p>+8.4%</p></div>
                <div class="card"><h3>Risk Level</h3><p>Balanced</p></div>
              </div>
              <p><a href="/profile">View profile</a> · <a href="/">Back to home</a></p>
            </div>
          </body>
        </html>
        ''', name=user['name'] 
  
)

    @app.route('/profile')
    def profile():
        redirect_result = require_login()
        if redirect_result:
            return redirect_result
        user = session['user']
        return render_template_string('''
        <!doctype html>
        <html lang="en">
          <head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>User Profile</title>
          <style>body{font-family:Arial,sans-serif;background:#07111f;color:#f5f7fb;margin:0} .wrap{max-width:900px;margin:0 auto;padding:2rem} .card{background:rgba(255,255,255,.07);padding:1.5rem;border-radius:20px;border:1px solid rgba(255,255,255,.12)} a{color:#f2c94c}</style></head>
          <body>
            <div class="wrap">
              <div class="card">
                <h1>User Profile</h1>
                <p><strong>Name:</strong> {{name}}</p>
                <p><strong>Email:</strong> {{email}}</p>
                <p><strong>Role:</strong> {{role}}</p>
                <p><strong>Status:</strong> Verified investor</p>
                <p><a href="/dashboard">Back to dashboard</a> · <a href="/">Back to home</a></p>
              </div>
            </div>
          </body>
        </html>
        ''', name=user['name'], email=user['email'], role=user['role'])

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

    @app.route('/logout')
    def logout():
        session.pop('user', None)
        return redirect(url_for('home'))

    return app


app = create_app()


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
