import streamlit as st
from streamlit_option_menu import option_menu
from pages.portco_reporting import portco_1, portco_2, portco_3

def creds_edtered():
    # if st.session_state['user'].strip() == 'JMAN-Client' and st.session_state['pass'].strip() == 'JMAN-PoC':
    if st.session_state['user'].strip() == 'admin' and st.session_state['pass'].strip() == 'admin':

        st.session_state['authenticated'] = True
    
    else:
        st.session_state['authenticated'] = False
        if not st.session_state['pass']:
            st.warning('Please enter Password')
        elif not st.session_state['user']:
            st.warning('Please enter Username')
        else:
            st.warning('Please enter Username & Password')

def authenticate_user():
    if 'authenticated' not in st.session_state:
        st.text_input(label='Username: ',value='', key='user', on_change=creds_edtered)
        st.text_input(label='Password: ',value='', key='pass', on_change=creds_edtered)

        return False

    else:
        if st.session_state['authenticated']:
            return True
        else:
            st.text_input(label='Username: ',value='', key='user', on_change=creds_edtered)
            st.text_input(label='Password: ',value='', key='pass', on_change=creds_edtered)
            return False

def main():
    if authenticate_user():

        v_menu = ['PortCo 1', 'PortCo 2', 'PortCo 3']

        with st.sidebar:
            st.header('PortCo Reporting')

            selected = option_menu(
                menu_title = None,
                options = v_menu,
                icons = None,
                menu_icon = 'menu-down',
                default_index = 0,
                # use_container_width=True
            )

        if selected == 'PortCo 1':
            portco_1.main()

        if selected == 'PortCo 2':
            portco_2.main()

        if selected == 'PortCo 3':
            portco_3.main()

        
        # st.markdown(
        #     "<h1 style='color: darkblue;'>STREAMLIT APP</h1>",
        #     unsafe_allow_html=True
        # )

        # st.markdown(
        #     "<h4 style='color: pink;'>Examining the investment funds of a private equity firm includes reviewing specifics of portfolio companies such as initial investment size, EBITDA, and valuation ratios. Comprehending these metrics aids in evaluating the investment's effectiveness and its potential for returns</h4>",
        #     unsafe_allow_html=True
        # )

if __name__ == '__main__':
    main()