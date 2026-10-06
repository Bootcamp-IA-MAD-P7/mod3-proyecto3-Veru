import os
os.environ["TRANSFORMERS_NO_TORCH_COMPILE"] = "1"

import streamlit as st
from transformers import pipeline
import torch

st.set_page_config(page_title="Generador de Contenido Automático", layout="centered")

MODEL_NAME = "Qwen/Qwen2.5-0.5B-Instruct"

@st.cache_resource(show_spinner=False)
def load_generator():
    return pipeline(
        "text-generation",
        model=MODEL_NAME,
        dtype=torch.float32,
        device=-1,
        trust_remote_code=False
    )

class ContentGenerator:
    def __init__(self):
        self.text_generator = load_generator()
    
    def _build_prompt(self, topic, audience, platform, custom_info=None):
        base_prompt = (
            f"Escribe un informe educativo en ESPAÑOL claro y correcto sobre {topic}, dirigido a {audience}.\n\n"
            f"Estructura: INTRODUCCIÓN, DESARROLLO, CONCLUSIÓN.\n"
            f"Tono: divulgativo, comprensible. Usa vocabulario adecuado.\n"
        )
        if custom_info and custom_info.strip():
            base_prompt += f"\nInstrucciones: {custom_info.strip()}\n\n"
        base_prompt += "Escribe el informe completo en español:\n\n"
        return base_prompt
    
    def generate_text(self, topic, audience, platform, custom_info=None):
        prompt = self._build_prompt(topic, audience, platform, custom_info)
        result = self.text_generator(
            prompt,
            max_new_tokens=200,
            num_return_sequences=1,
            do_sample=True,
            temperature=0.7,
            top_p=0.9,
            top_k=40,
            repetition_penalty=1.2,
            eos_token_id=151645,
            truncation=True
        )
        generated = result[0]["generated_text"]
        if generated.startswith(prompt):
            generated = generated[len(prompt):]
        return generated.strip()

if "content_gen" not in st.session_state:
    st.session_state.content_gen = ContentGenerator()

content_gen = st.session_state.content_gen

st.title("Generador de Contenido Automático")
topic = st.text_input("Tema:", key="topic")
audience = st.text_input("Audiencia:", key="audience")
platform = st.selectbox("Plataforma:", ["Blog","Twitter/X","Instagram","LinkedIn","Divulgación","Infantil","SEO"], key="platform")
custom_info = st.text_area("Información personalizada (opcional):", key="custom")

if st.button("Generar Contenido"):
    try:
        if not topic or not audience:
            st.warning("Rellena Tema y Audiencia")
        else:
            with st.spinner("Generando contenido..."):
                text_content = content_gen.generate_text(topic, audience, platform, custom_info)
            st.subheader("Contenido de Texto")
            st.write(text_content)
    except Exception as e:
        st.error(f"Error: {e}")
