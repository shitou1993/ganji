from multiprocessing import Pool
from page_parsing import get_item_info_from, url_list, item_info, get_links_from
from channel_extracing import channel_list



def get_all_links_from(channel):
    for i in range(1, 40):
        get_links_from(channel, i)


if __name__ == '__main__':
    # pool = Pool(processes=6)
    pool = Pool()
    pool.map(get_all_links_from, channel_list.split())
    db_urls = [item['url'] for item in url_list.find()]
    pool.map(get_item_info_from, db_urls)
    pool.close()
    pool.join()



