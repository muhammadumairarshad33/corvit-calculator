import streamlit as st
import time

st.set_page_config(
    page_title="Muhammad Umair Calculator for Corvit HCCDA AI ",
    page_icon="🧮"
)

# Default theme color set as there's no picker
theme_color = '#1467f0'

# CSS Style
st.html(f"""
<style>
        div[data-testid='column'] {{
        width: -moz-fit-content;
        width: 60px !important;
        text-align: center;
        float: center;
        flex: unset;
        }}

        div.stButton>button[kind='secondary']{{
        border: 1px solid grey;
        width:40px;
        font-size:3px;
        color:black;
        }}

        div.stButton>button[kind='secondary']:hover{{
        border:1px solid grey;
        color:black;
        }}

        div.stButton>button[kind='secondary']:active{{
        border:1px solid grey;
        color:black;
        background-color:white;
        }}

        div.stButton>button[kind='primary']{{
        border: 1px solid {theme_color};
        width:60px;
        background-color: {theme_color};
        color:white;
        }}

        div.stButton>button[kind='primary']:hover{{
        border: 1px solid {theme_color};
        color:white;
        }}

        div.stButton>button[kind='primary']:active{{
        border:1px solid {theme_color};
        background-color:{theme_color};
        color:white;
        }}
</style>""")

## Session State ##
if 'input' not in st.session_state:
    st.session_state.input = ''
if 'disable_button' not in st.session_state:
    st.session_state.disable_button = False

## Functions ##
def add_7():
    st.session_state.input += '7'

def add_4():
    st.session_state.input += '4'

def add_1():
    st.session_state.input += '1'

def add_8():
    st.session_state.input += '8'

def add_5():
    st.session_state.input += '5'

def add_2():
    st.session_state.input += '2'

def add_0():
    st.session_state.input += '0'

def add_9():
    st.session_state.input += '9'

def add_6():
    st.session_state.input += '6'

def add_3():
    st.session_state.input += '3'

def add_dot():
    st.session_state.input += '.'

def add_plus():
    st.session_state.input += '+'

def add_minus():
    st.session_state.input += '-'

def add_multiply():
    st.session_state.input += '×'

def add_divide():
    st.session_state.input += '÷'

def delete():
    st.session_state.input = st.session_state.input[:-1]

def clear_all():
    st.session_state.pop('input')
    st.session_state.disable_button = False

def calculate():
    st.session_state.input = st.session_state.input.replace('×', '*')
    st.session_state.input = st.session_state.input.replace('÷', '/')

    time.sleep(0.2)

    try:
        st.session_state.input = eval(st.session_state.input)
        st.session_state.input = "%g" % (float(st.session_state.input))

    except ZeroDivisionError:
        st.session_state.input = 'Math ERROR - Click [AC] to Reset'
    except:
        st.session_state.input = 'Syntax ERROR - Click [AC] to Reset'
    st.session_state.disable_button = True

st.markdown(f'<h1 style="color:{theme_color};text-align:center;font-size:52px;"><b>Muhammad Umair Calculator for Corvit HCCDA AI</b></h1>',
            unsafe_allow_html=True)

# Removed Disclaimer section

container = st.container(border=True)
container.write(f"<span style='font-size:12px;text-align:left;color:{theme_color};'><b>please enter the numbers</b></span>",
                unsafe_allow_html=True)
container.write(f"<p align='left'><span style='font-size:40px;'>{st.session_state.input}</span></p>",
                unsafe_allow_html=True)
container.divider()

## 8 Columns for sorting button
col1, col2, col3, col4, col5, col6, col7, col8 = container.columns([1, 1, 1, 1, 1, 1, 1, 1])
with col1:
    st.button(label='7', on_click=add_7, disabled=st.session_state.disable_button)
    st.button(label='4', on_click=add_4, disabled=st.session_state.disable_button)
    st.button(label='1', on_click=add_1, disabled=st.session_state.disable_button)

with col2:
    st.button(label='8', on_click=add_8, disabled=st.session_state.disable_button)
    st.button(label='5', on_click=add_5, disabled=st.session_state.disable_button)
    st.button(label='2', on_click=add_2, disabled=st.session_state.disable_button)
    st.button(label='0', on_click=add_0, disabled=st.session_state.disable_button)

with col3:
    st.button(label='9', on_click=add_9, disabled=st.session_state.disable_button)
    st.button(label='6', on_click=add_6, disabled=st.session_state.disable_button)
    st.button(label='3', on_click=add_3, disabled=st.session_state.disable_button)
    st.button(label='.', on_click=add_dot, disabled=st.session_state.disable_button)

with col4:
    st.button(label='**+**', on_click=add_plus, disabled=st.session_state.disable_button)
    st.button(label='**-**', on_click=add_minus, disabled=st.session_state.disable_button)
    st.button(label='×', on_click=add_multiply, disabled=st.session_state.disable_button)
    st.button(label='÷', on_click=add_divide, disabled=st.session_state.disable_button)

with col5:
    pass

with col6:
    st.button(label='DEL', type='primary', on_click=delete, disabled=st.session_state.disable_button)
    pass

with col7:
    st.button(label='AC', type='primary', on_click=clear_all)
    pass

with col8:
    st.button(label='=', type='primary', on_click=calculate, disabled=st.session_state.disable_button)

# Note
st.html(
    f'''
<details>
<summary><span id='Note' style="color:{theme_color};">ℹ️ <b>NOTE</b></span></summary>
<pre>This calculator only supports addition, subtraction, multiplication, and division.</pre>
</details>'''
)
