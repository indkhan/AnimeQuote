import gradio as gr
from main import openai_response


def greet(name):
    return "Hello " + name + "!"


demo = gr.Interface(fn=openai_response, inputs="text", outputs="text")

if __name__ == "__main__":
    demo.launch(show_api=False)
