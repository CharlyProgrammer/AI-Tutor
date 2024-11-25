import reflex as rx
from chatbot.app import assistant
# Add state and page to the app.
app = rx.App()
app.add_page(assistant, route="/home",title="Asistente virtual")