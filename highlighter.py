import time


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


if __name__ == "__main__":
    visited_steps = []
    steps = [1, 2, 3, 4]

    for step in steps:
        visited_steps.append(step)
        update_graph(visited_steps)
        time.sleep(5)
