import os
import subprocess

# Function to create a new React app
def create_react_app(app_name):
    try:
        # Create a new React app
        subprocess.run(["npx", "create-react-app", app_name], check=True)
        
        # Change directory to the app folder
        os.chdir(app_name)

        # Install necessary packages (React Router for navigation if needed)
        subprocess.run(["npm", "install", "react-router-dom"], check=True)

        # Create components directory
        os.makedirs("src/components", exist_ok=True)

        # Create basic structure files
        create_files()

    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e}")
        
def create_files():
    # Creating App.js (main file)
    app_js_content = """
import React from 'react';
import Header from './components/Header';
import Footer from './components/Footer';
import Home from './components/Home';

function App() {
  return (
    <div className="App">
      <Header />
      <Home />
      <Footer />
    </div>
  );
}

export default App;
    """
    with open('src/App.js', 'w') as file:
        file.write(app_js_content)

    # Create Header.js
    header_js_content = """
import React from 'react';

function Header() {
  return (
    <header>
      <nav>
        <ul>
          <li><a href="#">Join a Book Club</a></li>
          <li><a href="#">Find a Book</a></li>
          <li><a href="#">Blog</a></li>
          <li><a href="#">Discussion Guides</a></li>
        </ul>
        <button>Sign Up</button>
      </nav>
      <div className="hero">
        <h1>Zibby’s Book Club</h1>
        <p>Interactive, diverse book club experiences, connecting members worldwide.</p>
      </div>
    </header>
  );
}

export default Header;
    """
    with open('src/components/Header.js', 'w') as file:
        file.write(header_js_content)

    # Create Home.js (with book previews and testimonials)
    home_js_content = """
import React from 'react';

function Home() {
  return (
    <main>
      <section className="whats-new">
        <div className="book-list">
          <div className="book">
            <h2>The Complete List of Reese's Book Club Picks</h2>
            <p>Reese Witherspoon has been recommending...</p>
          </div>
          <div className="book">
            <h2>Learning to Love the World, One Crew at a Time</h2>
            <p>Margaret Renkl’s backyard crew and...</p>
          </div>
          <div className="book">
            <h2>Which Scents Suit Your Story?</h2>
            <p>Take the quiz to see which scent leads...</p>
          </div>
        </div>
      </section>

      <section className="testimonials">
        <div className="testimonial">
          <p>"Our club started as an experiment..."</p>
          <span>Happier Members</span>
        </div>
        <div className="testimonial">
          <p>"Has made it easier for our book club..."</p>
          <span>Saves Time</span>
        </div>
        <div className="testimonial">
          <p>"Fewer emails before Bookclubs!"</p>
          <span>Fewer Emails</span>
        </div>
      </section>
    </main>
  );
}

export default Home;
    """
    with open('src/components/Home.js', 'w') as file:
        file.write(home_js_content)

    # Create Footer.js
    footer_js_content = """
import React from 'react';

function Footer() {
  return (
    <footer>
      <section className="newsletter">
        <h2>Join the Newsletter</h2>
        <input type="email" placeholder="Enter email address" />
        <button>Subscribe</button>
      </section>
      <p>&copy; 2024 Zibby's Book Club. All rights reserved.</p>
      <div className="social">
        <a href="#">Instagram</a>
        <a href="#">Facebook</a>
        <a href="#">Twitter</a>
        <a href="#">TikTok</a>
      </div>
    </footer>
  );
}

export default Footer;
    """
    with open('src/components/Footer.js', 'w') as file:
        file.write(footer_js_content)

    print("Project structure created successfully.")

# Call the function to create the project
app_name = "bookclub_site"
create_react_app(app_name)
