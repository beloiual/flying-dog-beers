from dash import Dash
import dash_core_components as dcc
import dash_html_components as html

from dash.dependencies import Input, Output, State
from dash_table import DataTable

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
colors = {
    'background': '#fbf9c7',
    'text': '#e5e9f0'
}


app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.Div([
        html.H1('Alexandru D. Beloiu - My Portfolio'),
    ], style=dict(textAlign='center')),

   
    html.Div([

        html.Div([
            html.H2('About Me'),
            html.Label('I am currently an undergraduate studying Computer Engineering at the University of Michigan Ann Arbor, set to graduate in 2024.'),
            html.Label('Over this past summer, I have been developing skills in creating BlockChain smart contracts using the Solidity programming language and deploying them to testnets. Along with increasing my grasp on the vast applications of Blockchain development, I have also been developing my skills in web development.'),
            html.Br(),
            html.H5('The website you are on right now was programmed completely by me using the Juypter Dash library in Python.'),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Label('______________________________________________________________________________________________________________________________________________________________________________'),
            ], className="seven columns", ),
          html.Div([
            
            html.Img(src='https://cdn.discordapp.com/attachments/705838282440835164/746767914270589098/image0.png', style={'width':'33%'}),
            html.Label("Email: beloiual@umich.edu"),
            html.Label("LinkedIn: Alexandru Beloiu"),
            html.Label("Instagram: alex.beloiu"),
            html.Br(),

        ], className="four columns"),

        html.Div([
            html.H2('My Education'),
            html.H4('University of Michigan, Ann Arbor: Computer Engineering (2020-Present)'),
            html.H4('Current Course Schedule (Fall 2020)'),
            html.Label('• EECS 203: Discrete Math'),
            html.Br(),
            html.Label('• Engr 151: Accelerated Introduction into Computers and Programming (C++)'),
            html.Br(),
            html.Label('• Engr 100: Gaming for the Greater Good'),
            html.Br(),
            html.H4('My Previous Education (Northville High School)'),
            html.Label('• GPA: 3.96'),
            html.Br(),
            html.Label('• Awards: National Merit Commended, Academic Excellence Award Recipient, National AP Scholar, Presidential Award, Summa Cum Laude, University of Michigan Regents Scholarship'),
            html.Br(),
            html.Label('• Relavent Coursework Completed: AP Computer Science A (JAVA), AP Computer Science Principles (Python), AP Calc AB, AP Calc BC, AP Physics-C (Mechanics), AP Physics-C (E&M), AP Chemistry'),
            html.Br(),
            html.Label('______________________________________________________________________________________________________________________________________________________________________________'),
            ], className="seven columns"),  
            html.Div([
              html.Br(),
              html.Br(),
              html.Img(src='https://cdn.discordapp.com/attachments/705838282440835164/746884075289051246/U-M-logo-preview.png', style={'width':'75%'}),        
              ], className="four columns"),
        html.Div([
            html.Br(),
            html.H2('My Relavent Experience'),
            html.H4('Blockchain at the University of Michigan (7/2020 - Present)'),
            html.Label('• Worked in a 4 person project team to create a fully functional proof of concept for a charity that is 100% transparent by using Blockchain technology and Python web development'),
            html.Br(),
            html.Label('• Within my group, I developed a Truffle box and wrote JavaScript code to successfully deploy the blockchain smart contract to both an Infura Node and a Truffle Sandbox connected to the Ropsten testnet. In addition to this, I further worked on linking the webapp to the deployed smart contract using the Python Web3 library. This project is further detailed in the Project section'),
            html.Br(),
            html.Br(), 
            html.H4('President of Software Engineering Club (9/2017 – 6/2020)'),
            html.Label('• Established the Software Engineering Club to provide members the opportunity to learn and enhance their computer programing skills by working collaboratively in a friendly team environment outside of the classroom'),
            html.Br(),
            html.Label('• Coordinated and oversaw regular meetings with club members and student leaders'),
            html.Br(),
            html.Label('• Mentored new members and tutored struggling students in C++, Visual Basic, Java and Python to help them become successful in computer science classes'),
            html.Br(),
            html.Label('• Created a successful 3D printing service for students to design in CAD and print out objects for individual use and charity events'),
            html.Br(),
            html.Br(),
            html.Label('______________________________________________________________________________________________________________________________________________________________________________'),
            html.Br(),
        ], className="ten columns", style=dict(textAlign='left')),
     
        html.Div([
            html.H1('My Projects'),
            html.Label('Over the past year, I have worked on a few distinct projects in multiple languages, including Python, Solidity and MATLAB.'),


        ], className="Ten columns"),
      
        html.Div([
            html.H3('CryptoCharity'),
            html.Img(src='https://cdn.discordapp.com/attachments/738150178153955339/739574691949314159/Crypto-2.png', style={'width':'33%'}),
            html.Br(),
            html.Br(),
            html.Label('My team and I created a proof of concept for a charity that is 100% transparent through the use Blockchain technology and Python Web development.'),
            html.Br(),
            html.Label('Achieved this goal by coding a Smart Contract in Solidity and deploying it to a testnet using Truffle.'),
            html.Br(),
            html.Label('Created a front-end website using the Dash and Web3 Python libraries which allowed us to transact Ether	between the Donator and the Charity and display transactions publicly using the Smart Contract.'),
            html.Br(),
            html.H5('Currently preparing to deploy a polished version of this project to Coinbase so real Ether can be transacted'),
            html.Br(),
            html.Br(),
            html.A(html.Button('Github Repository (Smart Contract)', className='thirteen columns', style=dict(textAlign='center')),
            href='https://github.com/GeorgeFane/metacoin-box'),
            html.Br(),
            html.A(html.Button('Github Repository (Web App)', className='thirteen columns', style=dict(textAlign='center')),
            href='https://github.com/GeorgeFane/metacoin-box'),
            html.Br(),
            html.Br(),


        ], className="three columns", style=dict(textAlign='center')),

        html.Div([
            html.H3('Modeling and Analysis of the Vibration of a Bridge'),
            html.Img(src='https://cdn.discordapp.com/attachments/705838282440835164/746906202755301456/unknown.png', style={'width':'33%'}),
            html.Br(),
            html.Br(),
            html.Label('Created a mathematical model of a simple bridge using a single degree of freedom mass-spring-damper system 		and derived a second order differential equation that models the oscillation of the bridge when an excitation force is applied.'),
            html.Br(),
            html.Label('Used MATLAB to help me solve the equation by hand and to produce multiple graphs to display the oscillation at resonance frequency which allowed me conclude that the best way to prevent the breakage of a bridge at 		resonance frequency is to have a large damping coefficient created by bridge dampeners.'),
            html.Br(),
            html.Br(),
            html.A(html.Button('Download', className='thirteen columns', style=dict(textAlign='center')),
            href='https://www.dropbox.com/s/t38t9gw2x2iavsi/Modeling%20and%20Analysis%20of%20Bridge%20Vibrations%20Main%20Document.docx?dl=0'),
            html.Br(),
            html.Br(),
        ], className="four columns", style=dict(textAlign='center')),
        html.Div([
            html.H3('This Website'),
            html.Img(src='https://cdn.discordapp.com/attachments/705838282440835164/746805658183270522/3wgIDj3j.png', style={'width':'33%'}),
                   
            html.Label('I created this website in order to act as a database for my personal projects and my experiences for future employers to see.'),
            html.Br(),
            html.Label('This website was created using the Jupyter Dash library in Python and was deployed using Heroku'),
            html.Br(),
            html.A(html.Button('Source Code', className='thirteen columns', style=dict(textAlign='center')),
            href='https://github.com/beloiual/PortfolioWebsite'),
             html.Br(),
            html.Br(),
            html.Br(),


        ], className="four columns", style=dict(textAlign='center')),


        html.Div([
           
            html.Br(),
            html.Br(),

            html.Br(),
            html.Label('______________________________________________________________________________________________________________________________________________________________________________'),
            html.Br(), 
            html.H1('Summer Research'),
            html.Label('Throughout the 2019 summer, I participated in Solar Cell research at UCLA and presented my findings to faculty.'),
            html.H3('University of California at Los Angeles (UCLA) - Applications of Nanoscience Summer Institute (Summer 2019)'), html.Img(src='https://cdn.discordapp.com/attachments/705838282440835164/746888986135363665/AATXAJwL8Df4luwycQ8Bfi7XxaLx7Ll2KyhnXI3d_TUvs900-c-k-c0xffffffff-no-rj-mo.png', style={'width':'10%'}),
            html.Label('• Conducted experimental research on improving the efficiency of dye-synthesized solar cells'),
            html.Br(),
            html.Label('• Fabricated solar cells using MgO, TiO2, and ZnO metal oxides along with dye, conductive glass, and fluorine'),
            html.Br(),
            html.Label('• Tested different combinations of oxides within the solar cell to determine the most efficient combination'),
            html.Br(),
            html.Label('• Presented research findings to an audience of UCLA faculty and PhD student mentors'),
            html.Br(),
            html.Br(),
            html.A(html.Button('Presentation of Research', className='thirteen columns'),
            href='https://docs.google.com/presentation/d/1Q-Y89N856EosrPXJvpV2HqX1c5y88jDctkOtvcjmvN0/edit?usp=sharing'),
            html.Label('______________________________________________________________________________________________________________________________________________________________________________'),
            html.Br(),

        ], className="ten columns", style=dict(textAlign='left')),

       html.Div([
                 html.H2('My Leadership Experience'),
       ], className="ten columns"),
       html.Div([
                 html.H4('Northville High School Track and Field Team Captain (11th-12th)'),
                 html.Label('• Responsible for leading practice, organizing team-building events, ensuring athletes participation, and helping new runners improve technique'),
                 html.Label('• Organized winter track conditioning throughout the off-season '),
                 html.Label('• Organized and participated in community service events by cooking and packaging Thanksgiving meals and purchasing, wrapping and distributing Christmas gifts to families in need'),
       ], className="five columns"),
       html.Div([
                 html.H4('Northville High School Cross Country Team Captain (12th)'),
                 html.Label('• Responsible for leading practice, assisting coaches, motivating the team, and mentoring younger members'),
                 html.Label('• Led and planned runs for summer conditioning '),
                 html.Label('• Created posters, and organized a team car wash fundraiser, raising $800 for new uniforms and equipment'),
                 

       ], className="five columns"),


       html.Div([
            html.Br(),
            html.Label('______________________________________________________________________________________________________________________________________________________________________________'),
            html.H2('My Skills'),
            html.Label('Technical Programming Skills: Proficient in Solidity, Truffle, Python, JAVA, C++, and MATLAB'),
            html.Br(),
            html.Label('Technical 3D Modeling Skills: Proficient in Autodesk Inventor and Google Sketch-Up'),


        ], className="ten columns"),
        

    ], className="row"),

    
])

if __name__ == '__main__':
    app.run_server()