import streamlit as st
import logic

# KONFIGURASI HALAMAN
st.set_page_config(
    page_title="VizBiz Dashboard",
    page_icon="📊",
    layout="wide"
)

# HEADER
st.title("📊 VizBiz Analytics")

st.markdown("""
### Business Intelligence Dashboard

Pantau performa penjualan berdasarkan kategori produk dan wilayah secara real-time menggunakan implementasi Doubly Linked List.
""")

# SESSION STATE
if 'sales_list' not in st.session_state:
    st.session_state.sales_list = logic.SalesLinkedList()

# FORM INPUT DATA
with st.sidebar:

    st.header("➕ Input Data Penjualan")

    with st.form("form_penjualan"):

        tanggal = st.date_input("Tanggal")

        kategori = st.selectbox(
            "Kategori",
            [
                "Elektronik",
                "Fashion",
                "Kebutuhan Rumah",
                "Kesehatan"
            ]
        )

        wilayah = st.selectbox(
            "Wilayah",
            [
                "Jakarta",
                "Bandung",
                "Surabaya",
                "Makassar"
            ]
        )

        jumlah = st.number_input(
            "Jumlah Penjualan",
            min_value=1,
            step=1
        )

        pendapatan = st.number_input(
            "Pendapatan",
            min_value=1000
        )

        submit = st.form_submit_button("💾 Simpan Data")

        if submit:

            st.session_state.sales_list.insert_end(
                str(tanggal),
                kategori,
                wilayah,
                jumlah,
                pendapatan
            )

            st.success("Data berhasil ditambahkan")

# AMBIL DATA DARI LINKED LIST
df = st.session_state.sales_list.traversal_forward()
# KPI DASHBOARD
if not df.empty:

    st.subheader("📌 KPI Dashboard")

    metrics = logic.get_kpi_metrics(df)

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Total Revenue",
            f"Rp {metrics['total_revenue']:,.0f}"
        )

    with col2:
        st.metric(
            "Total Data",
            metrics['total_customer']
        )

    with col3:
        st.metric(
            "Rata-rata Penjualan",
            f"{metrics['avg_sales']:.2f}"
        )

    with col4:
        st.metric(
            "Rata-rata Pendapatan",
            f"Rp {metrics['avg_income']:,.0f}"
        )

        # VISUALISASI DATA
if not df.empty:

    st.subheader("📈 Visualisasi Penjualan")

    col_chart1, col_chart2 = st.columns(2)

    kategori_chart = (
        df.groupby('Kategori')['Total_Pendapatan']
        .sum()
    )

    wilayah_chart = (
        df.groupby('Wilayah')['Total_Pendapatan']
        .sum()
    )

    with col_chart1:
        st.markdown("#### Pendapatan per Kategori")
        st.bar_chart(kategori_chart)

    with col_chart2:
        st.markdown("#### Pendapatan per Wilayah")
        st.line_chart(wilayah_chart)

# SEARCH DATA
st.subheader("🔍 Cari Data")

keyword = st.text_input("Cari kategori")

if keyword:

    result = st.session_state.sales_list.search_category(
        keyword
    )

    if not result.empty:
        st.dataframe(result)
    else:
        st.warning("Data tidak ditemukan")

# TAMPILKAN DATA
st.subheader("📋 Data Penjualan")

if not df.empty:
    st.dataframe(df)
else:
    st.warning("Belum ada data")
    
    # DELETE DATA
st.subheader("🗑 Hapus Data")

hapus_kategori = st.selectbox(
    "Pilih kategori yang ingin dihapus",
    [
        "Elektronik",
        "Fashion",
        "Kebutuhan Rumah",
        "Kesehatan"
    ]
)

if st.button("Hapus Data"):

    deleted = st.session_state.sales_list.delete_by_category(
        hapus_kategori
    )

    if deleted:
        st.success("Data berhasil dihapus")
    else:
        st.error("Data tidak ditemukan")
        
        st.divider()

st.caption(
    "VizBiz Analytics Dashboard | UAS Struktur Data | Doubly Linked List + Streamlit"
)