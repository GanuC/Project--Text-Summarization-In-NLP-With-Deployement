import streamlit as st
import text_summary as ts
st.header("Text Summarization")
text = st.text_input("Enter Your Text Here")
if(st.button("Get_Summary")):
	st.subheader("Your Original Text")
	#st.text("Your Original Text")
	st.write(" ",text)
	#summary, doc,len(rawdocs.split(' ')),len(summary.split(' '))
	summary,doc,len_oriText,len_summText = ts.summarizer(text)
	st.subheader("Summary:")
	st.write(summary)
	st.write("Length of Original Text:",len_oriText)
	st.write("Length of Summary Text:",len_summText)
