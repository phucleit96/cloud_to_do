import streamlit as st
from PIL import Image, ImageEnhance

# Title of the application
st.title('Camera Application')
st.image(image="fulllogo.png", width=300)
with st.expander("Start Camera"):
    # Start the pages
    camera_image = st.camera_input('Camera')
    # Add an option to upload an image
    uploaded_image = st.file_uploader("Or upload an image", type=["png", "jpg", "jpeg"])

    # Use the uploaded image if it exists, otherwise use the camera image
    if uploaded_image is not None:
        img = Image.open(uploaded_image)
    elif camera_image is not None:
        img = Image.open(camera_image)
    else:
        img = None

    # Add a selectbox for the user to choose the image mode
    options = ['Original', 'Grayscale', 'Red Channel', 'Green Channel', 'Blue Channel', 'Bright', 'Reddish',
               'Yellowish']
    choice = st.selectbox('Choose an image mode', options)

    if img is not None:
        if choice == 'Grayscale':
            img = img.convert('L')
        elif choice == 'Red Channel':
            r, g, b = img.split()
            img = r
        elif choice == 'Green Channel':
            r, g, b = img.split()
            img = g
        elif choice == 'Blue Channel':
            r, g, b = img.split()
            img = b
        elif choice == 'Bright':
            enhancer = ImageEnhance.Brightness(img)
            img = enhancer.enhance(1.5)  # Increase brightness by 50%
        elif choice == 'Reddish':
            r, g, b = img.split()
            r = r.point(lambda i: i * 1.5)
            img = Image.merge('RGB', (r, g, b))
        elif choice == 'Yellowish':
            r, g, b = img.split()
            r = r.point(lambda i: i * 1.5)
            g = g.point(lambda i: i * 1.5)
            img = Image.merge('RGB', (r, g, b))

        # Render the image
        st.image(img, caption='Your image in ' + choice + ' mode')
        # Add an option to save the image
        img.save("output.png")
        with open("output.png", "rb") as img_file:
            st.download_button(
                label="Download image",
                data=img_file,
                file_name=f"output_{choice}.png",
                mime="image/png",
            )

# Add a footer
st.markdown('---')
st.markdown('**Camera Application** developed with ❤️ by [Phuc Le](https://github.com/phucleit96)')