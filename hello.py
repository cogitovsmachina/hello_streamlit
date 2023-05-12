import streamlit as st

st.title('My Portfolio')
page = st.sidebar.selectbox("Choose a page", ["Homepage", "Projects", "About Me"])

if page == "Homepage":
    st.header("Welcome to my personal portfolio website!")
    st.subheader("This is a brief introduction about myself and the work I do.")
    #st.image("path_to_your_image.jpg")  # add a picture if you'd like

elif page == "Projects":
    st.header("My Projects")
    st.markdown("## Project 1")
    st.markdown("Description about Project 1")
    st.markdown("## Project 2")
    st.markdown("Description about Project 2")

elif page == "About Me":
    st.header("About Me")
    st.markdown("## Education")
    st.markdown("Details about your education")
    st.markdown("## Experience")
    st.markdown("Details about your work experience")



st.markdown("### Enrique Diaz")
st.markdown("# Machine Learning Sensei")

st.markdown("## Machine Learning Engineer and Startup junki3")
st.markdown("""
    
    ### Hi there fellow hacker! 👋👋

    I'm Enrique (<i>aka Kike</i>) a self-taught computer science enthusiast with experience in learning communities. 
    I'm a Co-founder and Machine Learning Engineer at the DEVF, 
  where I co-lead the Data Science and Artificial Intelligence team of Senseis and code prototipes in order to 
  apply Machine Learning Algorithms. I'm passionate about building communities, empower others and create opportunities
   for those who cannot afford or be able to get access to high quality education.

""")

with st.container():
    image_col, text_col = st.columns((1,2))
    with image_col:
        st.image("https://cdn-images-1.medium.com/max/906/1*dVSDol9pouoO9IX_E_-35Q.png")

    with text_col:
        st.subheader("A Multi-page Interactive Dashboard with Streamlit and Plotly")
        st.write("""Beautiful interactive multipage dashboards are made easy with Streamlit
            """)
        st.markdown("[Read more...](https://towardsdatascience.com/a-multi-page-interactive-dashboard-with-streamlit-and-plotly-c3182443871a)")

with st.container():
    image_col, text_col = st.columns((1,2))
    with image_col:
        st.image("https://cdn-images-1.medium.com/max/906/1*hjhCIWGgLzOznTFwDyeIeA.png")

    with text_col:
        st.subheader("Rational UI Design with Streamlit")
        st.write("""
            From one point of view Streamlit is a retrograde step in web development because 
            it lets you mix up the logic of your app with the way it is presented. But from 
            another it is very much simplifying web design.""")
        st.markdown("[Read more...](https://towardsdatascience.com/rational-ui-design-with-streamlit-61619f7a6ea4)")
