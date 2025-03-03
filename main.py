import time
import os
import webbrowser


def generate_html(mermaid_code, output_file="graph.html"):
    html_template = f"""
    <html>
    <head>
        <script type="module">
            import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
            mermaid.initialize({{ startOnLoad: true }});
        </script>
    </head>
    <body>
        <div class="mermaid">
            {mermaid_code}
        </div>
        <script>
            setTimeout(() => location.reload(), 5000);
        </script>
    </body>
    </html>
    """
    with open(output_file, "w") as f:
        f.write(html_template)


if __name__ == "__main__":
    mermaid_file = "graph.mmd"
    html_file = "graph.html"

    if not os.path.exists(mermaid_file):
        print(f"Error: {mermaid_file} not found!")
        exit(1)

    webbrowser.open(f"file://{os.path.abspath(html_file)}")

    while True:
        with open(mermaid_file, "r") as f:
            mermaid_code = f.read()

        generate_html(mermaid_code, html_file)
        time.sleep(5)
