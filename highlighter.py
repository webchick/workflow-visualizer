import http.server
import socketserver


def update_graph(visited_steps):
    base_graph = """
    graph TD;
        e1[Start] --> e2[Process 1];
        e2 --> e3[Process 2];
        e3 --> e4[End];
    """

    highlight_styles = "\n".join([f"class e{step} active;" for step in visited_steps])

    style_definitions = """
    classDef active fill:#ff0000,stroke:#000,color:#fff;
    """

    graph_with_style = base_graph + "\n" + highlight_styles + "\n" + style_definitions

    with open("graph.mmd", "w") as f:
        f.write(graph_with_style)


visited_steps = []

class StepRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Use the following curl command to update step 1 to visited:
        # curl -X GET "http://localhost:8000/update-step=1"
        global visited_steps
        if self.path.startswith("/update-step"):
            try:
                step = int(self.path.split("=")[1])
                if step not in visited_steps:
                    visited_steps.append(step)
                update_graph(visited_steps)
                self.send_response(200)
                self.end_headers()
                self.wfile.write(b"Graph updated!")
            except (ValueError, IndexError):
                self.send_response(400)
                self.end_headers()
                self.wfile.write(b"Invalid step ID!")
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Invalid endpoint!")

def initialize_base_graph():
    with open("base_graph.mmd", "r") as graph_file:
        base_graph = graph_file.read()

    style_definitions = """
    classDef active fill:#ff0000,stroke:#000,color:#fff;
    """

    with open("graph.mmd", "w") as f:
        f.write(base_graph + "\n" + style_definitions)


if __name__ == "__main__":
    initialize_base_graph()
    PORT = 8000
    with socketserver.TCPServer(("", PORT), StepRequestHandler) as httpd:
        print(f"Serving HTTP on port {PORT}...")
        httpd.serve_forever()

