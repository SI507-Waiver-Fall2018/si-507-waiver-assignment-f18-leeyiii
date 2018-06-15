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
	
lst=[]

for i in table:
	m = i.replace('"','')
	lst.append(m)



	
print(m)


df.close()

'''

data = [go.Bar(
			x=[table[1][0], table[2][0] ],
			y=[int(table[1][1]), int(table[2][1]) ]
	)]

py.iplot(data,filename='part4_viz_image')

'''



