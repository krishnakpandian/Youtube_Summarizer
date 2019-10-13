#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: pandian_krishna
"""
import validators
import requests

#add in api information here, youtube data api and summarize_bot api
api_key = " "
summary_key= " "


'''
This function gets the data of the captions
'''
def video_json(vid_id):
    url = "http://video.google.com/timedtext?lang=en&v={}"
    #print(url.format(vid_id))
    response = requests.get(url.format(vid_id))
    #print(response)
    data = requests.post(url.format(vid_id, api_key), data = 'xml')
    return data.text
    
    
    '''
    Another Website that can take in captions
    url = "https://www.diycaptions.com/php/display-captions-as-text.php?id={}g&language=en"
    response = requests.get(url.format(vid_id))
    data = requests.post(url.format(vid_id, api_key), data = 'json')
    print(data.text)
    '''



#You can get a 14 day free trial of the Summarize Bot api

'''
This function gets the information from the caption file and summarizes it into another file
'''

def summarizer_validate():
    with open('', mode='rb') as file:  #input file here
        file = file.read()
    summary_api_url = "https://www.summarizebot.com/api/summarize?apiKey={}&size=20&keywords=10&fragments=15&filename={}"
    r = requests.get(summary_api_url.format(summary_key, file))
    json_res = r.json()
    print(json_res)
    file.close()
    
    file_write = open("", "w")   #input file here
    file_write.write(json_res)
    file_write.close()
    
'''
Checks if you have a valid youtube link to use
'''    

def youtube_validate(link):
    video_id_address = link.find('v=')
    video_id = link[video_id_address+2:]
    return video_id
    

'''
This functions is a parser and this goes through the caption data and removes out all the extra xml information
'''
def create_subtitles(data):
    subtitle_file= open(" ","a") #input file here
    index = data.find('</text>')
    initial = index
    
    if index == -1:
        subtitle_file.close()
        return 0
    
    while data[initial] != '>':
        initial -= 1
    initial += 1  
    
    store_string = (data[initial:index] + ' ')
    print(store_string)
    subtitle_file.write(store_string)
    
    
    new_string = (data[index+4:])
    subtitle_file.close()
    create_subtitles(new_string)
    return 0


'''
This is main and takes in the link to the youtube video
'''
def main():
    link = input('Please enter a Valid Youtube Video Link: ')
    valid = validators.url(link)
    if valid:
        print('')
    else:
        print('Website does not exist')
    video_id = youtube_validate(link)
    text = video_json(video_id)
    create_subtitles(text)
    summarizer_validate()


if __name__ == '__main__':
    main()


