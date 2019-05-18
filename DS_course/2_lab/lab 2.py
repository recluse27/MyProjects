from spyre import server
import pandas as pd
from matplotlib import pyplot as plt


class MyApp(server.App):
    title = "Vegetation Health Index"

    inputs = [{"type": 'dropdown',
               "label": "Index",
               "options": [{"label": 'VCI', "value": "VCI"},
                           {"label": 'TCI', "value": "TCI"},
                           {"label": 'VHI', "value": "VHI"}],
               "key": 'veg_index',
               "action_id": "update_data"
               },
              {"type": 'dropdown',
               "label": 'Region',
                "options" : [ {"label": "Cherkasy", "value":"01"},
                              {"label": "Chernihiv", "value":"02"},
                              {"label": "Chernivtsi", "value":"03"},
                              {"label": "Crimea", "value":"4"},
                              {"label": "Dnipropetrovs'k", "value":"05"},
                              {"label": "Donets'k", "value":"06"},
                              {"label": "Ivano-Frankivs'k", "value":"07"},
                              {"label": "Kharkiv", "value":"08"},
                              {"label": "Kherson", "value":"09"},
                              {"label": "Khmel'nits'kyy", "value":"10"},
                              {"label": "Kiev", "value":"11"},
                              {"label": "KievCity", "value":"12"},
                              {"label": "Kirovohrad", "value":"13"},
                              {"label": "Luhans'k", "value":"14"},
                              {"label": "L'viv", "value":"15"},
                              {"label": "Mykolayiv", "value":"16"},
                              {"label": "Odessa", "value":"17"},
                              {"label": "Poltava", "value":"18"},
                              {"label": "Rivne", "value":"19"},
                              {"label": "Sevastopol'", "value":"20"},
                              {"label": "Sumy", "value":"21"},
                              {"label": "Ternopil'", "value":"22"} ,
                              {"label": "Zacarpathia", "value":"23"},
                              {"label": "Vinnytsya", "value":"24"},
                              {"label": "Volyn", "value":"25"},
                              {"label": "Zaporizhzhya", "value":"26"},
                              {"label": "Zhytomyr", "value":"27"}
                            ],
               "key": 'region',
               "action_id": "update_data"
              },
              {"type": 'slider',
               "label": 'First year',
               "key": 'first_year',
               "value": 1990,
               "min": 1981,
               "max": 2016,
               "action_id": "update_data",
               "linked_key": 'title',
               "linked_type": 'text',
               },
              {"type": 'slider',
               "label": 'Second year',
               "key": 'second_year',
               "value": 2000,
               "min": 1981,
               "max": 2016,
               "action_id": "update_data",
               "linked_key": 'title',
               "linked_type": 'text',
               },
              {"type": 'slider',
               "label": 'First week',
               "key": 'first_week',
               "value": 20,
               "min": 1,
               "max": 52,
               "action_id": "update_data",
               "linked_key": 'title',
               "linked_type": 'text',
               },
              {"type": 'slider',
               "label": 'Last week',
               "key": 'last_week',
               "value": 40,
               "min": 1,
               "max": 52,
               "action_id": "update_data",
               "linked_key": 'title',
               "linked_type": 'text',
               }
    ]

    controls = [{"control_type": "button",
                "label": "Get data",
                "control_id": "update_data"}]

    tabs = ["Plot", "Table"]

    outputs = [{"type": "plot",
                "id": "plot",
                "control_id": "update_data",
                "tab": "Plot"},
               {"type": "table",
                "id": "table_id",
                "control_id": "update_data",
                "tab": "Table",
                "on_page_load": True }]

    def getPlot(self,params):
        path = "vhi_id_"+str(params['region'])+".csv"
        df = pd.read_csv(path, index_col=False, header=1)
        df = df[(df['VHI'] >= 0)&(df['TCI'] >= 0)&(df['VCI'] >= 0)&(df['SMN'] >= 0)&(df['SMT'] >= 0)]
        x1 = df[(df['year'] == int(params['first_year']))]
        x2 = df[(df['year'] == int(params['second_year']))]
        x1 = x1[(x1['week'] <= int(params['last_week']))]
        x1 = x1[(x1['week']>= int(params['first_week']))]
        x2 = x2[(x2['week'] <= int(params['last_week']))]
        x2 = x2[(x2['week'] >= int(params['first_week']))]
        y1_axis = x1[params['veg_index']]
        x1_axis = x1['week']
        y2_axis = x2[params['veg_index']]
        x2_axis = x2['week']
        plt.plot(x1_axis, y1_axis)
        plt.plot(x2_axis, y2_axis)
        return plt.gcf()

    def getData(self, params):
        path = "vhi_id_"+str(params['region'])+".csv"
        df = pd.read_csv(path, index_col=False, header=1)
        df = df[(df['VHI'] >= 0)&(df['TCI'] >= 0)|(df['VCI'] >= 0)&(df['SMN'] >= 0)&(df['SMT'] >= 0)]
        x = df[(df['year'] == int(params['first_year']))|(df['year']==int(params['second_year']))]
        x = x[(x['week'] >= int(params['first_week']))]
        x = x[(x['week'] <= int(params['last_week']))]
        x = x.rename(columns={'%Area_VHI_LESS_15':'AED'})
        x = x.rename(columns={'%Area_VHI_LESS_35':'AMD'})
        return x


app = MyApp()
app.launch(port=8000)