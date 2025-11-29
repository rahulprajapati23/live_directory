import streamlit as st
import os
import sys
from io import StringIO

# Set page config
st.set_page_config(page_title="Directory Viewer", layout="wide")

st.title("📂 Directory Viewer")

# Function to get all files recursively or just flat
def get_files():
    file_list = []
    for root, dirs, files in os.walk("."):
        # Skip hidden directories like .git
        if ".git" in root or ".venv" in root or "__pycache__" in root:
            continue
            
        for file in files:
            if file == "app.py" or file.startswith("."):
                continue
            
            # Get relative path
            rel_path = os.path.relpath(os.path.join(root, file), ".")
            file_list.append(rel_path)
    return sorted(file_list)

files = get_files()

if not files:
    st.warning("No files found in the directory.")
else:
    # Sidebar for file selection
    selected_file = st.sidebar.radio("Select a File", files)

    if selected_file:
        st.header(f"📄 {selected_file}")
        
        file_ext = os.path.splitext(selected_file)[1].lower()
        
        # Determine how to display the file
        try:
            if file_ext in ['.py', '.txt', '.md', '.json', '.csv', '.html', '.css', '.js']:
                # Text files: Show content and optional run for Python
                with open(selected_file, "r", encoding='utf-8') as f:
                    content = f.read()
                
                if file_ext == '.py':
                    tab1, tab2 = st.tabs(["View Code", "Run Output"])
                    with tab1:
                        st.code(content, language="python")
                    with tab2:
                        if st.button(f"Run {selected_file}"):
                            st.info("Running script...")
                            old_stdout = sys.stdout
                            redirected_output = sys.stdout = StringIO()
                            try:
                                exec(content)
                                output = redirected_output.getvalue()
                                if output:
                                    st.success("Output:")
                                    st.text(output)
                                else:
                                    st.info("Script ran successfully (no output).")
                            except Exception as e:
                                st.error(f"Error: {e}")
                            finally:
                                sys.stdout = old_stdout
                else:
                    # Generic text view
                    st.code(content)
                    
            elif file_ext in ['.png', '.jpg', '.jpeg', '.gif', '.webp']:
                # Images
                st.image(selected_file)
                
            else:
                # Binary/Other files: Provide download button
                st.info(f"This is a binary file ({file_ext}). You can download it below.")
                with open(selected_file, "rb") as f:
                    btn = st.download_button(
                        label=f"Download {selected_file}",
                        data=f,
                        file_name=os.path.basename(selected_file)
                    )
                    
        except Exception as e:
            st.error(f"Error reading file: {e}")
