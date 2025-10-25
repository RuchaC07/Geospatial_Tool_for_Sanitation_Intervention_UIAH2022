import streamlit as st

def main():
    st.title("Support")

    # Text area for the complaint
    form = st.text_area("Please describe your issue or feedback:")

    # Show submit button
    submit_button = st.button('Submit')

    # Validate if the form is not empty and submit button is pressed
    if form.strip() != "" and submit_button:
        # Call a function to handle submission
        submit_complaint(form)
        # Show a confirmation pop-up
        st.success("Thank you for your feedback! We'll address it as soon as possible.")

def submit_complaint(complaint):
    # Here you can implement the logic to store or handle the complaint
    # For demonstration purposes, let's just print it
    print("Submitted complaint:", complaint)

if __name__ == "__main__":
    main()
