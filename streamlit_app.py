import os
import pandas as pd
import streamlit as st

current_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(current_dir, "playlists.csv")

st.markdown("# Rediscover Your Middle School Hits")
st.write("Hey there! Remember your middle school days? Select the years you were in school and I'll create a Spotify playlist featuring the top hits from that era.")

df = pd.read_csv(csv_path)
year_range = st.slider("Select your middle school years:", min_value=1958, max_value=2022, value=(1995, 2010))

if st.button("Show me my playlist!"):
    if year_range[0] == year_range[1]:
        playlist_name = f"Top US Singles: {year_range[0]}"
    else:
        playlist_name = f"Top US Singles: {year_range[0]}-{year_range[1]}"
    
    if playlist_name in df['name'].values:
        playlist = df[df['name'] == playlist_name].iloc[0]
        st.markdown(f"### Here it is: [**{playlist['name']}**]({playlist['link']})")
    else:
        st.error("Oops! We don't have a playlist for that range. Try selecting a shorter span of years.")