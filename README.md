# Workflow execution visualization
Show stackholders what parts of the business flow being executed

# Create the workflow graph
edit the base graph file `base_graph.mmd` to represent your workflow


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

# About this project

## What?
We built a workflow visualisation tool with a mermaid frontend. The objective here is to be able to track the high level progress of a given workflow in a way that makes sense for non-developers.

## How
Workflows generate state (an actual mermaid diagram) and dump it to a file. Another component then takes this file and renders it.

## Why?
The main concepts of the project are:

* Being able to track workflow progress at a higher level than child workflows. As a non-technical user, you don't care about workflows or child workflows or activities. You care about what stage of the transaction a given transaction is:
  * Has my package been delivered?
  * Has the customer been charged?
* Keeping the visualisation layer outside of temporal (not for the hackaton tho)

Some of the unanswered questions:

* How do you handle complex workflows: child workflows want to send updates to the logic, how do you do this?
  * Some ideas were building on a concept similar to OTEL tracing: a global ID for that given business transaction.
