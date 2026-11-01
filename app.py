import streamlit as st
from practicals import PRACTICALS

st.set_page_config(
    page_title="ML Practical Code Finder",
    page_icon="📘",
    layout="centered",
)

st.title("📘 ML Practical Code Finder")
st.write("Open a link with a practical number to display its Python code.")

# Read the practical number from the URL query parameter.
# Example: https://your-app.streamlit.app/?practical=3
raw_number = st.query_params.get("practical", "")

if isinstance(raw_number, list):
    raw_number = raw_number[0] if raw_number else ""

if raw_number:
    try:
        practical_number = int(raw_number)
    except (TypeError, ValueError):
        practical_number = None

    if practical_number is None:
        st.error("The practical number in the URL must be a whole number.")
    elif practical_number not in PRACTICALS:
        available = ", ".join(str(n) for n in sorted(PRACTICALS))
        st.warning(f"Practical {practical_number} was not found.")
        st.caption(f"Available practical numbers: {available}")
    else:
        practical = PRACTICALS[practical_number]
        st.subheader(f"Practical {practical_number}: {practical['title']}")
        st.caption(practical.get("description", ""))
        st.code(practical["code"], language="python")
        st.caption("Use the copy icon on the code block to copy the practical.")
else:
    st.info("Add a practical number to the URL, for example: `?practical=1`")

    available_numbers = sorted(PRACTICALS)
    st.subheader("Available practicals")
    for number in available_numbers:
        practical = PRACTICALS[number]
        st.markdown(
            f"- **Practical {number}:** {practical['title']} "
            f"— [Open practical](?practical={number})"
        )

st.divider()
st.caption("Practical code reference • Runs in your browser • Created with Streamlit")
