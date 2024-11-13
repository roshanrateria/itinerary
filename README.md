# Itinerary 🎒

## Introduction 📜
Itinerary is a Flask-based web application designed to help users plan and organize their travel itineraries. The app allows users to create itineraries, add accommodations and activities, and view or edit their travel plans. This project uses Flask for the web framework and SQLAlchemy for database management.

## Features ✨
- Create and manage travel itineraries
- Add accommodations and activities to each itinerary
- View and edit existing itineraries
- Delete accommodations and activities

## Impact 🌟
This project simplifies travel planning by providing a centralized platform to organize all trip details. Users can efficiently manage their itineraries, ensuring a well-organized and enjoyable travel experience.

## Business Use Case 💼
Planning a trip can be a daunting task with various details to manage, such as accommodations, activities, and dates. Itinerary aims to solve this problem by offering a user-friendly platform where travelers can easily create, manage, and customize their travel plans. This ensures that all necessary information is organized in one place, reducing the risk of oversight and enhancing the overall travel experience.

## Installation ⚙️
1. Clone the repository:
   ```sh
   git clone https://github.com/roshanrateria/itinerary.git
   ```
2. Navigate to the project directory:
   ```sh
   cd itinerary
   ```
3. Install the required dependencies:
   ```sh
   pip install flask flask_sqlalchemy
   ```
4. Run the application:
   ```sh
   python app.py
   ```

## Usage 📖
1. Open your web browser and navigate to `http://127.0.0.1:5000/`.

## Project Structure 🗂️
- `app.py`: The main application file containing routes, models, and database initialization.
- `static/styles.css`: The stylesheet for the application's frontend.
- `templates/`: Directory containing HTML templates for rendering different pages.
  - `create_itinerary.html`: Template for creating a new itinerary.
  - `edit_itinerary.html`: Template for editing an existing itinerary.
  - `layout.html`: Base layout template for the application.
  - `view_itinerary.html`: Template for viewing a specific itinerary.
- `instance/travel_planner.db`: SQLite database file storing the itinerary data.

## Future Enhancements 🚀
- Integrate a user authentication system to allow multiple users to manage their itineraries.
- Add the ability to share itineraries with others.
- Implement a calendar view to visualize the itinerary schedule.
- Allow users to attach documents or images to activities and accommodations.

## Common Issues and Troubleshooting 🛠️
- **Database Connection Error**: Ensure that the SQLite database file (`travel_planner.db`) is located in the `instance` directory.
- **Flask Server Not Starting**: Verify that Flask and SQLAlchemy are installed correctly by running `pip install flask flask_sqlalchemy`.
- **Page Not Found**: Check the URL and ensure the Flask routes are defined correctly in `app.py`.


## Contact 📬
- **Author**: [Roshan Rateria](https://github.com/roshanrateria)
