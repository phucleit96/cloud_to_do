import streamlit as st

# Title of the application
st.title('Streamlit Demo')

# Add a sidebar
st.sidebar.title('Navigation')

st.image(image="fulllogo.png", width=300)
# Add a selectbox to the sidebar
options = ['Home', 'About', 'Contact']
choice = st.sidebar.selectbox('Choose a page', options)

# Display different page based on the choice
if choice == 'Home':
    st.subheader('Welcome to the Home Page')
    st.write('This is a simple Streamlit application.')
elif choice == 'About':
    st.subheader('About Page')
    st.write('This application is built with Streamlit by Phuc Proton.')
elif choice == 'Contact':
    st.subheader('Contact Page')
    st.write('You can contact us at phuc.le.it96@gmail.com.')