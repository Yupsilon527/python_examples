from pandas_datareader import data
import datetime

from bokeh.plotting import figure, show, output_file

start=datetime.datetime(2016,3,1)
end=datetime.datetime(2016,3,10)
df = data.DataReader(name = "goog",data_source="yahoo",start=start,end = end)
df.index[df.Close > df.Open]

def inc_dec(c,o):
    if c>o:
        return "Increase"
    elif c<o:
        return "Decrease"
    else:
        return "Equal"

df["Status"] = [inc_dec(c,o) for c,o in zip(df.Close,df.Open)]
df["Middle"] = (df.Open+df.Close)/2
df["Height"] = abs(df.Close-df.Open)

p = figure (x_axis_type="datetime",width=1000,height=300)
p.Title = "Market Share Chart"

hours = 12*60*60*1000

p.segment(df.index,df.High,df.index,df.Low, color = "black")
p.rect(df.index[df.Status=="Increase"],df.Middle[df.Status=="Increase"],hours,df.Height[df.Status=="Increase"],fill_color="green",line_color="black")
p.rect(df.index[df.Status=="Decrease"],df.Middle[df.Status=="Decrease"],hours,df.Height[df.Status=="Decrease"],fill_color="red",line_color="black")


output_file("CS.html")
show(p)