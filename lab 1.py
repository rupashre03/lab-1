# ---------- GRAPH ----------
graph = {
    'A': ['B', 'D'],
    'B': ['C', 'E', 'G'],
    'C': ['A'],
    'D': ['C'],
    'E': ['H'],
    'G': ['F', 'H'],
    'H': ['F', 'G'],
    'F': []
}

# ---------- BFS ----------
def bfs(start):
    visited = []
    queue = [start]

    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)

            # alphabetical neighbours
            for neigh in sorted(graph[node]):
                if neigh not in visited and neigh not in queue:
                    queue.append(neigh)

    return visited


# ---------- DFS ----------
def dfs(start):
    visited = []
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)

            # push in reverse alphabetical so pop follows A→Z
            for neigh in sorted(graph[node], reverse=True):
                if neigh not in visited:
                    stack.append(neigh)

    return visited


print("BFS order:", bfs('A'))
print("DFS order:", dfs('A'))


# ---------- STREAMLIT UI ----------
import streamlit as st

st.title("BFS & DFS Traversal (Alphabetical Ordering)")
st.write("This app runs BFS and DFS on the directed graph from Lab Report 1.")

st.subheader("Graph (Adjacency List)")
st.json(graph)

start_node = st.selectbox("Choose a starting node:", list(graph.keys()), index=0)

if st.button("Run Traversals"):
    bfs_result = bfs(start_node)
    dfs_result = dfs(start_node)

    st.subheader("BFS Result (Alphabetical)")
    st.write(" → ".join(bfs_result))

    st.subheader("DFS Result (Alphabetical)")
    st.write(" → ".join(dfs_result))

st.caption("BSD3513 • Lab 1 • Graph Search Algorithms")
