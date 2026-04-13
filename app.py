import streamlit as st
from benchmark import benchmark, MODELS, MODEL_INFO

st.set_page_config(page_title="Model Benchmark", page_icon="⚡", layout="wide")
st.title("⚡ LLM Model Comparison Dashboard")
st.caption("Run the same prompt across multiple local models and compare speed vs quality")

prompt = st.text_area(
    "Enter your prompt",
    value="Explain what overfitting is in machine learning in 2 sentences.",
    height=100
)

if st.button("Run Benchmark", type="primary"):
    if not prompt.strip():
        st.warning("Please enter a prompt first.")
    else:
        with st.spinner("Running all models... this may take a minute."):
            results = benchmark(prompt)

        st.divider()
        st.subheader("Results")

        fastest = min(results, key=lambda x: x["time"])
        slowest = max(results, key=lambda x: x["time"])
        cols = st.columns(len(MODELS))

        for i, result in enumerate(results):
            with cols[i]:
                is_fastest = result["model"] == fastest["model"]

                if is_fastest:
                    st.success(f"🏆 {result['model']}")
                else:
                    st.info(f"🤖 {result['model']}")

                info = MODEL_INFO[result["model"]]
                st.caption(f"{info['size']} · {info['params']} params")

                st.metric("Response time", f"{result['time']}s")

                bar_pct = result["time"] / slowest["time"]
                st.progress(bar_pct)

                st.markdown("**Answer:**")
                st.write(result["response"])

        st.divider()
        st.subheader("Summary")

        m1, m2, m3 = st.columns(3)
        speed_diff = round(slowest["time"] / fastest["time"], 1)

        m1.metric("Fastest model", fastest["model"])
        m2.metric("Fastest time", f"{fastest['time']}s")
        m3.metric("Speed difference", f"{speed_diff}x")