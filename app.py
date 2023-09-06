#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import streamlit as st
from icrawler.builtin import BingImageCrawler, GoogleImageCrawler

DOWNLOAD_DIR = './images'

st.title('Image Searcher')
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

if btn:
    if 'Bing' in options:
        bing_crawler = BingImageCrawler(
            downloader_threads=4,
            storage={'root_dir': image_dir})
        try:
            with st.spinner('Wait for it...'):
                bing_crawler.crawl(keyword=serch_text, max_num=max_num)
        except:
            st.error('Failed to get images from Bing.')

    if 'Google' in options:
        google_crawler = GoogleImageCrawler(
            downloader_threads=4,
            storage={'root_dir': image_dir})
        try:
            with st.spinner('Wait for it...'):
                google_crawler.crawl(keyword=serch_text,
                                     max_num=max_num)
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
            cols[0].image(f'{image_dir}/{fName_list[idx]}', width=150, caption=fName_list[idx])
            print(os.path.join(image_dir, fName_list[idx]))
            idx += 1
        if idx < len(fName_list):
            cols[1].image(f'{image_dir}/{fName_list[idx]}', width=150, caption=fName_list[idx])
            idx += 1
        if idx < len(fName_list):
            cols[2].image(f'{image_dir}/{fName_list[idx]}', width=150, caption=fName_list[idx])
            idx += 1
        if idx < len(fName_list):
            cols[3].image(f'{image_dir}/{fName_list[idx]}', width=150, caption=fName_list[idx])
            idx += 1
        else:
            break
