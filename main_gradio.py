import gradio as gr
import sqlite3
from opencc import OpenCC
import pandas as pd

def greet(name, intensity):
    return "Hello, " + name + "!" * int(intensity)

def search(query: str):
    # turn input to simple Chinese with OpenCC
    cc = OpenCC('t2s')
    search_text = cc.convert(query)

    # connect to database, which can detect multi-keywords (generate by GPT)
    conn = sqlite3.connect("ebook.db")
    c = conn.cursor()
    search_terms = search_text.split(',')
    like_clauses = " AND ".join(["(title LIKE ? OR describe LIKE ?)"] * len(search_terms))
    parameters = []
    for term in search_terms:
        parameters.extend(['%' + term + '%', '%' + term + '%'])
    query = f"SELECT * FROM ebook WHERE {like_clauses}"
    c.execute(query, parameters)
    #c.execute("SELECT * FROM ebook WHERE title LIKE ? OR describe LIKE ?", ('%' + search_text + '%', '%' + search_text + '%'))
    results = c.fetchall()
    conn.close()

    # change the result list to dataframe
    columns = ['ID', 'URL', 'Title', 'Author', 'Date', 'Description', 'Source']
    df = pd.DataFrame(results, columns=columns)
    return df

with gr.Blocks() as demo:
    with gr.Row():
        text1 = gr.Textbox(label="搜尋關鍵字（可用 , 隔開）")
    with gr.Row():
        btn = gr.Button("Go")
    with gr.Row():
        output = gr.Dataframe(headers=['ID', 'URL', 'Title', 'Author', 'Date', 'Description', 'Source'])
    btn.click(search,inputs=text1,outputs=output)

demo.launch()