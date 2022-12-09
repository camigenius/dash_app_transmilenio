from dash import Dash, dcc, html, Input, Output
from plotly.express import data
import pandas as pd
import plotly.express as px

df = pd.read_pickle('my_dataframe.pickle')


app = Dash(__name__)
server = app.server

app.layout = html.Div([
    
    html.H1('UN DIA CUALQUIERA EN TRANSMILENIO!!'),
    dcc.Graph(id="graph"),    
    dcc.Dropdown(df.Linea.unique(), id='dropdown',placeholder="Seleccione una estacón"),
    html.H4('Elaboradpo por camilo franco'),
     
    
    
    #html.Div(id='pandas-output-container-1'),

    
])


@app.callback(
    Output('graph','figure'),
    Input('dropdown', 'value')
)
def update_output(value):
    portal = df[df['Linea']==value]
    estaciones=portal['Estacion_Parada'].value_counts()
    fig = px.bar(estaciones, x=estaciones.index, y=estaciones)
    #fig.show()  
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
