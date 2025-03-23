import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import wbgapi as wb
import pathlib
import base64

# Set page config
st.set_page_config(
    page_title="Economic Indicators Dashboard",
    page_icon="📈",
    layout="wide"
)

# Load external CSS
def load_css():
    css_file = pathlib.Path(__file__).parent.parent / 'static' / 'streamlit_style.css'
    with open(css_file) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Load CSS
load_css()

# Add background image
def add_bg_from_local(image_file):
    with open(image_file, "rb") as file:
        encoded_string = base64.b64encode(file.read())
    st.markdown(
    f"""
    <style>
    .stApp > header + div {{
        background-image: url(data:image/webp;base64,{encoded_string.decode()});
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    </style>
    """,
    unsafe_allow_html=True
    )

# Load background image
bg_image = pathlib.Path(__file__).parent.parent / 'static' / 'background_image.webp'
if bg_image.exists():
    add_bg_from_local(str(bg_image))

@st.cache_data
def get_country_list():
    """Get list of all available countries from World Bank API"""
    countries = {}
    for country in wb.economy.list():
        country_id = country['id']
        if len(country_id) == 3 and country_id not in ['INX', 'XKX']:
            countries[country_id] = country['value']
    return countries

def create_visualization(selected_countries):
    if not selected_countries:
        return go.Figure()
        
    indicators = {
        'NY.GDP.MKTP.CD': 'GDP (current US$)',
        'FP.CPI.TOTL.ZG': 'Inflation Rate (%)',
        'SL.UEM.TOTL.ZS': 'Unemployment Rate (%)'
    }
    
    # Create tabs for different indicators
    tabs = st.tabs(list(indicators.values()))
    
    for tab, (indicator_code, indicator_name) in zip(tabs, indicators.items()):
        with tab:
            with st.spinner(f'Loading {indicator_name} data...'):
                df = wb.data.DataFrame(indicator_code, selected_countries, mrv=20)
                
                fig = go.Figure()
                for country in df.index:
                    fig.add_trace(
                        go.Scatter(
                            x=df.columns,
                            y=df.loc[country].values,
                            name=country,
                            mode='lines+markers'
                        )
                    )
                    
                fig.update_layout(
                    title=f"{indicator_name} by Country",
                    xaxis_title="Year",
                    yaxis_title="Value",
                    height=500,
                    template='plotly_dark',
                    hovermode='x unified',
                    margin=dict(t=50, l=50, r=50, b=50),
                    paper_bgcolor='rgba(26, 26, 26, 0.7)',
                    plot_bgcolor='rgba(26, 26, 26, 0.7)',
                    font=dict(color='#a8a8a8'),
                    xaxis=dict(gridcolor='rgba(168, 168, 168, 0.1)'),
                    yaxis=dict(gridcolor='rgba(168, 168, 168, 0.1)'),
                    legend=dict(
                        font=dict(size=14),
                        bgcolor='rgba(26, 26, 26, 0.7)',
                        bordercolor='rgba(168, 168, 168, 0.3)'
                    )
                )
                
                st.plotly_chart(fig, use_container_width=True)

def main():
    st.title("Economic Indicators Dashboard")
    
    # Sidebar
    with st.sidebar:
        st.markdown("### Country Selection")
        countries = get_country_list()
        selected_countries = st.multiselect(
            "Select countries to compare",
            options=list(countries.keys()),
            default=['USA', 'CHN', 'IND'],
            format_func=lambda x: countries[x]
        )
        
        st.markdown("""
        ### About This Dashboard
        This interactive dashboard visualizes key economic indicators across different countries:
        - GDP (current US$)
        - Inflation Rate (%)
        - Unemployment Rate (%)
        
        Select multiple countries from the list to compare their economic indicators.
        Use the tabs above the chart to switch between different indicators.
        """)
    
    # Main content
    if not selected_countries:
        st.warning("Please select at least one country from the sidebar.")
    else:
        create_visualization(selected_countries)

if __name__ == "__main__":
    main() 