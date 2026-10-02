import streamlit as st
from langchain import LangChain
import openai
from transformers import pipeline
import requests

# Configurar la Clave de API:
openai.api_key = 'your-openai-api-key'

#API de Texto

text_generator = pipeline('text-generation', model='gpt2')

# API de Imágenes: 
def generate_image(prompt):
    url = 'https://api.dall-e.com/generate'
    response = requests.post(url, json={'prompt': prompt})
    return response.json()['image_url']

# crear una clase LangChain que maneje tanto modelos locales como APIs gratuitas. 
class LangChain:
    def __init__(self, model_type='local', model_path='gpt2', api_key=None):
        self.model_type = model_type
        self.model_path = model_path
        self.api_key = api_key
        self.text_generator = None
        self.image_generator = None

        if self.model_type == 'local':
            self.text_generator = pipeline('text-generation', model=self.model_path)
        elif self.model_type == 'api':
            self.text_generator = pipeline('text-generation', model='huggingface/transformers')
            self.image_generator = self.api_image_generator

    def generate_text(self, topic, audience, platform, custom_info=None):
        prompt = f"Topic: {topic}\nAudience: {audience}\nPlatform: {platform}\n{custom_info if custom_info else ''}"
        if self.model_type == 'local':
            return self.text_generator(prompt, max_length=100)[0]['generated_text']
        else:
            return self.text_generator(prompt, max_length=100)[0]['generated_text']

    def generate_image(self, topic, audience, platform):
        if self.model_type == 'api':
            prompt = f"Topic: {topic}\nAudience: {audience}\nPlatform: {platform}"
            return self.image_generator(prompt)
        else:
            raise ValueError("Image generation not supported for local models")

    def api_image_generator(self, prompt):
        url = 'https://api.dall-e.com/generate'
        headers = {
            'Authorization': f'Bearer {self.api_key}'
        }
        response = requests.post(url, json={'prompt': prompt}, headers=headers)
        return response.json()['image_url']
    
# Integración con Streamlit   
# Inicializar LangChain
lc = LangChain(model_type='api', api_key='your-api-key)

# Interfaz de Streamlit
st.title("Generador de Contenido Automático")

# Entrada del usuario
topic = st.text_input("Tema:")
audience = st.text_input("Audiencia:")
platform = st.text_input("Plataforma:")
custom_info = st.text_area("Información Personalizada (opcional):")

# Botón para generar contenido
if st.button("Generar Contenido"):
    # Generar contenido de texto
    text_content = lc.generate_text(topic, audience, platform, custom_info)
    st.write("Contenido de Texto:")
    st.write(text_content)

    # Generar imágenes (usando una API gratuita como DALL-E)
    image_url = lc.generate_image(topic, audience, platform)
    st.image(image_url, caption="Imagen Generada")

# Nota: Asegúrate de manejar las excepciones y limitaciones de las APIs