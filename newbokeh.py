from bokeh.plotting import figure, output_file, save, show
from bokeh.layouts import layout, widgetbox, row, column
from bokeh.models.widgets import Select, Slider, Button
from bokeh.io import show, curdoc
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, CustomJS, Button
import matplotlib as mpl 
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from mlxtend.preprocessing import minmax_scaling
output_file("2.html")

mylistX1 = [370, 270, 270, 150]
mylistX2 = [150, 500, 180, 350]
sizes = [0, 0, 0, 0]
# colors = ['peachpuff', 'teal', 'yellow', 'coral']
colors = ['red','red','red','red']
labels = ['England', 'Scotland', 'Wales', 'Northern Ireland']
opacity=[0,0,0,0]

data = pd.read_csv('subregion2017.csv') 
data2 = pd.read_csv('qm2/python/practice/data/dataforbubblemap.csv')

# diagnosis_listed = data['2017'].tolist()
# publicint_new = minmax_scaling(publicint, columns= ['Public Interest in 2017 '],min_val=0, max_val=10)
# data.head()
print(data2.columns.tolist())
print(data)
print(data.columns.tolist())
public_interest_listed = data['2017'].tolist()

# print(diagnosis_listed)
print(public_interest_listed)


source = ColumnDataSource(data=dict(x=mylistX1, y=mylistX2, size=public_interest_listed, color=colors, label=labels, opacity =opacity))




plot = figure(plot_width=900, plot_height=585, x_range=(0, 1000), y_range=(0, 650), toolbar_location=None, title="Popularity of songs in different countries over time")
plot.image_url(url=["https://d-maps.com/m/europa/uk/royaumeuni/royaumeuni56.gif"], x=0, y=0, w=500, h=700, anchor="bottom_left")
plot.circle(x='x', y='y', size='size', source=source, color='color', fill_alpha='opacity')
# plot.legend.location = (0, 0)
# plot.legend.glyph_height = 20
plot.title.text_font_size = '20pt'
plot.axis.visible = False
print(source.data)


callback = CustomJS(args=dict(source=source), code="""
      var data = source.data
      var x = selector.value
      var f = sliders.value
      var scale = 60000
      opacity = data ['opacity']
      size = data['size']
      

      if(x == "Public interest"){
 
          if (f == 1){  
            size[0] = 52
            opacity[0] = 1

            size[1] = 67
            opacity[1] = 	0.10463916300083224

            size[2] = 43
            opacity[2] = 0.022185233622637024

            size[3] = 100
            opacity[3] = 0

          }
          if (f == 2){  
            size[0] = 65
            opacity[0] = 1

            size[1] = 87
            opacity[1] = 0.10749212103177287
            
            size[2] = 62
            opacity[2] = 0.021425383127510786

            size[3] = 100
            opacity[3] = 0

          }
          if (f == 3){  
            size[0] = 74
            opacity[0] = 1

            size[1] = 100
            opacity[1] = 0.10621408211840465
                       
            size[2] = 93
            opacity[2] = 	0.02120335660343300


            size[3] = 98
            opacity[3] = 0

          }
          if (f == 4){  
            size[0] = 81
            opacity[0] = 1

            size[1] = 100
            opacity[1] = 	0.10504876086572612
            
            size[2] = 95
            opacity[2] = 0.020807252320310814

            size[3] = 91
            opacity[3] = 0

          }

          if (f == 5){ 
            size[0] = 82
            opacity[0] = 1

            size[1] = 100
            opacity[1] = 0.091483692176508
            
            size[2] = 89
            opacity[2] = 0.01912527534996092

            size[3] = 94
            opacity[3] = 0

          }

          if (f == 6){  
            size[0] = 75
            opacity[0] = 1

            size[1] = 100
            opacity[1] = 0.09818281686272715
            
            size[2] = 86
            opacity[2] = 0.018897658390494936

            size[3] = 75
            opacity[3] = 0

          }

          if (f == 7){ 
            size[0] = 85
            opacity[0] = 1

            size[1] = 96
            opacity[1] = 	0.08480299344341505
            
            size[2] = 100
            opacity[2] = 0.01690553910634927

            size[3] = 78
            opacity[3] = 0

          }

          if (f == 8){  
            size[0] = 87
            opacity[0] = 1

            size[1] = 100
            opacity[1] = 0.07704905210258216
            
            size[2] = 100
            opacity[2] = 	0.016626091377506626

            size[3] = 85
            opacity[3] = 0

          }

          if (f == 9){  
            size[0] = 88 
            opacity[0] = 1

            size[1] = 93  
            opacity[1] = 0.0705055267529421
            
            size[2] = 100  
            opacity[2] = 0.018336063026712056

            size[3] = 81   
            opacity[3] = 0

          }

          if (f == 10){
            size[0] = 87
            opacity[0] = 1

            size[1] = 96
            opacity[1] = 0.06696083614624425

            size[2] = 100
            opacity[2] = 0.01698591511109303

            size[3] = 90
            opacity[3] = 0

          }
  
       }
        if (x == "Diagnosis"){
          size[0] = scale/5942613942*(-6.54*f**6 + 513.18*f**5 - 15528.74*f**4 + 225681.95*f**3 - 1582335.94*f**2 + 4314667.29*f + 5424331.10)    
          size[1] = scale/1668326300*(12.88*f**5 - 778.38*f**4 + 16732.87*f**3 - 152386.70*f**2 + 495781.01*f + 958668.48)
          size[2] = 100
          size[3] = 100
              
        }


  source.change.emit();

""")
slider = Slider(start=1, end=10, value=1, step=1, title="Year", callback=callback)
callback.args["sliders"] = slider

select = Select(title='Variable: ',
                options=["Diagnosis", "Public interest"],
                value="Public interest",
                callback=callback)
callback.args["selector"] = select

widgetbox=widgetbox(select, slider)
# widgetbox=widgetbox(slider)

layout = column([plot, widgetbox], sizing_mode='fixed')
show(layout)