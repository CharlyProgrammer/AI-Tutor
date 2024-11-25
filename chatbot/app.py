import reflex as rx
from chatbot.styles import style_chat
from chatbot.azure_and_llm.completion_llm import model_completion 
from chatbot.azure_and_llm.search_service import search_info
class State(rx.State):
     text_input:str = ""
     historial: list[tuple[str, str]]
     def actualizar_texto(self, new_value):
        self.text_input = new_value
     def guardar_texto(self):
        
        answer=run_conversation(self.text_input)
        self.historial.append((self.text_input,answer)) 
        self.text_input=""   
     def clear_hist(self):
         self.historial.clear()
def run_conversation(user_prompt):
    obj_llm_completion=model_completion("LLAMA_KEY","LLAMA_MODEL")
    client=obj_llm_completion.init_model()
    obj_search=search_info(key_service="AI_SEARCH_KEY",index_name="INDEX_NAME",endpoint_service="AI_SEARCH_ENDPOINT")
    headers,url=obj_search.init_service()
    docs_from_search=obj_search.retrieve_documents(user_prompt,headers=headers,search_url=url)
    context = "\n".join(docs_from_search)
    prompt = f"Context:\n{context}\n\nQuestion:\n{user_prompt}\n\nAnswer:"
    response=obj_llm_completion.generate_response(client=client,prompt=prompt,temperature=0.7)
   
    return response

def qa(question: str, answer: str) -> rx.Component:
    return rx.box(
        rx.box(
            rx.text(question, style=style_chat.question_style),
            text_align="right",
        ),
        rx.box(
            rx.text(answer, style=style_chat.answer_style),
            text_align="left",
        ),
        margin_y="1em",
        width="100%",
    )
    
def chat() -> rx.Component:
    
    return rx.box(
        rx.foreach(
            State.historial,
            lambda messages: qa(messages[0], messages[1]),
        )
        
         
    )

def action_bar() -> rx.Component:
    return rx.hstack(
        rx.input(
            value=State.text_input,
            placeholder="Realiza una pregunta",
            on_change=State.actualizar_texto, 
            style=style_chat.input_style,
            background_color="white"
        ),
        rx.button(
            "Enviar",
            on_click=State.guardar_texto,
            style=style_chat.button_style,
        ),
    )

def assistant() -> rx.Component:
    return rx.box(
        rx.flex(
            rx.flex(
                rx.image(
                    
                    src="https://static.vecteezy.com/system/resources/previews/021/942/891/non_2x/icon-llama-related-to-domestic-animals-symbol-simple-design-editable-simple-illustration-free-vector.jpg",  # URL de la imagen
                    alt="Descripción de la imagen",
                    width="6vw",  # Ancho de la imagen
                    height="auto",   # Altura ajustada automáticamente
                    align="center",
                ),
                rx.heading(
                    'DeepLearning.AI Tutor',
                    align="center",
                    
                    weight="medium",
                    high_contrast=True,
                    font_family="Times New Roman",
                    font_size="2vw",
                ),     
                width="120%",
                spacing='60px',
                direction="raw",
                alignItems="center",
                justifyContent="right",
            
            ),
            
            rx.flex(
                rx.heading(
                    "CHATBOT DE ASISTENCIA",
                    color_scheme="cyan",
                    weight="regular",
                    high_contrast=True,
                    font_family="Times New Roman",
                    font_size="2.5vh",
                    
                
                ),
                rx.heading(
                    "HACKATHON LLAMA IMPACT PAN-LATAM",
                    color_scheme="indigo",
                    weight="bold",
                    font_family="Times New Roman",
                    high_contrast=True,
                    font_size="2.5vh",
                    
                ),
                rx.heading(
                    "EQUIPO TECHLAB",
                    color_scheme="cyan",
                    weight="regular",
                    high_contrast=True,
                    font_family="Times New Roman",
                    font_size="2.5vh",
                    
                
                ),
                spacing='1px',
                direction="column",
                width="80%",
                
            
            ),
            
            width="100%",
            spacing='60px',
            height="16vh",
            max_height='24vh',
            align_items="center",
            
             style={'padding-left':'10vw'},
        ),
        rx.box(
             rx.flex(
                rx.heading(
                    "La base de conocimientos de este sistema de RAG se basan en esta plataforma de aprendizaje:",
                    color="white",
                    font_family="Arial",
                    font_size="16px"
                ),
                rx.link(
                    "deeplearning learning platform", 
                    href="https://www.deeplearning.ai/",
                    target="_blank",  # Abre en una nueva pestaña
                    style={
                        "color": "White",
                        "textDecoration": "underline"
                        }
                ),
                spacing='60px',
                direction="row",
            ),
            display="flex", 
            alignItems="center",
            justifyContent="right",
            background_color="black",
            height="4vh",
            min_height='50px',
            max_height='100px',
            paddingX='12vw'
        ),
        rx.center(
            rx.box(
                rx.center(
                    rx.box(
                        
                        rx.heading(
                            f"Bienvenid@s",
                            align="center",
                            font_family="Console",
                            font_size="38px",
                            weight="bold",
                            
                            style={
                                "text-shadow": "2px 2px 5px rgba(0, 0, 0, 0.5)"
                            }
                        
                        ),
                        rx.text(
                            f"Bienvenido a tu asistente de aprendizaje de inteligencia artificial basado en los mejores recursos disponibles en todo el mundo y domines lo necesario para ser parte de esta emocionante revolución",
                            align="center",
                            font_family="Console",
                            font_size="24px",
                            weight="bold",
                            paddingY="1vh",
                            style={
                                "text-shadow": "2px 2px 5px rgba(0, 0, 0, 0.5)"
                            }
                        
                        ),
                     
                    direction="column",
                    height="100%",
                    background_color="#E3E4E5",
                    width="70%",
                    paddingY='3vh',
                    border_color="black",  # Color del borde
                    border_width="2px",
                    
                    ),
                                  
                    spacing='40px',
                    direction="column",
                    paddingY='3vh'
                ), 
                rx.center(
                    
                    rx.vstack(
                        chat(),
                        action_bar(),
                        align="center",
                    )
                        
                ), 
                direction="column",
                height="100%",
                background_color="#ECE7CA",
                width="80%",
                paddingX='3vw'
                ),
            
            background_color="#b5b5b5",
            width="100%",
            height='fit-content',
            
          
            
            
        ),    
        
    height="100%",
    width="100%",
    )
    

