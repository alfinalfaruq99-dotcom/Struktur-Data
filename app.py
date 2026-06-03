import streamlit as st
import logic

# KONFIGURASI HALAMAN
st.set_page_config(
    page_title="VizBiz Dashboard",
    page_icon="📊",
    layout="wide"
)

# HEADER
st.title("📊 VizBiz Business Intelligence Dashboard")
st.caption("Dashboard Analisis Penjualan Menggunakan Doubly Linked List")

# SESSION STATE
if 'sales_list' not in st.session_state:
    st.session_state.sales_list = logic.SalesLinkedList()

st.subheader("Status Sistem")

st.success("Doubly Linked List berhasil diinisialisasi")




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

    submit = st.form_submit_button("Tambah Data")

    if submit:

        st.session_state.sales_list.insert_end(
            str(tanggal),
            kategori,
            wilayah,
            jumlah,
            pendapatan
        )

        st.success("Data berhasil ditambahkan")


