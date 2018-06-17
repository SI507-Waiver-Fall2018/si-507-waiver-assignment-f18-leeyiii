
#FULL NAME: Yi Lee
#UMICH UNIQUENAME: yilee

# Imports -- you may add others but do not need to
import plotly.plotly as py
import plotly.graph_objs as go


# Code here should involve creation of the bar chart as specified in instructions
# And opening / using the CSV file you created earlier with noun data from tweets


df = open('noun_data.csv', 'r')

data = df.readlines()

table=[]

for row in data:
	table.append(row)
	
noun_lst=[]
frequency_lst = []

for i in table[1:]:
    noun, frequency = i[:-1].split(",")
    noun_lst.append(noun)
    frequency_lst.append(int(frequency))
	
print(noun_lst)
print(frequency_lst)

df.close()

data = [go.Bar(
        x = noun_lst,
        y = frequency_lst
    )]

fig = go.Figure(data=data)
py.image.save_as(fig, filename='part4_viz_image.png')





