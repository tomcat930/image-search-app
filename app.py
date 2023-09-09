#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import streamlit as st
from icrawler.builtin import BingImageCrawler, GoogleImageCrawler

DOWNLOAD_DIR = './images'

st.title('🕵️‍♀️Image Searcher')
serch_text = st.text_input(label='Search word', value='Dog')
image_dir = '{}/{}'.format(DOWNLOAD_DIR, serch_text)
btn = st.button('search')

st.sidebar.title('Advanced Setting')
options = st.sidebar.multiselect(label='Search engine',
                                 options=['Bing', 'Google'],
                                 default=['Bing'])
max_num = st.sidebar.number_input(label='Maximum number of images to acquire',
                                  value=100,
                                  help="Up to 500 sheets")

bing_expander = st.sidebar.expander("Bing filter options")
google_expander = st.sidebar.expander("Google filter options")


# bing filter options
bing_filters_type = bing_expander.multiselect(
    label="Bing filters type",
    options=["photo", "clipart", "linedrawing", "transparent", "animated"])
bing_filters_color = bing_expander.multiselect(
    label="Bing filters color",
    options=["color", "blackandwhite", "red", "orange", "yellow", "green",
             "teal", "blue", "purple", "pink", "white", "gray", "black", "brown"])
bing_filters_size = bing_expander.multiselect(
    label="Bing filters size",
    options=["large", "medium", "small"])
bing_filters_license = bing_expander.multiselect(
    label="Bing filters license",
    options=["creativecommons", "publicdomain", "noncommercial", "commercial",
             "noncommercial,modify", "commercial,modify"])
bing_filters_layout = bing_expander.multiselect(
    label="Bing filters layout",
    options=["square", "wide", "tall"])
bing_filters_people = bing_expander.multiselect(
    label="Bing filters people",
    options=["face", "portrait"])

bing_filters = dict(
    type=bing_filters_type,
    color=bing_filters_color,
    size=bing_filters_size,
    license=bing_filters_license,
    layout=bing_filters_layout,
    people=bing_filters_people)

# google filter options
google_filters_type = google_expander.multiselect(
    label="Google filters type",
    options=["photo", "face", "clipart", "linedrawing", "animated"])
google_filters_color = google_expander.multiselect(
    label="Google filters color",
    options=["color", "blackandwhite", "transparent", "red", "orange",
             "yellow", "green", "teal", "blue", "purple", "pink", "white",
             "gray", "black", "brown"])
google_filters_size = google_expander.multiselect(
    label="Google filters size",
    options=["large", "medium", "icon"])
google_filters_license = google_expander.multiselect(
    label="Google filters license",
    options=["noncommercial", "commercial",
             "noncommercial,modify", "commercial,modify"])

google_filters = dict(
    type=google_filters_type,
    color=google_filters_color,
    size=google_filters_size,
    license=google_filters_license)


if btn:
    if 'Bing' in options:
        bing_crawler = BingImageCrawler(
            downloader_threads=4,
            storage={'root_dir': image_dir})
        try:
            with st.spinner('Wait for it...'):
                bing_crawler.crawl(keyword=serch_text,
                                   max_num=max_num,
                                   filters=bing_filters
                                   )
        except:
            st.error('Failed to get images from Bing.')

    if 'Google' in options:
        google_crawler = GoogleImageCrawler(
            downloader_threads=4,
            storage={'root_dir': image_dir})
        try:
            with st.spinner('Wait for it...'):
                google_crawler.crawl(keyword=serch_text,
                                     max_num=max_num,
                                     filters=google_filters
                                     )
        except:
            st.error('Failed to get image from Google.')

    st.success('Completion.')

    # Get list of image files
    fName_list = os.listdir(image_dir)
    # Number of image files
    img_file_num = len(os.listdir(image_dir))
    st.write("files : {}".format(len(os.listdir(image_dir))))

    # display multiple images
    idx = 0
    for _ in range(len(fName_list)-1):
        cols = st.columns(4)

        if idx < len(fName_list):
            cols[0].image(f'{image_dir}/{fName_list[idx]}',
                          width=150, caption=fName_list[idx])
            print(os.path.join(image_dir, fName_list[idx]))
            idx += 1
        if idx < len(fName_list):
            cols[1].image(f'{image_dir}/{fName_list[idx]}',
                          width=150, caption=fName_list[idx])
            idx += 1
        if idx < len(fName_list):
            cols[2].image(f'{image_dir}/{fName_list[idx]}',
                          width=150, caption=fName_list[idx])
            idx += 1
        if idx < len(fName_list):
            cols[3].image(f'{image_dir}/{fName_list[idx]}',
                          width=150, caption=fName_list[idx])
            idx += 1
        else:
            break
