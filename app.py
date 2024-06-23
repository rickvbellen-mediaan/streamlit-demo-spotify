import streamlit as st
import pandas as pd

def main():
    st.title("My Streamlit App")
    
    data = st.file_uploader("Upload a dataset", type="csv")

    if data is not None:
        df = pd.read_csv(data)
        selected_artist = st.selectbox("Select an artist", df["artists"].unique())
        filtered_df = df[df['artists'] == selected_artist]
        st.dataframe(filtered_df)
        st.bar_chart(filtered_df, x="album_name", y="danceability")

main()