import gradio as gr
from dotenv import load_dotenv
from research_manager import ResearchManager

load_dotenv(override=True)


async def run(query: str, email: str):
    async for chunk in ResearchManager().run(query, email):
        yield chunk


with gr.Blocks(theme=gr.themes.Default(primary_hue="sky")) as ui:
    gr.Markdown("# Deep Research")
    query_textbox = gr.Textbox(label="What topic would you like to research?")
    email_textbox = gr.Textbox(label="Email (optional, to receive the report)")
    run_button = gr.Button("Run", variant="primary")
    report = gr.Markdown(label="Report")
    
    run_button.click(fn=run, inputs=[query_textbox, email_textbox], outputs=report)
    query_textbox.submit(fn=run, inputs=[query_textbox, email_textbox], outputs=report)

ui.launch(inbrowser=True)

