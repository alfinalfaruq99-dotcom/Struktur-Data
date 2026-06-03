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

st.write("Head:", st.session_state.sales_list.head)
st.write("Tail:", st.session_state.sales_list.tail)
st.write("Size:", st.session_state.sales_list.size)