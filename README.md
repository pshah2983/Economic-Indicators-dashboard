# Economic Indicators Dashboard

## Overview
An interactive web-based dashboard that visualizes and compares key economic indicators across different countries using World Bank data. This tool enables users to analyze trends in GDP, inflation rates, and unemployment rates through an intuitive interface.

## Features
- **Multi-Country Comparison**: Select and compare multiple countries simultaneously
- **Key Economic Indicators**:
  - GDP (current US$)
  - Inflation Rate (%)
  - Unemployment Rate (%)
- **Interactive Visualization**:
  - Dynamic time-series graphs
  - Interactive legends
  - Hover tooltips with detailed information
- **User-Friendly Interface**:
  - Dropdown menu for country selection
  - One-click updates
  - Responsive design for all screen sizes

## Technology Stack
- **Frontend**: Dash, Plotly
- **Backend**: Python
- **Data Source**: World Bank API (wbgapi)
- **Styling**: Dash Bootstrap Components

## Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)
- Git

### Setup Steps
1. Clone the repository
```bash
git clone https://github.com/yourusername/economic-indicators-dashboard.git
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
python src/app.py
```

5. Access the dashboard
Open your web browser and navigate to: `http://127.0.0.1:8050`

## Project Structure

```
economic-indicators-dashboard/
│
├── data/                  # Data storage directory
├── docs/                  # Documentation files
├── notebooks/            # Jupyter notebooks for analysis
├── src/                  # Source code
├── static/              # Static files (CSS, JS)
├── templates/           # HTML templates
└── tests/               # Unit tests
```

## Data Sources

This project uses data from:
- World Bank API (GDP, inflation rates)
- Other economic databases (as needed)

## Contributing

Feel free to open issues and pull requests for any improvements.

## License

MIT License 