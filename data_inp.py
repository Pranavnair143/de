import pandas as pd
from django.http import HttpResponseRedirect
import os
import django
import chardet

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pcx.settings')
django.setup()

from api.product.models import Product

csv_data=pd.read_csv('laptops.csv',encoding='ISO-8859-1')
for i in range(1,1300):
    data=Product()
    data.brand_name=csv_data['Company'][i]
    data.name=csv_data['Product'][i]
    data.type=csv_data['TypeName'][i]
    data.price=csv_data['Price_euros'][i]*89.47
    data.imageUrl="https://e7.pngegg.com/pngimages/515/571/png-clipart-laptop-graphy-laptop-electronics-3d-computer-graphics.png"
    data.description="It's not only writers who can benefit from this free online tool. If you're a programmer who's working on a project where blocks of text are needed, this tool can be a great way to get that. It's a good way to test"
    data.save()