from __future__ import unicode_literals
import youtube_dl
import pandas as pd
import logging
import time
import os
import sys
import numpy as np
from multiprocessing import Pool

DOWNLOAD_TYPES = ["Single","Single-CSV","Multi-CSV"]

LOGGING_TYPES = {
    'debug': logging.DEBUG,
    'info': logging.INFO,
    'warning': logging.WARNING,
    'error': logging.ERROR,
    'critical': logging.CRITICAL,
    'fatal': logging.FATAL,
    'warn':logging.WARN
}

#Change this variable to change the download type.
#By default, it is set to Single
#Single requires the user to input a url
#Single-CSV requires the user to input a row entry in URLs.csv
#Multi-CSV requires no input (URLs.csv is implicit)
download_type = 0


#Default directory to save downloaded videos to
dir = 'Downloader/raw_videos'

#Directory to save audio to
audio_dir = 'Downloader/audio'

#Directory for processing videos
process_dir = 'Downloader/processing'

#Directory for final processed videos
final_dir = 'Downloader/videos'

#Directory to write log files to
log_dir = "Downloader/logs/"

#Directory to csv file
query_file = 'Downloader/URLs.csv'

def create_log_directory(name,id):
    dir_name = name + " ({0}) ".format(id) + time.ctime()
    dir_name = dir_name.replace(":",";")
    os.mkdir(log_dir+ dir_name)
    return os.getcwd() + "/" + log_dir + dir_name + "/"


def download(link, name = None,file_ext = 'mp4'):
    # Downloads a user-specified video
    formatType = 'best[ext='+file_ext+']'
    options = {
        'format':formatType,
        'forceurl':True,
        'logger':logging.getLogger(),
        #default file name 
        'outtmpl': dir +'/' + (u'%(title)s' if name == None else name) + u'.%(ext)s',     #name the file the ID of the video
        'noplaylist':True,
        'nocheckcertificate':True,
    }

    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download(link)

def download_async(args):
    link,name,file_ext = args
    # Downloads a user-specified video
    formatType = 'best[ext='+file_ext+']'
    options = {
        'format':formatType,
        'forceurl':True,
        'logger':logging.getLogger(),
        #default file name 
        'outtmpl': dir +'/' + (u'%(title)s' if name == None else name) + u'.%(ext)s',     #name the file the ID of the video
        'noplaylist':True,
        'nocheckcertificate':True,
    }

    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download(link)


def multi_async():
    data = pd.read_csv(query_file)
    # data = data.loc[data.flag, :]
    data = data.replace(np.nan,None)
    links = [[link] for link in data['URLs'].to_list()]
    names = data['Name'].to_list()
    file_exts = data['File_Extension'].to_list()
    args = list(zip(links,names,file_exts))
    logging.info("Arguement Data:")
    logging.info(args)
    #args = [(name, [link]) for link in links]
    with Pool() as mp_pool:
        results = mp_pool.map(download_async, args)
    #for link in links:
    #    download_audio([link],name=name)
         
def main(query_file,url = None, index = None):
    #try to download a single audio file
    # args = [(row['Name'], data_path + row['Query 1'].replace(" ", "_") + ".csv") for _, row in queries.iterrows()]
    # for name, filename in args[10:]:
    if(url == None and index != None):
        queries = pd.read_csv(query_file)
        url = queries.iloc[index]['URLs']
        queries = queries.replace(np.nan,None)
        name = queries.iloc[index]['Name']
        name = None if name == np.nan else name
        logging.info(name)
    elif(index == None and url != None):
        name = None
    else:
        exit()
    try:

        logging.info("Downloading audio for "+ url)
        download([url],name=name)
    except:
        exit()
    
    

if __name__ == "__main__":
    log_path = create_log_directory('AudioTest','JPopMafuMafu')
    logging.basicConfig(filename= log_path+"info.log",encoding='utf-8',filemode='w',level=(LOGGING_TYPES['debug']))
    logging.getLogger().addHandler(logging.StreamHandler(sys.stdout))
    procedure_type = DOWNLOAD_TYPES[download_type]
    match procedure_type:
        case "Single":
            url = input("Please input the url for the video to be downloaded. Youtube and Vimeo are common choices though many other platforms are also supported (be sure to include the 'https:' part of the url): ")
            main(query_file,url)
        case "Single-CSV":
            index = int(input("Please input the row index in URLs.csv to be downloaded: "))
            main(query_file,index=index)
        case "Multi-CSV":
            multi_async()
    
