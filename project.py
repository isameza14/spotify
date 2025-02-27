import os
import pandas as pd

def load_playlist_data(csv_path):
    """
    Loads playlist data from a CSV file.
    
    Args:
        csv_path (str): Path to the CSV file.
        
    Returns:
        pd.DataFrame: DataFrame containing the playlist data.
    """
    return pd.read_csv(csv_path)

def get_playlist_name(year_range):
    """
    Constructs the playlist name given a tuple (start_year, end_year).
    
    Args:
        year_range (tuple[int, int]): A tuple with two integers representing the start and end year.
        
    Returns:
        str: The formatted playlist name.
    """
    if year_range[0] == year_range[1]:
        return f"Top US Singles: {year_range[0]}"
    else:
        return f"Top US Singles: {year_range[0]}-{year_range[1]}"

def get_playlist_link(df, playlist_name):
    """
    Retrieves the Spotify playlist link from the DataFrame based on the playlist name.
    
    Args:
        df (pd.DataFrame): DataFrame containing the playlist data.
        playlist_name (str): The name of the playlist to look for.
        
    Returns:
        str or None: The playlist link if found; otherwise, None.
    """
    if playlist_name in df['name'].values:
        playlist = df[df['name'] == playlist_name].iloc[0]
        return playlist['link']
    else:
        return None

def main():
    """
    Main function for the command-line interface of the project.
    Loads the playlist data, constructs a playlist name with a default year range,
    and prints the matching playlist link if available.
    """
    print("Welcome to Rediscover Your Middle School Hits!")
    
    # Determine the absolute path to playlists.csv
    current_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(current_dir, "playlists.csv")
    
    # Load the playlist data
    try:
        df = load_playlist_data(csv_path)
    except Exception as e:
        print(f"Error loading CSV: {e}")
        return
    
    # For demonstration, use a default year range.
    default_year_range = (1995, 2010)
    playlist_name = get_playlist_name(default_year_range)
    playlist_link = get_playlist_link(df, playlist_name)
    
    print("Selected Year Range:", default_year_range)
    print("Playlist Name:", playlist_name)
    
    if playlist_link:
        print("Playlist Link:", playlist_link)
    else:
        print("Playlist not found for the given range.")

if __name__ == "__main__":
    main()