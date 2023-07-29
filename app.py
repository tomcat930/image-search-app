import streamlit as st
from icrawler.builtin import BingImageCrawler, GoogleImageCrawler

DOWNLOAD_DIR = './images'

st.title('Image Searcher')
serch_text = st.text_input(label='Search word', value='Dog')
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
            storage={'root_dir': '{}/{}'.format(DOWNLOAD_DIR, serch_text)})
        try:
            with st.spinner('Wait for it...'):
                bing_crawler.crawl(keyword=serch_text,max_num=max_num)
        except:
            st.error('Failed to get images from Bing.')

    if 'Google' in options:
        google_crawler = GoogleImageCrawler(
            downloader_threads=4 ,
            storage={'root_dir': '{}/{}'.format(DOWNLOAD_DIR, serch_text)})
        try:
            with st.spinner('Wait for it...'):
                google_crawler.crawl(keyword=serch_text,
                                     max_num=max_num)
        except:
            st.error('Failed to get image from Google.')

    st.success('Completion.')