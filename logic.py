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