from slack_sdk.rtm_v2 import RTMClient
from slack_sdk import WebClient
from weather_info_parser import WeatherInfoParser
import os

rtm = RTMClient(token=os.getenv('slack_token'))
web_client = WebClient(token=os.getenv('slack_token'))
weather_info_parser = WeatherInfoParser()

def send_weather_info():
    weather_info = weather_info_parser.getWeatherInfo(keyword='강남 날씨')

    channel_id = 'C05FY0BCUD6'

    rtm.web_client.chat_postMessage(
        channel=channel_id,
        blocks=[
            {'type':'divider'},
            {
                'type':'section',
                'text': {
                    'type':'plain_text',
                    'text':f'{weather_info.area}'
                }
            },
            {'type':'divider'},
            {
                'type':'section',
                'text': {
                    'type':'plain_text',
                    'text':f"""{weather_info.weather_today}
현재기온:{weather_info.temperature_now}
최고기온:{weather_info.temperature_high}
최저기온:{weather_info.temperature_low}
"""
                }
            },
        ],
    )

    weather_info_parser.getScreenshot(keyword='강남 날씨')

    web_client.files_upload_v2(
        channel=channel_id,
        file='info.png',
        title='날씨 정보',
    )

def main():
    send_weather_info()

if __name__ == '__main__':
    main()
