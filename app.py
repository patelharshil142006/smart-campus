import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt

st.markdown("""
<style>

/* ---- Background ---- */

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');

/* Apply font globally */
html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
}
.stApp {
    background: #3B4953;
    color : #EBF4DD;
    font-family: Lucida Handwriting;
}

/* ---- Titles ---- */
h1 {
    text-align: center;
    color:#90AB8B ;
    font-weight: 800;
}
h2, h3 {
    color: #5A7863;
}

/* ---- Card Style ---- */
.card {
    background: rgba(255, 255, 255, 0.15);
    backdrop-filter: blur(12px);
    border-radius: 20px;
    padding: 25px;
    margin-bottom: 20px;
    box-shadow: 0 8px 25px rgba(0,0,0,0.3);
}

/* ---- Inputs ---- */
.stSelectbox select, .stTextInput input {
    border-radius: 12px !important;
    color : #3B4953;
    font-size: 16px;
    padding: 10px;
}


/* ---- Button ---- */
.stButton > button {
    width: 100%;
    background: #90AB8B;
    color:#344F1F ;
    font-size: 18px;
    font-weight: bold;
    padding: 14px;
    border-radius: 15px;
    border: none;
    transition: all 0.3s ease;
}
.stButton > button:hover {
    transform: scale(1.05);
    background: #5A7863;
    color : white;
}

/* ---- Map Container ---- */
.map-box {
    background: #90AB8B;
    border-radius: 20px;
    padding: 15px;
    margin-top: 20px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.4);
}

/* ---- Footer ---- */
.footer {
    text-align: center;
    color: #5A7863;
    font-size: 14px;
    margin-top: 40px;
}

.stwarning {
    color : black;
}

</style>
""", unsafe_allow_html=True)

campus_coordinates = {

    "A": (9, 5),
    "B": (7, 0),
    "C": (5, 5),
    "D": (3, 0),
    "E": (1, 5),
    "F": (3, 10),
    "G": (1, 15),
    "H": (3, 20),
    "I": (5, 15),
    "J": (7, 20),
    "K": (9, 15),
    "L": (7, 10),
    "M": (3, 35),
    "N": (1, 33),
    "W": (6, 30)
}

campus_graph = nx.Graph()

# Add nodes
for block in campus_coordinates:
    campus_graph.add_node(block)

# Add edges (paths)
edges = [
    ("A", "L"), ("C", "L"), ("K", "L"), ("I", "L"),
    ("C", "B"), ("C", "D"), ("C", "F"),
    ("D", "E"), ("F", "G"), ("F", "I"),
    ("I", "H"), ("I", "J"), ("I", "W"),
    ("M", "N"), ("M", "W")
]

campus_graph.add_edges_from(edges)

def draw_campus_map(graph, coordinates, path=None):
    fig, ax = plt.subplots(figsize=(8, 10))

    # Draw full campus
    nx.draw(
        graph,
        pos=coordinates,
        with_labels=True,
        node_color="#3B4953",
        node_size=2500,
        font_size=14,
        font_color="white",
        font_weight="bold",
        width=3,
        ax=ax
    )

# Highlight shortest path
    if path:
        path_edges = list(zip(path, path[1:]))

        nx.draw_networkx_edges(
            graph,
            pos=coordinates,
            edgelist=path_edges,
            edge_color="#5A7863",
            width=6,
            ax=ax
        )

        nx.draw_networkx_nodes(
            graph,
            pos=coordinates,
            nodelist=path,
            node_color="#5A7863",
            node_size=3000,
            ax=ax
        )

    ax.set_title("VGEC Campus Navigation Map")
    st.pyplot(fig)

st.set_page_config(page_title="Campus Navigator" ,page_icon=":compass:",initial_sidebar_state="expanded")
st.title("🧭 Smart Campus Block Navigator")
st.write("Navigate easily between campus blocks using visual routing.")

# st.markdown("<div class='card'>", unsafe_allow_html=True)

st.subheader("📍 Step 1: Select Your Current Block")
source_block = st.selectbox(
    "You are currently at",
    sorted(campus_coordinates.keys())
)

st.subheader("🎯 Step 2: Select Destination Block")
destination_block = st.selectbox(
    "You want to go to",
    sorted(campus_coordinates.keys())
)

# st.markdown("</div>", unsafe_allow_html=True)

# st.markdown("<div class='card'>", unsafe_allow_html=True)
navigate = st.button("🧭 Start Navigation")
# st.markdown("</div>", unsafe_allow_html=True)


if navigate:
    if source_block == destination_block:
        st.warning("You are already at the destination block.")
    else:
        try:
            path = nx.shortest_path(
                campus_graph,
                source_block,
                destination_block
            )

            st.success("✅ Route Found!")
            st.info("🚶 Follow the green highlighted path on the map.")

            # st.markdown("<div class='map-box'>", unsafe_allow_html=True)
            st.subheader("🗺️ Campus Route")
            draw_campus_map(campus_graph, campus_coordinates, path)
            # st.markdown("</div>", unsafe_allow_html=True)

            st.info(f"🏁 Destination Reached: Block {destination_block}")

        except nx.NetworkXNoPath:
            st.error("❌ No path exists between selected blocks.")

