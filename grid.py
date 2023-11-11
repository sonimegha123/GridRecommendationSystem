import itertools
import pandas as pd
import streamlit as st
import pandas as pd
import itertools
import matplotlib.pyplot as plt
from itertools import combinations
import random
import pandas as pd 

# Define the structure of the DataFrame as shown in the user's table
data = {
    ('Paragraph', 'paragraph_800'): {'25%': True, '33V%': True, '33H%': True, '50% V': True, '50% H': True, '67V%': True, '67H%': True, '100%': True},
    ('Paragraph', 'paragraph_1000'): {'25%': False, '33V%': True, '33H%': True, '50% V': True, '50% H': True, '67V%': True, '67H%': True, '100%': True},
    ('Paragraph', 'paragraph_1500'): {'25%': False, '33V%': False, '33H%': True, '50% V': True, '50% H': True, '67V%': True, '67H%': True, '100%': True},
    ('Paragraph', 'paragraph_1800'): {'25%': False, '33V%': False, '33H%': False, '50% V': False, '50% H': True, '67V%': True, '67H%': True, '100%': True},
    ('Paragraph', 'paragraph_3000'): {'25%': False, '33V%': False, '33H%': False, '50% V': False, '50% H': False, '67V%': False, '67H%': False, '100%': True},
    ('Bullet Point (Headings Only)', 'bullethead_8l'): {'25%': True, '33V%': True, '33H%': False, '50% V': True, '50% H': True, '67V%': True, '67H%': True, '100%': True},
    ('Bullet Point (Headings Only)', 'bullethead_16l'): {'25%': False, '33V%': False, '33H%': False, '50% V': False, '50% H': True, '67V%': False, '67H%': True, '100%': False},
    ('Bullet Point (Headings Only)', 'bullethead_2g'): {'25%': True, '33V%': True, '33H%': True, '50% V': True, '50% H': True, '67V%': True, '67H%': True, '100%': True},
    ('Bullet Point (Headings Only)', 'bullethead_3g'): {'25%': False, '33V%': True, '33H%': True, '50% V': True, '50% H': True, '67V%': True, '67H%': True, '100%': True},
    ('Bullet Point (Headings Only)', 'bullethead_4g'): {'25%': False, '33V%': True, '33H%': True, '50% V': True, '50% H': True, '67V%': True, '67H%': True, '100%': True},
    ('Bullet Point (Headings Only)', 'bullethead_5g'): {'25%': False, '33V%': True, '33H%': True, '50% V': True, '50% H': True, '67V%': True, '67H%': True, '100%': True},
    ('Bullet Point (Headings Only)', 'bullethead_6g'): {'25%': False, '33V%': False, '33H%': False, '50% V': True, '50% H': True, '67V%': True, '67H%': True, '100%': True},
    ('Bullet Point (Headings Only)', 'bullethead_7g'): {'25%': False, '33V%': False, '33H%': False, '50% V': False, '50% H': True, '67V%': True, '67H%': False, '100%': False},
    ('Bullet Point (Headings Only)', 'bullethead_8g'): {'25%': False, '33V%': False, '33H%': False, '50% V': False, '50% H': True, '67V%': True, '67H%': False, '100%': False},
    ('Bullet Point (Headings Only)', 'bullethead_9g'): {'25%': False, '33V%': False, '33H%': False, '50% V': False, '50% H': True, '67V%': True, '67H%': False, '100%': False},
    ('Bullet Point (Headings Only)', 'bullethead_10g'): {'25%': False, '33V%': False, '33H%': False, '50% V': False, '50% H': True, '67V%': True, '67H%': False, '100%': False},
    ('Bullet Point (Heading + Body)', 'bulletheadbody_2l'): {'25%': True, '33V%': True, '33H%': True, '50% V': True, '50% H': True, '67V%': True, '67H%': True, '100%': True},
    ('Bullet Point (Heading + Body)', 'bulletheadbody_6l'): {'25%': False, '33V%': False, '33H%': False, '50% V': False, '50% H': True, '67V%': True, '67H%': True, '100%': True},
    ('Bullet Point (Heading + Body)', 'bulletheadbody_10l'): {'25%': False, '33V%': False, '33H%': False, '50% V': False, '50% H': False, '67V%': True, '67H%': True, '100%': True},
    ('Bullet Point (Heading + Body)', 'bulletheadbody_2g'): {'25%': True, '33V%': True, '33H%': True, '50% V': True, '50% H': True, '67V%': True, '67H%': True, '100%': True},
    ('Bullet Point (Heading + Body)', 'bulletheadbody_3g'): {'25%': True, '33V%': True, '33H%': True, '50% V': True, '50% H': True, '67V%': True, '67H%': True, '100%': True},
    ('Bullet Point (Heading + Body)', 'bulletheadbody_4g'): {'25%': True, '33V%': False, '33H%': False, '50% V': True, '50% H': True, '67V%': True, '67H%': True, '100%': True},
    ('Bullet Point (Heading + Body)', 'bulletheadbody_5g'): {'25%': False, '33V%': False, '33H%': False, '50% V': False, '50% H': True, '67V%': True, '67H%': True, '100%': True},
    ('Bullet Point (Heading + Body)', 'bulletheadbody_6g'): {'25%': False, '33V%': False, '33H%': False, '50% V': False, '50% H': True, '67V%': True, '67H%': True, '100%': True},
    ('Bullet Point (Heading + Body)', 'bulletheadbody_7g'): {'25%': False, '33V%': False, '33H%': False, '50% V': False, '50% H': False, '67V%': True, '67H%': True, '100%': True},
    ('Bullet Point (Heading + Body)', 'bulletheadbody_8g'): {'25%': False, '33V%': False, '33H%': False, '50% V': False, '50% H': False, '67V%': True, '67H%': True, '100%': True},
    ('Bullet Point (Heading + Body)', 'bulletheadbody_9g'): {'25%': False, '33V%': False, '33H%': False, '50% V': False, '50% H': False, '67V%': True, '67H%': True, '100%': True},
    ('Bullet Point (Heading + Body)', 'bulletheadbody_10g'): {'25%': False, '33V%': False, '33H%': False, '50% V': False, '50% H': False, '67V%': True, '67H%': True, '100%': True},
    ('Image', 'image_1'): {'25%': True, '33V%': True, '33H%': True, '50% V': True, '50% H': True, '67V%': True, '67H%': True, '100%': True},
    ('Image', 'image_2'): {'25%': True, '33V%': True, '33H%': True, '50% V': True, '50% H': True, '67V%': True, '67H%': True, '100%': True},
    ('Image', 'image_3'): {'25%': False, '33V%': False, '33H%': False, '50% V': False, '50% H': False, '67V%': False, '67H%': False, '100%': True},
    ('Image', 'image_4'): {'25%': False, '33V%': False, '33H%': False, '50% V': False, '50% H': False, '67V%': False, '67H%': False, '100%': True},
    ('Image', 'image_5'): {'25%': False, '33V%': False, '33H%': False, '50% V': False, '50% H': False, '67V%': False, '67H%': False, '100%': True},
    ('Image', 'image_6'): {'25%': False, '33V%': False, '33H%': False, '50% V': False, '50% H': False, '67V%': False, '67H%': False, '100%': True},
    ('Image', 'image_7'): {'25%': False, '33V%': False, '33H%': False, '50% V': False, '50% H': False, '67V%': False, '67H%': False, '100%': True},
    ('Image', 'image_8'): {'25%': False, '33V%': False, '33H%': False, '50% V': False, '50% H': False, '67V%': False, '67H%': False, '100%': True},
    ('Image', 'image_9'): {'25%': False, '33V%': False, '33H%': False, '50% V': False, '50% H': False, '67V%': False, '67H%': False, '100%': True},
    ('Image', 'image_10'): {'25%': False, '33V%': False, '33H%': False, '50% V': False, '50% H': False, '67V%': False, '67H%': False, '100%': True},

    ('Table', '4.1'): {'25%': True, '33V%': True, '33H%': True, '50% V': True, '50% H': True, '67V%': True, '67H%': True, '100%': True},
    ('Table', '4.2'): {'25%': False, '33V%': True, '33H%': True, '50% V': True, '50% H': True, '67V%': True, '67H%': True, '100%': True},
    ('Table', '4.3'): {'25%': False, '33V%': False, '33H%': False, '50% V': True, '50% H': True, '67V%': True, '67H%': True, '100%': True},
    ('Table', '4.4'): {'25%': False, '33V%': False, '33H%': False, '50% V': False, '50% H': False, '67V%': True, '67H%': True, '100%': True},
    
    
   # ('Table', 'table'): {'25%': True, '33V%': True, '33H%': True, '50% V': True, '50% H': True, '67V%': True, '67H%': True, '100%': True},
    ('Quote', 'quote_1'): {'25%': True, '33V%': True, '33H%': True, '50% V': True, '50% H': True, '67V%': True, '67H%': True, '100%': True},
    ('Quote', 'quote_2'): {'25%': False, '33V%': False, '33H%': False, '50% V': False, '50% H': False, '67V%': False, '67H%': False, '100%': True},
    ('Quote', 'quote_3'): {'25%': False, '33V%': False, '33H%': False, '50% V': False, '50% H': False, '67V%': False, '67H%': False, '100%': True},
    ('Quote', 'quote_4'): {'25%': False, '33V%': False, '33H%': False, '50% V': False, '50% H': False, '67V%': False, '67H%': False, '100%': True},
    ('List', 'list_1'): {'25%': True, '33V%': True, '33H%': True, '50% V': True, '50% H': True, '67V%': True, '67H%': True, '100%': True},
    ('List', 'list_2'): {'25%': True, '33V%': True, '33H%': True, '50% V': True, '50% H': True, '67V%': True, '67H%': True, '100%': True},
    ('List', 'list_3'): {'25%': True, '33V%': True, '33H%': True, '50% V': True, '50% H': True, '67V%': True, '67H%': True, '100%': True},
    ('List', 'list_4'): {'25%': True, '33V%': True, '33H%': True, '50% V': True, '50% H': True, '67V%': True, '67H%': True, '100%': True},
    ('List', 'list_5'): {'25%': False, '33V%': False, '33H%': False, '50% V': True, '50% H': True, '67V%': True, '67H%': True, '100%': True},
    ('List', 'list_6'): {'25%': False, '33V%': True, '33H%': True, '50% V': True, '50% H': True, '67V%': True, '67H%': True, '100%': True},
    ('List', 'list_7'): {'25%': False, '33V%': False, '33H%': False, '50% V': True, '50% H': True, '67V%': True, '67H%': True, '100%': True},
    ('List', 'list_8'): {'25%': False, '33V%': True, '33H%': True, '50% V': True, '50% H': True, '67V%': True, '67H%': True, '100%': True},
    ('List', 'list_9'): {'25%': False, '33V%': False, '33H%': False, '50% V': False, '50% H': True, '67V%': True, '67H%': True, '100%': True},
    ('List', 'list_10'): {'25%': False, '33V%': False, '33H%': False, '50% V': True, '50% H': True, '67V%': True, '67H%': True, '100%': True},
    ('List', 'list_11'): {'25%': False, '33V%': False, '33H%': False, '50% V': False, '50% H': False, '67V%': False, '67H%': False, '100%': True},
    ('List', 'list_12'): {'25%': False, '33V%': False, '33H%': False, '50% V': False, '50% H': False, '67V%': False, '67H%': False, '100%': True},
    ('List', 'list_15'): {'25%': False, '33V%': False, '33H%': False, '50% V': False, '50% H': False, '67V%': False, '67H%': False, '100%': True},
    ('List', 'list_16'): {'25%': False, '33V%': False, '33H%': False, '50% V': False, '50% H': False, '67V%': False, '67H%': False, '100%': True},
    ('List', 'list_20'): {'25%': False, '33V%': False, '33H%': False, '50% V': False, '50% H': False, '67V%': False, '67H%': False, '100%': True},
    ('List', 'list_25'): {'25%': False, '33V%': False, '33H%': False, '50% V': False, '50% H': False, '67V%': False, '67H%': False, '100%': True},
    ('Cycle', 'cycle_2'): {'25%': True, '33V%': True, '33H%': True, '50% V': True, '50% H': True, '67V%': True, '67H%': True, '100%': False},
    ('Cycle', 'cycle_3'): {'25%': True, '33V%': True, '33H%': True, '50% V': True, '50% H': True, '67V%': True, '67H%': True, '100%': False},
    ('Cycle', 'cycle_4'): {'25%': False, '33V%': False, '33H%': False, '50% V': True, '50% H': True, '67V%': True, '67H%': True, '100%': False},
    ('Cycle', 'cycle_5'): {'25%': False, '33V%': True, '33H%': True, '50% V': True, '50% H': True, '67V%': True, '67H%': True, '100%': False},
    ('Cycle', 'cycle_6'): {'25%': False, '33V%': True, '33H%': True, '50% V': True, '50% H': True, '67V%': True, '67H%': True, '100%': False},
    ('Process', 'process_1'): {'25%': True, '33V%': True, '33H%': True, '50% V': True, '50% H': True, '67V%': True, '67H%': True, '100%': False},
    ('Process', 'process_2'): {'25%': True, '33V%': True, '33H%': True, '50% V': True, '50% H': True, '67V%': True, '67H%': True, '100%': False},
    ('Process', 'process_3'): {'25%': True, '33V%': True, '33H%': True, '50% V': True, '50% H': True, '67V%': True, '67H%': True, '100%': False},
    ('Process', 'process_4'): {'25%': False, '33V%': False, '33H%': False, '50% V': True, '50% H': True, '67V%': True, '67H%': True, '100%': False},
    ('Process', 'process_5'): {'25%': False, '33V%': False, '33H%': False, '50% V': False, '50% H': False, '67V%': True, '67H%': True, '100%': False},
    ('Timeline', 'timeline_2'): {'25%': True, '33V%': True, '33H%': True, '50% V': True, '50% H': True, '67V%': True, '67H%': True, '100%': False},
    ('Timeline', 'timeline_3'): {'25%': True, '33V%': True, '33H%': True, '50% V': True, '50% H': True, '67V%': True, '67H%': True, '100%': False},
    ('Timeline', 'timeline_4'): {'25%': True, '33V%': True, '33H%': True, '50% V': True, '50% H': True, '67V%': True, '67H%': True, '100%': False},
    ('Timeline', 'timeline_5'): {'25%': True, '33V%': True, '33H%': True, '50% V': True, '50% H': True, '67V%': True, '67H%': True, '100%': False},
    ('Timeline', 'timeline_6'): {'25%': True, '33V%': True, '33H%': True, '50% V': True, '50% H': True, '67V%': True, '67H%': True, '100%': False},
    ('Timeline', 'timeline_7'): {'25%': True, '33V%': True, '33H%': True, '50% V': True, '50% H': True, '67V%': True, '67H%': True, '100%': False},
    ('Timeline', 'timeline_8'): {'25%': True, '33V%': True, '33H%': True, '50% V': True, '50% H': True, '67V%': True, '67H%': True, '100%': False},
    ('Funnel', 'funnel_2'): {'25%': True, '33V%': True, '33H%': True, '50% V': True, '50% H': True, '67V%': True, '67H%': True, '100%': False},
    ('Funnel', 'funnel_3'): {'25%': True, '33V%': True, '33H%': True, '50% V': True, '50% H': True, '67V%': True, '67H%': True, '100%': False},
    ('Funnel', 'funnel_4'): {'25%': True, '33V%': True, '33H%': True, '50% V': True, '50% H': True, '67V%': True, '67H%': True, '100%': False},
    ('Funnel', 'funnel_5'): {'25%': False, '33V%': True, '33H%': True, '50% V': True, '50% H': True, '67V%': True, '67H%': True, '100%': False},
    ('Funnel', 'funnel_6'): {'25%': False, '33V%': True, '33H%': True, '50% V': True, '50% H': True, '67V%': True, '67H%': True, '100%': False},
    ('Pyramid', 'pyramid_1'): {'25%': True, '33V%': True, '33H%': True, '50% V': True, '50% H': True, '67V%': True, '67H%': True, '100%': False},
    ('Pyramid', 'pyramid_2'): {'25%': True, '33V%': True, '33H%': True, '50% V': True, '50% H': True, '67V%': True, '67H%': True, '100%': False},
    ('Pyramid', 'pyramid_3'): {'25%': True, '33V%': True, '33H%': True, '50% V': True, '50% H': True, '67V%': True, '67H%': True, '100%': False},
    ('Pyramid', 'pyramid_4'): {'25%': False, '33V%': True, '33H%': True, '50% V': True, '50% H': True, '67V%': True, '67H%': True, '100%': False},
    ('Pyramid', 'pyramid_5'): {'25%': False, '33V%': True, '33H%': True, '50% V': True, '50% H': True, '67V%': True, '67H%': True, '100%': False},
    ('Pyramid', 'pyramid_6'): {'25%': False, '33V%': False, '33H%': False, '50% V': False, '50% H': False, '67V%': True, '67H%': True, '100%': False},
}
# Create a MultiIndex from the tuple keys
index = pd.MultiIndex.from_tuples(data.keys(), names=["Element", "Subset"])

# Create the DataFrame
df = pd.DataFrame(data.values(), index=index)

df.rename(columns = {'33V%':'33% V'}, inplace = True)
df.rename(columns = {'33H%':'33% H'}, inplace = True)
df.rename(columns = {'67V%':'67% V'}, inplace = True)
df.rename(columns = {'67H%':'67% H'}, inplace = True)



data = {"subset":['paragraph_800', 'paragraph_1000', 'paragraph_1500', 'paragraph_1800', 'paragraph_3000', 'bullethead_8l', 'bullethead_16l', 'bullethead_2g', 'bullethead_3g', 'bullethead_4g', 'bullethead_5g', 'bullethead_6g', 'bullethead_7g', 'bullethead_8g', 'bullethead_9g', 'bullethead_10g', 'bulletheadbody_2l', 'bulletheadbody_6l', 'bulletheadbody_10l', 'bulletheadbody_2g', 'bulletheadbody_3g', 'bulletheadbody_4g', 'bulletheadbody_5g', 'bulletheadbody_6g', 'bulletheadbody_7g', 'bulletheadbody_8g', 'bulletheadbody_9g', 'bulletheadbody_10g', 'image_1', 'image_2', 'image_3', 'image_4', 'image_5', 'image_6', 'image_7', 'image_8', 'image_9', 'image_10', '4.1', '4.2', '4.3', '4.4', 'quote_1', 'quote_2', 'quote_3', 'quote_4', 'list_1', 'list_2', 'list_3', 'list_4', 'list_5', 'list_6', 'list_7', 'list_8', 'list_9', 'list_10', 'list_11', 'list_12', 'list_15', 'list_16', 'list_20', 'list_25', 'cycle_2', 'cycle_3', 'cycle_4', 'cycle_5', 'cycle_6', 'process_1', 'process_2', 'process_3', 'process_4', 'process_5', 'timeline_2', 'timeline_3', 'timeline_4', 'timeline_5', 'timeline_6', 'timeline_7', 'timeline_8', 'funnel_2', 'funnel_3', 'funnel_4', 'funnel_5', 'funnel_6', 'pyramid_1', 'pyramid_2', 'pyramid_3', 'pyramid_4', 'pyramid_5', 'pyramid_6'],
     "Weights" : [0.5, 0.5, 0.5, 0.5, 0.5, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.6, 0.6, 0.6, 0.6, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.5, 0.5, 0.5, 0.5, 0.5, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6],
    "Size weights" :[0.5, 0.5, 0.5, 0.8, 1.0, 0.5, 1.0, 0.4, 0.5, 0.6, 0.6, 0.6, 0.6, 0.7, 0.8, 1.0, 0.5, 0.8, 1.0, 0.5, 0.5, 0.6, 0.7, 0.75, 0.8, 0.9, 1.0, 1.0, 0.4, 0.4, 0.5, 0.6, 0.7, 0.7, 0.9, 0.9, 0.9, 1.0, 0.5, 0.5, 0.7, 0.9, 0.6, 0.8, 1.0, 1.0, 0.5, 0.6, 0.6, 0.7, 0.8, 0.8, 0.9, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.6, 0.7, 0.8, 0.9, 1.0, 0.6, 0.7, 0.8, 0.9, 1.0, 0.5, 0.6, 0.6, 0.7, 0.8, 0.9, 1.0, 0.6, 0.7, 0.8, 0.9, 1.0, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0],
    "Combined Weight" : [0.25, 0.25, 0.25, 0.4, 0.5, 0.15, 0.3, 0.12, 0.15, 0.18, 0.18, 0.18, 0.18, 0.21, 0.24, 0.3, 0.3, 0.48, 0.6, 0.3, 0.3, 0.36, 0.42, 0.45, 0.48, 0.54, 0.6, 0.6, 0.16, 0.16, 0.2, 0.24, 0.28, 0.28, 0.36, 0.36, 0.36, 0.4, 0.2, 0.2, 0.28, 0.36, 0.36, 0.48, 0.6, 0.6, 0.35, 0.42, 0.42, 0.49, 0.56, 0.56, 0.63, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.3, 0.35, 0.4, 0.45, 0.5, 0.54, 0.63, 0.72, 0.81, 0.9, 0.45, 0.54, 0.54, 0.63, 0.72, 0.81, 0.9, 0.36, 0.42, 0.48, 0.54, 0.6, 0.3, 0.36, 0.42, 0.48, 0.54, 0.6]}

# Convert the dictionary to a pandas DataFrame
df_2 = pd.DataFrame(data)


def assign_weights(df_2, user_inputs, combinations):
    """
    Assign weights to user_inputs based on the data in df_2.
    
    Parameters:
    - df_2: DataFrame containing the weights.
    - user_inputs: List of user inputs to be sorted.
    - combinations: Recommendations to map to sorted inputs.

    Returns:
    A dictionary mapping user inputs to recommendations.
    """
    sorted_inputs = sorted(user_inputs, key=lambda x: df_2.set_index('subset')['Combined Weight'].get(x[1], 0), reverse=True)
    sorted_recommendations = sorted(combinations, key=lambda x: int(x.rstrip('% V H')), reverse=True)
    return {element[0]: recommendation for element, recommendation in zip(sorted_inputs, sorted_recommendations)}

def recommend_grids(df, df_2, user_inputs):
    """
    Recommend grids based on user input.

    Parameters:
    - df: DataFrame containing available grid combinations.
    - df_2: DataFrame containing weights.
    - user_inputs: List of tuples containing user input.

    Returns:
    A list of dictionaries containing recommended grids.
    """
    user_subsets = [t[1] for t in user_inputs]
    user_rows = df.loc[user_inputs]
    available_percentages = [row.index[row].tolist() for _, row in user_rows.iterrows()]
    all_combinations = list(itertools.product(*available_percentages))

    valid_combinations = [combo for combo in all_combinations if sum(int(percent.split('%')[0]) for percent in combo) in (100, 99)]

    if len(user_subsets) == 1:
        #return [{'0%': '100%'}]
        return [{user_inputs[0][0]: '100%'}]

    # Filter out symmetric combinations
    def is_symmetric(combination):
        return (combination[0], combination[1]) not in [('50% V', '50% H'), ('50% H', '50% V'), ('25% V', '25% H')]
   
    valid_combinations = list(filter(is_symmetric, valid_combinations))

    if valid_combinations:
        return [assign_weights(df_2, user_inputs, combo) for combo in valid_combinations]
    else:
        subset_weights = df_2[df_2['subset'].isin(user_subsets)]['Combined Weight']
        highest_weight_element = subset_weights.idxmax()
        top_subset = df_2['subset'][highest_weight_element]
        st.subheader(f"""For {top_subset}, the recommended grid is 100% """)
        other = [t for t in user_inputs if t[1] != top_subset]
        return recommend_grids(df, df_2, other)

def split_combinations(lst):
    if not lst:
        return [[]]
    combinations = []
    for i in range(1, len(lst)):
        for combo in split_combinations(lst[i:]):
            combinations.append([lst[:i]] + combo)
    return combinations

# Define the Streamlit app
def main():
    st.title("Grid Recommendation App")

    # User input section
    st.sidebar.header("User Input")

    # Multi-select for selecting elements
    selected_elements = st.sidebar.multiselect(
        "Select Elements",
        df.index.get_level_values('Element').unique(),
        default=[]  # Initially, no elements are selected
    )

    user_inputs = []  # Initialize an empty list for user inputs

    # Display selected elements
    st.sidebar.header("Selected Elements")
    for element in selected_elements:
        st.sidebar.write(f"Element: {element}")

    # For each selected element, allow selection of subsets
    for element in selected_elements:
        available_subsets = df.loc[element].index.tolist()
        subset = st.sidebar.selectbox(f"Select Subset for {element}", available_subsets, key=element)
        user_inputs.append((element, subset))


    # Display user inputs
    st.sidebar.header("Selected Inputs")
    for user_input in user_inputs:
        st.sidebar.write(f"Element: {user_input[0]}, Subset: {user_input[1]}")

    if st.sidebar.button("Get Recommendations"):
    # Check if user inputs have more than 3 elements
        if len(user_inputs) > 3:
        # Split in half (from Code 2)
            split_index = len(user_inputs) // 2
            halves = [(user_inputs[:split_index], user_inputs[split_index:])]
        
        # Additional splits: Choose 2 random split points
            random_splits = random.sample(range(1, len(user_inputs)), 2)
            for split in random_splits:
                halves.append((user_inputs[:split], user_inputs[split:]))

        # Display recommendations for each split
            for first_half, second_half in halves:
                st.subheader(f"Recommendations for Split {len(first_half)}-{len(second_half)}:")
                recommendations_first_half = recommend_grids(df, df_2, first_half)
                recommendations_second_half = recommend_grids(df, df_2, second_half)
            
                display_recommendations(recommendations_first_half)
                display_recommendations(recommendations_second_half)

        # Final recommendations for the entire list (from Code 1)
            recommendations = recommend_grids(df, df_2, user_inputs)
            display_recommendations(recommendations)
        else:
            recommendations = recommend_grids(df, df_2, user_inputs)
            display_recommendations(recommendations)

# Function to display the recommended grid as pie charts
def display_recommendations(recommendations):
    if len(recommendations) == 0:
        st.error("No valid recommendations found.")
    else:
        st.success("Unique Recommended Grids:")
        for i, recommendation in enumerate(recommendations, start=1):
            st.subheader(f"Recommendation {i}")
            display_grid(recommendation)

# Function to display the recommended grid as a pie chart
def display_grid(recommendation):
    fig, ax = plt.subplots(figsize=(6, 4))
    percentages = [int(percent.split('%')[0]) for percent in recommendation.values()]
    labels = recommendation.keys()
    ax.pie(percentages, labels=labels, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')
    st.pyplot(fig)

if __name__ == "__main__":
    main()
