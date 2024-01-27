# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
  
import tiktoken
import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)

# creating tokens
def create_tokens(input):                                          # generates tokens
    '''Takes any input (str or int or arr) and returns its tokens'''
    cl100k_base = tiktoken.get_encoding('cl100k_base')
    text_encoded_tokens = cl100k_base.encode(input)
    return text_encoded_tokens

#######################################################
    #   STREAMLIT APP
#######################################################
def run():
    st.set_page_config(page_title = 'Insights Hub', page_icon = ':mag:', layout = 'centered')
    st.title(':mag: Insights Hub')
    st.caption('Uncover the magic of text understanding')
    st.divider()

    # helpful variables
    session = st.session_state

    # UI components
    st.text_input(label = 'Write/paste your text here to see how computer handles it.', placeholder = 'a white cat', key = 'text')
    st.button(label = 'Process Text', key = 'process_btn', type = 'primary')


    # conditional statements
    if session.text and session.process_btn:
        tokens = create_tokens(st.session_state.text)

        # displaying tokens in a beautiful way
        input_chunks = session.text.split(' ')

        dataframe = {
            'Word': input_chunks,
            'Converted Form': tokens
        }
        st.dataframe(dataframe, use_container_width = True, )

if __name__ == "__main__":
    run()