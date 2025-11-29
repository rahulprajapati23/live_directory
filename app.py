import streamlit as st
import os
import sys
from io import StringIO

# Set page config
st.set_page_config(page_title="Source Code Viewer", layout="wide")

st.title("📂 Source Code Viewer & Runner")

# Get list of Python files
files = [f for f in os.listdir('.') if f.endswith('.py') and f != 'app.py']
files.sort()

if not files:
    st.warning("No Python files found in the directory.")
else:
    # Sidebar for file selection
    selected_file = st.sidebar.radio("Select a File", files)

    if selected_file:
        st.header(f"📄 {selected_file}")

        # Read file content
        with open(selected_file, "r") as f:
            code_content = f.read()

        # Tabs for View and Run
        tab1, tab2 = st.tabs(["View Code", "Run Output"])

        with tab1:
            st.code(code_content, language="python")

        with tab2:
            if st.button(f"Run {selected_file}"):
                st.info("Running script...")
                
                # Capture stdout
                old_stdout = sys.stdout
                redirected_output = sys.stdout = StringIO()

                try:
                    # Execute the code
                    exec(code_content)
                    output = redirected_output.getvalue()
                    if output:
                        st.success("Output:")
                        st.text(output)
                    else:
                        st.info("Script ran successfully but produced no output.")
                except Exception as e:
                    st.error(f"Error occurred: {e}")
                finally:
                    # Reset stdout
                    sys.stdout = old_stdout
