import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.llms import Ollama
from datetime import datetime

# Initialize Ollama LLaMA model
llm = Ollama(model="coderindajungle/llama-3b-8b")

# Define a prompt template
prompt_template = PromptTemplate(
    input_variables=["user_input"],
    template="The user wants to book a dental appointment. Respond appropriately: {user_input}"
)

# Set up the conversational chain using LangChain
conversation_chain = LLMChain(llm=llm, prompt=prompt_template)

# Streamlit app layout
st.title("Dental Clinic Appointment Booking Assistant")

if "conversation_history" not in st.session_state:
    st.session_state.conversation_history = []

def add_to_chat_history(role, text):
    st.session_state.conversation_history.append({"role": role, "text": text})

def render_chat_history():
    st.write(
        """
        <style>
        .user-message {
            background-color: #DCF8C6;
            padding: 10px;
            border-radius: 10px;
            margin-bottom: 10px;
            text-align: left;
        }
        .bot-message {
            background-color: #E2E3E5;
            padding: 10px;
            border-radius: 10px;
            margin-bottom: 10px;
            text-align: left;
        }
        </style>
        """, unsafe_allow_html=True
    )
    for message in st.session_state.conversation_history:
        if message["role"] == "user":
            st.markdown(f"<div class='user-message'>{message['text']}</div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div class='bot-message'>{message['text']}</div>", unsafe_allow_html=True)

# Define a basic conversation flow for booking an appointment
class BookingAssistant:
    def __init__(self):
        self.appointment = {}

    def book_appointment(self, name, date, time):
        self.appointment['name'] = name
        self.appointment['date'] = date
        self.appointment['time'] = time
        return f"Booking an appointment for {name} on {date.strftime('%B %d, %Y')} at {time.strftime('%I:%M %p')}... Done! Your appointment is confirmed."

# Initialize the booking assistant
assistant = BookingAssistant()

# Ask for user's name
user_name = st.text_input("Please enter your name:")

if user_name:
    # Add user's name to chat history
    add_to_chat_history("user", f"My name is {user_name}.")
    
    # User input for booking
    user_input = st.text_input("You: ", placeholder="Hi, I would like to book an appointment.", key="user_input")
    
    if user_input:
        add_to_chat_history("user", user_input)
        
        # Generate a response using the LangChain LLM model
        response = conversation_chain.run(user_input=user_input)
        
        # Display date and time pickers for the user to select
        st.write("Please select a date and time for your appointment:")
        
        appointment_date = st.date_input("Select a date")
        appointment_time = st.time_input("Select a time")
        
        if st.button("Confirm Appointment"):
            booking_confirmation = assistant.book_appointment(user_name, appointment_date, appointment_time)
            add_to_chat_history("bot", booking_confirmation)
        else:
            add_to_chat_history("bot", response)

# Render the conversation history in Streamlit
render_chat_history()
