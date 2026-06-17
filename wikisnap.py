import wikipedia
import streamlit as st

wikipedia.set_user_agent("MyEducationApp/1.0 (contact: test@example.com)")

st.title("📚 WikiSummarizer")
st.caption("Fast Wikipedia summaries powered by Wikipedia API")


search_phrase = st.text_input("Enter a topic to search:")

st.sidebar.title("Settings")
sentences = st.sidebar.slider("Summary length", 1, 10, 3)

@st.cache_data
def get_summary(topic, sentences):
    return wikipedia.summary(topic, sentences=sentences)

if st.button("Get Summary"):

    if not search_phrase.strip():
        st.stop()
        st.warning("Please enter a valid topic.")
    else:
        try:
            with st.spinner("Fetching Wikipedia summary..."):
                summary = get_summary(search_phrase, sentences)
                st.markdown("### Summary")
                st.markdown(f"#### Topic: {search_phrase}")
                st.info(summary)

        except wikipedia.exceptions.DisambiguationError as e:
            st.error("Too vague. Try one of these options:")
            st.write(e.options[:5])

        except wikipedia.exceptions.PageError:
            st.error("No page found for that topic.")

        except Exception as e:
            st.error(f"Unexpected error: {e}")

else:
    st.info("Enter a topic and click 'Get Summary' to begin.")