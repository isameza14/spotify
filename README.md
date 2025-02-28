# Rediscover Your Middle School Hits

#### Video Demo: [https://youtu.be/YourVideoDemoURL](https://youtu.be/YourVideoDemoURL)

#### Team Members: Isabela Meza and Amelia Jorge

#### Description:
"Rediscover Your Middle School Hits" is a complete Python project that allows users to relive the golden years of their middle school experience by giving them a custom Spotify playlist of the top songs from that era. This project integrates a command-line interface with a web application built using Streamlit, making it accessible for both technical and non-technical users. By using a CSV data source, Python modules, and testing via pytest, the project demonstrates modular, maintainable, and testable code that meets the standards of software design.

The core functionality of this project is to load pre-defined playlist data (stored in a CSV file) and, based on user input of a year range, generate a corresponding Spotify playlist link. The project is divided into multiple components:
- **Command-Line Interface:** Implemented in `project.py`, this interface allows users to run the program directly on their terminal. It takes a default or user-specified year range, constructs a unique playlist name, and prints out the corresponding Spotify link if one exists.
- **Web Interface:** The file `streamlit_app.py` utilizes Streamlit to provide an interactive experience. Users can select a year range via a slider and click a button to retrieve their playlist. All data validation, file loading, and error handling are performed to ensure a smooth user experience.
- **Data Handling:** The CSV file `playlists.csv` contains the mapping of playlist names (formatted according to year ranges, such as "Top US Singles: 1995-2010") to the actual Spotify links. This allows easy updates and maintenance without modifying the core code.
- **Testing:** To ensure the reliability and correctness of our functions, `test_project.py` contains several pytest test cases. Each custom function defined in `project.py` is tested thoroughly, ensuring modularity and error-free behavior.

This project was created as a final assignment for our course computer science. It required thoughtful design decisions to integrate different components (CLI and web interface), manage data efficiently, and adhere to high-quality coding standards. The project structure is clear and well-documented, making it easy to navigate and extend in the future.

## File Structure and Contents:
SPOTIFY [CODESPACES: ...]
├── devcontainer # Contains Codespace configuration files
├── playlists.csv # CSV file with playlist names and Spotify links
├── project.py # Command-line interface containing main() and core functions
├── README.md # This detailed project documentation file
├── requirements.txt # Lists all pip-installable dependencies
├── streamlit_app.py # Web-based application interface built with Streamlit
└── test_project.py # Pytest test cases verifying functions in project.py


## Features

- **Command-Line Interface:** Run `project.py` to see the core functionality in action, including data loading and playlist retrieval based on a default or user-specified year range.
- **Web Interface:** Use `streamlit_app.py` to interactively select a year range via a slider and view the associated Spotify playlist, making the experience approachable for all users.
- **Reusable Functions:** The project includes functions such as `load_playlist_data`, `get_playlist_name`, and `get_playlist_link` in `project.py` for efficient data handling and presentation.
- **Comprehensive Testing:** The tests in `test_project.py` ensure that each function performs as expected, providing reliability and confidence in the project's overall quality.
- **Modular and Extensible Design:** The separation of concerns and clear project structure allow for easy modifications and future enhancements, such as integrating live Spotify API data.

## Getting Started

To set up and run this project, follow these steps:

1. **Clone the Repository:**  
   ```bash
   git clone https://github.com/yourusername/your-repository.git
2. **Navigate to the Project Directory:**
    cd your-repository
3. **Install Dependencies:**
    pip install -r requirements.txt
4. Run the Command-Line Interface:
    python project.py
5. **Run the Web Application:**
    streamlit run streamlit_app.py
6. **Run Tests:**
    pytest test_project.py

## Design Decisions and Future Improvements

- **Design Choices:**
    - Modular Code: Core functions for loading data and retrieving playlists are all in project.py. This allows both the command-line and web interfaces to share the same logic.
    - Dual Interfaces: By providing both a CLI and a web-based interface (via Streamlit), the project is accessible to a wider range of users and scenarios.
    - CSV Data Storage: Using playlists.csv simplifies data updates. Playlists can be added or modified without the need to change code.
    - Testing: Extensive testing with pytest ensures each function behaves correctly, which is crucial for maintainability and future improvements.

- **Challenges and Solutions:**
    - File Path Handling: Ensuring that the CSV file loads correctly across different environments required using os.path.abspath().
    - Interface Integration: Sharing core logic between CLI and web interfaces was achieved by encapsulating functionality in independent functions.
    - User Input Validation: Error handling and clear error messages ensure that the application responds gracefully to invalid inputs or missing data.

- **Future Improvements:**
    - Spotify API Integration: Future versions might retrieve dynamic playlists directly from Spotify, replacing the static CSV file.
    - Enhanced User Personalization: Additional features such as user accounts or saving favorite playlists could be introduced.
    - Improved UI/UX: Enhancing the web interface with custom styling and interactive elements will improve user engagement.
    - Logging and Error Reporting: Integrating logging could help track usage and troubleshoot issues more efficiently.

## Conclusion

"Rediscover Your Middle School Hits" satisfies the final project requirements with both a command-line interface and an engaging web interface. By separating concerns, rigorously testing functionality, and maintaining clear documentation, this project not only delivers a nostalgic experience but also stands as a model of clean, modular, and maintainable code.

Enjoy reliving your middle school memories with every playlist, and feel free to contribute or suggest improvements!

****Credits:****
Developed by Isabela Meza and Amelia Jorge.

*(CHATGPT was used to resolve some questions/amplify this assigment)*