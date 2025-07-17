import streamlit as st
import base64

# ---- PAGE CONFIG ----
st.set_page_config(page_title="Kamlesh Zore", layout="wide")

# ---- CSS STYLES ----
st.markdown("""
    <style>
        .stApp {
            background-color: #f2f6fb;
            font-family: 'Segoe UI', sans-serif;
            padding-top: 30px;
        }
        .profile-img {
            border-radius: 50%;
            width: 180px;
            height: 180px;
            object-fit: cover;
            border: 5px solid #dbe9f4;
        }
        .download-button {
            display: inline-block;
            background-color: #1a73e8;
            color: white;
            padding: 0.5em 1.5em;
            border-radius: 6px;
            text-decoration: none;
            font-weight: bold;
            margin-top: 10px;
        }
        .download-button:hover {
            background-color: #1558b0;
        }
        .email {
            font-size: 16px;
            margin-top: 10px;
            margin-bottom: 15px;
        }
        .social-links a {
            margin: 0 15px;
            font-size: 16px;
            color: #1a73e8;
            text-decoration: none;
            font-weight: bold;
        }
        .social-links a:hover {
            text-decoration: underline;
        }
    </style>
""", unsafe_allow_html=True)

# ---- PDF DOWNLOAD FUNCTION ----
def get_pdf_download_link(pdf_file):
    with open(pdf_file, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode("utf-8")
    href = f'<a class="download-button" href="data:application/octet-stream;base64,{base64_pdf}" download="Kamlesh_Zore_Resume.pdf">📄 Download Resume</a>'
    return href

# ---- TOP LAYOUT ----
col1, col2 = st.columns([1, 2])

with col1:
    # st.markdown('<img src="profile.jpg" class="profile-img">', unsafe_allow_html=True)
    st.markdown('<div class="profile-img-wrapper">', unsafe_allow_html=True)
    st.image("profile.jpg", width=300)
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown("## Kamlesh Zore")
    st.markdown("""
    **Senior Data Analyst**  
    Power BI | Python | SQL | Advance Excel


    """)
    st.markdown(get_pdf_download_link("Untitled (5).pdf"), unsafe_allow_html=True)
    st.markdown('<div class="email">📬 <a href="mailto:kamleshzore5@gmail.com">kamleshzore5@gmail.com</a></div>', unsafe_allow_html=True)
    st.markdown('<div class="email">📬 <a href="https://www.linkedin.com/in/kamlesh-zore-196117109/" target="_blank">LinkedIn</a></div>',unsafe_allow_html=True)

# ---- SOCIAL LINKS ----
# st.markdown("""
# <div class="social-links" style="text-align: center; margin-top: 30px;">
#     <a href="https://www.linkedin.com/in/kamleshzore" target="_blank">LinkedIn</a>
#     <a href="https://github.com/yourgithub" target="_blank">GitHub</a>
#     <a href="https://twitter.com/yourtwitter" target="_blank">Twitter</a>
#     <a href="https://youtube.com/yourchannel" target="_blank">YouTube</a>
# </div>
# """, unsafe_allow_html=True)


# --- MAIN CONTENT ---
# st.title("📄 Resume - Kamlesh Zore")

st.header("🧠 Professional Summary")
st.markdown("""
Dynamic and results-driven Analytics Professional with over 3 + years of experience across ERP, Audit, and
E-commerce domains. Proven expertise in leveraging Power BI to transform complex datasets into actionable insights. Adept at managing end-to-end reporting processes, including data integration, cleaning, modeling, and visualization.
Proficient in Python, SQL, and Power Apps, with advanced knowledge of Excel to automate processes and optimize workflows. Demonstrates exceptional analytical, project management, and client-handling skills, coupled with a passion for learning new technologies.
""")

st.header("🛠️ Skills")
cols = st.columns(2)
with cols[0]:
    st.markdown("""
    - Data Visualization  
    - Data Cleaning & Modeling  
    - KPI Calculation  
    - End-to-End Dashboard Development  
    - Project & Time Management
    """)
with cols[1]:
    st.markdown("""
    - Programming & Automation  
    - Client & Stakeholder Communication  
    - Collaboration & Reporting  
    - Data Management  
    - Industry Expertise
    """)

st.header("💼 Employment History")
st.markdown("""
**Sr. Data Analyst | A A Garg & Co | 2022 – Present | Mumbai**  
- Designed and implemented Power BI dashboards by importing and preparing data from Python, SQL Server, and other sources, delivering impactful insights to clients 
- Automated MIS reports using advanced Excel techniques, significantly reducing manual effort and increasing efficiency.  
- Published Power BI reports to the server, set up scheduled refreshes, and ensured secure client access via embedded reports. 
- Managed IT administration tasks, ensuring seamless operations and adherence to organizational standards. 

**Data Science Intern | iNeuron | 2021 (1 Month)**  
- Built ML models using domain-specific datasets 

**Project Coordinator / Sales Engineer | Rajiv Plastic Industries | 2021 – 2022**  
- Successfully handled multiple clients and on-field marketing personnel, involved in implementing new sales and marketing strategies. 

**Inside Sales Executive | AIC Lab Equipment | 2020 (4 Months)**  
- Achieved targeted sales as inside sales executive  

**Project Engineer | Visual Mitra | 2019 – 2020**  
- Executed visual management projects  

**Project Coordinator | Hilda Automation | 2016 – 2018**  
- Delivered end-to-end beverage project solutions
""")

st.header("🎓 Education")
st.markdown("- **Bachelor of Engineering (B.E.) in Mechanical Engineering – 2016**")

st.header("📁 Projects")
st.markdown("""
**Automated BOT Using Python**  
- Utilized Python libraries (Selenium, webdriver-manager, reportlab, BeautifulSoup) to develop an automated bot. 
- Consolidated client data and facilitated uploads to government portals.
- Extracted data from government portals, including Plastic Waste Management, Battery Waste Management, and E-Waste Management 

**Plastic Footprint Dashboard (P&G India)**  
- Analyzed raw client data and implemented data cleaning activities in Power BI.
- Developed KPIs to assess product SKUs and recycling metrics per the client’s business model.
- Created an interactive dashboard enabling state-wise insights and a summary deck for stakeholder presentations.

**EPR Dashboard (Mondelez)**  
- Collaborated with clients to gather technical and business requirements.
- Conducted data cleaning and modeling in Power BI to calculate key KPIs.
- Delivered a dashboard enabling stakeholders to monitor agent performance and ensure compliance with targets.  

**Plastic Footprint Dashboard (Japan)**  
- Processed raw data using Python for backend logic and Flask for data upload functionality.  
- Developed a Power BI dashboard summarizing results and generating downloadable reports.

**MIS Report Automation (Faces Canada)**  
- Cleaned and merged data from over 20 sources, including sales data and client mapping sheets.
- Built Python-based bots to scrape e-commerce portal data and implemented backend logic.
- Created comprehensive dashboards with pivots, charts, and matrix views, incorporating row-level security
""")
