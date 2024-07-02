import streamlit as st
import hmac


def check_password():
    def login_form():
        with st.form("Credentials"):
            st.text_input("Username", key="username")
            st.text_input("Password", type="password", key="password")
            st.form_submit_button("Log in", on_click=password_entered)

    def password_entered():
        if st.session_state["username"] in st.secrets["passwords"] and hmac.compare_digest(st.session_state["password"],
                                                                                           st.secrets.passwords[
                                                                                               st.session_state[
                                                                                                   "username"]]):
            st.session_state["password_correct"] = True
            del st.session_state["username"]
            del st.session_state["password"]
        else:
            st.session_state["password_correct"] = False

    if st.session_state.get("password_correct", False):
        return True

    login_form()
    if "password_correct" in st.session_state:
        st.error("😒Try again.")
    return False

if not check_password():
    st.stop()

map = st.Page(
    "map.py",
    title="Bản đồ Việt Nam",
    icon="🗺️"
)

heatmap = st.Page(
    "heatmap.py",
    title="Dân số các thành phố tại Việt Nam",
    icon="🏙️"
)

weather = st.Page(
    "weather.py", title="Thời tiết", icon="🌡️"
)

simplified_pdf = st.Page(
    "readpaper.py",
    title="Tóm tắt báo",
    icon="📰"
)

chatbot = st.Page(
    "chatbot.py",
    title="Chatbot nghịch",
    icon="💬"
)

map_page = [map, heatmap]
weather_page = [weather]
pdf = [simplified_pdf]
chatbot = [chatbot]


page_dict = {}
page_dict["Bản đồ"] = map_page
page_dict["Dự báo thời tiết"] = weather_page
page_dict["Học tập"] = pdf
page_dict["Trò chuyện với máy"] = chatbot

pg = st.navigation(page_dict)
pg.run()
