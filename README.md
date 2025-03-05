# Workflow execution visualization
Show stackholders what parts of the business flow being executed

# Create the workflow graph
edit the base graph file `base_graph.mmd`


### Run the highlighter server

```bash
python highlighter.py
```

### Run the UI server

```bash
python ui_server.py

```
### Updating a Node in the Execution Graph

Use the following `curl` command to update a node in the execution graph:

```bash
curl -X GET "http://localhost:8000/update-step=N"
```

Replace `N` with the specific step or node value you wish to update.


