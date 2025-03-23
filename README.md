# Economic Indicators Dashboard

## Overview
An interactive web-based dashboard that visualizes and compares key economic indicators across different countries using World Bank data. This tool enables users to analyze trends in GDP, inflation rates, and unemployment rates through an intuitive interface.

## Features
* **Multi-Country Comparison**: Select and compare multiple countries simultaneously
* **Key Economic Indicators**:
  * GDP (current US$)
  * Inflation Rate (%)
  * Unemployment Rate (%)
* **Interactive Visualization**:
  * Dynamic time-series graphs
  * Interactive legends
  * Hover tooltips with detailed information
* **User-Friendly Interface**:
  * Clean, modern dark theme
  * Intuitive country selection
  * Responsive design for all screen sizes
  * Background image with semi-transparent overlays

## Technology Stack
* **Frontend**: Streamlit, Plotly
* **Backend**: Python
* **Data Source**: World Bank API (wbgapi)
* **Styling**: Custom CSS with dark theme

## Installation

### Prerequisites
* Python 3.8 or higher
* pip (Python package installer)
* Git

### Setup Steps
1. Clone the repository
```bash
git clone https://github.com/pshah2983/economic-indicators-dashboard.git
cd economic-indicators-dashboard
```

2. Create and activate virtual environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Run the application
```bash
streamlit run src/app.py
```

5. Access the dashboard
Open your web browser and navigate to: `http://localhost:8501`

## Project Structure
```
economic-indicators-dashboard/
│
├── src/                  # Source code
│   └── app.py           # Main Streamlit application
├── static/              # Static files
│   ├── streamlit_style.css    # Custom styling
│   └── background_image.webp  # Background image
├── venv/               # Virtual environment
├── .gitignore         # Git ignore rules
├── README.md          # Project documentation
└── requirements.txt   # Project dependencies
```

## Data Sources
This project uses data from:
* World Bank API (GDP, inflation rates, unemployment rates)

## Features
* Dark theme with semi-transparent elements
* Background image for enhanced visual appeal
* Responsive design for all screen sizes
* Interactive plots with hover information
* Multi-country comparison capabilities
* Easy-to-use interface with Streamlit

## Contributing
Feel free to open issues and pull requests for any improvements.

## License
MIT License 