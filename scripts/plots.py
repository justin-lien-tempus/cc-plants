import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def connect_to_database(db_path):
    """Create connection to SQLite database"""
    try:
        # Add text_factory to handle encoding issues
        conn = sqlite3.connect(db_path)
        conn.text_factory = lambda x: str(x, 'utf-8', 'ignore')
        return conn
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
        return None

def create_visualizations():
    """Create interactive visualizations for plant data"""
    
    # Connect to database
    conn = connect_to_database('../data/plants.db')  # Adjust path as needed
    
    if conn is None:
        print("Failed to connect to database")
        return
    
    # Query 1: Sunlight requirements distribution
    query1 = """
    SELECT sunlight, COUNT(*) AS num_plants 
    FROM plants 
    GROUP BY sunlight
    ORDER BY num_plants DESC;
    """
    
    # Query 2: Growth rate distribution
    query2 = """
    SELECT growth, COUNT(*) AS count
    FROM plants 
    GROUP BY growth;
    """
    
    # Query 3: Fast growing plants by sunlight type
    query3 = """
    SELECT sunlight, COUNT(*) AS fast_growing_count
    FROM plants 
    WHERE growth = 'fast'
    GROUP BY sunlight
    ORDER BY fast_growing_count DESC;
    """
    
    # Query 4: Sunlight vs Growth rate
    query4 = """
    SELECT sunlight, growth, COUNT(*) AS count
    FROM plants 
    GROUP BY sunlight, growth;
    """
    
    # Query 5: Plant name lengths by growth rate (simplified to avoid encoding issues)
    query5 = """
    SELECT growth, LENGTH(plant_name) AS name_length
    FROM plants;
    """
    
    # Execute queries and create DataFrames
    df_sunlight = pd.read_sql_query(query1, conn)
    df_growth = pd.read_sql_query(query2, conn)
    df_fast_sunlight = pd.read_sql_query(query3, conn)
    df_sunlight_growth = pd.read_sql_query(query4, conn)
    df_name_lengths = pd.read_sql_query(query5, conn)
    
    conn.close()
    
    # Create visualizations
    
    # 1. Sunlight Requirements Distribution (Bar Chart)
    fig1 = px.bar(
        df_sunlight, 
        x='sunlight', 
        y='num_plants',
        title='Distribution of Plants by Sunlight Requirements',
        labels={'sunlight': 'Sunlight Type', 'num_plants': 'Number of Plants'},
        color='num_plants',
        color_continuous_scale='viridis'
    )
    fig1.update_layout(xaxis_tickangle=-45)
    fig1.show()
    
    # 2. Growth Rate Distribution (Pie Chart)
    fig2 = px.pie(
        df_growth, 
        values='count', 
        names='growth',
        title='Plant Growth Rate Distribution',
        color_discrete_sequence=px.colors.qualitative.Set3
    )
    fig2.show()
    
    # 3. Fast Growing Plants by Sunlight (Horizontal Bar Chart)
    fig3 = px.bar(
        df_fast_sunlight, 
        x='fast_growing_count', 
        y='sunlight',
        orientation='h',
        title='Fast Growing Plants by Sunlight Type',
        labels={'fast_growing_count': 'Number of Fast Growing Plants', 'sunlight': 'Sunlight Type'},
        color='fast_growing_count',
        color_continuous_scale='greens'
    )
    fig3.show()
    
    # 4. Sunlight vs Growth Rate (Heatmap)
    pivot_df = df_sunlight_growth.pivot(index='sunlight', columns='growth', values='count').fillna(0)
    
    fig4 = px.imshow(
        pivot_df,
        labels=dict(x="Growth Rate", y="Sunlight Type", color="Number of Plants"),
        title="Plant Count by Sunlight Type and Growth Rate",
        color_continuous_scale='blues'
    )
    fig4.show()
    
    # 5. Plant Name Lengths by Growth Rate (Box Plot)
    fig5 = px.box(
        df_name_lengths, 
        x='growth', 
        y='name_length',
        title='Distribution of Plant Name Lengths by Growth Rate',
        labels={'growth': 'Growth Rate', 'name_length': 'Name Length (characters)'},
        color='growth'
    )
    fig5.show()
    
    # Create a static matplotlib visualization
    plt.style.use('seaborn-v0_8')
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 12))
    
    # Sunlight distribution
    ax1.bar(df_sunlight['sunlight'], df_sunlight['num_plants'], color='skyblue')
    ax1.set_title('Plants by Sunlight Requirements')
    ax1.set_xlabel('Sunlight Type')
    ax1.set_ylabel('Number of Plants')
    ax1.tick_params(axis='x', rotation=45)
    
    # Growth rate pie chart
    ax2.pie(df_growth['count'], labels=df_growth['growth'], autopct='%1.1f%%', startangle=90)
    ax2.set_title('Growth Rate Distribution')
    
    # Fast growing plants by sunlight
    ax3.barh(df_fast_sunlight['sunlight'], df_fast_sunlight['fast_growing_count'], color='lightgreen')
    ax3.set_title('Fast Growing Plants by Sunlight')
    ax3.set_xlabel('Number of Plants')
    
    # Name length distribution
    for growth_type in df_name_lengths['growth'].unique():
        data = df_name_lengths[df_name_lengths['growth'] == growth_type]['name_length']
        ax4.hist(data, alpha=0.7, label=growth_type, bins=10)
    ax4.set_title('Name Length Distribution by Growth Rate')
    ax4.set_xlabel('Name Length (characters)')
    ax4.set_ylabel('Frequency')
    ax4.legend()
    
    plt.tight_layout()
    plt.show()
    
    # Print some summary statistics
    print("\n=== SUMMARY STATISTICS ===")
    print(f"Total number of plants: {df_sunlight['num_plants'].sum()}")
    print(f"Most common sunlight requirement: {df_sunlight.iloc[0]['sunlight']}")
    print(f"Most common growth rate: {df_growth.loc[df_growth['count'].idxmax(), 'growth']}")
    print(f"Average plant name length: {df_name_lengths['name_length'].mean():.1f} characters")

if __name__ == "__main__":
    # Install required packages if needed:
    # pip install pandas matplotlib seaborn plotly sqlite3
    
    print("Creating plant data visualizations...")
    print("Make sure your plants.db file is in the same directory as this script!")
    
    create_visualizations()
    
    print("\nVisualization complete! Check your browser for interactive plots.")