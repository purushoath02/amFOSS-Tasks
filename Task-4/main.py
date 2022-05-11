
from operator import imod
import string
from urllib import response
import typer 
from datetime import datetime  
import requests
from PIL import Image
from io import BytesIO
import json
import urllib.request

API_KEY = "nhfgBcXplGi2UZjGgW2znBmkGrFZnJHiE2mkYW32" 



app = typer.Typer()

@app.command()
def fetch_img(date: datetime, id: int): 
    print("Sending API Req")
    date = str(date.date())
     
    API_URL = f"https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?earth_date={date}&api_key={API_KEY}"
    
    response = requests.get(API_URL)
    raw_data = json.loads(response.content)
    
    for x in raw_data['photos']:
        for y in x: 
            
            if x['id'] == id:
                print(x['img_src'])
                
                

    
  


if __name__=='__main__': 
    app()