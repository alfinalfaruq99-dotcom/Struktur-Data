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