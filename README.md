### Step 1: Create Project Directory

1. Open your terminal or command prompt.
2. Create a new directory for your Streamlit project:
   ```bash
   mkdir my_streamlit_app
   cd my_streamlit_app
   ```

### Step 2: Create `app.py`

Create a file named `app.py` in the project directory. You can use any text editor or IDE to create this file. Here’s a simple example of what you might include in `app.py`:

```python
# app.py

import streamlit as st

# Title of the app
st.title("My First Streamlit App")

# Text input
user_input = st.text_input("Enter some text:")

# Display the input
if user_input:
    st.write(f"You entered: {user_input}")

# A simple button
if st.button("Click Me"):
    st.write("Button clicked!")
```

### Step 3: Create `requirements.txt`

Next, create a file named `requirements.txt` in the same directory. This file will list the dependencies required for your Streamlit app. For a basic Streamlit app, you can include the following:

```
streamlit
```

If you plan to use additional libraries, you can add them to this file as well. For example, if you want to use NumPy and Pandas, your `requirements.txt` might look like this:

```
streamlit
numpy
pandas
```

### Step 4: Install Dependencies

Before deploying your app, you need to install the required dependencies. You can do this using pip. Run the following command in your terminal:

```bash
pip install -r requirements.txt
```

### Step 5: Run Your Streamlit App

You can run your Streamlit app locally to test it. Use the following command:

```bash
streamlit run app.py
```

This will start a local server, and you can view your app in your web browser at `http://localhost:8501`.

### Step 6: Deployment

To deploy your Streamlit app, you can use platforms like Streamlit Sharing, Heroku, or AWS. Each platform has its own deployment process, but generally, you will need to push your code to a repository (like GitHub) and then connect that repository to the deployment platform.

### Summary

Your project structure should look like this:

```
my_streamlit_app/
│
├── app.py
└── requirements.txt
```

You now have a basic Streamlit project set up and ready for further development or deployment!