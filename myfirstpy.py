from flask import Flask, render_template, request, render_template_string
import random

app = Flask(__name__)

@app.route("/")  
def helloworld():
    return "Hello, World!"

@app.route("/stat")  
def hellostat():
    return "Hello, STAT KKU!"

@app.route("/research")
def research_page():
    faculty_research = {
    "Dr. Alice Smith": [
        "Statistical Modeling of Climate Change Impacts",
        "Advanced Methods in Time Series Analysis",
        "Machine Learning Applications in Biostatistics",
    ],
    "Dr. Bob Johnson": [
        "Bayesian Inference in Social Sciences",
        "Quantitative Analysis of Economic Trends",
        "Development of Robust Statistical Software",
    ],
    "Dr. Carol Davis": [
        "Optimization Techniques in Big Data Analytics",
        "Statistical Approaches to Epidemiology",
        "Survey Data Analysis for Policy Decisions",
    ],
    }

    faculty, research_projects = random.choice(list(faculty_research.items()))
    
    return render_template("research.html", faculty=faculty, research_projects=research_projects)


@app.route('/contact',methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        user_email = request.form.get("email")
        with open ("email.txt", "a") as myfile:
            myfile.write(f'{user_email}\n')
        return render_template_string("""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Contact Us</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    margin: 0;
                    padding: 0;
                    background-color: #f9f9f9;
                    color: #333;
                }
                header {
                    background-color: #0078d7;
                    color: white;
                    text-align: center;
                    padding: 1rem 0;
                }
                main {
                    padding: 2rem;
                    max-width: 600px;
                    margin: auto;
                    text-align: left;
                    background: white;
                    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
                    border-radius: 8px;
                }
                h1 {
                    color: #005ea6;
                }
                p {
                    line-height: 1.6;
                }
                footer {
                    text-align: center;
                    margin-top: 2rem;
                    font-size: 0.9rem;
                    color: #666;
                }
            </style>
        </head>
        <body>
            <header>
                <h1>Contact Us</h1>
            </header>
            <main>
                <h2>Admin Contact Details</h2>
                <p><strong>Name:</strong> John Doe</p>
                <p><strong>Email:</strong> admin@example.com</p>
                <p><strong>Phone:</strong> +1-234-567-890</p>
                <p>If you have any questions or need assistance, please don’t hesitate to reach out. Our admin is here to help you!</p>
                <h2>Thank you {{user}}</h2>
                <h2><a href="/statHTML>Home</a> <h2>
            </main>
            <footer>
                <p>&copy; 2025 Stat KKU. All rights reserved.</p>
            </footer>
        </body>
        </html>
        """,user=user_email)
    else:
        return """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Contact Us</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    margin: 0;
                    padding: 0;
                    background-color: #f9f9f9;
                    color: #333;
                }
                header {
                    background-color: #0078d7;
                    color: white;
                    text-align: center;
                    padding: 1rem 0;
                }
                main {
                    padding: 2rem;
                    max-width: 600px;
                    margin: auto;
                    text-align: left;
                    background: white;
                    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
                    border-radius: 8px;
                }
                h1 {
                    color: #005ea6;
                }
                p {
                    line-height: 1.6;
                }
                footer {
                    text-align: center;
                    margin-top: 2rem;
                    font-size: 0.9rem;
                    color: #666;
                }
            </style>
        </head>
        <body>
            <header>
                <h1>Contact Us</h1>
            </header>
            <main>
                <h2><a href="/statHTML">Admin</a> Contact Details</h2>
                <p><strong>Name:</strong> John Doe</p>
                <p><strong>Email:</strong> admin@example.com</p>
                <p><strong>Phone:</strong> +1-234-567-890</p>
                <p>If you have any questions or need assistance, please don’t hesitate to reach out. Our admin is here to help you!</p>
                <h2>Submit Your Email So We Can Contact You Back</h2>
                <form method="POST">
                    <label for="email">Your Email:</label>
                    <input type="email" id="email" name="email" required placeholder="Enter your email">
                    <button type="submit">Submit</button>
                </form>
            </main>
            <footer>
                <p>&copy; 2025 Stat KKU. All rights reserved.</p>
            </footer>
        </body>
        </html>
        """

@app.route("/statHTML") 
def helloSTAThtml():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Stat KKU - Homepage</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
                background-color: #f4f4f9;
                color: #333;
            }
            header {
                background-color: #0078d7;
                color: white;
                padding: 1rem 0;
                text-align: center;
            }
            nav {
                background-color: #005ea6;
                display: flex;
                justify-content: center;
                padding: 0.5rem 0;
            }
            nav a {
                color: white;
                text-decoration: none;
                margin: 0 1rem;
            }
            nav a:hover {
                text-decoration: underline;
            }
            main {
                padding: 2rem;
                text-align: center;
            }
            footer {
                background-color: #0078d7;
                color: white;
                text-align: center;
                padding: 1rem 0;
                position: fixed;
                bottom: 0;
                width: 100%;
            }
        </style>
    </head>
    <body>
        <header>
            <h1>Welcome to Stat KKU</h1>
            <p>Department of Statistics, Khon Kaen University</p>
        </header>
        <nav>
            <a href="#about">About Us</a>
            <a href="#programs">Programs</a>
            <a href="/research">Research</a>
            <a href="/contact">Contact</a>
        </nav>
        <main>
            <section id="about">
                <h2>About Us</h2>
                <p>The Department of Statistics at Khon Kaen University is dedicated to excellence in teaching and research in the field of statistics.</p>
            </section>
                <p>Welcome to <strong>[Your Company Name]</strong>, where innovation meets passion. We are a team of dedicated professionals driven by the desire to create meaningful solutions that make a difference. Since our inception, our mission has been to empower individuals and businesses to achieve their goals through cutting-edge technologies and services.</p>
                <p>At <strong>[Your Company Name]</strong>, we believe that success is a journey, not a destination. That’s why we are committed to continuous learning, adapting, and evolving with the ever-changing landscape of the industries we serve. Our team works tirelessly to stay ahead of trends and deliver solutions that are both effective and forward-thinking.</p>
                <p>We pride ourselves on fostering an environment of inclusivity and collaboration. Our diverse team brings together unique perspectives and skills, which allow us to tackle challenges creatively and efficiently. By embracing diversity, we ensure that our solutions resonate with people from all walks of life.</p>
                <p>Integrity is at the core of everything we do. We build trust by delivering on our promises and maintaining transparency in all our interactions. This unwavering commitment to ethical practices is what has earned us the loyalty of our clients and partners over the years.</p>
                <p>Innovation drives our work. From developing advanced technologies to streamlining processes, we constantly push the boundaries of what’s possible. Our solutions are designed to be not only functional but also transformative, helping our clients stay competitive in their respective markets.</p>
                <p>Sustainability is a value we hold dear. As we innovate, we remain conscious of our impact on the environment. We are committed to adopting sustainable practices in our operations and encouraging our clients and partners to do the same. Together, we strive to create a better future for generations to come.</p>
                <p>We value our clients as partners in our journey. Your success is our success, and we go above and beyond to understand your needs and aspirations. By tailoring our services to meet your specific requirements, we ensure that you receive the best possible outcomes.</p>
                <p>Our team is our greatest asset. Each member brings expertise, creativity, and dedication to the table, contributing to a vibrant and dynamic workplace. We invest in our people through training and development, ensuring that they are equipped to thrive and excel.</p>
                <p>Giving back to the community is an integral part of our identity. Through various initiatives and partnerships, we aim to make a positive impact in the lives of those around us. Whether it’s supporting local charities or mentoring young talent, we believe in using our resources to uplift others.</p>
                <p>As we look to the future, we remain steadfast in our commitment to excellence. We are excited to continue serving our clients, growing our partnerships, and making a difference in the world. Thank you for being a part of our journey – together, we can achieve incredible things.</p>
            <section id="programs">
                <h2>Programs</h2>
                <p>We offer undergraduate and postgraduate programs in statistics to prepare students for successful careers.</p>
            </section>
            <section id="research">
                <h2>Research</h2>
                <p>Our faculty members are engaged in cutting-edge research to address real-world challenges using statistical methods.</p>
            </section>
            <section id="contact">
                <h2>Contact</h2>
                <p>Email: info@statkku.ac.th</p>
                <p>Phone: +66-1234-5678</p>
            </section>
        </main>
        <footer>
            <p>&copy; 2025 Stat KKU. All rights reserved.</p>
        </footer>
    </body>
    </html>
    """

if __name__ == "__main__":   # run code 
    app.run() # more ip and port like app.run(host='0.0.0.0',debug=True,port=5001)#host='0.0.0.0' = run on internet ,port=5001