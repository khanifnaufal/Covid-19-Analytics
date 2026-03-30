import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# ==========================================
# Konfigurasi Halaman & Tema
# ==========================================
st.set_page_config(
    page_title="Global COVID-19 Analytics",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# Custom Premium CSS UI/UX
# ==========================================
st.markdown("""
<style>
/* Font Utama */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&display=swap');
html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

/* Gradient Judul Utama */
.title-gradient {
    background: -webkit-linear-gradient(45deg, #FF6B6B, #4ECDC4, #45B7D1);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-size: 3.5rem !important;
    font-weight: 800 !important;
    margin-bottom: 0px;
    padding-bottom: 0px;
}

/* Styling Komponen Metrik (KPI Cards) */
div[data-testid="metric-container"] {
    background-color: #ffffff;
    border: 1px solid #e2e8f0;
    padding: 20px;
    border-radius: 12px;
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}
div[data-testid="metric-container"]:hover {
    transform: translateY(-5px);
    box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
    border-color: #4ECDC4;
}

/* Styling Tabs */
div[data-baseweb="tab-list"] {
    gap: 10px;
}
div[data-baseweb="tab"] {
    background-color: #f8fafc;
    border-radius: 8px 8px 0px 0px;
    padding: 10px 20px;
    border: 1px solid #e2e8f0;
    border-bottom: none;
}
div[aria-selected="true"] {
    background-color: #ffffff;
    border-top: 3px solid #4ECDC4;
    font-weight: 800;
}

/* Sidebar Styling */
[data-testid="stSidebar"] {
    background-color: #f8fafc;
    border-right: 1px solid #e2e8f0;
}
</style>
""", unsafe_allow_html=True)

# ==========================================
# Konfigurasi Tema Plotly Global
# ==========================================
# Menerapkan tampilan premium untuk semua grafik
def apply_premium_layout(fig):
    fig.update_layout(
        font_family="Inter",
        title_font_family="Inter",
        title_font_size=22,
        title_font_color="#1E293B",
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        xaxis=dict(showgrid=True, gridcolor='#e2e8f0', linecolor='#cbd5e1'),
        yaxis=dict(showgrid=True, gridcolor='#e2e8f0', linecolor='#cbd5e1'),
        hoverlabel=dict(bgcolor="white", font_size=14, font_family="Inter"),
        margin=dict(l=40, r=40, t=60, b=40)
    )
    return fig

# ==========================================
# Caching & Load Data
# ==========================================
@st.cache_data
def load_data():
    day_wise = pd.read_csv('dataset/day_wise.csv')
    world = pd.read_csv('dataset/worldometer_data.csv')
    grouped = pd.read_csv('dataset/full_grouped.csv')
    
    day_wise['Date'] = pd.to_datetime(day_wise['Date'])
    grouped['Date'] = pd.to_datetime(grouped['Date'])
    
    numeric_cols = world.select_dtypes(include=['float64', 'int64']).columns
    world[numeric_cols] = world[numeric_cols].fillna(0)
    
    try:
        usa = pd.read_csv('dataset/usa_county_wise.csv')
        usa['Date'] = pd.to_datetime(usa['Date'], format='mixed')
    except Exception:
        usa = pd.DataFrame()
        
    return day_wise, world, grouped, usa

with st.spinner('Memuat simulasi sekumpulan database COVID-19 skala besar...'):
    df_day, df_world, df_grouped, df_usa = load_data()

# ==========================================
# Header & KPI Utama
# ==========================================
# Menggunakan kolom untuk Logo dan Teks
col_head1, col_head2 = st.columns([1, 10])
with col_head1:
    st.image("https://cdn-icons-png.flaticon.com/512/2913/2913604.png", width=70)
with col_head2:
    st.markdown('<h1 class="title-gradient">Global COVID-19 Analytics</h1>', unsafe_allow_html=True)

st.markdown("""
<div style='color: #64748b; font-size: 1.1rem; margin-bottom: 20px;'>
Dashboard interaktif premium yang menyajikan analisis menyeluruh mengenai pandemi COVID-19 menggunakan integrasi miliaran parameter skala global.
</div>
""", unsafe_allow_html=True)

global_cases = df_world['TotalCases'].sum()
global_deaths = df_world['TotalDeaths'].sum()
global_recovered = df_world['TotalRecovered'].sum()

# Card Metrics
c1, c2, c3 = st.columns(3)
with c1:
    st.metric("🌍 Total Kasus Terkonfirmasi", f"{global_cases:,.0f}")
with c2:
    st.metric("💀 Angka Kematian Absolut", f"{global_deaths:,.0f}")
with c3:
    st.metric("❤️ Total Pasien Sembuh", f"{global_recovered:,.0f}")
    
st.markdown("<br>", unsafe_allow_html=True)

# ==========================================
# TABS NAVIGASI UTAMA
# ==========================================
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📈 TREN GLOBAL", 
    "🗺️ PETA DUNIA", 
    "📊 KOMPARASI NEGARA", 
    "🏆 PAPAN PERINGKAT", 
    "🇺🇸 EPISENTRUM USA"
])

# ------------------------------------------
# TAB 1: Tren Pandemi Global
# ------------------------------------------
with tab1:
    st.markdown("### 📈 Eskalasi Tren Pandemi Global")
    st.markdown("<span style='color: #64748b;'>Grafik ini menggambarkan kurva interaktif pergerakan agregat harian infeksi di seluruh penjuru dunia.</span>", unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    metric_options = st.multiselect(
        "Pilih Dimensi Parameter Kurva:",
        ['Confirmed', 'Recovered', 'Deaths', 'Active', 'New cases'],
        default=['Confirmed', 'Recovered', 'Deaths']
    )
    
    if metric_options:
        fig_global_trend = px.line(
            df_day, x='Date', y=metric_options,
            color_discrete_sequence=['#3b82f6', '#10b981', '#ef4444', '#f59e0b', '#8b5cf6'],
            labels={'value': 'Total Akumulasi', 'Date': 'Garis Waktu (Bulan/Tahun)', 'variable': 'Metrik'}
        )
        # Menghapus title dari parameter agar kita bisa gunakan custom styling
        fig_global_trend.update_layout(title="<b>Kurva Waktu COVID-19 Sejagat</b>")
        fig_global_trend.update_layout(hovermode="x unified")
        fig_global_trend.update_traces(line=dict(width=3.5))
        fig_global_trend = apply_premium_layout(fig_global_trend)
        
        st.plotly_chart(fig_global_trend, use_container_width=True)
    else:
        st.warning("⚠️ Opsi metrik kurva tidak boleh kosong.")

# ------------------------------------------
# TAB 2: Peta Persebaran Kasus
# ------------------------------------------
with tab2:
    st.markdown("### 🗺️ Lanskap Geografis Terkini")
    st.markdown("<span style='color: #64748b;'>Interpretasi visual tata letak geopolitik terkait hantaman wabah (Choropleth Map).</span>", unsafe_allow_html=True)
    
    col_map_1, col_map_2 = st.columns([1, 4])
    with col_map_1:
        st.markdown("<br><br>", unsafe_allow_html=True)
        metric_map = st.selectbox(
            "📍 Pilih Metrik Sensitivitas Peta:",
            ['TotalCases', 'TotalDeaths', 'ActiveCases', 'TotalTests', 'Deaths/1M pop']
        )
        st.info("💡 Arahkan kursor Anda ke sebuah negara di dalam peta untuk melihat angka absolut yang spesifik dari wilayah tersebut.")
        
    with col_map_2:
        colorscale_choice = px.colors.sequential.Viridis if 'Tests' in metric_map else px.colors.sequential.Sunsetdark
        
        fig_map = px.choropleth(
            df_world,
            locations="Country/Region",
            locationmode="country names",
            color=metric_map,
            hover_name="Country/Region",
            hover_data=['TotalCases', 'TotalDeaths', 'TotalRecovered', 'Population'],
            color_continuous_scale=colorscale_choice,
        )
        fig_map.update_layout(
            geo=dict(
                showframe=False,
                showcoastlines=True,
                coastlinecolor="#cbd5e1",
                projection_type='natural earth',
                bgcolor='rgba(0,0,0,0)'
            ),
            margin=dict(l=0, r=0, t=10, b=0),
            paper_bgcolor="rgba(0,0,0,0)",
        )
        st.plotly_chart(fig_map, use_container_width=True)

# ------------------------------------------
# TAB 3: Komparasi Negara
# ------------------------------------------
with tab3:
    st.markdown("### 📊 Head-to-Head Komparasi Negara")
    st.markdown("<span style='color: #64748b;'>Sandandingkan laju kecepatan perpindahan virus secara langsung (*side-by-side*) dari berbagai negara pilihan Anda.</span>", unsafe_allow_html=True)
    
    col_c1, col_c2 = st.columns([1, 2])
    all_countries = df_grouped['Country/Region'].unique().tolist()
    def_countries = ['US', 'India', 'Brazil'] if 'US' in all_countries else all_countries[:3]
    
    with col_c1:
        selected_countries = st.multiselect(
            "🔍 Pilih Negara untuk Diadu:",
            all_countries,
            default=def_countries
        )
        comp_metric = st.radio("📈 Evaluator Kurva:", ['Confirmed', 'Deaths', 'New cases', 'Active'], horizontal=True)
    
    if selected_countries:
        comp_df = df_grouped[df_grouped['Country/Region'].isin(selected_countries)]
        
        fig_comp = px.line(
            comp_df, x='Date', y=comp_metric, color='Country/Region',
            labels={comp_metric: f"Angka {comp_metric}"},
            color_discrete_sequence=px.colors.qualitative.Bold
        )
        fig_comp.update_layout(hovermode="x unified")
        fig_comp.update_traces(line=dict(width=3))
        fig_comp = apply_premium_layout(fig_comp)
        
        st.plotly_chart(fig_comp, use_container_width=True)

# ------------------------------------------
# TAB 4: Papan Peringkat
# ------------------------------------------
with tab4:
    st.markdown("### 🏆 Papan Klasemen Internasional")
    st.markdown("<span style='color: #64748b;'>Mengamati peringkat ketahanan dan keterpurukan performa mitigasi pandemi negara secara global.</span>", unsafe_allow_html=True)
    
    sort_by = st.selectbox(
        "Kriteria Penyusunan Klasemen (Top 15):",
        ['TotalCases', 'TotalDeaths', 'TotalRecovered', 'Tests/1M pop', 'Deaths/1M pop']
    )
    
    df_board = df_world[df_world['Country/Region'].notna()]
    df_board = df_board.sort_values(sort_by, ascending=False).head(15)
    
    fig_board = px.bar(
        df_board, x=sort_by, y='Country/Region',
        orientation='h',
        color=sort_by,
        color_continuous_scale='Magma' if 'Death' in sort_by else 'Teal',
        text_auto=".2s"
    )
    fig_board.update_layout(yaxis={'categoryorder':'total ascending'})
    fig_board = apply_premium_layout(fig_board)
    # Hide axis titles for cleaner look
    fig_board.update_xaxes(title="")
    fig_board.update_yaxes(title="")
    
    st.plotly_chart(fig_board, use_container_width=True)

# ------------------------------------------
# TAB 5: Pelacakan Episentrum USA
# ------------------------------------------
with tab5:
    st.markdown("### 🇺🇸 Kedalaman Spasial (USA Data Drilling)")
    st.markdown("<span style='color: #64748b;'>Representasi detail jutaan laporan untuk mengekstraksi tingkat gawat darurat spesifik per negara bagian (State) di AS.</span>", unsafe_allow_html=True)
    
    if not df_usa.empty:
        max_date = df_usa['Date'].max()
        usa_latest = df_usa[df_usa['Date'] == max_date].copy()
        
        state_aggr = usa_latest.groupby('Province_State')[['Confirmed', 'Deaths']].sum().reset_index()
        state_aggr = state_aggr.sort_values('Confirmed', ascending=False)
        
        st.info(f"📅 **Data Akurat Tertanggal: {max_date.strftime('%d %B %Y')}**")
        
        col_us_1, col_us_2 = st.columns([6, 4])
        with col_us_1:
            fig_us_bar = px.bar(
                state_aggr.head(15), x='Confirmed', y='Province_State', orientation='h',
                color='Deaths',
                color_continuous_scale="Reds",
                labels={'Confirmed':'Total Kasus Terkonfirmasi', 'Province_State':'Negara Bagian', 'Deaths':'Kematian'},
                title="Top 15 Terparah"
            )
            fig_us_bar.update_layout(yaxis={'categoryorder':'total ascending'})
            fig_us_bar = apply_premium_layout(fig_us_bar)
            st.plotly_chart(fig_us_bar, use_container_width=True)
            
        with col_us_2:
            st.markdown("<br><br>", unsafe_allow_html=True)
            # Menampilkan tabel premium dengan style bawaan Pandas
            st.dataframe(
                state_aggr[['Province_State', 'Confirmed', 'Deaths']].style.background_gradient(cmap='Reds', subset=['Deaths']), 
                hide_index=True,
                use_container_width=True,
                height=450
            )
    else:
        st.error("Gagal menjangkau dataset `usa_county_wise.csv`.")

st.markdown("<br><br>", unsafe_allow_html=True)
st.divider()
st.caption("✨ Dibuat oleh: Khanifnaufal | Data Analyst Portfolio Project")
