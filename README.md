## Descripción del Proyecto
Este proyecto consiste en crear un sistema de generación automática de contenido para diversos medios y audiencias utilizando inteligencia artificial generativa.

## Funcionalidades
- **Generación de Contenido de Texto**: Generar contenido de texto basado en el tema, audiencia y plataforma proporcionados.
- **Generación de Contenido de Imágenes**: Generar imágenes basadas en el tema, audiencia y plataforma proporcionados.
- **Interfaz Web**: Crear una interfaz web que permita a los usuarios interactuar con el sistema y generar contenido.
- **Personalización del Contenido**: Incluir información de la empresa o persona en el contenido generado.

## Tecnologías Utilizadas
- **Lenguaje Principal**: Python
- **Framework**: LangChain
- **Librerías**: LangChain, LangSmith, LangGraph, LlamaIndex, CrewAI, Ollama, Groq, Huggingface
- **Modelos de IA**: LLMs gratuitos o con pruebas gratuitas
- **Bases de Datos de Vectores**: Chroma, Faiss, Pinecone
- **Front-end**: Streamlit
- **Gestión del Proyecto**: Trello

## Despliegue
- **Despliegue Sencillo**: Usaremos Streamlit para el despliegue de la aplicación.

## Pruebas y Documentación
- **Pruebas**: Realizar pruebas de funcionalidad, personalización y rendimiento.
- **Documentación**: Documentar el código y crear un README en GitHub.

## Extensibilidad
- **Extensibilidad**: Usar frameworks como LangChain para facilitar la extensibilidad del sistema.

## Niveles de Entrega
- **Nivel Esencial**: Generar contenido de texto, interfaz web, artículo en Medium, repositorio Git, documentación.
- **Nivel Medio**: Dockerizar la aplicación, seleccionar LLMs, personalización de contenido, generación de imágenes.

## Desarrollo Iterativo
- **Desarrollo Iterativo**: Usaremos un enfoque iterativo para tomar decisiones técnicas y automatizar el proceso de cumplimiento de los requisitos.
```

### 2. **Automatizar el Proceso de Cumplimiento de Requisitos**

Para mantener un desarrollo ordenado, podemos seguir los siguientes pasos:

#### 1. **Control de Versiones**
- **Git**: Utilizar Git para el control de versiones y gestionar el historial del código.
- **GitHub**: Crear un repositorio en GitHub para almacenar el código fuente y gestionar las ramas y commits.

#### 2. **Desarrollo Iterativo**
- **Iteraciones**: Realizar iteraciones para mejorar y optimizar el sistema.

#### 3. **Despliegue**
- **Streamlit**: Usar Streamlit para el despliegue sencillo de la aplicación.

## Cómo ejecutar el proyecto

1. **Clonar el repositorio**
```bash
git clone https://github.com/Bootcamp-IA-MAD-P7/mod3-proyecto3-Veru.git
cd mod3-proyecto3-Veru
```

2. **Crear y activar un entorno virtual (recomendado)**
```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux/Mac
source .venv/bin/activate
```

3. **Instalar dependencias**
```bash
pip install -r requirements.txt
```

4. **Ejecutar la aplicación**
```bash
streamlit run path/to/your/app.py
```

> **Nota:** Por defecto, el proyecto utiliza un modelo local (`gpt2`) a través de Hugging Face Transformers, con el objetivo de **minimizar el gasto**, tal como se solicita en el briefing.