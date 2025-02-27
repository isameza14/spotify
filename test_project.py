import os
import pandas as pd
import tempfile
import pytest
from project import load_playlist_data, get_playlist_name, get_playlist_link

def test_get_playlist_name_same_year():
    assert get_playlist_name((2000, 2000)) == "Top US Singles: 2000"

def test_get_playlist_name_range():
    assert get_playlist_name((1995, 2010)) == "Top US Singles: 1995-2010"

def test_load_playlist_data(tmp_path):
    # Create a temporary CSV file with sample data.
    sample_data = "name,link\nTop US Singles: 1995-2010,https://example.com/playlist1\n"
    temp_file = tmp_path / "playlists.csv"
    temp_file.write_text(sample_data)
    
    df = load_playlist_data(str(temp_file))
    assert 'name' in df.columns
    assert 'link' in df.columns
    assert df.iloc[0]['name'] == "Top US Singles: 1995-2010"

def test_get_playlist_link():
    # Create a DataFrame that mimics playlists.csv
    data = {
        "name": ["Top US Singles: 1995-2010", "Top US Singles: 2000"],
        "link": ["https://example.com/playlist1", "https://example.com/playlist2"]
    }
    df = pd.DataFrame(data)
    
    result = get_playlist_link(df, "Top US Singles: 1995-2010")
    assert result == "https://example.com/playlist1"
    
    result_none = get_playlist_link(df, "Top US Singles: 2010")
    assert result_none is None