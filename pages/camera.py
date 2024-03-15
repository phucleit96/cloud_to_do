import streamlit as st
from PIL import Image, ImageEnhance

# Title of the application
st.title('Camera Converter Application')
st.image(image="fulllogo.png", width=300)
with st.expander("Start Camera"):
    # Start the pages
    uploaded_image = st.file_uploader('Upload an image', type=["png", "jpg", "jpeg"])
    camera_image = st.camera_input('Camera')

# Add a selectbox for the user to choose the image mode

if uploaded_image:
    img = Image.open(uploaded_image)
elif camera_image:
    # Create a pillow image object
    img = Image.open(camera_image)
else:
    img = None

if img:
    options = ['Original', 'Grayscale', 'Red Channel', 'Green Channel', 'Blue Channel', 'Bright', 'Reddish', 'Yellowish']
    choice = st.selectbox('Choose an image mode', options)
    if choice == 'Grayscale':
        # Convert the pillow image to grayscale
        img = img.convert('L')
    elif choice == 'Red Channel':
        # Split the image into R, G, B channels and take the R channel
        r, g, b = img.split()
        img = r
    elif choice == 'Green Channel':
        # Split the image into R, G, B channels and take the G channel
        r, g, b = img.split()
        img = g
    elif choice == 'Blue Channel':
        # Split the image into R, G, B channels and take the B channel
        r, g, b = img.split()
        img = b
    elif choice == 'Bright':
        # Increase the brightness of the image
        enhancer = ImageEnhance.Brightness(img)
        img = enhancer.enhance(1.5)  # Increase brightness by 50%
    elif choice == 'Reddish':
        # Increase the red channel
        r, g, b = img.split()
        r = r.point(lambda i: i * 1.5)
        img = Image.merge('RGB', (r, g, b))
    elif choice == 'Yellowish':
        # Increase the red and green channels
        r, g, b = img.split()
        r = r.point(lambda i: i * 1.5)
        g = g.point(lambda i: i * 1.5)
        img = Image.merge('RGB', (r, g, b))

    # Render the image
    st.image(img, caption='Your image in ' + choice + ' mode')

    # Add an option to save the image
    img.save('output.png')
    with open('output.png', 'rb') as img_file:
        st.download_button(label='Download Image', data=img_file, file_name=f'output_{choice}.png', mime='image/png')
# Add a footer
st.markdown('---')
st.markdown('**Camera Application** developed with ❤️ by [Phuc Le](https://github.com/phucleit96)')