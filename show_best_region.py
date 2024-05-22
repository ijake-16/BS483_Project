import plotly.express as px
import plotly.graph_objects as go

# Example sequence (replace with your actual sequence)
sequence = "AGCTTAGCTAGCTACGATCGTACGATCGTAGCTAGCTACGATCGATCG" \
           "TAGCTAGCTACGATCGTACGATCGTAGCTAGCTACGATCGATCGTAGCT"

# Create a simple visualization of the sequence
fig = go.Figure()

# Add the sequence as a text annotation
fig.add_trace(go.Scatter(
    x=list(range(len(sequence))),
    y=[1] * len(sequence),
    mode="text",
    text=list(sequence),
    textposition="top center"
))

# Update layout
fig.update_layout(
    title="DNA Sequence Visualization",
    xaxis_title="Nucleotide Position",
    yaxis=dict(visible=False)
)

# Show the plot
fig.show()
