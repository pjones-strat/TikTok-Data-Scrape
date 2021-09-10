from TikTokApi import TikTokApi
import pandas as pd
api = TikTokApi()
n_videos = 1000
username = 'ryanair'
user_videos = api.by_username(username, count=n_videos)
print(user_videos)


def simple_dict(tiktok_dict):
    to_return = {'user_name': tiktok_dict['author']['uniqueId'], 'user_id': tiktok_dict['author']['id'],
                 'video_id': tiktok_dict['id'], 'video_desc': tiktok_dict['desc'],
                 'video_time': tiktok_dict['createTime'], 'video_length': tiktok_dict['video']['duration']}
    to_return['video_link'] = 'https://www.tiktok.com/@{}/video/{}?lang=en'.format(to_return['user_name'],
                                                                                   to_return['video_id'])
    to_return['n_likes'] = tiktok_dict['stats']['diggCount']
    to_return['n_shares'] = tiktok_dict['stats']['shareCount']
    to_return['n_comments'] = tiktok_dict['stats']['commentCount']
    to_return['n_plays'] = tiktok_dict['stats']['playCount']

    return to_return


user_videos = [simple_dict(v) for v in user_videos]
user_videos_df = pd.DataFrame(user_videos)
user_videos_df.to_csv('{}_videos.csv'.format(username), index=False)

