function Header() {
      return (
          <header className="site-header">
                <div className="container nav-bar">
                        <a className="brand" href="#hero">
                                  <img src="/logo.svg" alt="Bitfury Tech Investment logo" />
                                            <span>Bitfury Tech</span>
                                                    </a>

                                                            <button className="menu-toggle" aria-label="Toggle menu">
                                                                      <span></span>
                                                                                <span></span>
                                                                                          <span></span>
                                                                                                  </button>

                                                                                                          <nav className="site-nav">
                                                                                                                    <a href="#hero">Home</a>
                                                                                                                              <a href="#about">About</a>
                                                                                                                                        <a href="#plans">Plans</a>
                                                                                                                                                  <a href="#services">Services</a>
                                                                                                                                                            <a href="#contact">Contact</a>

                                                                                                                                                                      <a className="btn btn-secondary nav-btn" href="/login">
                                                                                                                                                                                  Login
                                                                                                                                                                                            </a>

                                                                                                                                                                                                      <a className="btn btn-primary nav-btn" href="/register">
                                                                                                                                                                                                                  Register
                                                                                                                                                                                                                            </a>
                                                                                                                                                                                                                                    </nav>
                                                                                                                                                                                                                                          </div>
                                                                                                                                                                                                                                              </header>
                                                                                                                                                                                                                                                );
                                                                                                                                                                                                                                                }

                                                                                                                                                                                                                                                export default Header;
