from app import app
from database import db, Job

with app.app_context():

    Job.query.delete()

    jobs = [

        Job(
            title="Frontend Developer",
            company="Infosys",
            location="Hyderabad",
            salary="₹6 LPA",
            experience="0-2 Years",
            education="B.Tech / MCA",
            skills="React, HTML, CSS, JavaScript",
            description="Develop modern responsive web applications using React and frontend technologies.",
            requirements="React, APIs, Responsive Design"
        ),

        Job(
            title="Python Developer",
            company="TCS",
            location="Bangalore",
            salary="₹7 LPA",
            experience="1-3 Years",
            education="B.Tech / MCA",
            skills="Python, Flask, SQL",
            description="Develop backend applications and REST APIs using Python.",
            requirements="Python, Flask, SQL"
        ),

        Job(
            title="Data Analyst",
            company="Accenture",
            location="Pune",
            salary="₹8 LPA",
            experience="0-2 Years",
            education="B.Tech / B.Sc",
            skills="Python, SQL, Power BI",
            description="Analyze business data and generate reports and dashboards.",
            requirements="SQL, Power BI, Excel"
        ),

        Job(
            title="AI ML Engineer",
            company="Wipro",
            location="Chennai",
            salary="₹10 LPA",
            experience="1-3 Years",
            education="B.Tech / MCA",
            skills="Machine Learning, Python, TensorFlow",
            description="Build AI models and machine learning systems.",
            requirements="TensorFlow, Python, Deep Learning"
        ),

        Job(
            title="Backend Developer",
            company="Capgemini",
            location="Noida",
            salary="₹8 LPA",
            experience="1-3 Years",
            education="B.Tech",
            skills="Node.js, MongoDB, Express",
            description="Build scalable backend APIs and server-side applications.",
            requirements="Node.js, MongoDB"
        ),

        Job(
            title="Cloud Engineer",
            company="IBM",
            location="Mumbai",
            salary="₹12 LPA",
            experience="2-4 Years",
            education="B.Tech",
            skills="AWS, Docker, Kubernetes",
            description="Manage cloud infrastructure and deployment pipelines.",
            requirements="AWS, Docker, Kubernetes"
        ),

        Job(
            title="Cyber Security Analyst",
            company="HCL",
            location="Hyderabad",
            salary="₹9 LPA",
            experience="1-3 Years",
            education="B.Tech",
            skills="Linux, Ethical Hacking, Networking",
            description="Monitor and protect systems against cyber threats.",
            requirements="Cyber Security, Linux"
        ),

        Job(
            title="DevOps Engineer",
            company="Oracle",
            location="Bangalore",
            salary="₹11 LPA",
            experience="2-4 Years",
            education="B.Tech",
            skills="Docker, Jenkins, CI/CD",
            description="Automate deployment and infrastructure processes.",
            requirements="DevOps, CI/CD"
        ),

        Job(
            title="Java Developer",
            company="Cognizant",
            location="Chennai",
            salary="₹7 LPA",
            experience="1-3 Years",
            education="B.Tech",
            skills="Java, Spring Boot, SQL",
            description="Develop enterprise Java applications.",
            requirements="Java, Spring Boot"
        ),

        Job(
            title="Full Stack Developer",
            company="Tech Mahindra",
            location="Pune",
            salary="₹9 LPA",
            experience="1-3 Years",
            education="B.Tech",
            skills="React, Node.js, MongoDB",
            description="Develop frontend and backend systems.",
            requirements="Full Stack Development"
        ),

        Job(
            title="UI/UX Designer",
            company="Zoho",
            location="Chennai",
            salary="₹6 LPA",
            experience="0-2 Years",
            education="Any Degree",
            skills="Figma, Adobe XD",
            description="Design modern and user-friendly interfaces.",
            requirements="UI Design, Wireframing"
        ),

        Job(
            title="Mobile App Developer",
            company="Paytm",
            location="Noida",
            salary="₹10 LPA",
            experience="1-3 Years",
            education="B.Tech",
            skills="Flutter, React Native",
            description="Develop mobile applications for Android and iOS.",
            requirements="Flutter, Mobile Development"
        ),

        Job(
            title="Business Analyst",
            company="Deloitte",
            location="Hyderabad",
            salary="₹8 LPA",
            experience="1-2 Years",
            education="MBA / B.Tech",
            skills="Excel, SQL, Power BI",
            description="Analyze business workflows and generate insights.",
            requirements="Analytics, Communication"
        ),

        Job(
            title="Software Tester",
            company="Mindtree",
            location="Bangalore",
            salary="₹5 LPA",
            experience="0-2 Years",
            education="B.Tech",
            skills="Testing, Selenium",
            description="Test software applications and report bugs.",
            requirements="Manual Testing, Automation"
        ),

        Job(
            title="Database Administrator",
            company="Infosys",
            location="Pune",
            salary="₹9 LPA",
            experience="2-4 Years",
            education="B.Tech",
            skills="SQL, Oracle",
            description="Manage and optimize enterprise databases.",
            requirements="SQL, Database Management"
        ),

        Job(
    title="System Administrator",
    company="Dell",
    location="Hyderabad",
    salary="₹7 LPA",
    experience="1-3 Years",
    education="B.Tech",
    skills="Linux, Networking, Servers",
    description="Manage and maintain enterprise IT infrastructure.",
    requirements="Linux, Networking"
),

Job(
    title="Blockchain Developer",
    company="Polygon",
    location="Remote",
    salary="₹15 LPA",
    experience="2-4 Years",
    education="B.Tech",
    skills="Solidity, Ethereum, Web3",
    description="Develop decentralized blockchain applications.",
    requirements="Blockchain, Smart Contracts"
),

Job(
    title="Game Developer",
    company="Ubisoft",
    location="Pune",
    salary="₹10 LPA",
    experience="1-3 Years",
    education="B.Tech",
    skills="Unity, C#, Unreal Engine",
    description="Design and develop interactive games.",
    requirements="Unity, Game Physics"
),

Job(
    title="Embedded Systems Engineer",
    company="Bosch",
    location="Bangalore",
    salary="₹9 LPA",
    experience="1-3 Years",
    education="B.Tech",
    skills="C, C++, Microcontrollers",
    description="Develop embedded software for hardware devices.",
    requirements="Embedded C, RTOS"
),

Job(
    title="Network Engineer",
    company="Cisco",
    location="Chennai",
    salary="₹8 LPA",
    experience="1-3 Years",
    education="B.Tech",
    skills="Networking, Routing, Switching",
    description="Configure and manage enterprise networks.",
    requirements="CCNA, Network Security"
),

Job(
    title="Site Reliability Engineer",
    company="Google",
    location="Bangalore",
    salary="₹18 LPA",
    experience="2-5 Years",
    education="B.Tech",
    skills="Linux, Kubernetes, Cloud",
    description="Ensure reliability and scalability of systems.",
    requirements="DevOps, Monitoring"
),

Job(
    title="Data Scientist",
    company="Amazon",
    location="Hyderabad",
    salary="₹14 LPA",
    experience="1-3 Years",
    education="B.Tech / MCA",
    skills="Python, Machine Learning, Pandas",
    description="Build predictive models and analyze large datasets.",
    requirements="ML, Data Analytics"
),

Job(
    title="AR VR Developer",
    company="Meta",
    location="Remote",
    salary="₹20 LPA",
    experience="2-4 Years",
    education="B.Tech",
    skills="Unity, ARCore, VR Development",
    description="Develop immersive AR and VR experiences.",
    requirements="Unity, 3D Graphics"
)

    ]

    db.session.add_all(jobs)

    db.session.commit()

    print("15 Jobs Added Successfully")