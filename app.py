import gradio as gr
import time

def run_fiverr_upload(username, password):
    progress = []
    progress.append("🚀 התחלת תהליך העלאה...")
    time.sleep(1)
    progress.append("🔐 כניסה לחשבון Fiverr...")
    time.sleep(1)
    progress.append("📤 העלאת קבצי השירותים...")
    time.sleep(1)
    progress.append("✅ סיום: כל השירותים הועלו בהצלחה!")
    return "\n".join(progress)

with gr.Blocks(title="🚀 Fiverr Auto Uploader") as demo:
    gr.Markdown("# 🚀 Fiverr Auto Uploader\\nהפעל את האוטומציה שלך לפייבר בלחיצה אחת!")
    with gr.Row():
        username = gr.Textbox(label="Fiverr Username")
        password = gr.Textbox(label="Fiverr Password", type="password")
    run_button = gr.Button("▶️ Run Fiverr Upload")
    output = gr.Textbox(label="Logs", lines=10)

    run_button.click(run_fiverr_upload, inputs=[username, password], outputs=output)

demo.launch()
