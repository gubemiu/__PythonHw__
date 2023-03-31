import requests
import csv
from io import StringIO
import password


class Site(object):
    def __init__(self, name, county, aqi):
        super().__init__()
        self.site_name = name
        self.county = county
        try:
            self.aqi = int(aqi)
        except:
            self.aqi = 999  # if空字串塞999

    def __repr__(self):
        return f"站點:{self.site_name},城市:{self.county},aqi:{self.aqi}" #list放置資料的位置：Site(item[0], item[1], item[2])


class Taiwan_AQI(list):  # class Taiwan_AQI(list)=>這是內建語法，(list)代表繼承list，擁有list所有功能(用繼承是因為要加更多功能)=>()裡面的是一個class，代表你要繼承的功能
    '''
    
    @classmethod
    def download_aqi(cls) -> list:
        response = requests.get(
            f'https://data.epa.gov.tw/api/v2/aqx_p_432?api_key={password.API_KEY}&limit=1000&sort=ImportDate desc&format=CSV')

        if response.ok:
            # print(response.text)
            # file = open('./lesson17/aqi.csv',mode='w',encoding='utf-8')
            # file.write(response.text)
            # file.close()
            file = StringIO(response.text, newline='')
            csvReader = csv.reader(file)
            next(csvReader)
            dataList = []
            for item in csvReader:
                site = Site(item[0], item[1], item[2])
                dataList.append(site)
            return dataList

        else:
            raise Exception("下載失敗")
    '''

    def __init__(self):  # 加更多功能：自訂__init__，再把list多加一些功能，self代表我，我就是list
        super().__init__()

        # 要增加下載資料、自動加入資料功能
        response = requests.get(
            f'https://data.epa.gov.tw/api/v2/aqx_p_432?api_key={password.API_KEY}&limit=1000&sort=ImportDate desc&format=CSV')

        if response.ok:
            file = StringIO(response.text, newline='')
            csvReader = csv.reader(file)
            next(csvReader)
            # dataList = [] #不用加這行變list，因為Taiwan_AQI(list)本身就是list
            for item in csvReader:
                if item[2] != 999:  # 判斷如果aqi不等於999才做下面的動作(排除空字串999)，item[2]裡面放的是aqi
                    site = Site(item[0], item[1], item[2]) #item裡面放的是site
                    self.append(site) #下載的資料放在這裡
        else:
            raise Exception("下載失敗")


    # 最差的AQI    
    def get_bad(self,n=3): #n預設為3個，所以呼叫這個function時如果不寫n=幾個，就預設會帶三個
        '''
        @param n(參數),定義最差的數量
        取出AQI最差的n筆site list
        list裡面放的元素是Site實體
        '''
        sorted_aqi = sorted(self, key=lambda site:site.aqi, reverse=False)  
        # 內建build in的function，任何地方都可以呼叫；sorted後會傳出全新的list，所以要用新的sorted_aqi去接；key後面要接function，用lambda匿名的function裡面有參數，lambda site:site.aqi是註冊function
        return sorted_aqi[-n:]

    
    # 最好的AQI
    def get_better(self, n=3):
        '''
        @param n(參數),定義最好的數量
        取出AQI最好的n筆site list
        list裡面放的元素是Site實體
        '''
        sorted_aqi = sorted(self, key=lambda site: site.aqi,reverse=False)  
        return sorted_aqi[:n]
    
