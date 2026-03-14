# import the library
import streamlit as st
# adding the title of your app
st.title("My First Apps")
# Now adding simple text
st.write("Hello World")
# user input
number = st.slider('Pick a Number', min_value=1, max_value=10, value=5)
# print the text of number when we click the button
st.write(f'You selected: {number}')

# adding the button 
if st.button("Say hello"):
    st.write("Why hello there")
else:
    st.write("Goodbye")
# add the radio button with option 
option = st.radio(
    "What is your favorite color?",
    ("Blue", "Red", "Green"))
# print the text of number when we click the button
st.write(f'You selected: {option}')
# add a drop down list
selected_fruit = st.selectbox(
    'Select a fruit',
    ('Apple', 'Banana', 'Cherry'))
# print the text of number when we click the button
st.write(f'You selected: {selected_fruit}')
# add the drop down list on the left sidebar
selected_fruit = st.sidebar.selectbox(
    'Select a fruit',
    ('Apple', 'Banana', 'Cherry'))
# print the text of number when we click the button
st.write(f'You selected: {selected_fruit}')
# add your wathsap number 
st.sidebar.text_input("Your WhatsApp number")
# add file uploader 
st.sidebar.file_uploader("Upload a file", type=["jpg", "png", "jpeg"])
# create the line plot 
# plotting 
data = pd.DataFrame(
    'first column': list(range(1, 11)),
    'second column': list(range(11, 21)))
st.line_chart(data)