import streamlit as st
from utils import extract_text_from_pdf
from qa_chain import create_qa_chain

st.set_page_config(page_title="📄 Chat with PDF (Groq)", layout="wide")
st.title("📄 PDF Insights & Q&A (LLM-powered)")

uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

if uploaded_file:
    with st.spinner("Extracting PDF text..."):
        pdf_text = extract_text_from_pdf(uploaded_file)
        st.success("PDF text extracted.")

    chain = create_qa_chain(pdf_text)

    st.subheader("Ask questions about the PDF:")

    user_query = st.text_input("Enter your question here")

    if user_query:
        with st.spinner("Searching..."):
            output = chain.invoke(user_query)

        st.markdown("### 🧠 Answer:")
        st.write(output['result'])

        with st.expander("📚 Source Documents"):
            for doc in output["source_documents"]:
                st.markdown(doc.page_content)
