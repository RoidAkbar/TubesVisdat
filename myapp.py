#!/usr/bin/env python
# coding: utf-8

# **FINAL PROJECT VISDAT - PERGERAKAN SAHAM**
# 
# Anggota Kelompok:
# 1.   Muhammad Ro'id Akbar Aslami
# 2.   Dhikayla Azizah Putri
# 3.   Ghifari Fazlul Makmur

# In[97]:


# Data handling
import pandas as pd
import numpy as np

# Bokeh libraries
from bokeh.io import output_file, output_notebook
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource
from bokeh.layouts import row, column, gridplot
from bokeh.models.widgets import Tabs, Panel


# In[98]:


# Baca dataset
df_sm = pd.read_csv('stock_market.csv')


# In[99]:


df_sm.head()


# In[100]:


# Mengubah column Date menjadi datetime
df_sm['Date']= pd.to_datetime(df_sm['Date'])
# df_sm.head()


# In[101]:


# Assign data untuk tiap indeks saham
hangseng = df_sm[df_sm['Name'] == 'HANG SENG']
nasdaq = df_sm[df_sm['Name'] == 'NASDAQ']
nikkei = df_sm[df_sm['Name'] == 'NIKKEI']

# Membuat ColumDataSource untuk tiap indeks saham
hangseng_new = ColumnDataSource(hangseng)
nasdaq_new = ColumnDataSource(nasdaq)
nikkei_new = ColumnDataSource(nikkei)


# In[102]:


# Membuat figure
fig = figure(x_axis_type='datetime',
             plot_height=400, plot_width=900,
             title='Perbandingan Pergerakan 3 Saham',
             x_axis_label='Tanggal', y_axis_label='Harga Tutup')

# Render indeks saham dalam plot line
hangseng_line = fig.line('Date', 'Adj Close', 
         color='blue', legend_label='HANG SENG', 
         source=hangseng_new)

nasdaq_line = fig.line('Date', 'Adj Close', 
         color='green', legend_label='NASDAQ', 
         source=nasdaq_new)

nikkei_line = fig.line('Date', 'Adj Close', 
         color='purple', legend_label='NIKKEI', 
         source=nikkei_new)


# In[105]:


# Membuat interaksi
from bokeh.models.tools import HoverTool

# Tooltip
tooltips = [
            ('Name','@Name'),
            ('Price', '@{Adj Close}'),
           ]

# Membuat interaksi hover untuk tiap indeks saham
fig.add_tools(HoverTool(tooltips=tooltips,renderers=[hangseng_line]))
fig.add_tools(HoverTool(tooltips=tooltips,renderers=[nasdaq_line]))
fig.add_tools(HoverTool(tooltips=tooltips,renderers=[nikkei_line]))

# Membuat interkasi di legend
fig.legend.location = 'top_right'
fig.legend.click_policy="hide"

# Menampilkan figure
show(fig)
output_notebook()

