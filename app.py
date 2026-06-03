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