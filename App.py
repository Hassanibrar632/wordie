import streamlit as st
from streamlit_extras.stylable_container import stylable_container

def get_words(filename):
    with open(filename, 'r') as file:
        words = file.readlines()
    words = [word.strip().replace('"', '') for word in words]
    words = [word.upper() for word in words if len(word) == 5]
    st.session_state.words_list = words

class wordie:
    def __init__(self):
        self.setofwords = st.session_state.words_list

    def view_words(self):
        return self.setofwords

    def black(self, letters):
        for l in letters:
            self.setofwords = [i for i in self.setofwords if l not in i]
        return
    
    def yellow(self, letters):
        for l, j in letters:
            self.setofwords = [i for i in self.setofwords if l in i and i[j] != l]
        return

    def green(self, letters):
        for l, j in letters:
            self.setofwords = [i for i in self.setofwords if i[j] == l]
        return

    def reset(self):
        self.setofwords = st.session_state.words_list
        return

def submit():
    st.session_state.my_text = st.session_state.widget
    st.session_state.widget = ""

def Game():
    st.text_input("Enter your guess", key="widget", on_change=submit)
    if len(st.session_state.my_text) == 5:
        st.session_state.words.append(st.session_state.my_text.upper())
        st.session_state.attrs.extend([0 for _ in range(5)])
        st.session_state.my_text = ""

    green_pair = []
    yellow_pair = []
    black = []
    gusser.reset()

    for i, word in enumerate(st.session_state.words):
        cols = st.columns(5)
        for j, l in enumerate(word):
            with cols[j]:
                index = i*5+j
                temp = st.session_state.attrs[index]
                t_col = t_colour[temp]
                b_col = b_colour[temp]
                with stylable_container(c_colour[temp], css_styles=style.replace('123', b_col).replace('321', t_col)):
                    if st.button(f"{l}", key=index):
                        st.session_state.attrs[index] = (temp+1)%3
                        st.rerun()
                    if temp == 0:
                        black.append(l)
                    elif temp == 1:
                        yellow_pair.append([l, j])
                    else:
                        green_pair.append([l, j])

    gusser.black(black)
    gusser.yellow(yellow_pair)
    gusser.green(green_pair)

    st.text_area(label ="Expected Words:",value="\n".join(gusser.view_words()))
    if st.button('Reset'):
        st.session_state.words = []
        st.session_state.attrs = []
        st.session_state.my_text = ""
        st.rerun()

b_colour = ['#000000', '#FFFF00', '#00FF00']
t_colour = ['white', 'black', 'white']
c_colour = ['black', 'yellow', 'green']

style = "button{ background-color: 123; color: 321; }"
get_words(r'wordlist-20210729.txt')
gusser = wordie()

if 'words' not in st.session_state:
    st.session_state.words = []
    st.session_state.attrs = []
    st.session_state.my_text = ""

if __name__ == '__main__':
    Game()