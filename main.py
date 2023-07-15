import streamlit as st 
import streamlit.components.v1 as components
from PIL import Image
from streamlit_timeline import timeline
import pandas as pd
import webbrowser
from bokeh.models.widgets import Div
from streamlit_elements import elements, mui, html, sync



st.set_page_config(page_title='Sheldon.ai', page_icon='🧊', layout="wide",initial_sidebar_state="expanded")

with st.sidebar:
    image = Image.open("static/forweb.jpg")
    st.image(image, width = 200)
    st.title("Sheldon ")
    components.html('<script src="https://platform.linkedin.com/badges/js/profile.js" async defer type="text/javascript"></script><div class="badge-base LI-profile-badge" data-locale="en_US" data-size="medium" data-theme="dark" data-type="VERTICAL" data-vanity="vipulchaube" data-version="v1"><a class="badge-base__link LI-simple-link" href="https://in.linkedin.com/in/vipulchaube?trk=profile-badge"></a></div>', height = 310 )
    # if st.button("Linkedin 🧑‍💼"):
    #   js = "window.open('https://www.linkedin.com/in/vipulchaube/')"  # New tab or window
    #   html = '<img src onerror="{}">'.format(js)
    #   div = Div(text=html)
    #   st.bokeh_chart(div)  
    if st.button("Github 👨‍💻"):
      js = "window.open('https://github.com/harshit-wadhwani')"  # New tab or window
      html = '<img src onerror="{}">'.format(js)
      div = Div(text=html)
      st.bokeh_chart(div)  
    with open("static/reliance-annual-report-21.pdf", "rb") as file:
        btn = st.download_button(
                label="Download Resume 📥",
                data=file,
                file_name="static/reliance-annual-report-21.pdf"
            )
col1, col2, col3 = st.columns(3)
with col1:
  st.latex(r"\big( \Big( \bigg( \Bigg(")
with col2:     
  st.title ("{me}:genie:")
with col3:
  st.latex(r"\big) \Big) \bigg) \Bigg)")
st.write("Meet Sheldon, your adorable yet highly professional virtual assistant! With an endearing personality and a wealth of knowledge, Sheldon is here to help you conquer your tasks with a touch of charm and efficiency.")

st.title ("Build on ⚒️")
col1, col2, col3 = st.columns(3)

with col1:
    st.button('Python')
    st.button('Streamlit')
    
with col2:
    st.button("Mongodb")
    st.button('Pinecone')

with col3:
    st.button("OpenAI")
    st.button('HuggingFace')

json = [{'provider': 'HuggingfaceHubProvider',
  'name': 'hf_pythia',
  'cost': {'full': 'OpenAssistant/oasst-sft-4-pythia-12b-epoch-3.5',
   'prompt': 0,
   'completion': 0,
   'token_limit': 2048}},
 {'provider': 'HuggingfaceHubProvider',
  'name': 'hf_mptinstruct',
  'cost': {'full': 'mosaicml/mpt-7b-instruct',
   'prompt': 0,
   'completion': 0,
   'token_limit': 2048}},
 {'provider': 'HuggingfaceHubProvider',
  'name': 'hf_mptchat',
  'cost': {'full': 'mosaicml/mpt-7b-chat',
   'prompt': 0,
   'completion': 0,
   'token_limit': 2048}},
 {'provider': 'HuggingfaceHubProvider',
  'name': 'hf_llava',
  'cost': {'full': 'liuhaotian/LLaVA-Lightning-MPT-7B-preview',
   'prompt': 0,
   'completion': 0,
   'token_limit': 2048}},
 {'provider': 'HuggingfaceHubProvider',
  'name': 'hf_dolly',
  'cost': {'full': 'databricks/dolly-v2-12b',
   'prompt': 0,
   'completion': 0,
   'token_limit': -1}},
 {'provider': 'OpenAIProvider',
  'name': 'gpt-3.5-turbo',
  'cost': {'prompt': 2.0, 'completion': 2.0, 'token_limit': 4000}},
 {'provider': 'AnthropicProvider',
  'name': 'claude-instant-v1.1',
  'cost': {'prompt': 1.63, 'completion': 5.51, 'token_limit': 9000}},
 {'provider': 'AnthropicProvider',
  'name': 'claude-instant-v1',
  'cost': {'prompt': 1.63, 'completion': 5.51, 'token_limit': 9000}},
 {'provider': 'AlephAlphaProvider',
  'name': 'luminous-base',
  'cost': {'prompt': 6.6, 'completion': 7.6, 'token_limit': 2048}},
 {'provider': 'AI21Provider',
  'name': 'j2-grande-instruct',
  'cost': {'prompt': 10.0, 'completion': 10.0, 'token_limit': 8192}},
 {'provider': 'AlephAlphaProvider',
  'name': 'luminous-extended',
  'cost': {'prompt': 9.9, 'completion': 10.9, 'token_limit': 2048}},
 {'provider': 'AI21Provider',
  'name': 'j2-jumbo-instruct',
  'cost': {'prompt': 15.0, 'completion': 15.0, 'token_limit': 8192}},
 {'provider': 'OpenAIProvider',
  'name': 'text-davinci-003',
  'cost': {'prompt': 20.0, 'completion': 20.0, 'token_limit': 4097}},
 {'provider': 'AnthropicProvider',
  'name': 'claude-v1',
  'cost': {'prompt': 11.02, 'completion': 32.68, 'token_limit': 9000}},
 {'provider': 'CohereProvider',
  'name': 'command',
  'cost': {'prompt': 25.0, 'completion': 25, 'token_limit': 2048}},
 {'provider': 'CohereProvider',
  'name': 'command-nightly',
  'cost': {'prompt': 25.0, 'completion': 25, 'token_limit': 4096}},
 {'provider': 'AlephAlphaProvider',
  'name': 'luminous-supreme',
  'cost': {'prompt': 38.5, 'completion': 42.5, 'token_limit': 2048}},
 {'provider': 'OpenAIProvider',
  'name': 'gpt-4',
  'cost': {'prompt': 30.0, 'completion': 60.0, 'token_limit': 8000}},
 {'provider': 'AlephAlphaProvider',
  'name': 'luminous-supreme-control',
  'cost': {'prompt': 48.5, 'completion': 53.6, 'token_limit': 2048}}]


st.title ("Connected to ⚒️")

col1, col2, col3 = st.columns(3)  

for index, entry in enumerate(json):
    provider = entry['provider']
    name = entry['name']
    cost = entry['cost']
    full_cost = cost.get('full', 'Not available')
    prompt_cost = cost['prompt']
    completion_cost = cost['completion']
    token_limit = cost['token_limit']
    
    if index % 3 == 0:
        column = col1
    elif index % 3 == 1:
        column = col2
    else:
        column = col3

    with column:
        st.write("Provider:", provider)
        st.write("Name:", name)
        st.write("Full Cost:", full_cost)
        st.write("Prompt Cost:", prompt_cost)
        st.write("Completion Cost:", completion_cost)
        st.write("Token Limit:", token_limit)
        st.write("-----")


#Capabilities
IMAGES = [
    "https://static.startuptalky.com/2022/12/OpenAI-startuptalky.jpg",
    "https://images.squarespace-cdn.com/content/v1/56e2e0c520c6472a2586add2/1593683608007-L71NCKC2O54GFBHPB0W9/CP%2BLogos%2B2%2B%25288%2529.jpg?format=1500w",
    "https://cdn.tech.eu/uploads/2021/08/al-1-1536x672.jpg",
    "https://techcrunch.com/wp-content/uploads/2023/04/anthropic-header.jpg?w=1390&crop=1",
    "https://martechseries.com/wp-content/uploads/2023/04/AI21-Labs-Integrates-Generative-AI-Capabilities-into-Google-Docs_-Enhancing-the-Writing-Experience-for-Hundreds-of-Millions-of-People-Around-the-World-750x430.png",
    "https://txt.cohere.com/content/images/size/w2000/2023/06/C-Blog-Post-4x-pink--1-.png",
]


def slideshow_swipeable(images):
    # Generate a session state key based on images.
    key = f"slideshow_swipeable_{str(images).encode().hex()}"

    # Initialize the default slideshow index.
    if key not in st.session_state:
        st.session_state[key] = 0

    # Get the current slideshow index.
    index = st.session_state[key]

    # Create a new elements frame.
    with elements(f"frame_{key}"):

        # Use mui.Stack to vertically display the slideshow and the pagination centered.
        # https://mui.com/material-ui/react-stack/#usage
        with mui.Stack(spacing=2, alignItems="center"):

            # Create a swipeable view that updates st.session_state[key] thanks to sync().
            # It also sets the index so that changing the pagination (see below) will also
            # update the swipeable view.
            # https://mui.com/material-ui/react-tabs/#full-width
            # https://react-swipeable-views.com/demos/demos/
            with mui.SwipeableViews(index=index, resistance=True, onChangeIndex=sync(key)):
                for image in images:
                    html.img(src=image, css={"width": "100%"})

            # Create a handler for mui.Pagination.
            # https://mui.com/material-ui/react-pagination/#controlled-pagination
            def handle_change(event, value):
                # Pagination starts at 1, but our index starts at 0, explaining the '-1'.
                st.session_state[key] = value-1

            # Display the pagination.
            # As the index value can also be updated by the swipeable view, we explicitely
            # set the page value to index+1 (page value starts at 1).
            # https://mui.com/material-ui/react-pagination/#controlled-pagination
            mui.Pagination(page=index+1, count=len(images), color="primary", onChange=handle_change)

st.subheader("Swipeable slideshow")
slideshow_swipeable(IMAGES)

#Certification
st.title("Solving User Problems")

col1, col2, col3 = st.columns(3)

with col1:
  if st.button('Question a PDF'):
    #webbrowser.open('https://www.coursera.org/account/accomplishments/certificate/ZHMGLQXRRSSG')
    js = "window.open('https://www.coursera.org/account/accomplishments/certificate/ZHMGLQXRRSSG')"  # New tab or window
    html = '<img src onerror="{}">'.format(js)
    div = Div(text=html)
    st.bokeh_chart(div)   
  if st.button("Question CSV"):
    #webbrowser.open('https://www.coursera.org/account/accomplishments/certificate/PWNWHE3NX2PN')
    js = "window.open('https://www.coursera.org/account/accomplishments/certificate/PWNWHE3NX2PN')"  # New tab or window
    html = '<img src onerror="{}">'.format(js)
    div = Div(text=html)
    st.bokeh_chart(div)     
  
  
with col2:
  if st.button("Question Database"):
    #webbrowser.open('https://www.coursera.org/account/accomplishments/certificate/CTZFB8SVEQA8')
    js = "window.open('https://www.coursera.org/account/accomplishments/certificate/CTZFB8SVEQA8')"  # New tab or window
    html = '<img src onerror="{}">'.format(js)
    div = Div(text=html)
    st.bokeh_chart(div)     
  if st.button('Own your data'):
    #webbrowser.open('https://www.coursera.org/account/accomplishments/certificate/NTDLB8L2VLFB')
    js = "window.open('https://www.coursera.org/account/accomplishments/certificate/NTDLB8L2VLFB')"  # New tab or window
    html = '<img src onerror="{}">'.format(js)
    div = Div(text=html)
    st.bokeh_chart(div)     
with col3:
  if st.button("Chatbots about ur website"):
    #webbrowser.open('https://www.coursera.org/account/accomplishments/certificate/EEBXPHDN2NSL')
    js = "window.open('https://www.coursera.org/account/accomplishments/certificate/EEBXPHDN2NSL')"  # New tab or window
    html = '<img src onerror="{}">'.format(js)
    div = Div(text=html)
    st.bokeh_chart(div) 
  if st.button('Hosted Vector Db'):
    #webbrowser.open("https://www.coursera.org/account/accomplishments/certificate/28MEE66PT68D")
    js = "window.open('https://www.coursera.org/account/accomplishments/certificate/28MEE66PT68D')"  # New tab or window
    html = '<img src onerror="{}">'.format(js)
    div = Div(text=html)
    st.bokeh_chart(div)     


#Certification
st.title("Solving Industry Problems")

col1, col2, col3 = st.columns(3)

with col1:
  if st.button('Hallucination'):
    #webbrowser.open('https://www.coursera.org/account/accomplishments/certificate/ZHMGLQXRRSSG')
    js = "window.open('https://www.coursera.org/account/accomplishments/certificate/ZHMGLQXRRSSG')"  # New tab or window
    html = '<img src onerror="{}">'.format(js)
    div = Div(text=html)
    st.bokeh_chart(div)   
  if st.button("Private"):
    #webbrowser.open('https://www.coursera.org/account/accomplishments/certificate/PWNWHE3NX2PN')
    js = "window.open('https://www.coursera.org/account/accomplishments/certificate/PWNWHE3NX2PN')"  # New tab or window
    html = '<img src onerror="{}">'.format(js)
    div = Div(text=html)
    st.bokeh_chart(div)     
  
  
with col2:
  if st.button("Customized"):
    #webbrowser.open('https://www.coursera.org/account/accomplishments/certificate/CTZFB8SVEQA8')
    js = "window.open('https://www.coursera.org/account/accomplishments/certificate/CTZFB8SVEQA8')"  # New tab or window
    html = '<img src onerror="{}">'.format(js)
    div = Div(text=html)
    st.bokeh_chart(div)     
  if st.button('Bepoke'):
    #webbrowser.open('https://www.coursera.org/account/accomplishments/certificate/NTDLB8L2VLFB')
    js = "window.open('https://www.coursera.org/account/accomplishments/certificate/NTDLB8L2VLFB')"  # New tab or window
    html = '<img src onerror="{}">'.format(js)
    div = Div(text=html)
    st.bokeh_chart(div)     
with col3:
  if st.button("Self Trained"):
    #webbrowser.open('https://www.coursera.org/account/accomplishments/certificate/EEBXPHDN2NSL')
    js = "window.open('https://www.coursera.org/account/accomplishments/certificate/EEBXPHDN2NSL')"  # New tab or window
    html = '<img src onerror="{}">'.format(js)
    div = Div(text=html)
    st.bokeh_chart(div) 
  if st.button('Professional'):
    #webbrowser.open("https://www.coursera.org/account/accomplishments/certificate/28MEE66PT68D")
    js = "window.open('https://www.coursera.org/account/accomplishments/certificate/28MEE66PT68D')"  # New tab or window
    html = '<img src onerror="{}">'.format(js)
    div = Div(text=html)
    st.bokeh_chart(div)     

st.title('Testimonials')
st.subheader('Data Analysis at a finger-tip')
st.write('Disecting IPL Audience Analytics (Joseph Eapen) · Jun 12, 2023')
st.write('TThe Indian Premier League (IPL) has emerged as one of the most captivating and widely followed sporting events globally, attracting millions of fans each season. Behind the thrilling matches and electrifying atmosphere lies a wealth of valuable data waiting to be explored. By dissecting IPL audience analytics, we can unravel fascinating insights into viewer preferences, engagement patterns, and demographic trends, ultimately unlocking the key to a more targeted and impactful fan experience. From understanding the most popular teams and players to identifying viewership patterns across different regions, the analysis of IPL audience data presents a treasure trove of information for teams, broadcasters, and advertisers alike. By harnessing the power of advanced analytics techniques, we can paint a detailed picture of the IPLs passionate fan base, enabling stakeholders to make data-driven decisions and create an even more captivating and immersive cricketing spectacle.')
if st.button("Show Publication"):
  #webbrowser.open('https://www.technoarete.org/common_abstract/pdf/IJERCSE/v9/i12/Ext_50731.pdf')
  js = "window.open('https://www.technoarete.org/common_abstract/pdf/IJERCSE/v9/i12/Ext_50731.pdf')"  # New tab or window
  html = '<img src onerror="{}">'.format(js)
  div = Div(text=html)
  st.bokeh_chart(div)
  # st.bokeh_chart(open_link('https://www.technoarete.org/common_abstract/pdf/IJERCSE/v9/i12/Ext_50731.pdf'))

  
st.header(":mailbox: Get In Touch With Me!")


contact_form = """
<form action="https://formsubmit.co/YOUREMAIL@EMAIL.COM" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your message here"></textarea>
     <button type="submit">Send</button>
</form>
"""

st.markdown(contact_form, unsafe_allow_html=True)

# Use Local CSS File
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")