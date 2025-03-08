import streamlit as st
from streamlit_option_menu import option_menu

def sidebar():
    with st.sidebar:
        st.markdown("## Why & IF Framework")
        st.markdown("### Navigation")

        # Menu với icon
        page = option_menu(
            menu_title="Go to:",
            options=["Home", "Fine-Tune", "Logs", "Settings"],
            icons=["house", "sliders", "file-earmark-text", "gear"],
            menu_icon="cast",
            default_index=0,
            styles={
                "container": {"background-color": "#1e1e1e"},
                "icon": {"color": "#FFFFFF", "font-size": "18px"},
                "nav-link": {"color": "#BBBBBB", "text-align": "left"},
                "nav-link-selected": {"background-color": "#009688"},
            }
        )

        # Hiển thị trạng thái hệ thống
        st.markdown("---")
        st.markdown("### System Info")
        st.markdown("✅ **AI Running**")
        st.markdown("⚡ **GPU:** A6000 Ada x4")
        st.markdown("📦 **Memory:** 64GB DDR5")

    return page
