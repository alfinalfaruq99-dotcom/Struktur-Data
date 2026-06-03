import pandas as pd

# CLASS NODE
class SalesNode:

    def __init__(self,tanggal,kategori,wilayah,jumlah,pendapatan):

        self.tanggal = tanggal
        self.kategori = kategori
        self.wilayah = wilayah
        self.jumlah = jumlah
        self.pendapatan = pendapatan

        self.total = jumlah * pendapatan

        self.next = None
        self.prev = None


# =========================
# DOUBLY LINKED LIST
# =========================
class SalesLinkedList:

    def __init__(self):

        self.head = None
        self.tail = None
        self.size = 0

    # INSERT DATA
    def insert_end(self,tanggal,kategori,wilayah,jumlah,pendapatan):

        new_node = SalesNode(tanggal,kategori,wilayah,jumlah,pendapatan)

        # Jika linked list kosong
        if self.head is None:

            self.head = new_node
            self.tail = new_node

        # Jika sudah ada isi
        else:

            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

        self.size += 1

    # TRAVERSAL FORWARD
    def traversal_forward(self):

        current = self.head
        data = []

        while current:

            data.append({
                'Tanggal': current.tanggal,
                'Kategori': current.kategori,
                'Wilayah': current.wilayah,
                'Jumlah_Penjualan': current.jumlah,
                'Pendapatan': current.pendapatan,
                'Total_Pendapatan': current.total
            })

            current = current.next

        return pd.DataFrame(data)

    # SEARCH DATA
    def search_category(self, keyword):

        current = self.head
        result = []

        while current:

            if keyword.lower() in current.kategori.lower():

                result.append({
                    'Tanggal': current.tanggal,
                    'Kategori': current.kategori,
                    'Wilayah': current.wilayah,
                    'Jumlah_Penjualan': current.jumlah,
                    'Pendapatan': current.pendapatan,
                    'Total_Pendapatan': current.total
                })

            current = current.next

        return pd.DataFrame(result)
    
    # DELETE DATA

    def delete_by_category(self, category):

        current = self.head

        while current:

            if current.kategori == category:

            # Jika node pertama
             if current.prev is None:

                self.head = current.next

                if self.head:
                    self.head.prev = None

            # Jika node tengah / akhir
            else:

                current.prev.next = current.next

            # Jika node terakhir
            if current.next:
                current.next.prev = current.prev

            else:
                self.tail = current.prev

            self.size -= 1

            return True

            current = current.next

        return False
    
    # KPI DATA
def get_kpi_metrics(df):

        total_revenue = df['Total_Pendapatan'].sum()

        total_customer = len(df)

        avg_sales = df['Jumlah_Penjualan'].mean()

        avg_income = df['Pendapatan'].mean()

        return {
            
        'total_revenue': total_revenue,
        'total_customer': total_customer,
        'avg_sales': avg_sales,
        'avg_income': avg_income
        
        }