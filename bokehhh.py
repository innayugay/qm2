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

mylistX1 = [390, 270, 270, 150]
mylistX2 = [120, 500, 180, 350]
sizes = [0, 0, 0, 0]
# colors = ['peachpuff', 'teal', 'yellow', 'coral']
colors = ['maroon','maroon','maroon','maroon']
labels = ['England', 'Scotland', 'Wales', 'Northern Ireland']
opacity=[0,0,0,0]

data = pd.read_csv('subregion2017.csv') 


# diagnosis_listed = data['2017'].tolist()
# publicint_new = minmax_scaling(publicint, columns= ['Public Interest in 2017 '],min_val=0, max_val=10)
# data.head()
# print(data2.columns.tolist())
print(data)
print(data.columns.tolist())
public_interest_listed = data['2017'].tolist()

# print(diagnosis_listed)
print(public_interest_listed)


source = ColumnDataSource(data=dict(x=mylistX1, y=mylistX2, size=public_interest_listed, color=colors, label=labels, opacity =opacity))


plot = figure(plot_width=900, plot_height=585, x_range=(0, 1000), y_range=(0, 650), toolbar_location=None, title="Public interest in dementia and number across the UK")
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
 
          if (f == 2008){  
            size[0] = 52
            opacity[0] = 0.9

            size[1] = 67
            opacity[1] = 	0.1451740327

            size[2] = 43
            opacity[2] = 0.06645296623

            size[3] = 100
            opacity[3] = 0.04527210483

          }
          if (f == 2009){  
            size[0] = 65
            opacity[0] = 0.9

            size[1] = 87
            opacity[1] = 0.1483371338
            
            size[2] = 62
            opacity[2] = 0.06620918126

            size[3] = 100
            opacity[3] = 0.04576431614

          }
          if (f ==2010){  
            size[0] = 74
            opacity[0] = 0.9

            size[1] = 100
            opacity[1] = 0.1465066964
                       
            size[2] = 93
            opacity[2] = 	0.06532832524


            size[3] = 98
            opacity[3] = 0.04508083363

          }
          if (f == 2011){  
            size[0] = 81
            opacity[0] = 0.9

            size[1] = 100
            opacity[1] = 	0.1449210152
            
            size[2] = 95
            opacity[2] = 0.06443267078

            size[3] = 91
            opacity[3] = 0.04455243216

          }

          if (f == 2012){ 
            size[0] = 82
            opacity[0] = 0.9

            size[1] = 100
            opacity[1] = 0.1294589056176508
            
            size[2] = 89
            opacity[2] = 0.06012500936

            size[3] = 94
            opacity[3] = 0.04179915435

          }

          if (f == 2013){  
            size[0] = 75
            opacity[0] = 0.9

            size[1] = 100
            opacity[1] = 0.1344373001
            
            size[2] = 86
            opacity[2] = 0.05833953099

            size[3] = 75
            opacity[3] = 0.04020158848

          }

          if (f == 2014){ 
            size[0] = 85
            opacity[0] = 0.9

            size[1] = 96
            opacity[1] = 	0.1175761581
            
            size[2] = 100
            opacity[2] = 0.05211010864

            size[3] = 78
            opacity[3] = 0.03580995615

          }

          if (f == 2015){  
            size[0] = 87
            opacity[0] = 0.9

            size[1] = 100
            opacity[1] = 0.1067789834
            
            size[2] = 100
            opacity[2] = 	0.04830235633

            size[3] = 85
            opacity[3] = 0.03221182165

          }

          if (f == 2016){  
            size[0] = 88 
            opacity[0] = 0.9

            size[1] = 93  
            opacity[1] = 0.09955275499
            
            size[2] = 100  
            opacity[2] = 0.04901361653

            size[3] = 81   
            opacity[3] = 0.03125056585

          }

          if (f == 2017){
            size[0] = 87
            opacity[0] = 0.9

            size[1] = 96
            opacity[1] = 0.09584029391

            size[2] = 100
            opacity[2] = 0.04741219821

            size[3] = 90
            opacity[3] = 0.03095203169

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
slider = Slider(start=2008, end=2017, value=2008, step=1, title="Year", callback=callback)
callback.args["sliders"] = slider

select = Select(title='Variable: ',
                options=["Public interest"],
                value="Public interest",
                callback=callback)
callback.args["selector"] = select

widgetbox=widgetbox(select, slider)
# widgetbox=widgetbox(slider)

layout = column([plot, widgetbox], sizing_mode='fixed')
show(layout)