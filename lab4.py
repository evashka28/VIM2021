{
 "metadata": {
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  },
  "orig_nbformat": 2,
  "kernelspec": {
   "name": "python374jvsc74a57bd0684b1123683431d89d3bfe9a89cc763215f4b8cd94b4aba1fb40ad45ff7c8b41",
   "display_name": "Python 3.7.4 64-bit"
  },
  "metadata": {
   "interpreter": {
    "hash": "684b1123683431d89d3bfe9a89cc763215f4b8cd94b4aba1fb40ad45ff7c8b41"
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2,
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 47,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\r\n",
    "import operator\r\n",
    "import seaborn as sns\r\n",
    "import plotly "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "metadata": {},
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "           Name  Gender Korean Name  Debut    Company  Members  Orig. Memb.  \\\n",
       "0      Spectrum       0        스펙트럼   2018       WYNN        6            7   \n",
       "1  Golden Child       0      골든 차일드   2017    Woollim       10           11   \n",
       "2           ONF       0        온앤오프   2017         WM        6            7   \n",
       "3         MR.MR       0      미스터미스터   2012  WinningIn        6            5   \n",
       "4        A.cian       0         에이션   2012      Wings        4            5   \n",
       "\n",
       "  Fanclub Name  disband  \n",
       "0            -        1  \n",
       "1            -        1  \n",
       "2            -        1  \n",
       "3            -        1  \n",
       "4            -     2017  "
      ],
      "text/html": "<div>\n<style scoped>\n    .dataframe tbody tr th:only-of-type {\n        vertical-align: middle;\n    }\n\n    .dataframe tbody tr th {\n        vertical-align: top;\n    }\n\n    .dataframe thead th {\n        text-align: right;\n    }\n</style>\n<table border=\"1\" class=\"dataframe\">\n  <thead>\n    <tr style=\"text-align: right;\">\n      <th></th>\n      <th>Name</th>\n      <th>Gender</th>\n      <th>Korean Name</th>\n      <th>Debut</th>\n      <th>Company</th>\n      <th>Members</th>\n      <th>Orig. Memb.</th>\n      <th>Fanclub Name</th>\n      <th>disband</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>0</th>\n      <td>Spectrum</td>\n      <td>0</td>\n      <td>스펙트럼</td>\n      <td>2018</td>\n      <td>WYNN</td>\n      <td>6</td>\n      <td>7</td>\n      <td>-</td>\n      <td>1</td>\n    </tr>\n    <tr>\n      <th>1</th>\n      <td>Golden Child</td>\n      <td>0</td>\n      <td>골든 차일드</td>\n      <td>2017</td>\n      <td>Woollim</td>\n      <td>10</td>\n      <td>11</td>\n      <td>-</td>\n      <td>1</td>\n    </tr>\n    <tr>\n      <th>2</th>\n      <td>ONF</td>\n      <td>0</td>\n      <td>온앤오프</td>\n      <td>2017</td>\n      <td>WM</td>\n      <td>6</td>\n      <td>7</td>\n      <td>-</td>\n      <td>1</td>\n    </tr>\n    <tr>\n      <th>3</th>\n      <td>MR.MR</td>\n      <td>0</td>\n      <td>미스터미스터</td>\n      <td>2012</td>\n      <td>WinningIn</td>\n      <td>6</td>\n      <td>5</td>\n      <td>-</td>\n      <td>1</td>\n    </tr>\n    <tr>\n      <th>4</th>\n      <td>A.cian</td>\n      <td>0</td>\n      <td>에이션</td>\n      <td>2012</td>\n      <td>Wings</td>\n      <td>4</td>\n      <td>5</td>\n      <td>-</td>\n      <td>2017</td>\n    </tr>\n  </tbody>\n</table>\n</div>"
     },
     "metadata": {},
     "execution_count": 48
    }
   ],
   "source": [
    "df = pd.read_csv(\"k-pop_group_new.csv\")\n",
    "df.head()"
   ]
  },
  {
   "source": [
    "# Старые гипотезы\n"
   ],
   "cell_type": "markdown",
   "metadata": {}
  },
  {
   "source": [
    "### Активна ли группа"
   ],
   "cell_type": "markdown",
   "metadata": {}
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [
    {
     "output_type": "display_data",
     "data": {
      "application/vnd.plotly.v1+json": {
       "config": {
        "plotlyServerURL": "https://plot.ly"
       },
       "data": [
        {
         "labels": [
          "Active",
          "Inactive"
         ],
         "type": "pie",
         "values": [
          207,
          92
         ]
        }
       ],
       "layout": {
        "template": {
         "data": {
          "bar": [
           {
            "error_x": {
             "color": "#2a3f5f"
            },
            "error_y": {
             "color": "#2a3f5f"
            },
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             }
            },
            "type": "bar"
           }
          ],
          "barpolar": [
           {
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             }
            },
            "type": "barpolar"
           }
          ],
          "carpet": [
           {
            "aaxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "baxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "type": "carpet"
           }
          ],
          "choropleth": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "choropleth"
           }
          ],
          "contour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "contour"
           }
          ],
          "contourcarpet": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "contourcarpet"
           }
          ],
          "heatmap": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmap"
           }
          ],
          "heatmapgl": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmapgl"
           }
          ],
          "histogram": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "histogram"
           }
          ],
          "histogram2d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2d"
           }
          ],
          "histogram2dcontour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2dcontour"
           }
          ],
          "mesh3d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "mesh3d"
           }
          ],
          "parcoords": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "parcoords"
           }
          ],
          "pie": [
           {
            "automargin": true,
            "type": "pie"
           }
          ],
          "scatter": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter"
           }
          ],
          "scatter3d": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter3d"
           }
          ],
          "scattercarpet": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattercarpet"
           }
          ],
          "scattergeo": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergeo"
           }
          ],
          "scattergl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergl"
           }
          ],
          "scattermapbox": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattermapbox"
           }
          ],
          "scatterpolar": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolar"
           }
          ],
          "scatterpolargl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolargl"
           }
          ],
          "scatterternary": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterternary"
           }
          ],
          "surface": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "surface"
           }
          ],
          "table": [
           {
            "cells": {
             "fill": {
              "color": "#EBF0F8"
             },
             "line": {
              "color": "white"
             }
            },
            "header": {
             "fill": {
              "color": "#C8D4E3"
             },
             "line": {
              "color": "white"
             }
            },
            "type": "table"
           }
          ]
         },
         "layout": {
          "annotationdefaults": {
           "arrowcolor": "#2a3f5f",
           "arrowhead": 0,
           "arrowwidth": 1
          },
          "autotypenumbers": "strict",
          "coloraxis": {
           "colorbar": {
            "outlinewidth": 0,
            "ticks": ""
           }
          },
          "colorscale": {
           "diverging": [
            [
             0,
             "#8e0152"
            ],
            [
             0.1,
             "#c51b7d"
            ],
            [
             0.2,
             "#de77ae"
            ],
            [
             0.3,
             "#f1b6da"
            ],
            [
             0.4,
             "#fde0ef"
            ],
            [
             0.5,
             "#f7f7f7"
            ],
            [
             0.6,
             "#e6f5d0"
            ],
            [
             0.7,
             "#b8e186"
            ],
            [
             0.8,
             "#7fbc41"
            ],
            [
             0.9,
             "#4d9221"
            ],
            [
             1,
             "#276419"
            ]
           ],
           "sequential": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ],
           "sequentialminus": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ]
          },
          "colorway": [
           "#636efa",
           "#EF553B",
           "#00cc96",
           "#ab63fa",
           "#FFA15A",
           "#19d3f3",
           "#FF6692",
           "#B6E880",
           "#FF97FF",
           "#FECB52"
          ],
          "font": {
           "color": "#2a3f5f"
          },
          "geo": {
           "bgcolor": "white",
           "lakecolor": "white",
           "landcolor": "#E5ECF6",
           "showlakes": true,
           "showland": true,
           "subunitcolor": "white"
          },
          "hoverlabel": {
           "align": "left"
          },
          "hovermode": "closest",
          "mapbox": {
           "style": "light"
          },
          "paper_bgcolor": "white",
          "plot_bgcolor": "#E5ECF6",
          "polar": {
           "angularaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "radialaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "scene": {
           "xaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "yaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "zaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           }
          },
          "shapedefaults": {
           "line": {
            "color": "#2a3f5f"
           }
          },
          "ternary": {
           "aaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "baxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "caxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "title": {
           "x": 0.05
          },
          "xaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          },
          "yaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          }
         }
        }
       }
      }
     },
     "metadata": {}
    }
   ],
   "source": [
    "act_df = df.loc[df[\"disband\"] == 1]\n",
    "act_num = act_df.shape[0]\n",
    "nact_df = df.loc[df[\"disband\"] != 1]\n",
    "nact_num = nact_df.shape[0]\n",
    "labels = [\"Active\",\"Inactive\"]\n",
    "values = [act_num, nact_num]\n",
    "fig = go.Figure(data=[go.Pie(labels=labels, values=values)])\n",
    "fig.show()"
   ]
  },
  {
   "source": [
    "### Имеет ли группа название фандома"
   ],
   "cell_type": "markdown",
   "metadata": {}
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "output_type": "display_data",
     "data": {
      "application/vnd.plotly.v1+json": {
       "config": {
        "plotlyServerURL": "https://plot.ly"
       },
       "data": [
        {
         "labels": [
          "Have",
          "Haven't"
         ],
         "type": "pie",
         "values": [
          107,
          192
         ]
        }
       ],
       "layout": {
        "template": {
         "data": {
          "bar": [
           {
            "error_x": {
             "color": "#2a3f5f"
            },
            "error_y": {
             "color": "#2a3f5f"
            },
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             }
            },
            "type": "bar"
           }
          ],
          "barpolar": [
           {
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             }
            },
            "type": "barpolar"
           }
          ],
          "carpet": [
           {
            "aaxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "baxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "type": "carpet"
           }
          ],
          "choropleth": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "choropleth"
           }
          ],
          "contour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "contour"
           }
          ],
          "contourcarpet": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "contourcarpet"
           }
          ],
          "heatmap": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmap"
           }
          ],
          "heatmapgl": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmapgl"
           }
          ],
          "histogram": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "histogram"
           }
          ],
          "histogram2d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2d"
           }
          ],
          "histogram2dcontour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2dcontour"
           }
          ],
          "mesh3d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "mesh3d"
           }
          ],
          "parcoords": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "parcoords"
           }
          ],
          "pie": [
           {
            "automargin": true,
            "type": "pie"
           }
          ],
          "scatter": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter"
           }
          ],
          "scatter3d": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter3d"
           }
          ],
          "scattercarpet": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattercarpet"
           }
          ],
          "scattergeo": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergeo"
           }
          ],
          "scattergl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergl"
           }
          ],
          "scattermapbox": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattermapbox"
           }
          ],
          "scatterpolar": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolar"
           }
          ],
          "scatterpolargl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolargl"
           }
          ],
          "scatterternary": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterternary"
           }
          ],
          "surface": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "surface"
           }
          ],
          "table": [
           {
            "cells": {
             "fill": {
              "color": "#EBF0F8"
             },
             "line": {
              "color": "white"
             }
            },
            "header": {
             "fill": {
              "color": "#C8D4E3"
             },
             "line": {
              "color": "white"
             }
            },
            "type": "table"
           }
          ]
         },
         "layout": {
          "annotationdefaults": {
           "arrowcolor": "#2a3f5f",
           "arrowhead": 0,
           "arrowwidth": 1
          },
          "autotypenumbers": "strict",
          "coloraxis": {
           "colorbar": {
            "outlinewidth": 0,
            "ticks": ""
           }
          },
          "colorscale": {
           "diverging": [
            [
             0,
             "#8e0152"
            ],
            [
             0.1,
             "#c51b7d"
            ],
            [
             0.2,
             "#de77ae"
            ],
            [
             0.3,
             "#f1b6da"
            ],
            [
             0.4,
             "#fde0ef"
            ],
            [
             0.5,
             "#f7f7f7"
            ],
            [
             0.6,
             "#e6f5d0"
            ],
            [
             0.7,
             "#b8e186"
            ],
            [
             0.8,
             "#7fbc41"
            ],
            [
             0.9,
             "#4d9221"
            ],
            [
             1,
             "#276419"
            ]
           ],
           "sequential": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ],
           "sequentialminus": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ]
          },
          "colorway": [
           "#636efa",
           "#EF553B",
           "#00cc96",
           "#ab63fa",
           "#FFA15A",
           "#19d3f3",
           "#FF6692",
           "#B6E880",
           "#FF97FF",
           "#FECB52"
          ],
          "font": {
           "color": "#2a3f5f"
          },
          "geo": {
           "bgcolor": "white",
           "lakecolor": "white",
           "landcolor": "#E5ECF6",
           "showlakes": true,
           "showland": true,
           "subunitcolor": "white"
          },
          "hoverlabel": {
           "align": "left"
          },
          "hovermode": "closest",
          "mapbox": {
           "style": "light"
          },
          "paper_bgcolor": "white",
          "plot_bgcolor": "#E5ECF6",
          "polar": {
           "angularaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "radialaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "scene": {
           "xaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "yaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "zaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           }
          },
          "shapedefaults": {
           "line": {
            "color": "#2a3f5f"
           }
          },
          "ternary": {
           "aaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "baxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "caxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "title": {
           "x": 0.05
          },
          "xaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          },
          "yaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          }
         }
        }
       }
      }
     },
     "metadata": {}
    }
   ],
   "source": [
    "act_df = df.loc[df[\"Fanclub Name\"] != \"-\"]\n",
    "act_num = act_df.shape[0]\n",
    "nact_df = df.loc[df[\"Fanclub Name\"] == \"-\"]\n",
    "nact_num = nact_df.shape[0]\n",
    "labels = [\"Have\",\"Haven't\"]\n",
    "values = [act_num, nact_num]\n",
    "fig = go.Figure(data=[go.Pie(labels=labels, values=values)])\n",
    "fig.show()"
   ]
  },
  {
   "source": [
    "### Каких групп больше женских ии мужских"
   ],
   "cell_type": "markdown",
   "metadata": {}
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "metadata": {},
   "outputs": [
    {
     "output_type": "display_data",
     "data": {
      "application/vnd.plotly.v1+json": {
       "config": {
        "plotlyServerURL": "https://plot.ly"
       },
       "data": [
        {
         "labels": [
          "M",
          "F"
         ],
         "type": "pie",
         "values": [
          147,
          152
         ]
        }
       ],
       "layout": {
        "template": {
         "data": {
          "bar": [
           {
            "error_x": {
             "color": "#2a3f5f"
            },
            "error_y": {
             "color": "#2a3f5f"
            },
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             }
            },
            "type": "bar"
           }
          ],
          "barpolar": [
           {
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             }
            },
            "type": "barpolar"
           }
          ],
          "carpet": [
           {
            "aaxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "baxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "type": "carpet"
           }
          ],
          "choropleth": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "choropleth"
           }
          ],
          "contour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "contour"
           }
          ],
          "contourcarpet": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "contourcarpet"
           }
          ],
          "heatmap": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmap"
           }
          ],
          "heatmapgl": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmapgl"
           }
          ],
          "histogram": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "histogram"
           }
          ],
          "histogram2d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2d"
           }
          ],
          "histogram2dcontour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2dcontour"
           }
          ],
          "mesh3d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "mesh3d"
           }
          ],
          "parcoords": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "parcoords"
           }
          ],
          "pie": [
           {
            "automargin": true,
            "type": "pie"
           }
          ],
          "scatter": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter"
           }
          ],
          "scatter3d": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter3d"
           }
          ],
          "scattercarpet": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattercarpet"
           }
          ],
          "scattergeo": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergeo"
           }
          ],
          "scattergl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergl"
           }
          ],
          "scattermapbox": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattermapbox"
           }
          ],
          "scatterpolar": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolar"
           }
          ],
          "scatterpolargl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolargl"
           }
          ],
          "scatterternary": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterternary"
           }
          ],
          "surface": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "surface"
           }
          ],
          "table": [
           {
            "cells": {
             "fill": {
              "color": "#EBF0F8"
             },
             "line": {
              "color": "white"
             }
            },
            "header": {
             "fill": {
              "color": "#C8D4E3"
             },
             "line": {
              "color": "white"
             }
            },
            "type": "table"
           }
          ]
         },
         "layout": {
          "annotationdefaults": {
           "arrowcolor": "#2a3f5f",
           "arrowhead": 0,
           "arrowwidth": 1
          },
          "autotypenumbers": "strict",
          "coloraxis": {
           "colorbar": {
            "outlinewidth": 0,
            "ticks": ""
           }
          },
          "colorscale": {
           "diverging": [
            [
             0,
             "#8e0152"
            ],
            [
             0.1,
             "#c51b7d"
            ],
            [
             0.2,
             "#de77ae"
            ],
            [
             0.3,
             "#f1b6da"
            ],
            [
             0.4,
             "#fde0ef"
            ],
            [
             0.5,
             "#f7f7f7"
            ],
            [
             0.6,
             "#e6f5d0"
            ],
            [
             0.7,
             "#b8e186"
            ],
            [
             0.8,
             "#7fbc41"
            ],
            [
             0.9,
             "#4d9221"
            ],
            [
             1,
             "#276419"
            ]
           ],
           "sequential": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ],
           "sequentialminus": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ]
          },
          "colorway": [
           "#636efa",
           "#EF553B",
           "#00cc96",
           "#ab63fa",
           "#FFA15A",
           "#19d3f3",
           "#FF6692",
           "#B6E880",
           "#FF97FF",
           "#FECB52"
          ],
          "font": {
           "color": "#2a3f5f"
          },
          "geo": {
           "bgcolor": "white",
           "lakecolor": "white",
           "landcolor": "#E5ECF6",
           "showlakes": true,
           "showland": true,
           "subunitcolor": "white"
          },
          "hoverlabel": {
           "align": "left"
          },
          "hovermode": "closest",
          "mapbox": {
           "style": "light"
          },
          "paper_bgcolor": "white",
          "plot_bgcolor": "#E5ECF6",
          "polar": {
           "angularaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "radialaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "scene": {
           "xaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "yaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "zaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           }
          },
          "shapedefaults": {
           "line": {
            "color": "#2a3f5f"
           }
          },
          "ternary": {
           "aaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "baxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "caxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "title": {
           "x": 0.05
          },
          "xaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          },
          "yaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          }
         }
        }
       }
      }
     },
     "metadata": {}
    }
   ],
   "source": [
    "male_df = df.loc[df[\"Gender\"] == 0]\n",
    "m_num = male_df.shape[0]\n",
    "fem_df = df.loc[df[\"Gender\"] == 1]\n",
    "f_num = fem_df.shape[0]\n",
    "labels = [\"M\",\"F\"]\n",
    "values = [m_num, f_num]\n",
    "fig = go.Figure(data=[go.Pie(labels=labels, values=values)])\n",
    "fig.show()"
   ]
  },
  {
   "source": [
    "### Какая компания выпустила больше всего групп?"
   ],
   "cell_type": "markdown",
   "metadata": {}
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {},
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "<AxesSubplot:xlabel='Company', ylabel='Num'>"
      ]
     },
     "metadata": {},
     "execution_count": 41
    },
    {
     "output_type": "display_data",
     "data": {
      "text/plain": "<Figure size 432x288 with 1 Axes>",
      "image/svg+xml": "<?xml version=\"1.0\" encoding=\"utf-8\" standalone=\"no\"?>\r\n<!DOCTYPE svg PUBLIC \"-//W3C//DTD SVG 1.1//EN\"\r\n  \"http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd\">\r\n<svg height=\"262.19625pt\" version=\"1.1\" viewBox=\"0 0 411.059375 262.19625\" width=\"411.059375pt\" xmlns=\"http://www.w3.org/2000/svg\" xmlns:xlink=\"http://www.w3.org/1999/xlink\">\r\n <metadata>\r\n  <rdf:RDF xmlns:cc=\"http://creativecommons.org/ns#\" xmlns:dc=\"http://purl.org/dc/elements/1.1/\" xmlns:rdf=\"http://www.w3.org/1999/02/22-rdf-syntax-ns#\">\r\n   <cc:Work>\r\n    <dc:type rdf:resource=\"http://purl.org/dc/dcmitype/StillImage\"/>\r\n    <dc:date>2021-04-20T22:10:52.687905</dc:date>\r\n    <dc:format>image/svg+xml</dc:format>\r\n    <dc:creator>\r\n     <cc:Agent>\r\n      <dc:title>Matplotlib v3.4.1, https://matplotlib.org/</dc:title>\r\n     </cc:Agent>\r\n    </dc:creator>\r\n   </cc:Work>\r\n  </rdf:RDF>\r\n </metadata>\r\n <defs>\r\n  <style type=\"text/css\">*{stroke-linecap:butt;stroke-linejoin:round;}</style>\r\n </defs>\r\n <g id=\"figure_1\">\r\n  <g id=\"patch_1\">\r\n   <path d=\"M 0 262.19625 \r\nL 411.059375 262.19625 \r\nL 411.059375 0 \r\nL 0 0 \r\nz\r\n\" style=\"fill:none;\"/>\r\n  </g>\r\n  <g id=\"axes_1\">\r\n   <g id=\"patch_2\">\r\n    <path d=\"M 69.059375 224.64 \r\nL 403.859375 224.64 \r\nL 403.859375 7.2 \r\nL 69.059375 7.2 \r\nz\r\n\" style=\"fill:#ffffff;\"/>\r\n   </g>\r\n   <g id=\"patch_3\">\r\n    <path clip-path=\"url(#p61a91bb0c0)\" d=\"M 69.059375 9.616 \r\nL 182.936926 9.616 \r\nL 182.936926 28.944 \r\nL 69.059375 28.944 \r\nz\r\n\" style=\"fill:#3274a1;\"/>\r\n   </g>\r\n   <g id=\"patch_4\">\r\n    <path clip-path=\"url(#p61a91bb0c0)\" d=\"M 69.059375 33.776 \r\nL 182.936926 33.776 \r\nL 182.936926 53.104 \r\nL 69.059375 53.104 \r\nz\r\n\" style=\"fill:#e1812c;\"/>\r\n   </g>\r\n   <g id=\"patch_5\">\r\n    <path clip-path=\"url(#p61a91bb0c0)\" d=\"M 69.059375 57.936 \r\nL 182.936926 57.936 \r\nL 182.936926 77.264 \r\nL 69.059375 77.264 \r\nz\r\n\" style=\"fill:#3a923a;\"/>\r\n   </g>\r\n   <g id=\"patch_6\">\r\n    <path clip-path=\"url(#p61a91bb0c0)\" d=\"M 69.059375 82.096 \r\nL 182.936926 82.096 \r\nL 182.936926 101.424 \r\nL 69.059375 101.424 \r\nz\r\n\" style=\"fill:#c03d3e;\"/>\r\n   </g>\r\n   <g id=\"patch_7\">\r\n    <path clip-path=\"url(#p61a91bb0c0)\" d=\"M 69.059375 106.256 \r\nL 205.712436 106.256 \r\nL 205.712436 125.584 \r\nL 69.059375 125.584 \r\nz\r\n\" style=\"fill:#9372b2;\"/>\r\n   </g>\r\n   <g id=\"patch_8\">\r\n    <path clip-path=\"url(#p61a91bb0c0)\" d=\"M 69.059375 130.416 \r\nL 205.712436 130.416 \r\nL 205.712436 149.744 \r\nL 69.059375 149.744 \r\nz\r\n\" style=\"fill:#845b53;\"/>\r\n   </g>\r\n   <g id=\"patch_9\">\r\n    <path clip-path=\"url(#p61a91bb0c0)\" d=\"M 69.059375 154.576 \r\nL 228.487946 154.576 \r\nL 228.487946 173.904 \r\nL 69.059375 173.904 \r\nz\r\n\" style=\"fill:#d684bd;\"/>\r\n   </g>\r\n   <g id=\"patch_10\">\r\n    <path clip-path=\"url(#p61a91bb0c0)\" d=\"M 69.059375 178.736 \r\nL 319.589987 178.736 \r\nL 319.589987 198.064 \r\nL 69.059375 198.064 \r\nz\r\n\" style=\"fill:#7f7f7f;\"/>\r\n   </g>\r\n   <g id=\"patch_11\">\r\n    <path clip-path=\"url(#p61a91bb0c0)\" d=\"M 69.059375 202.896 \r\nL 387.916518 202.896 \r\nL 387.916518 222.224 \r\nL 69.059375 222.224 \r\nz\r\n\" style=\"fill:#a9aa35;\"/>\r\n   </g>\r\n   <g id=\"matplotlib.axis_1\">\r\n    <g id=\"xtick_1\">\r\n     <g id=\"line2d_1\">\r\n      <defs>\r\n       <path d=\"M 0 0 \r\nL 0 3.5 \r\n\" id=\"mca558c8b39\" style=\"stroke:#000000;stroke-width:0.8;\"/>\r\n      </defs>\r\n      <g>\r\n       <use style=\"stroke:#000000;stroke-width:0.8;\" x=\"69.059375\" xlink:href=\"#mca558c8b39\" y=\"224.64\"/>\r\n      </g>\r\n     </g>\r\n     <g id=\"text_1\">\r\n      <!-- 0 -->\r\n      <g transform=\"translate(65.878125 239.238437)scale(0.1 -0.1)\">\r\n       <defs>\r\n        <path d=\"M 2034 4250 \r\nQ 1547 4250 1301 3770 \r\nQ 1056 3291 1056 2328 \r\nQ 1056 1369 1301 889 \r\nQ 1547 409 2034 409 \r\nQ 2525 409 2770 889 \r\nQ 3016 1369 3016 2328 \r\nQ 3016 3291 2770 3770 \r\nQ 2525 4250 2034 4250 \r\nz\r\nM 2034 4750 \r\nQ 2819 4750 3233 4129 \r\nQ 3647 3509 3647 2328 \r\nQ 3647 1150 3233 529 \r\nQ 2819 -91 2034 -91 \r\nQ 1250 -91 836 529 \r\nQ 422 1150 422 2328 \r\nQ 422 3509 836 4129 \r\nQ 1250 4750 2034 4750 \r\nz\r\n\" id=\"DejaVuSans-30\" transform=\"scale(0.015625)\"/>\r\n       </defs>\r\n       <use xlink:href=\"#DejaVuSans-30\"/>\r\n      </g>\r\n     </g>\r\n    </g>\r\n    <g id=\"xtick_2\">\r\n     <g id=\"line2d_2\">\r\n      <g>\r\n       <use style=\"stroke:#000000;stroke-width:0.8;\" x=\"114.610395\" xlink:href=\"#mca558c8b39\" y=\"224.64\"/>\r\n      </g>\r\n     </g>\r\n     <g id=\"text_2\">\r\n      <!-- 2 -->\r\n      <g transform=\"translate(111.429145 239.238437)scale(0.1 -0.1)\">\r\n       <defs>\r\n        <path d=\"M 1228 531 \r\nL 3431 531 \r\nL 3431 0 \r\nL 469 0 \r\nL 469 531 \r\nQ 828 903 1448 1529 \r\nQ 2069 2156 2228 2338 \r\nQ 2531 2678 2651 2914 \r\nQ 2772 3150 2772 3378 \r\nQ 2772 3750 2511 3984 \r\nQ 2250 4219 1831 4219 \r\nQ 1534 4219 1204 4116 \r\nQ 875 4013 500 3803 \r\nL 500 4441 \r\nQ 881 4594 1212 4672 \r\nQ 1544 4750 1819 4750 \r\nQ 2544 4750 2975 4387 \r\nQ 3406 4025 3406 3419 \r\nQ 3406 3131 3298 2873 \r\nQ 3191 2616 2906 2266 \r\nQ 2828 2175 2409 1742 \r\nQ 1991 1309 1228 531 \r\nz\r\n\" id=\"DejaVuSans-32\" transform=\"scale(0.015625)\"/>\r\n       </defs>\r\n       <use xlink:href=\"#DejaVuSans-32\"/>\r\n      </g>\r\n     </g>\r\n    </g>\r\n    <g id=\"xtick_3\">\r\n     <g id=\"line2d_3\">\r\n      <g>\r\n       <use style=\"stroke:#000000;stroke-width:0.8;\" x=\"160.161416\" xlink:href=\"#mca558c8b39\" y=\"224.64\"/>\r\n      </g>\r\n     </g>\r\n     <g id=\"text_3\">\r\n      <!-- 4 -->\r\n      <g transform=\"translate(156.980166 239.238437)scale(0.1 -0.1)\">\r\n       <defs>\r\n        <path d=\"M 2419 4116 \r\nL 825 1625 \r\nL 2419 1625 \r\nL 2419 4116 \r\nz\r\nM 2253 4666 \r\nL 3047 4666 \r\nL 3047 1625 \r\nL 3713 1625 \r\nL 3713 1100 \r\nL 3047 1100 \r\nL 3047 0 \r\nL 2419 0 \r\nL 2419 1100 \r\nL 313 1100 \r\nL 313 1709 \r\nL 2253 4666 \r\nz\r\n\" id=\"DejaVuSans-34\" transform=\"scale(0.015625)\"/>\r\n       </defs>\r\n       <use xlink:href=\"#DejaVuSans-34\"/>\r\n      </g>\r\n     </g>\r\n    </g>\r\n    <g id=\"xtick_4\">\r\n     <g id=\"line2d_4\">\r\n      <g>\r\n       <use style=\"stroke:#000000;stroke-width:0.8;\" x=\"205.712436\" xlink:href=\"#mca558c8b39\" y=\"224.64\"/>\r\n      </g>\r\n     </g>\r\n     <g id=\"text_4\">\r\n      <!-- 6 -->\r\n      <g transform=\"translate(202.531186 239.238437)scale(0.1 -0.1)\">\r\n       <defs>\r\n        <path d=\"M 2113 2584 \r\nQ 1688 2584 1439 2293 \r\nQ 1191 2003 1191 1497 \r\nQ 1191 994 1439 701 \r\nQ 1688 409 2113 409 \r\nQ 2538 409 2786 701 \r\nQ 3034 994 3034 1497 \r\nQ 3034 2003 2786 2293 \r\nQ 2538 2584 2113 2584 \r\nz\r\nM 3366 4563 \r\nL 3366 3988 \r\nQ 3128 4100 2886 4159 \r\nQ 2644 4219 2406 4219 \r\nQ 1781 4219 1451 3797 \r\nQ 1122 3375 1075 2522 \r\nQ 1259 2794 1537 2939 \r\nQ 1816 3084 2150 3084 \r\nQ 2853 3084 3261 2657 \r\nQ 3669 2231 3669 1497 \r\nQ 3669 778 3244 343 \r\nQ 2819 -91 2113 -91 \r\nQ 1303 -91 875 529 \r\nQ 447 1150 447 2328 \r\nQ 447 3434 972 4092 \r\nQ 1497 4750 2381 4750 \r\nQ 2619 4750 2861 4703 \r\nQ 3103 4656 3366 4563 \r\nz\r\n\" id=\"DejaVuSans-36\" transform=\"scale(0.015625)\"/>\r\n       </defs>\r\n       <use xlink:href=\"#DejaVuSans-36\"/>\r\n      </g>\r\n     </g>\r\n    </g>\r\n    <g id=\"xtick_5\">\r\n     <g id=\"line2d_5\">\r\n      <g>\r\n       <use style=\"stroke:#000000;stroke-width:0.8;\" x=\"251.263457\" xlink:href=\"#mca558c8b39\" y=\"224.64\"/>\r\n      </g>\r\n     </g>\r\n     <g id=\"text_5\">\r\n      <!-- 8 -->\r\n      <g transform=\"translate(248.082207 239.238437)scale(0.1 -0.1)\">\r\n       <defs>\r\n        <path d=\"M 2034 2216 \r\nQ 1584 2216 1326 1975 \r\nQ 1069 1734 1069 1313 \r\nQ 1069 891 1326 650 \r\nQ 1584 409 2034 409 \r\nQ 2484 409 2743 651 \r\nQ 3003 894 3003 1313 \r\nQ 3003 1734 2745 1975 \r\nQ 2488 2216 2034 2216 \r\nz\r\nM 1403 2484 \r\nQ 997 2584 770 2862 \r\nQ 544 3141 544 3541 \r\nQ 544 4100 942 4425 \r\nQ 1341 4750 2034 4750 \r\nQ 2731 4750 3128 4425 \r\nQ 3525 4100 3525 3541 \r\nQ 3525 3141 3298 2862 \r\nQ 3072 2584 2669 2484 \r\nQ 3125 2378 3379 2068 \r\nQ 3634 1759 3634 1313 \r\nQ 3634 634 3220 271 \r\nQ 2806 -91 2034 -91 \r\nQ 1263 -91 848 271 \r\nQ 434 634 434 1313 \r\nQ 434 1759 690 2068 \r\nQ 947 2378 1403 2484 \r\nz\r\nM 1172 3481 \r\nQ 1172 3119 1398 2916 \r\nQ 1625 2713 2034 2713 \r\nQ 2441 2713 2670 2916 \r\nQ 2900 3119 2900 3481 \r\nQ 2900 3844 2670 4047 \r\nQ 2441 4250 2034 4250 \r\nQ 1625 4250 1398 4047 \r\nQ 1172 3844 1172 3481 \r\nz\r\n\" id=\"DejaVuSans-38\" transform=\"scale(0.015625)\"/>\r\n       </defs>\r\n       <use xlink:href=\"#DejaVuSans-38\"/>\r\n      </g>\r\n     </g>\r\n    </g>\r\n    <g id=\"xtick_6\">\r\n     <g id=\"line2d_6\">\r\n      <g>\r\n       <use style=\"stroke:#000000;stroke-width:0.8;\" x=\"296.814477\" xlink:href=\"#mca558c8b39\" y=\"224.64\"/>\r\n      </g>\r\n     </g>\r\n     <g id=\"text_6\">\r\n      <!-- 10 -->\r\n      <g transform=\"translate(290.451977 239.238437)scale(0.1 -0.1)\">\r\n       <defs>\r\n        <path d=\"M 794 531 \r\nL 1825 531 \r\nL 1825 4091 \r\nL 703 3866 \r\nL 703 4441 \r\nL 1819 4666 \r\nL 2450 4666 \r\nL 2450 531 \r\nL 3481 531 \r\nL 3481 0 \r\nL 794 0 \r\nL 794 531 \r\nz\r\n\" id=\"DejaVuSans-31\" transform=\"scale(0.015625)\"/>\r\n       </defs>\r\n       <use xlink:href=\"#DejaVuSans-31\"/>\r\n       <use x=\"63.623047\" xlink:href=\"#DejaVuSans-30\"/>\r\n      </g>\r\n     </g>\r\n    </g>\r\n    <g id=\"xtick_7\">\r\n     <g id=\"line2d_7\">\r\n      <g>\r\n       <use style=\"stroke:#000000;stroke-width:0.8;\" x=\"342.365497\" xlink:href=\"#mca558c8b39\" y=\"224.64\"/>\r\n      </g>\r\n     </g>\r\n     <g id=\"text_7\">\r\n      <!-- 12 -->\r\n      <g transform=\"translate(336.002997 239.238437)scale(0.1 -0.1)\">\r\n       <use xlink:href=\"#DejaVuSans-31\"/>\r\n       <use x=\"63.623047\" xlink:href=\"#DejaVuSans-32\"/>\r\n      </g>\r\n     </g>\r\n    </g>\r\n    <g id=\"xtick_8\">\r\n     <g id=\"line2d_8\">\r\n      <g>\r\n       <use style=\"stroke:#000000;stroke-width:0.8;\" x=\"387.916518\" xlink:href=\"#mca558c8b39\" y=\"224.64\"/>\r\n      </g>\r\n     </g>\r\n     <g id=\"text_8\">\r\n      <!-- 14 -->\r\n      <g transform=\"translate(381.554018 239.238437)scale(0.1 -0.1)\">\r\n       <use xlink:href=\"#DejaVuSans-31\"/>\r\n       <use x=\"63.623047\" xlink:href=\"#DejaVuSans-34\"/>\r\n      </g>\r\n     </g>\r\n    </g>\r\n    <g id=\"text_9\">\r\n     <!-- Company -->\r\n     <g transform=\"translate(212.671875 252.916562)scale(0.1 -0.1)\">\r\n      <defs>\r\n       <path d=\"M 4122 4306 \r\nL 4122 3641 \r\nQ 3803 3938 3442 4084 \r\nQ 3081 4231 2675 4231 \r\nQ 1875 4231 1450 3742 \r\nQ 1025 3253 1025 2328 \r\nQ 1025 1406 1450 917 \r\nQ 1875 428 2675 428 \r\nQ 3081 428 3442 575 \r\nQ 3803 722 4122 1019 \r\nL 4122 359 \r\nQ 3791 134 3420 21 \r\nQ 3050 -91 2638 -91 \r\nQ 1578 -91 968 557 \r\nQ 359 1206 359 2328 \r\nQ 359 3453 968 4101 \r\nQ 1578 4750 2638 4750 \r\nQ 3056 4750 3426 4639 \r\nQ 3797 4528 4122 4306 \r\nz\r\n\" id=\"DejaVuSans-43\" transform=\"scale(0.015625)\"/>\r\n       <path d=\"M 1959 3097 \r\nQ 1497 3097 1228 2736 \r\nQ 959 2375 959 1747 \r\nQ 959 1119 1226 758 \r\nQ 1494 397 1959 397 \r\nQ 2419 397 2687 759 \r\nQ 2956 1122 2956 1747 \r\nQ 2956 2369 2687 2733 \r\nQ 2419 3097 1959 3097 \r\nz\r\nM 1959 3584 \r\nQ 2709 3584 3137 3096 \r\nQ 3566 2609 3566 1747 \r\nQ 3566 888 3137 398 \r\nQ 2709 -91 1959 -91 \r\nQ 1206 -91 779 398 \r\nQ 353 888 353 1747 \r\nQ 353 2609 779 3096 \r\nQ 1206 3584 1959 3584 \r\nz\r\n\" id=\"DejaVuSans-6f\" transform=\"scale(0.015625)\"/>\r\n       <path d=\"M 3328 2828 \r\nQ 3544 3216 3844 3400 \r\nQ 4144 3584 4550 3584 \r\nQ 5097 3584 5394 3201 \r\nQ 5691 2819 5691 2113 \r\nL 5691 0 \r\nL 5113 0 \r\nL 5113 2094 \r\nQ 5113 2597 4934 2840 \r\nQ 4756 3084 4391 3084 \r\nQ 3944 3084 3684 2787 \r\nQ 3425 2491 3425 1978 \r\nL 3425 0 \r\nL 2847 0 \r\nL 2847 2094 \r\nQ 2847 2600 2669 2842 \r\nQ 2491 3084 2119 3084 \r\nQ 1678 3084 1418 2786 \r\nQ 1159 2488 1159 1978 \r\nL 1159 0 \r\nL 581 0 \r\nL 581 3500 \r\nL 1159 3500 \r\nL 1159 2956 \r\nQ 1356 3278 1631 3431 \r\nQ 1906 3584 2284 3584 \r\nQ 2666 3584 2933 3390 \r\nQ 3200 3197 3328 2828 \r\nz\r\n\" id=\"DejaVuSans-6d\" transform=\"scale(0.015625)\"/>\r\n       <path d=\"M 1159 525 \r\nL 1159 -1331 \r\nL 581 -1331 \r\nL 581 3500 \r\nL 1159 3500 \r\nL 1159 2969 \r\nQ 1341 3281 1617 3432 \r\nQ 1894 3584 2278 3584 \r\nQ 2916 3584 3314 3078 \r\nQ 3713 2572 3713 1747 \r\nQ 3713 922 3314 415 \r\nQ 2916 -91 2278 -91 \r\nQ 1894 -91 1617 61 \r\nQ 1341 213 1159 525 \r\nz\r\nM 3116 1747 \r\nQ 3116 2381 2855 2742 \r\nQ 2594 3103 2138 3103 \r\nQ 1681 3103 1420 2742 \r\nQ 1159 2381 1159 1747 \r\nQ 1159 1113 1420 752 \r\nQ 1681 391 2138 391 \r\nQ 2594 391 2855 752 \r\nQ 3116 1113 3116 1747 \r\nz\r\n\" id=\"DejaVuSans-70\" transform=\"scale(0.015625)\"/>\r\n       <path d=\"M 2194 1759 \r\nQ 1497 1759 1228 1600 \r\nQ 959 1441 959 1056 \r\nQ 959 750 1161 570 \r\nQ 1363 391 1709 391 \r\nQ 2188 391 2477 730 \r\nQ 2766 1069 2766 1631 \r\nL 2766 1759 \r\nL 2194 1759 \r\nz\r\nM 3341 1997 \r\nL 3341 0 \r\nL 2766 0 \r\nL 2766 531 \r\nQ 2569 213 2275 61 \r\nQ 1981 -91 1556 -91 \r\nQ 1019 -91 701 211 \r\nQ 384 513 384 1019 \r\nQ 384 1609 779 1909 \r\nQ 1175 2209 1959 2209 \r\nL 2766 2209 \r\nL 2766 2266 \r\nQ 2766 2663 2505 2880 \r\nQ 2244 3097 1772 3097 \r\nQ 1472 3097 1187 3025 \r\nQ 903 2953 641 2809 \r\nL 641 3341 \r\nQ 956 3463 1253 3523 \r\nQ 1550 3584 1831 3584 \r\nQ 2591 3584 2966 3190 \r\nQ 3341 2797 3341 1997 \r\nz\r\n\" id=\"DejaVuSans-61\" transform=\"scale(0.015625)\"/>\r\n       <path d=\"M 3513 2113 \r\nL 3513 0 \r\nL 2938 0 \r\nL 2938 2094 \r\nQ 2938 2591 2744 2837 \r\nQ 2550 3084 2163 3084 \r\nQ 1697 3084 1428 2787 \r\nQ 1159 2491 1159 1978 \r\nL 1159 0 \r\nL 581 0 \r\nL 581 3500 \r\nL 1159 3500 \r\nL 1159 2956 \r\nQ 1366 3272 1645 3428 \r\nQ 1925 3584 2291 3584 \r\nQ 2894 3584 3203 3211 \r\nQ 3513 2838 3513 2113 \r\nz\r\n\" id=\"DejaVuSans-6e\" transform=\"scale(0.015625)\"/>\r\n       <path d=\"M 2059 -325 \r\nQ 1816 -950 1584 -1140 \r\nQ 1353 -1331 966 -1331 \r\nL 506 -1331 \r\nL 506 -850 \r\nL 844 -850 \r\nQ 1081 -850 1212 -737 \r\nQ 1344 -625 1503 -206 \r\nL 1606 56 \r\nL 191 3500 \r\nL 800 3500 \r\nL 1894 763 \r\nL 2988 3500 \r\nL 3597 3500 \r\nL 2059 -325 \r\nz\r\n\" id=\"DejaVuSans-79\" transform=\"scale(0.015625)\"/>\r\n      </defs>\r\n      <use xlink:href=\"#DejaVuSans-43\"/>\r\n      <use x=\"69.824219\" xlink:href=\"#DejaVuSans-6f\"/>\r\n      <use x=\"131.005859\" xlink:href=\"#DejaVuSans-6d\"/>\r\n      <use x=\"228.417969\" xlink:href=\"#DejaVuSans-70\"/>\r\n      <use x=\"291.894531\" xlink:href=\"#DejaVuSans-61\"/>\r\n      <use x=\"353.173828\" xlink:href=\"#DejaVuSans-6e\"/>\r\n      <use x=\"416.552734\" xlink:href=\"#DejaVuSans-79\"/>\r\n     </g>\r\n    </g>\r\n   </g>\r\n   <g id=\"matplotlib.axis_2\">\r\n    <g id=\"ytick_1\">\r\n     <g id=\"line2d_9\">\r\n      <defs>\r\n       <path d=\"M 0 0 \r\nL -3.5 0 \r\n\" id=\"m8f2b8fd4c8\" style=\"stroke:#000000;stroke-width:0.8;\"/>\r\n      </defs>\r\n      <g>\r\n       <use style=\"stroke:#000000;stroke-width:0.8;\" x=\"69.059375\" xlink:href=\"#m8f2b8fd4c8\" y=\"19.28\"/>\r\n      </g>\r\n     </g>\r\n     <g id=\"text_10\">\r\n      <!-- Big Hit -->\r\n      <g transform=\"translate(28.675 23.079219)scale(0.1 -0.1)\">\r\n       <defs>\r\n        <path d=\"M 1259 2228 \r\nL 1259 519 \r\nL 2272 519 \r\nQ 2781 519 3026 730 \r\nQ 3272 941 3272 1375 \r\nQ 3272 1813 3026 2020 \r\nQ 2781 2228 2272 2228 \r\nL 1259 2228 \r\nz\r\nM 1259 4147 \r\nL 1259 2741 \r\nL 2194 2741 \r\nQ 2656 2741 2882 2914 \r\nQ 3109 3088 3109 3444 \r\nQ 3109 3797 2882 3972 \r\nQ 2656 4147 2194 4147 \r\nL 1259 4147 \r\nz\r\nM 628 4666 \r\nL 2241 4666 \r\nQ 2963 4666 3353 4366 \r\nQ 3744 4066 3744 3513 \r\nQ 3744 3084 3544 2831 \r\nQ 3344 2578 2956 2516 \r\nQ 3422 2416 3680 2098 \r\nQ 3938 1781 3938 1306 \r\nQ 3938 681 3513 340 \r\nQ 3088 0 2303 0 \r\nL 628 0 \r\nL 628 4666 \r\nz\r\n\" id=\"DejaVuSans-42\" transform=\"scale(0.015625)\"/>\r\n        <path d=\"M 603 3500 \r\nL 1178 3500 \r\nL 1178 0 \r\nL 603 0 \r\nL 603 3500 \r\nz\r\nM 603 4863 \r\nL 1178 4863 \r\nL 1178 4134 \r\nL 603 4134 \r\nL 603 4863 \r\nz\r\n\" id=\"DejaVuSans-69\" transform=\"scale(0.015625)\"/>\r\n        <path d=\"M 2906 1791 \r\nQ 2906 2416 2648 2759 \r\nQ 2391 3103 1925 3103 \r\nQ 1463 3103 1205 2759 \r\nQ 947 2416 947 1791 \r\nQ 947 1169 1205 825 \r\nQ 1463 481 1925 481 \r\nQ 2391 481 2648 825 \r\nQ 2906 1169 2906 1791 \r\nz\r\nM 3481 434 \r\nQ 3481 -459 3084 -895 \r\nQ 2688 -1331 1869 -1331 \r\nQ 1566 -1331 1297 -1286 \r\nQ 1028 -1241 775 -1147 \r\nL 775 -588 \r\nQ 1028 -725 1275 -790 \r\nQ 1522 -856 1778 -856 \r\nQ 2344 -856 2625 -561 \r\nQ 2906 -266 2906 331 \r\nL 2906 616 \r\nQ 2728 306 2450 153 \r\nQ 2172 0 1784 0 \r\nQ 1141 0 747 490 \r\nQ 353 981 353 1791 \r\nQ 353 2603 747 3093 \r\nQ 1141 3584 1784 3584 \r\nQ 2172 3584 2450 3431 \r\nQ 2728 3278 2906 2969 \r\nL 2906 3500 \r\nL 3481 3500 \r\nL 3481 434 \r\nz\r\n\" id=\"DejaVuSans-67\" transform=\"scale(0.015625)\"/>\r\n        <path id=\"DejaVuSans-20\" transform=\"scale(0.015625)\"/>\r\n        <path d=\"M 628 4666 \r\nL 1259 4666 \r\nL 1259 2753 \r\nL 3553 2753 \r\nL 3553 4666 \r\nL 4184 4666 \r\nL 4184 0 \r\nL 3553 0 \r\nL 3553 2222 \r\nL 1259 2222 \r\nL 1259 0 \r\nL 628 0 \r\nL 628 4666 \r\nz\r\n\" id=\"DejaVuSans-48\" transform=\"scale(0.015625)\"/>\r\n        <path d=\"M 1172 4494 \r\nL 1172 3500 \r\nL 2356 3500 \r\nL 2356 3053 \r\nL 1172 3053 \r\nL 1172 1153 \r\nQ 1172 725 1289 603 \r\nQ 1406 481 1766 481 \r\nL 2356 481 \r\nL 2356 0 \r\nL 1766 0 \r\nQ 1100 0 847 248 \r\nQ 594 497 594 1153 \r\nL 594 3053 \r\nL 172 3053 \r\nL 172 3500 \r\nL 594 3500 \r\nL 594 4494 \r\nL 1172 4494 \r\nz\r\n\" id=\"DejaVuSans-74\" transform=\"scale(0.015625)\"/>\r\n       </defs>\r\n       <use xlink:href=\"#DejaVuSans-42\"/>\r\n       <use x=\"68.603516\" xlink:href=\"#DejaVuSans-69\"/>\r\n       <use x=\"96.386719\" xlink:href=\"#DejaVuSans-67\"/>\r\n       <use x=\"159.863281\" xlink:href=\"#DejaVuSans-20\"/>\r\n       <use x=\"191.650391\" xlink:href=\"#DejaVuSans-48\"/>\r\n       <use x=\"266.845703\" xlink:href=\"#DejaVuSans-69\"/>\r\n       <use x=\"294.628906\" xlink:href=\"#DejaVuSans-74\"/>\r\n      </g>\r\n     </g>\r\n    </g>\r\n    <g id=\"ytick_2\">\r\n     <g id=\"line2d_10\">\r\n      <g>\r\n       <use style=\"stroke:#000000;stroke-width:0.8;\" x=\"69.059375\" xlink:href=\"#m8f2b8fd4c8\" y=\"43.44\"/>\r\n      </g>\r\n     </g>\r\n     <g id=\"text_11\">\r\n      <!-- Cube -->\r\n      <g transform=\"translate(36.2375 47.239219)scale(0.1 -0.1)\">\r\n       <defs>\r\n        <path d=\"M 544 1381 \r\nL 544 3500 \r\nL 1119 3500 \r\nL 1119 1403 \r\nQ 1119 906 1312 657 \r\nQ 1506 409 1894 409 \r\nQ 2359 409 2629 706 \r\nQ 2900 1003 2900 1516 \r\nL 2900 3500 \r\nL 3475 3500 \r\nL 3475 0 \r\nL 2900 0 \r\nL 2900 538 \r\nQ 2691 219 2414 64 \r\nQ 2138 -91 1772 -91 \r\nQ 1169 -91 856 284 \r\nQ 544 659 544 1381 \r\nz\r\nM 1991 3584 \r\nL 1991 3584 \r\nz\r\n\" id=\"DejaVuSans-75\" transform=\"scale(0.015625)\"/>\r\n        <path d=\"M 3116 1747 \r\nQ 3116 2381 2855 2742 \r\nQ 2594 3103 2138 3103 \r\nQ 1681 3103 1420 2742 \r\nQ 1159 2381 1159 1747 \r\nQ 1159 1113 1420 752 \r\nQ 1681 391 2138 391 \r\nQ 2594 391 2855 752 \r\nQ 3116 1113 3116 1747 \r\nz\r\nM 1159 2969 \r\nQ 1341 3281 1617 3432 \r\nQ 1894 3584 2278 3584 \r\nQ 2916 3584 3314 3078 \r\nQ 3713 2572 3713 1747 \r\nQ 3713 922 3314 415 \r\nQ 2916 -91 2278 -91 \r\nQ 1894 -91 1617 61 \r\nQ 1341 213 1159 525 \r\nL 1159 0 \r\nL 581 0 \r\nL 581 4863 \r\nL 1159 4863 \r\nL 1159 2969 \r\nz\r\n\" id=\"DejaVuSans-62\" transform=\"scale(0.015625)\"/>\r\n        <path d=\"M 3597 1894 \r\nL 3597 1613 \r\nL 953 1613 \r\nQ 991 1019 1311 708 \r\nQ 1631 397 2203 397 \r\nQ 2534 397 2845 478 \r\nQ 3156 559 3463 722 \r\nL 3463 178 \r\nQ 3153 47 2828 -22 \r\nQ 2503 -91 2169 -91 \r\nQ 1331 -91 842 396 \r\nQ 353 884 353 1716 \r\nQ 353 2575 817 3079 \r\nQ 1281 3584 2069 3584 \r\nQ 2775 3584 3186 3129 \r\nQ 3597 2675 3597 1894 \r\nz\r\nM 3022 2063 \r\nQ 3016 2534 2758 2815 \r\nQ 2500 3097 2075 3097 \r\nQ 1594 3097 1305 2825 \r\nQ 1016 2553 972 2059 \r\nL 3022 2063 \r\nz\r\n\" id=\"DejaVuSans-65\" transform=\"scale(0.015625)\"/>\r\n       </defs>\r\n       <use xlink:href=\"#DejaVuSans-43\"/>\r\n       <use x=\"69.824219\" xlink:href=\"#DejaVuSans-75\"/>\r\n       <use x=\"133.203125\" xlink:href=\"#DejaVuSans-62\"/>\r\n       <use x=\"196.679688\" xlink:href=\"#DejaVuSans-65\"/>\r\n      </g>\r\n     </g>\r\n    </g>\r\n    <g id=\"ytick_3\">\r\n     <g id=\"line2d_11\">\r\n      <g>\r\n       <use style=\"stroke:#000000;stroke-width:0.8;\" x=\"69.059375\" xlink:href=\"#m8f2b8fd4c8\" y=\"67.6\"/>\r\n      </g>\r\n     </g>\r\n     <g id=\"text_12\">\r\n      <!-- Starship -->\r\n      <g transform=\"translate(20.878125 71.399219)scale(0.1 -0.1)\">\r\n       <defs>\r\n        <path d=\"M 3425 4513 \r\nL 3425 3897 \r\nQ 3066 4069 2747 4153 \r\nQ 2428 4238 2131 4238 \r\nQ 1616 4238 1336 4038 \r\nQ 1056 3838 1056 3469 \r\nQ 1056 3159 1242 3001 \r\nQ 1428 2844 1947 2747 \r\nL 2328 2669 \r\nQ 3034 2534 3370 2195 \r\nQ 3706 1856 3706 1288 \r\nQ 3706 609 3251 259 \r\nQ 2797 -91 1919 -91 \r\nQ 1588 -91 1214 -16 \r\nQ 841 59 441 206 \r\nL 441 856 \r\nQ 825 641 1194 531 \r\nQ 1563 422 1919 422 \r\nQ 2459 422 2753 634 \r\nQ 3047 847 3047 1241 \r\nQ 3047 1584 2836 1778 \r\nQ 2625 1972 2144 2069 \r\nL 1759 2144 \r\nQ 1053 2284 737 2584 \r\nQ 422 2884 422 3419 \r\nQ 422 4038 858 4394 \r\nQ 1294 4750 2059 4750 \r\nQ 2388 4750 2728 4690 \r\nQ 3069 4631 3425 4513 \r\nz\r\n\" id=\"DejaVuSans-53\" transform=\"scale(0.015625)\"/>\r\n        <path d=\"M 2631 2963 \r\nQ 2534 3019 2420 3045 \r\nQ 2306 3072 2169 3072 \r\nQ 1681 3072 1420 2755 \r\nQ 1159 2438 1159 1844 \r\nL 1159 0 \r\nL 581 0 \r\nL 581 3500 \r\nL 1159 3500 \r\nL 1159 2956 \r\nQ 1341 3275 1631 3429 \r\nQ 1922 3584 2338 3584 \r\nQ 2397 3584 2469 3576 \r\nQ 2541 3569 2628 3553 \r\nL 2631 2963 \r\nz\r\n\" id=\"DejaVuSans-72\" transform=\"scale(0.015625)\"/>\r\n        <path d=\"M 2834 3397 \r\nL 2834 2853 \r\nQ 2591 2978 2328 3040 \r\nQ 2066 3103 1784 3103 \r\nQ 1356 3103 1142 2972 \r\nQ 928 2841 928 2578 \r\nQ 928 2378 1081 2264 \r\nQ 1234 2150 1697 2047 \r\nL 1894 2003 \r\nQ 2506 1872 2764 1633 \r\nQ 3022 1394 3022 966 \r\nQ 3022 478 2636 193 \r\nQ 2250 -91 1575 -91 \r\nQ 1294 -91 989 -36 \r\nQ 684 19 347 128 \r\nL 347 722 \r\nQ 666 556 975 473 \r\nQ 1284 391 1588 391 \r\nQ 1994 391 2212 530 \r\nQ 2431 669 2431 922 \r\nQ 2431 1156 2273 1281 \r\nQ 2116 1406 1581 1522 \r\nL 1381 1569 \r\nQ 847 1681 609 1914 \r\nQ 372 2147 372 2553 \r\nQ 372 3047 722 3315 \r\nQ 1072 3584 1716 3584 \r\nQ 2034 3584 2315 3537 \r\nQ 2597 3491 2834 3397 \r\nz\r\n\" id=\"DejaVuSans-73\" transform=\"scale(0.015625)\"/>\r\n        <path d=\"M 3513 2113 \r\nL 3513 0 \r\nL 2938 0 \r\nL 2938 2094 \r\nQ 2938 2591 2744 2837 \r\nQ 2550 3084 2163 3084 \r\nQ 1697 3084 1428 2787 \r\nQ 1159 2491 1159 1978 \r\nL 1159 0 \r\nL 581 0 \r\nL 581 4863 \r\nL 1159 4863 \r\nL 1159 2956 \r\nQ 1366 3272 1645 3428 \r\nQ 1925 3584 2291 3584 \r\nQ 2894 3584 3203 3211 \r\nQ 3513 2838 3513 2113 \r\nz\r\n\" id=\"DejaVuSans-68\" transform=\"scale(0.015625)\"/>\r\n       </defs>\r\n       <use xlink:href=\"#DejaVuSans-53\"/>\r\n       <use x=\"63.476562\" xlink:href=\"#DejaVuSans-74\"/>\r\n       <use x=\"102.685547\" xlink:href=\"#DejaVuSans-61\"/>\r\n       <use x=\"163.964844\" xlink:href=\"#DejaVuSans-72\"/>\r\n       <use x=\"205.078125\" xlink:href=\"#DejaVuSans-73\"/>\r\n       <use x=\"257.177734\" xlink:href=\"#DejaVuSans-68\"/>\r\n       <use x=\"320.556641\" xlink:href=\"#DejaVuSans-69\"/>\r\n       <use x=\"348.339844\" xlink:href=\"#DejaVuSans-70\"/>\r\n      </g>\r\n     </g>\r\n    </g>\r\n    <g id=\"ytick_4\">\r\n     <g id=\"line2d_12\">\r\n      <g>\r\n       <use style=\"stroke:#000000;stroke-width:0.8;\" x=\"69.059375\" xlink:href=\"#m8f2b8fd4c8\" y=\"91.76\"/>\r\n      </g>\r\n     </g>\r\n     <g id=\"text_13\">\r\n      <!-- YG -->\r\n      <g transform=\"translate(48.203125 95.559219)scale(0.1 -0.1)\">\r\n       <defs>\r\n        <path d=\"M -13 4666 \r\nL 666 4666 \r\nL 1959 2747 \r\nL 3244 4666 \r\nL 3922 4666 \r\nL 2272 2222 \r\nL 2272 0 \r\nL 1638 0 \r\nL 1638 2222 \r\nL -13 4666 \r\nz\r\n\" id=\"DejaVuSans-59\" transform=\"scale(0.015625)\"/>\r\n        <path d=\"M 3809 666 \r\nL 3809 1919 \r\nL 2778 1919 \r\nL 2778 2438 \r\nL 4434 2438 \r\nL 4434 434 \r\nQ 4069 175 3628 42 \r\nQ 3188 -91 2688 -91 \r\nQ 1594 -91 976 548 \r\nQ 359 1188 359 2328 \r\nQ 359 3472 976 4111 \r\nQ 1594 4750 2688 4750 \r\nQ 3144 4750 3555 4637 \r\nQ 3966 4525 4313 4306 \r\nL 4313 3634 \r\nQ 3963 3931 3569 4081 \r\nQ 3175 4231 2741 4231 \r\nQ 1884 4231 1454 3753 \r\nQ 1025 3275 1025 2328 \r\nQ 1025 1384 1454 906 \r\nQ 1884 428 2741 428 \r\nQ 3075 428 3337 486 \r\nQ 3600 544 3809 666 \r\nz\r\n\" id=\"DejaVuSans-47\" transform=\"scale(0.015625)\"/>\r\n       </defs>\r\n       <use xlink:href=\"#DejaVuSans-59\"/>\r\n       <use x=\"61.083984\" xlink:href=\"#DejaVuSans-47\"/>\r\n      </g>\r\n     </g>\r\n    </g>\r\n    <g id=\"ytick_5\">\r\n     <g id=\"line2d_13\">\r\n      <g>\r\n       <use style=\"stroke:#000000;stroke-width:0.8;\" x=\"69.059375\" xlink:href=\"#m8f2b8fd4c8\" y=\"115.92\"/>\r\n      </g>\r\n     </g>\r\n     <g id=\"text_14\">\r\n      <!-- DSP -->\r\n      <g transform=\"translate(41.98125 119.719219)scale(0.1 -0.1)\">\r\n       <defs>\r\n        <path d=\"M 1259 4147 \r\nL 1259 519 \r\nL 2022 519 \r\nQ 2988 519 3436 956 \r\nQ 3884 1394 3884 2338 \r\nQ 3884 3275 3436 3711 \r\nQ 2988 4147 2022 4147 \r\nL 1259 4147 \r\nz\r\nM 628 4666 \r\nL 1925 4666 \r\nQ 3281 4666 3915 4102 \r\nQ 4550 3538 4550 2338 \r\nQ 4550 1131 3912 565 \r\nQ 3275 0 1925 0 \r\nL 628 0 \r\nL 628 4666 \r\nz\r\n\" id=\"DejaVuSans-44\" transform=\"scale(0.015625)\"/>\r\n        <path d=\"M 1259 4147 \r\nL 1259 2394 \r\nL 2053 2394 \r\nQ 2494 2394 2734 2622 \r\nQ 2975 2850 2975 3272 \r\nQ 2975 3691 2734 3919 \r\nQ 2494 4147 2053 4147 \r\nL 1259 4147 \r\nz\r\nM 628 4666 \r\nL 2053 4666 \r\nQ 2838 4666 3239 4311 \r\nQ 3641 3956 3641 3272 \r\nQ 3641 2581 3239 2228 \r\nQ 2838 1875 2053 1875 \r\nL 1259 1875 \r\nL 1259 0 \r\nL 628 0 \r\nL 628 4666 \r\nz\r\n\" id=\"DejaVuSans-50\" transform=\"scale(0.015625)\"/>\r\n       </defs>\r\n       <use xlink:href=\"#DejaVuSans-44\"/>\r\n       <use x=\"77.001953\" xlink:href=\"#DejaVuSans-53\"/>\r\n       <use x=\"140.478516\" xlink:href=\"#DejaVuSans-50\"/>\r\n      </g>\r\n     </g>\r\n    </g>\r\n    <g id=\"ytick_6\">\r\n     <g id=\"line2d_14\">\r\n      <g>\r\n       <use style=\"stroke:#000000;stroke-width:0.8;\" x=\"69.059375\" xlink:href=\"#m8f2b8fd4c8\" y=\"140.08\"/>\r\n      </g>\r\n     </g>\r\n     <g id=\"text_15\">\r\n      <!-- MBK -->\r\n      <g transform=\"translate(40.0125 143.879219)scale(0.1 -0.1)\">\r\n       <defs>\r\n        <path d=\"M 628 4666 \r\nL 1569 4666 \r\nL 2759 1491 \r\nL 3956 4666 \r\nL 4897 4666 \r\nL 4897 0 \r\nL 4281 0 \r\nL 4281 4097 \r\nL 3078 897 \r\nL 2444 897 \r\nL 1241 4097 \r\nL 1241 0 \r\nL 628 0 \r\nL 628 4666 \r\nz\r\n\" id=\"DejaVuSans-4d\" transform=\"scale(0.015625)\"/>\r\n        <path d=\"M 628 4666 \r\nL 1259 4666 \r\nL 1259 2694 \r\nL 3353 4666 \r\nL 4166 4666 \r\nL 1850 2491 \r\nL 4331 0 \r\nL 3500 0 \r\nL 1259 2247 \r\nL 1259 0 \r\nL 628 0 \r\nL 628 4666 \r\nz\r\n\" id=\"DejaVuSans-4b\" transform=\"scale(0.015625)\"/>\r\n       </defs>\r\n       <use xlink:href=\"#DejaVuSans-4d\"/>\r\n       <use x=\"86.279297\" xlink:href=\"#DejaVuSans-42\"/>\r\n       <use x=\"154.882812\" xlink:href=\"#DejaVuSans-4b\"/>\r\n      </g>\r\n     </g>\r\n    </g>\r\n    <g id=\"ytick_7\">\r\n     <g id=\"line2d_15\">\r\n      <g>\r\n       <use style=\"stroke:#000000;stroke-width:0.8;\" x=\"69.059375\" xlink:href=\"#m8f2b8fd4c8\" y=\"164.24\"/>\r\n      </g>\r\n     </g>\r\n     <g id=\"text_16\">\r\n      <!-- FNC -->\r\n      <g transform=\"translate(41.84375 168.039219)scale(0.1 -0.1)\">\r\n       <defs>\r\n        <path d=\"M 628 4666 \r\nL 3309 4666 \r\nL 3309 4134 \r\nL 1259 4134 \r\nL 1259 2759 \r\nL 3109 2759 \r\nL 3109 2228 \r\nL 1259 2228 \r\nL 1259 0 \r\nL 628 0 \r\nL 628 4666 \r\nz\r\n\" id=\"DejaVuSans-46\" transform=\"scale(0.015625)\"/>\r\n        <path d=\"M 628 4666 \r\nL 1478 4666 \r\nL 3547 763 \r\nL 3547 4666 \r\nL 4159 4666 \r\nL 4159 0 \r\nL 3309 0 \r\nL 1241 3903 \r\nL 1241 0 \r\nL 628 0 \r\nL 628 4666 \r\nz\r\n\" id=\"DejaVuSans-4e\" transform=\"scale(0.015625)\"/>\r\n       </defs>\r\n       <use xlink:href=\"#DejaVuSans-46\"/>\r\n       <use x=\"57.519531\" xlink:href=\"#DejaVuSans-4e\"/>\r\n       <use x=\"132.324219\" xlink:href=\"#DejaVuSans-43\"/>\r\n      </g>\r\n     </g>\r\n    </g>\r\n    <g id=\"ytick_8\">\r\n     <g id=\"line2d_16\">\r\n      <g>\r\n       <use style=\"stroke:#000000;stroke-width:0.8;\" x=\"69.059375\" xlink:href=\"#m8f2b8fd4c8\" y=\"188.4\"/>\r\n      </g>\r\n     </g>\r\n     <g id=\"text_17\">\r\n      <!-- JYP -->\r\n      <g transform=\"translate(46.971875 192.199219)scale(0.1 -0.1)\">\r\n       <defs>\r\n        <path d=\"M 628 4666 \r\nL 1259 4666 \r\nL 1259 325 \r\nQ 1259 -519 939 -900 \r\nQ 619 -1281 -91 -1281 \r\nL -331 -1281 \r\nL -331 -750 \r\nL -134 -750 \r\nQ 284 -750 456 -515 \r\nQ 628 -281 628 325 \r\nL 628 4666 \r\nz\r\n\" id=\"DejaVuSans-4a\" transform=\"scale(0.015625)\"/>\r\n       </defs>\r\n       <use xlink:href=\"#DejaVuSans-4a\"/>\r\n       <use x=\"29.492188\" xlink:href=\"#DejaVuSans-59\"/>\r\n       <use x=\"90.576172\" xlink:href=\"#DejaVuSans-50\"/>\r\n      </g>\r\n     </g>\r\n    </g>\r\n    <g id=\"ytick_9\">\r\n     <g id=\"line2d_17\">\r\n      <g>\r\n       <use style=\"stroke:#000000;stroke-width:0.8;\" x=\"69.059375\" xlink:href=\"#m8f2b8fd4c8\" y=\"212.56\"/>\r\n      </g>\r\n     </g>\r\n     <g id=\"text_18\">\r\n      <!-- SM -->\r\n      <g transform=\"translate(47.082813 216.359219)scale(0.1 -0.1)\">\r\n       <use xlink:href=\"#DejaVuSans-53\"/>\r\n       <use x=\"63.476562\" xlink:href=\"#DejaVuSans-4d\"/>\r\n      </g>\r\n     </g>\r\n    </g>\r\n    <g id=\"text_19\">\r\n     <!-- Num -->\r\n     <g transform=\"translate(14.798437 127.699687)rotate(-90)scale(0.1 -0.1)\">\r\n      <use xlink:href=\"#DejaVuSans-4e\"/>\r\n      <use x=\"74.804688\" xlink:href=\"#DejaVuSans-75\"/>\r\n      <use x=\"138.183594\" xlink:href=\"#DejaVuSans-6d\"/>\r\n     </g>\r\n    </g>\r\n   </g>\r\n   <g id=\"line2d_18\">\r\n    <path clip-path=\"url(#p61a91bb0c0)\" d=\"M 0 0 \r\n\" style=\"fill:none;stroke:#424242;stroke-linecap:square;stroke-width:2.7;\"/>\r\n   </g>\r\n   <g id=\"line2d_19\">\r\n    <path clip-path=\"url(#p61a91bb0c0)\" d=\"M 0 0 \r\n\" style=\"fill:none;stroke:#424242;stroke-linecap:square;stroke-width:2.7;\"/>\r\n   </g>\r\n   <g id=\"line2d_20\">\r\n    <path clip-path=\"url(#p61a91bb0c0)\" d=\"M 0 0 \r\n\" style=\"fill:none;stroke:#424242;stroke-linecap:square;stroke-width:2.7;\"/>\r\n   </g>\r\n   <g id=\"line2d_21\">\r\n    <path clip-path=\"url(#p61a91bb0c0)\" d=\"M 0 0 \r\n\" style=\"fill:none;stroke:#424242;stroke-linecap:square;stroke-width:2.7;\"/>\r\n   </g>\r\n   <g id=\"line2d_22\">\r\n    <path clip-path=\"url(#p61a91bb0c0)\" d=\"M 0 0 \r\n\" style=\"fill:none;stroke:#424242;stroke-linecap:square;stroke-width:2.7;\"/>\r\n   </g>\r\n   <g id=\"line2d_23\">\r\n    <path clip-path=\"url(#p61a91bb0c0)\" d=\"M 0 0 \r\n\" style=\"fill:none;stroke:#424242;stroke-linecap:square;stroke-width:2.7;\"/>\r\n   </g>\r\n   <g id=\"line2d_24\">\r\n    <path clip-path=\"url(#p61a91bb0c0)\" d=\"M 0 0 \r\n\" style=\"fill:none;stroke:#424242;stroke-linecap:square;stroke-width:2.7;\"/>\r\n   </g>\r\n   <g id=\"line2d_25\">\r\n    <path clip-path=\"url(#p61a91bb0c0)\" d=\"M 0 0 \r\n\" style=\"fill:none;stroke:#424242;stroke-linecap:square;stroke-width:2.7;\"/>\r\n   </g>\r\n   <g id=\"line2d_26\">\r\n    <path clip-path=\"url(#p61a91bb0c0)\" d=\"M 0 0 \r\n\" style=\"fill:none;stroke:#424242;stroke-linecap:square;stroke-width:2.7;\"/>\r\n   </g>\r\n   <g id=\"patch_12\">\r\n    <path d=\"M 69.059375 224.64 \r\nL 69.059375 7.2 \r\n\" style=\"fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;\"/>\r\n   </g>\r\n   <g id=\"patch_13\">\r\n    <path d=\"M 403.859375 224.64 \r\nL 403.859375 7.2 \r\n\" style=\"fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;\"/>\r\n   </g>\r\n   <g id=\"patch_14\">\r\n    <path d=\"M 69.059375 224.64 \r\nL 403.859375 224.64 \r\n\" style=\"fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;\"/>\r\n   </g>\r\n   <g id=\"patch_15\">\r\n    <path d=\"M 69.059375 7.2 \r\nL 403.859375 7.2 \r\n\" style=\"fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;\"/>\r\n   </g>\r\n  </g>\r\n </g>\r\n <defs>\r\n  <clipPath id=\"p61a91bb0c0\">\r\n   <rect height=\"217.44\" width=\"334.8\" x=\"69.059375\" y=\"7.2\"/>\r\n  </clipPath>\r\n </defs>\r\n</svg>\r\n",
      "image/png": "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\n"
     },
     "metadata": {
      "needs_background": "light"
     }
    }
   ],
   "source": [
    "\n",
    "company_data = {comp: df[\"Company\"].to_list().count(comp) for comp in set(df[\"Company\"])}\n",
    "company_data=sorted(company_data.items(), key=operator.itemgetter(0))\n",
    "company_data=dict(company_data)\n",
    "del_data=[]\n",
    "for i in company_data:\n",
    "  if company_data[i]<5: \n",
    "   del_data.append(i)\n",
    "for j in del_data:\n",
    "  del company_data[j]\n",
    "company_data = sorted(company_data.items(), key=operator.itemgetter(1))\n",
    "company_data=dict(company_data)\n",
    "import matplotlib.pyplot as plt\n",
    "comp_df = pd.DataFrame.from_dict(data=company_data, orient=\"index\", columns=[\"Company\"])\n",
    "comp_df[\"Num\"]=comp_df.index\n",
    "sns.barplot(data=comp_df, x=\"Company\", y=\"Num\")"
   ]
  },
  {
   "source": [
    "### Распределение групп по полу в SM"
   ],
   "cell_type": "markdown",
   "metadata": {}
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "metadata": {},
   "outputs": [
    {
     "output_type": "display_data",
     "data": {
      "application/vnd.plotly.v1+json": {
       "config": {
        "plotlyServerURL": "https://plot.ly"
       },
       "data": [
        {
         "labels": [
          "M",
          "F"
         ],
         "type": "pie",
         "values": [
          9,
          5
         ]
        }
       ],
       "layout": {
        "template": {
         "data": {
          "bar": [
           {
            "error_x": {
             "color": "#2a3f5f"
            },
            "error_y": {
             "color": "#2a3f5f"
            },
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             }
            },
            "type": "bar"
           }
          ],
          "barpolar": [
           {
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             }
            },
            "type": "barpolar"
           }
          ],
          "carpet": [
           {
            "aaxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "baxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "type": "carpet"
           }
          ],
          "choropleth": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "choropleth"
           }
          ],
          "contour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "contour"
           }
          ],
          "contourcarpet": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "contourcarpet"
           }
          ],
          "heatmap": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmap"
           }
          ],
          "heatmapgl": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmapgl"
           }
          ],
          "histogram": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "histogram"
           }
          ],
          "histogram2d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2d"
           }
          ],
          "histogram2dcontour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2dcontour"
           }
          ],
          "mesh3d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "mesh3d"
           }
          ],
          "parcoords": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "parcoords"
           }
          ],
          "pie": [
           {
            "automargin": true,
            "type": "pie"
           }
          ],
          "scatter": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter"
           }
          ],
          "scatter3d": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter3d"
           }
          ],
          "scattercarpet": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattercarpet"
           }
          ],
          "scattergeo": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergeo"
           }
          ],
          "scattergl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergl"
           }
          ],
          "scattermapbox": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattermapbox"
           }
          ],
          "scatterpolar": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolar"
           }
          ],
          "scatterpolargl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolargl"
           }
          ],
          "scatterternary": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterternary"
           }
          ],
          "surface": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "surface"
           }
          ],
          "table": [
           {
            "cells": {
             "fill": {
              "color": "#EBF0F8"
             },
             "line": {
              "color": "white"
             }
            },
            "header": {
             "fill": {
              "color": "#C8D4E3"
             },
             "line": {
              "color": "white"
             }
            },
            "type": "table"
           }
          ]
         },
         "layout": {
          "annotationdefaults": {
           "arrowcolor": "#2a3f5f",
           "arrowhead": 0,
           "arrowwidth": 1
          },
          "autotypenumbers": "strict",
          "coloraxis": {
           "colorbar": {
            "outlinewidth": 0,
            "ticks": ""
           }
          },
          "colorscale": {
           "diverging": [
            [
             0,
             "#8e0152"
            ],
            [
             0.1,
             "#c51b7d"
            ],
            [
             0.2,
             "#de77ae"
            ],
            [
             0.3,
             "#f1b6da"
            ],
            [
             0.4,
             "#fde0ef"
            ],
            [
             0.5,
             "#f7f7f7"
            ],
            [
             0.6,
             "#e6f5d0"
            ],
            [
             0.7,
             "#b8e186"
            ],
            [
             0.8,
             "#7fbc41"
            ],
            [
             0.9,
             "#4d9221"
            ],
            [
             1,
             "#276419"
            ]
           ],
           "sequential": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ],
           "sequentialminus": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ]
          },
          "colorway": [
           "#636efa",
           "#EF553B",
           "#00cc96",
           "#ab63fa",
           "#FFA15A",
           "#19d3f3",
           "#FF6692",
           "#B6E880",
           "#FF97FF",
           "#FECB52"
          ],
          "font": {
           "color": "#2a3f5f"
          },
          "geo": {
           "bgcolor": "white",
           "lakecolor": "white",
           "landcolor": "#E5ECF6",
           "showlakes": true,
           "showland": true,
           "subunitcolor": "white"
          },
          "hoverlabel": {
           "align": "left"
          },
          "hovermode": "closest",
          "mapbox": {
           "style": "light"
          },
          "paper_bgcolor": "white",
          "plot_bgcolor": "#E5ECF6",
          "polar": {
           "angularaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "radialaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "scene": {
           "xaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "yaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "zaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           }
          },
          "shapedefaults": {
           "line": {
            "color": "#2a3f5f"
           }
          },
          "ternary": {
           "aaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "baxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "caxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "title": {
           "x": 0.05
          },
          "xaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          },
          "yaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          }
         }
        }
       }
      }
     },
     "metadata": {}
    }
   ],
   "source": [
    "fan_df = df.loc[df[\"Company\"] == \"SM\"]\n",
    "\n",
    "male_df = fan_df.loc[fan_df[\"Gender\"] == 0]\n",
    "m_num = male_df.shape[0]\n",
    "fem_df = fan_df.loc[fan_df[\"Gender\"] == 1]\n",
    "f_num = fem_df.shape[0]\n",
    "\n",
    "\n",
    "labels = [\"M\",\"F\"]\n",
    "values = [m_num, f_num]\n",
    "fig = go.Figure(data=[go.Pie(labels=labels, values=values)])\n",
    "fig.show()"
   ]
  },
  {
   "source": [
    "### Самое популярное количество участников"
   ],
   "cell_type": "markdown",
   "metadata": {}
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "metadata": {},
   "outputs": [
    {
     "output_type": "stream",
     "name": "stdout",
     "text": [
      "{2: 16, 3: 25, 4: 63, 5: 76, 6: 44, 7: 35, 8: 9, 9: 15, 10: 6, 11: 2, 12: 4, 13: 2, 14: 1, 18: 1}\n[(2, 16), (3, 25), (4, 63), (5, 76), (6, 44), (7, 35), (8, 9), (9, 15), (10, 6), (11, 2), (12, 4), (13, 2), (14, 1), (18, 1)]\n{2: 16, 3: 25, 4: 63, 5: 76, 6: 44, 7: 35, 8: 9, 9: 15, 10: 6, 11: 2, 12: 4, 13: 2, 14: 1, 18: 1}\n{2: 16, 3: 25, 4: 63, 5: 76, 6: 44, 7: 35, 8: 9, 9: 15, 10: 6}\n"
     ]
    },
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "<AxesSubplot:xlabel='Num', ylabel='Members'>"
      ]
     },
     "metadata": {},
     "execution_count": 58
    },
    {
     "output_type": "display_data",
     "data": {
      "text/plain": "<Figure size 432x288 with 1 Axes>",
      "image/svg+xml": "<?xml version=\"1.0\" encoding=\"utf-8\" standalone=\"no\"?>\r\n<!DOCTYPE svg PUBLIC \"-//W3C//DTD SVG 1.1//EN\"\r\n  \"http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd\">\r\n<svg height=\"262.19625pt\" version=\"1.1\" viewBox=\"0 0 382.603125 262.19625\" width=\"382.603125pt\" xmlns=\"http://www.w3.org/2000/svg\" xmlns:xlink=\"http://www.w3.org/1999/xlink\">\r\n <metadata>\r\n  <rdf:RDF xmlns:cc=\"http://creativecommons.org/ns#\" xmlns:dc=\"http://purl.org/dc/elements/1.1/\" xmlns:rdf=\"http://www.w3.org/1999/02/22-rdf-syntax-ns#\">\r\n   <cc:Work>\r\n    <dc:type rdf:resource=\"http://purl.org/dc/dcmitype/StillImage\"/>\r\n    <dc:date>2021-04-20T22:38:45.262931</dc:date>\r\n    <dc:format>image/svg+xml</dc:format>\r\n    <dc:creator>\r\n     <cc:Agent>\r\n      <dc:title>Matplotlib v3.4.1, https://matplotlib.org/</dc:title>\r\n     </cc:Agent>\r\n    </dc:creator>\r\n   </cc:Work>\r\n  </rdf:RDF>\r\n </metadata>\r\n <defs>\r\n  <style type=\"text/css\">*{stroke-linecap:butt;stroke-linejoin:round;}</style>\r\n </defs>\r\n <g id=\"figure_1\">\r\n  <g id=\"patch_1\">\r\n   <path d=\"M 0 262.19625 \r\nL 382.603125 262.19625 \r\nL 382.603125 0 \r\nL 0 0 \r\nz\r\n\" style=\"fill:none;\"/>\r\n  </g>\r\n  <g id=\"axes_1\">\r\n   <g id=\"patch_2\">\r\n    <path d=\"M 40.603125 224.64 \r\nL 375.403125 224.64 \r\nL 375.403125 7.2 \r\nL 40.603125 7.2 \r\nz\r\n\" style=\"fill:#ffffff;\"/>\r\n   </g>\r\n   <g id=\"patch_3\">\r\n    <path clip-path=\"url(#p5be4b671e0)\" d=\"M 44.323125 224.64 \r\nL 74.083125 224.64 \r\nL 74.083125 181.043008 \r\nL 44.323125 181.043008 \r\nz\r\n\" style=\"fill:#3274a1;\"/>\r\n   </g>\r\n   <g id=\"patch_4\">\r\n    <path clip-path=\"url(#p5be4b671e0)\" d=\"M 81.523125 224.64 \r\nL 111.283125 224.64 \r\nL 111.283125 156.519699 \r\nL 81.523125 156.519699 \r\nz\r\n\" style=\"fill:#e1812c;\"/>\r\n   </g>\r\n   <g id=\"patch_5\">\r\n    <path clip-path=\"url(#p5be4b671e0)\" d=\"M 118.723125 224.64 \r\nL 148.483125 224.64 \r\nL 148.483125 52.976842 \r\nL 118.723125 52.976842 \r\nz\r\n\" style=\"fill:#3a923a;\"/>\r\n   </g>\r\n   <g id=\"patch_6\">\r\n    <path clip-path=\"url(#p5be4b671e0)\" d=\"M 155.923125 224.64 \r\nL 185.683125 224.64 \r\nL 185.683125 17.554286 \r\nL 155.923125 17.554286 \r\nz\r\n\" style=\"fill:#c03d3e;\"/>\r\n   </g>\r\n   <g id=\"patch_7\">\r\n    <path clip-path=\"url(#p5be4b671e0)\" d=\"M 193.123125 224.64 \r\nL 222.883125 224.64 \r\nL 222.883125 104.748271 \r\nL 193.123125 104.748271 \r\nz\r\n\" style=\"fill:#9372b2;\"/>\r\n   </g>\r\n   <g id=\"patch_8\">\r\n    <path clip-path=\"url(#p5be4b671e0)\" d=\"M 230.323125 224.64 \r\nL 260.083125 224.64 \r\nL 260.083125 129.271579 \r\nL 230.323125 129.271579 \r\nz\r\n\" style=\"fill:#845b53;\"/>\r\n   </g>\r\n   <g id=\"patch_9\">\r\n    <path clip-path=\"url(#p5be4b671e0)\" d=\"M 267.523125 224.64 \r\nL 297.283125 224.64 \r\nL 297.283125 200.116692 \r\nL 267.523125 200.116692 \r\nz\r\n\" style=\"fill:#d684bd;\"/>\r\n   </g>\r\n   <g id=\"patch_10\">\r\n    <path clip-path=\"url(#p5be4b671e0)\" d=\"M 304.723125 224.64 \r\nL 334.483125 224.64 \r\nL 334.483125 183.76782 \r\nL 304.723125 183.76782 \r\nz\r\n\" style=\"fill:#7f7f7f;\"/>\r\n   </g>\r\n   <g id=\"patch_11\">\r\n    <path clip-path=\"url(#p5be4b671e0)\" d=\"M 341.923125 224.64 \r\nL 371.683125 224.64 \r\nL 371.683125 208.291128 \r\nL 341.923125 208.291128 \r\nz\r\n\" style=\"fill:#a9aa35;\"/>\r\n   </g>\r\n   <g id=\"matplotlib.axis_1\">\r\n    <g id=\"xtick_1\">\r\n     <g id=\"line2d_1\">\r\n      <defs>\r\n       <path d=\"M 0 0 \r\nL 0 3.5 \r\n\" id=\"m130e48efa4\" style=\"stroke:#000000;stroke-width:0.8;\"/>\r\n      </defs>\r\n      <g>\r\n       <use style=\"stroke:#000000;stroke-width:0.8;\" x=\"59.203125\" xlink:href=\"#m130e48efa4\" y=\"224.64\"/>\r\n      </g>\r\n     </g>\r\n     <g id=\"text_1\">\r\n      <!-- 2 -->\r\n      <g transform=\"translate(56.021875 239.238437)scale(0.1 -0.1)\">\r\n       <defs>\r\n        <path d=\"M 1228 531 \r\nL 3431 531 \r\nL 3431 0 \r\nL 469 0 \r\nL 469 531 \r\nQ 828 903 1448 1529 \r\nQ 2069 2156 2228 2338 \r\nQ 2531 2678 2651 2914 \r\nQ 2772 3150 2772 3378 \r\nQ 2772 3750 2511 3984 \r\nQ 2250 4219 1831 4219 \r\nQ 1534 4219 1204 4116 \r\nQ 875 4013 500 3803 \r\nL 500 4441 \r\nQ 881 4594 1212 4672 \r\nQ 1544 4750 1819 4750 \r\nQ 2544 4750 2975 4387 \r\nQ 3406 4025 3406 3419 \r\nQ 3406 3131 3298 2873 \r\nQ 3191 2616 2906 2266 \r\nQ 2828 2175 2409 1742 \r\nQ 1991 1309 1228 531 \r\nz\r\n\" id=\"DejaVuSans-32\" transform=\"scale(0.015625)\"/>\r\n       </defs>\r\n       <use xlink:href=\"#DejaVuSans-32\"/>\r\n      </g>\r\n     </g>\r\n    </g>\r\n    <g id=\"xtick_2\">\r\n     <g id=\"line2d_2\">\r\n      <g>\r\n       <use style=\"stroke:#000000;stroke-width:0.8;\" x=\"96.403125\" xlink:href=\"#m130e48efa4\" y=\"224.64\"/>\r\n      </g>\r\n     </g>\r\n     <g id=\"text_2\">\r\n      <!-- 3 -->\r\n      <g transform=\"translate(93.221875 239.238437)scale(0.1 -0.1)\">\r\n       <defs>\r\n        <path d=\"M 2597 2516 \r\nQ 3050 2419 3304 2112 \r\nQ 3559 1806 3559 1356 \r\nQ 3559 666 3084 287 \r\nQ 2609 -91 1734 -91 \r\nQ 1441 -91 1130 -33 \r\nQ 819 25 488 141 \r\nL 488 750 \r\nQ 750 597 1062 519 \r\nQ 1375 441 1716 441 \r\nQ 2309 441 2620 675 \r\nQ 2931 909 2931 1356 \r\nQ 2931 1769 2642 2001 \r\nQ 2353 2234 1838 2234 \r\nL 1294 2234 \r\nL 1294 2753 \r\nL 1863 2753 \r\nQ 2328 2753 2575 2939 \r\nQ 2822 3125 2822 3475 \r\nQ 2822 3834 2567 4026 \r\nQ 2313 4219 1838 4219 \r\nQ 1578 4219 1281 4162 \r\nQ 984 4106 628 3988 \r\nL 628 4550 \r\nQ 988 4650 1302 4700 \r\nQ 1616 4750 1894 4750 \r\nQ 2613 4750 3031 4423 \r\nQ 3450 4097 3450 3541 \r\nQ 3450 3153 3228 2886 \r\nQ 3006 2619 2597 2516 \r\nz\r\n\" id=\"DejaVuSans-33\" transform=\"scale(0.015625)\"/>\r\n       </defs>\r\n       <use xlink:href=\"#DejaVuSans-33\"/>\r\n      </g>\r\n     </g>\r\n    </g>\r\n    <g id=\"xtick_3\">\r\n     <g id=\"line2d_3\">\r\n      <g>\r\n       <use style=\"stroke:#000000;stroke-width:0.8;\" x=\"133.603125\" xlink:href=\"#m130e48efa4\" y=\"224.64\"/>\r\n      </g>\r\n     </g>\r\n     <g id=\"text_3\">\r\n      <!-- 4 -->\r\n      <g transform=\"translate(130.421875 239.238437)scale(0.1 -0.1)\">\r\n       <defs>\r\n        <path d=\"M 2419 4116 \r\nL 825 1625 \r\nL 2419 1625 \r\nL 2419 4116 \r\nz\r\nM 2253 4666 \r\nL 3047 4666 \r\nL 3047 1625 \r\nL 3713 1625 \r\nL 3713 1100 \r\nL 3047 1100 \r\nL 3047 0 \r\nL 2419 0 \r\nL 2419 1100 \r\nL 313 1100 \r\nL 313 1709 \r\nL 2253 4666 \r\nz\r\n\" id=\"DejaVuSans-34\" transform=\"scale(0.015625)\"/>\r\n       </defs>\r\n       <use xlink:href=\"#DejaVuSans-34\"/>\r\n      </g>\r\n     </g>\r\n    </g>\r\n    <g id=\"xtick_4\">\r\n     <g id=\"line2d_4\">\r\n      <g>\r\n       <use style=\"stroke:#000000;stroke-width:0.8;\" x=\"170.803125\" xlink:href=\"#m130e48efa4\" y=\"224.64\"/>\r\n      </g>\r\n     </g>\r\n     <g id=\"text_4\">\r\n      <!-- 5 -->\r\n      <g transform=\"translate(167.621875 239.238437)scale(0.1 -0.1)\">\r\n       <defs>\r\n        <path d=\"M 691 4666 \r\nL 3169 4666 \r\nL 3169 4134 \r\nL 1269 4134 \r\nL 1269 2991 \r\nQ 1406 3038 1543 3061 \r\nQ 1681 3084 1819 3084 \r\nQ 2600 3084 3056 2656 \r\nQ 3513 2228 3513 1497 \r\nQ 3513 744 3044 326 \r\nQ 2575 -91 1722 -91 \r\nQ 1428 -91 1123 -41 \r\nQ 819 9 494 109 \r\nL 494 744 \r\nQ 775 591 1075 516 \r\nQ 1375 441 1709 441 \r\nQ 2250 441 2565 725 \r\nQ 2881 1009 2881 1497 \r\nQ 2881 1984 2565 2268 \r\nQ 2250 2553 1709 2553 \r\nQ 1456 2553 1204 2497 \r\nQ 953 2441 691 2322 \r\nL 691 4666 \r\nz\r\n\" id=\"DejaVuSans-35\" transform=\"scale(0.015625)\"/>\r\n       </defs>\r\n       <use xlink:href=\"#DejaVuSans-35\"/>\r\n      </g>\r\n     </g>\r\n    </g>\r\n    <g id=\"xtick_5\">\r\n     <g id=\"line2d_5\">\r\n      <g>\r\n       <use style=\"stroke:#000000;stroke-width:0.8;\" x=\"208.003125\" xlink:href=\"#m130e48efa4\" y=\"224.64\"/>\r\n      </g>\r\n     </g>\r\n     <g id=\"text_5\">\r\n      <!-- 6 -->\r\n      <g transform=\"translate(204.821875 239.238437)scale(0.1 -0.1)\">\r\n       <defs>\r\n        <path d=\"M 2113 2584 \r\nQ 1688 2584 1439 2293 \r\nQ 1191 2003 1191 1497 \r\nQ 1191 994 1439 701 \r\nQ 1688 409 2113 409 \r\nQ 2538 409 2786 701 \r\nQ 3034 994 3034 1497 \r\nQ 3034 2003 2786 2293 \r\nQ 2538 2584 2113 2584 \r\nz\r\nM 3366 4563 \r\nL 3366 3988 \r\nQ 3128 4100 2886 4159 \r\nQ 2644 4219 2406 4219 \r\nQ 1781 4219 1451 3797 \r\nQ 1122 3375 1075 2522 \r\nQ 1259 2794 1537 2939 \r\nQ 1816 3084 2150 3084 \r\nQ 2853 3084 3261 2657 \r\nQ 3669 2231 3669 1497 \r\nQ 3669 778 3244 343 \r\nQ 2819 -91 2113 -91 \r\nQ 1303 -91 875 529 \r\nQ 447 1150 447 2328 \r\nQ 447 3434 972 4092 \r\nQ 1497 4750 2381 4750 \r\nQ 2619 4750 2861 4703 \r\nQ 3103 4656 3366 4563 \r\nz\r\n\" id=\"DejaVuSans-36\" transform=\"scale(0.015625)\"/>\r\n       </defs>\r\n       <use xlink:href=\"#DejaVuSans-36\"/>\r\n      </g>\r\n     </g>\r\n    </g>\r\n    <g id=\"xtick_6\">\r\n     <g id=\"line2d_6\">\r\n      <g>\r\n       <use style=\"stroke:#000000;stroke-width:0.8;\" x=\"245.203125\" xlink:href=\"#m130e48efa4\" y=\"224.64\"/>\r\n      </g>\r\n     </g>\r\n     <g id=\"text_6\">\r\n      <!-- 7 -->\r\n      <g transform=\"translate(242.021875 239.238437)scale(0.1 -0.1)\">\r\n       <defs>\r\n        <path d=\"M 525 4666 \r\nL 3525 4666 \r\nL 3525 4397 \r\nL 1831 0 \r\nL 1172 0 \r\nL 2766 4134 \r\nL 525 4134 \r\nL 525 4666 \r\nz\r\n\" id=\"DejaVuSans-37\" transform=\"scale(0.015625)\"/>\r\n       </defs>\r\n       <use xlink:href=\"#DejaVuSans-37\"/>\r\n      </g>\r\n     </g>\r\n    </g>\r\n    <g id=\"xtick_7\">\r\n     <g id=\"line2d_7\">\r\n      <g>\r\n       <use style=\"stroke:#000000;stroke-width:0.8;\" x=\"282.403125\" xlink:href=\"#m130e48efa4\" y=\"224.64\"/>\r\n      </g>\r\n     </g>\r\n     <g id=\"text_7\">\r\n      <!-- 8 -->\r\n      <g transform=\"translate(279.221875 239.238437)scale(0.1 -0.1)\">\r\n       <defs>\r\n        <path d=\"M 2034 2216 \r\nQ 1584 2216 1326 1975 \r\nQ 1069 1734 1069 1313 \r\nQ 1069 891 1326 650 \r\nQ 1584 409 2034 409 \r\nQ 2484 409 2743 651 \r\nQ 3003 894 3003 1313 \r\nQ 3003 1734 2745 1975 \r\nQ 2488 2216 2034 2216 \r\nz\r\nM 1403 2484 \r\nQ 997 2584 770 2862 \r\nQ 544 3141 544 3541 \r\nQ 544 4100 942 4425 \r\nQ 1341 4750 2034 4750 \r\nQ 2731 4750 3128 4425 \r\nQ 3525 4100 3525 3541 \r\nQ 3525 3141 3298 2862 \r\nQ 3072 2584 2669 2484 \r\nQ 3125 2378 3379 2068 \r\nQ 3634 1759 3634 1313 \r\nQ 3634 634 3220 271 \r\nQ 2806 -91 2034 -91 \r\nQ 1263 -91 848 271 \r\nQ 434 634 434 1313 \r\nQ 434 1759 690 2068 \r\nQ 947 2378 1403 2484 \r\nz\r\nM 1172 3481 \r\nQ 1172 3119 1398 2916 \r\nQ 1625 2713 2034 2713 \r\nQ 2441 2713 2670 2916 \r\nQ 2900 3119 2900 3481 \r\nQ 2900 3844 2670 4047 \r\nQ 2441 4250 2034 4250 \r\nQ 1625 4250 1398 4047 \r\nQ 1172 3844 1172 3481 \r\nz\r\n\" id=\"DejaVuSans-38\" transform=\"scale(0.015625)\"/>\r\n       </defs>\r\n       <use xlink:href=\"#DejaVuSans-38\"/>\r\n      </g>\r\n     </g>\r\n    </g>\r\n    <g id=\"xtick_8\">\r\n     <g id=\"line2d_8\">\r\n      <g>\r\n       <use style=\"stroke:#000000;stroke-width:0.8;\" x=\"319.603125\" xlink:href=\"#m130e48efa4\" y=\"224.64\"/>\r\n      </g>\r\n     </g>\r\n     <g id=\"text_8\">\r\n      <!-- 9 -->\r\n      <g transform=\"translate(316.421875 239.238437)scale(0.1 -0.1)\">\r\n       <defs>\r\n        <path d=\"M 703 97 \r\nL 703 672 \r\nQ 941 559 1184 500 \r\nQ 1428 441 1663 441 \r\nQ 2288 441 2617 861 \r\nQ 2947 1281 2994 2138 \r\nQ 2813 1869 2534 1725 \r\nQ 2256 1581 1919 1581 \r\nQ 1219 1581 811 2004 \r\nQ 403 2428 403 3163 \r\nQ 403 3881 828 4315 \r\nQ 1253 4750 1959 4750 \r\nQ 2769 4750 3195 4129 \r\nQ 3622 3509 3622 2328 \r\nQ 3622 1225 3098 567 \r\nQ 2575 -91 1691 -91 \r\nQ 1453 -91 1209 -44 \r\nQ 966 3 703 97 \r\nz\r\nM 1959 2075 \r\nQ 2384 2075 2632 2365 \r\nQ 2881 2656 2881 3163 \r\nQ 2881 3666 2632 3958 \r\nQ 2384 4250 1959 4250 \r\nQ 1534 4250 1286 3958 \r\nQ 1038 3666 1038 3163 \r\nQ 1038 2656 1286 2365 \r\nQ 1534 2075 1959 2075 \r\nz\r\n\" id=\"DejaVuSans-39\" transform=\"scale(0.015625)\"/>\r\n       </defs>\r\n       <use xlink:href=\"#DejaVuSans-39\"/>\r\n      </g>\r\n     </g>\r\n    </g>\r\n    <g id=\"xtick_9\">\r\n     <g id=\"line2d_9\">\r\n      <g>\r\n       <use style=\"stroke:#000000;stroke-width:0.8;\" x=\"356.803125\" xlink:href=\"#m130e48efa4\" y=\"224.64\"/>\r\n      </g>\r\n     </g>\r\n     <g id=\"text_9\">\r\n      <!-- 10 -->\r\n      <g transform=\"translate(350.440625 239.238437)scale(0.1 -0.1)\">\r\n       <defs>\r\n        <path d=\"M 794 531 \r\nL 1825 531 \r\nL 1825 4091 \r\nL 703 3866 \r\nL 703 4441 \r\nL 1819 4666 \r\nL 2450 4666 \r\nL 2450 531 \r\nL 3481 531 \r\nL 3481 0 \r\nL 794 0 \r\nL 794 531 \r\nz\r\n\" id=\"DejaVuSans-31\" transform=\"scale(0.015625)\"/>\r\n        <path d=\"M 2034 4250 \r\nQ 1547 4250 1301 3770 \r\nQ 1056 3291 1056 2328 \r\nQ 1056 1369 1301 889 \r\nQ 1547 409 2034 409 \r\nQ 2525 409 2770 889 \r\nQ 3016 1369 3016 2328 \r\nQ 3016 3291 2770 3770 \r\nQ 2525 4250 2034 4250 \r\nz\r\nM 2034 4750 \r\nQ 2819 4750 3233 4129 \r\nQ 3647 3509 3647 2328 \r\nQ 3647 1150 3233 529 \r\nQ 2819 -91 2034 -91 \r\nQ 1250 -91 836 529 \r\nQ 422 1150 422 2328 \r\nQ 422 3509 836 4129 \r\nQ 1250 4750 2034 4750 \r\nz\r\n\" id=\"DejaVuSans-30\" transform=\"scale(0.015625)\"/>\r\n       </defs>\r\n       <use xlink:href=\"#DejaVuSans-31\"/>\r\n       <use x=\"63.623047\" xlink:href=\"#DejaVuSans-30\"/>\r\n      </g>\r\n     </g>\r\n    </g>\r\n    <g id=\"text_10\">\r\n     <!-- Num -->\r\n     <g transform=\"translate(196.223437 252.916562)scale(0.1 -0.1)\">\r\n      <defs>\r\n       <path d=\"M 628 4666 \r\nL 1478 4666 \r\nL 3547 763 \r\nL 3547 4666 \r\nL 4159 4666 \r\nL 4159 0 \r\nL 3309 0 \r\nL 1241 3903 \r\nL 1241 0 \r\nL 628 0 \r\nL 628 4666 \r\nz\r\n\" id=\"DejaVuSans-4e\" transform=\"scale(0.015625)\"/>\r\n       <path d=\"M 544 1381 \r\nL 544 3500 \r\nL 1119 3500 \r\nL 1119 1403 \r\nQ 1119 906 1312 657 \r\nQ 1506 409 1894 409 \r\nQ 2359 409 2629 706 \r\nQ 2900 1003 2900 1516 \r\nL 2900 3500 \r\nL 3475 3500 \r\nL 3475 0 \r\nL 2900 0 \r\nL 2900 538 \r\nQ 2691 219 2414 64 \r\nQ 2138 -91 1772 -91 \r\nQ 1169 -91 856 284 \r\nQ 544 659 544 1381 \r\nz\r\nM 1991 3584 \r\nL 1991 3584 \r\nz\r\n\" id=\"DejaVuSans-75\" transform=\"scale(0.015625)\"/>\r\n       <path d=\"M 3328 2828 \r\nQ 3544 3216 3844 3400 \r\nQ 4144 3584 4550 3584 \r\nQ 5097 3584 5394 3201 \r\nQ 5691 2819 5691 2113 \r\nL 5691 0 \r\nL 5113 0 \r\nL 5113 2094 \r\nQ 5113 2597 4934 2840 \r\nQ 4756 3084 4391 3084 \r\nQ 3944 3084 3684 2787 \r\nQ 3425 2491 3425 1978 \r\nL 3425 0 \r\nL 2847 0 \r\nL 2847 2094 \r\nQ 2847 2600 2669 2842 \r\nQ 2491 3084 2119 3084 \r\nQ 1678 3084 1418 2786 \r\nQ 1159 2488 1159 1978 \r\nL 1159 0 \r\nL 581 0 \r\nL 581 3500 \r\nL 1159 3500 \r\nL 1159 2956 \r\nQ 1356 3278 1631 3431 \r\nQ 1906 3584 2284 3584 \r\nQ 2666 3584 2933 3390 \r\nQ 3200 3197 3328 2828 \r\nz\r\n\" id=\"DejaVuSans-6d\" transform=\"scale(0.015625)\"/>\r\n      </defs>\r\n      <use xlink:href=\"#DejaVuSans-4e\"/>\r\n      <use x=\"74.804688\" xlink:href=\"#DejaVuSans-75\"/>\r\n      <use x=\"138.183594\" xlink:href=\"#DejaVuSans-6d\"/>\r\n     </g>\r\n    </g>\r\n   </g>\r\n   <g id=\"matplotlib.axis_2\">\r\n    <g id=\"ytick_1\">\r\n     <g id=\"line2d_10\">\r\n      <defs>\r\n       <path d=\"M 0 0 \r\nL -3.5 0 \r\n\" id=\"mf972018463\" style=\"stroke:#000000;stroke-width:0.8;\"/>\r\n      </defs>\r\n      <g>\r\n       <use style=\"stroke:#000000;stroke-width:0.8;\" x=\"40.603125\" xlink:href=\"#mf972018463\" y=\"224.64\"/>\r\n      </g>\r\n     </g>\r\n     <g id=\"text_11\">\r\n      <!-- 0 -->\r\n      <g transform=\"translate(27.240625 228.439219)scale(0.1 -0.1)\">\r\n       <use xlink:href=\"#DejaVuSans-30\"/>\r\n      </g>\r\n     </g>\r\n    </g>\r\n    <g id=\"ytick_2\">\r\n     <g id=\"line2d_11\">\r\n      <g>\r\n       <use style=\"stroke:#000000;stroke-width:0.8;\" x=\"40.603125\" xlink:href=\"#mf972018463\" y=\"197.39188\"/>\r\n      </g>\r\n     </g>\r\n     <g id=\"text_12\">\r\n      <!-- 10 -->\r\n      <g transform=\"translate(20.878125 201.191098)scale(0.1 -0.1)\">\r\n       <use xlink:href=\"#DejaVuSans-31\"/>\r\n       <use x=\"63.623047\" xlink:href=\"#DejaVuSans-30\"/>\r\n      </g>\r\n     </g>\r\n    </g>\r\n    <g id=\"ytick_3\">\r\n     <g id=\"line2d_12\">\r\n      <g>\r\n       <use style=\"stroke:#000000;stroke-width:0.8;\" x=\"40.603125\" xlink:href=\"#mf972018463\" y=\"170.143759\"/>\r\n      </g>\r\n     </g>\r\n     <g id=\"text_13\">\r\n      <!-- 20 -->\r\n      <g transform=\"translate(20.878125 173.942978)scale(0.1 -0.1)\">\r\n       <use xlink:href=\"#DejaVuSans-32\"/>\r\n       <use x=\"63.623047\" xlink:href=\"#DejaVuSans-30\"/>\r\n      </g>\r\n     </g>\r\n    </g>\r\n    <g id=\"ytick_4\">\r\n     <g id=\"line2d_13\">\r\n      <g>\r\n       <use style=\"stroke:#000000;stroke-width:0.8;\" x=\"40.603125\" xlink:href=\"#mf972018463\" y=\"142.895639\"/>\r\n      </g>\r\n     </g>\r\n     <g id=\"text_14\">\r\n      <!-- 30 -->\r\n      <g transform=\"translate(20.878125 146.694858)scale(0.1 -0.1)\">\r\n       <use xlink:href=\"#DejaVuSans-33\"/>\r\n       <use x=\"63.623047\" xlink:href=\"#DejaVuSans-30\"/>\r\n      </g>\r\n     </g>\r\n    </g>\r\n    <g id=\"ytick_5\">\r\n     <g id=\"line2d_14\">\r\n      <g>\r\n       <use style=\"stroke:#000000;stroke-width:0.8;\" x=\"40.603125\" xlink:href=\"#mf972018463\" y=\"115.647519\"/>\r\n      </g>\r\n     </g>\r\n     <g id=\"text_15\">\r\n      <!-- 40 -->\r\n      <g transform=\"translate(20.878125 119.446738)scale(0.1 -0.1)\">\r\n       <use xlink:href=\"#DejaVuSans-34\"/>\r\n       <use x=\"63.623047\" xlink:href=\"#DejaVuSans-30\"/>\r\n      </g>\r\n     </g>\r\n    </g>\r\n    <g id=\"ytick_6\">\r\n     <g id=\"line2d_15\">\r\n      <g>\r\n       <use style=\"stroke:#000000;stroke-width:0.8;\" x=\"40.603125\" xlink:href=\"#mf972018463\" y=\"88.399398\"/>\r\n      </g>\r\n     </g>\r\n     <g id=\"text_16\">\r\n      <!-- 50 -->\r\n      <g transform=\"translate(20.878125 92.198617)scale(0.1 -0.1)\">\r\n       <use xlink:href=\"#DejaVuSans-35\"/>\r\n       <use x=\"63.623047\" xlink:href=\"#DejaVuSans-30\"/>\r\n      </g>\r\n     </g>\r\n    </g>\r\n    <g id=\"ytick_7\">\r\n     <g id=\"line2d_16\">\r\n      <g>\r\n       <use style=\"stroke:#000000;stroke-width:0.8;\" x=\"40.603125\" xlink:href=\"#mf972018463\" y=\"61.151278\"/>\r\n      </g>\r\n     </g>\r\n     <g id=\"text_17\">\r\n      <!-- 60 -->\r\n      <g transform=\"translate(20.878125 64.950497)scale(0.1 -0.1)\">\r\n       <use xlink:href=\"#DejaVuSans-36\"/>\r\n       <use x=\"63.623047\" xlink:href=\"#DejaVuSans-30\"/>\r\n      </g>\r\n     </g>\r\n    </g>\r\n    <g id=\"ytick_8\">\r\n     <g id=\"line2d_17\">\r\n      <g>\r\n       <use style=\"stroke:#000000;stroke-width:0.8;\" x=\"40.603125\" xlink:href=\"#mf972018463\" y=\"33.903158\"/>\r\n      </g>\r\n     </g>\r\n     <g id=\"text_18\">\r\n      <!-- 70 -->\r\n      <g transform=\"translate(20.878125 37.702377)scale(0.1 -0.1)\">\r\n       <use xlink:href=\"#DejaVuSans-37\"/>\r\n       <use x=\"63.623047\" xlink:href=\"#DejaVuSans-30\"/>\r\n      </g>\r\n     </g>\r\n    </g>\r\n    <g id=\"text_19\">\r\n     <!-- Members -->\r\n     <g transform=\"translate(14.798438 139.091875)rotate(-90)scale(0.1 -0.1)\">\r\n      <defs>\r\n       <path d=\"M 628 4666 \r\nL 1569 4666 \r\nL 2759 1491 \r\nL 3956 4666 \r\nL 4897 4666 \r\nL 4897 0 \r\nL 4281 0 \r\nL 4281 4097 \r\nL 3078 897 \r\nL 2444 897 \r\nL 1241 4097 \r\nL 1241 0 \r\nL 628 0 \r\nL 628 4666 \r\nz\r\n\" id=\"DejaVuSans-4d\" transform=\"scale(0.015625)\"/>\r\n       <path d=\"M 3597 1894 \r\nL 3597 1613 \r\nL 953 1613 \r\nQ 991 1019 1311 708 \r\nQ 1631 397 2203 397 \r\nQ 2534 397 2845 478 \r\nQ 3156 559 3463 722 \r\nL 3463 178 \r\nQ 3153 47 2828 -22 \r\nQ 2503 -91 2169 -91 \r\nQ 1331 -91 842 396 \r\nQ 353 884 353 1716 \r\nQ 353 2575 817 3079 \r\nQ 1281 3584 2069 3584 \r\nQ 2775 3584 3186 3129 \r\nQ 3597 2675 3597 1894 \r\nz\r\nM 3022 2063 \r\nQ 3016 2534 2758 2815 \r\nQ 2500 3097 2075 3097 \r\nQ 1594 3097 1305 2825 \r\nQ 1016 2553 972 2059 \r\nL 3022 2063 \r\nz\r\n\" id=\"DejaVuSans-65\" transform=\"scale(0.015625)\"/>\r\n       <path d=\"M 3116 1747 \r\nQ 3116 2381 2855 2742 \r\nQ 2594 3103 2138 3103 \r\nQ 1681 3103 1420 2742 \r\nQ 1159 2381 1159 1747 \r\nQ 1159 1113 1420 752 \r\nQ 1681 391 2138 391 \r\nQ 2594 391 2855 752 \r\nQ 3116 1113 3116 1747 \r\nz\r\nM 1159 2969 \r\nQ 1341 3281 1617 3432 \r\nQ 1894 3584 2278 3584 \r\nQ 2916 3584 3314 3078 \r\nQ 3713 2572 3713 1747 \r\nQ 3713 922 3314 415 \r\nQ 2916 -91 2278 -91 \r\nQ 1894 -91 1617 61 \r\nQ 1341 213 1159 525 \r\nL 1159 0 \r\nL 581 0 \r\nL 581 4863 \r\nL 1159 4863 \r\nL 1159 2969 \r\nz\r\n\" id=\"DejaVuSans-62\" transform=\"scale(0.015625)\"/>\r\n       <path d=\"M 2631 2963 \r\nQ 2534 3019 2420 3045 \r\nQ 2306 3072 2169 3072 \r\nQ 1681 3072 1420 2755 \r\nQ 1159 2438 1159 1844 \r\nL 1159 0 \r\nL 581 0 \r\nL 581 3500 \r\nL 1159 3500 \r\nL 1159 2956 \r\nQ 1341 3275 1631 3429 \r\nQ 1922 3584 2338 3584 \r\nQ 2397 3584 2469 3576 \r\nQ 2541 3569 2628 3553 \r\nL 2631 2963 \r\nz\r\n\" id=\"DejaVuSans-72\" transform=\"scale(0.015625)\"/>\r\n       <path d=\"M 2834 3397 \r\nL 2834 2853 \r\nQ 2591 2978 2328 3040 \r\nQ 2066 3103 1784 3103 \r\nQ 1356 3103 1142 2972 \r\nQ 928 2841 928 2578 \r\nQ 928 2378 1081 2264 \r\nQ 1234 2150 1697 2047 \r\nL 1894 2003 \r\nQ 2506 1872 2764 1633 \r\nQ 3022 1394 3022 966 \r\nQ 3022 478 2636 193 \r\nQ 2250 -91 1575 -91 \r\nQ 1294 -91 989 -36 \r\nQ 684 19 347 128 \r\nL 347 722 \r\nQ 666 556 975 473 \r\nQ 1284 391 1588 391 \r\nQ 1994 391 2212 530 \r\nQ 2431 669 2431 922 \r\nQ 2431 1156 2273 1281 \r\nQ 2116 1406 1581 1522 \r\nL 1381 1569 \r\nQ 847 1681 609 1914 \r\nQ 372 2147 372 2553 \r\nQ 372 3047 722 3315 \r\nQ 1072 3584 1716 3584 \r\nQ 2034 3584 2315 3537 \r\nQ 2597 3491 2834 3397 \r\nz\r\n\" id=\"DejaVuSans-73\" transform=\"scale(0.015625)\"/>\r\n      </defs>\r\n      <use xlink:href=\"#DejaVuSans-4d\"/>\r\n      <use x=\"86.279297\" xlink:href=\"#DejaVuSans-65\"/>\r\n      <use x=\"147.802734\" xlink:href=\"#DejaVuSans-6d\"/>\r\n      <use x=\"245.214844\" xlink:href=\"#DejaVuSans-62\"/>\r\n      <use x=\"308.691406\" xlink:href=\"#DejaVuSans-65\"/>\r\n      <use x=\"370.214844\" xlink:href=\"#DejaVuSans-72\"/>\r\n      <use x=\"411.328125\" xlink:href=\"#DejaVuSans-73\"/>\r\n     </g>\r\n    </g>\r\n   </g>\r\n   <g id=\"line2d_18\">\r\n    <path clip-path=\"url(#p5be4b671e0)\" d=\"M 0 0 \r\n\" style=\"fill:none;stroke:#424242;stroke-linecap:square;stroke-width:2.7;\"/>\r\n   </g>\r\n   <g id=\"line2d_19\">\r\n    <path clip-path=\"url(#p5be4b671e0)\" d=\"M 0 0 \r\n\" style=\"fill:none;stroke:#424242;stroke-linecap:square;stroke-width:2.7;\"/>\r\n   </g>\r\n   <g id=\"line2d_20\">\r\n    <path clip-path=\"url(#p5be4b671e0)\" d=\"M 0 0 \r\n\" style=\"fill:none;stroke:#424242;stroke-linecap:square;stroke-width:2.7;\"/>\r\n   </g>\r\n   <g id=\"line2d_21\">\r\n    <path clip-path=\"url(#p5be4b671e0)\" d=\"M 0 0 \r\n\" style=\"fill:none;stroke:#424242;stroke-linecap:square;stroke-width:2.7;\"/>\r\n   </g>\r\n   <g id=\"line2d_22\">\r\n    <path clip-path=\"url(#p5be4b671e0)\" d=\"M 0 0 \r\n\" style=\"fill:none;stroke:#424242;stroke-linecap:square;stroke-width:2.7;\"/>\r\n   </g>\r\n   <g id=\"line2d_23\">\r\n    <path clip-path=\"url(#p5be4b671e0)\" d=\"M 0 0 \r\n\" style=\"fill:none;stroke:#424242;stroke-linecap:square;stroke-width:2.7;\"/>\r\n   </g>\r\n   <g id=\"line2d_24\">\r\n    <path clip-path=\"url(#p5be4b671e0)\" d=\"M 0 0 \r\n\" style=\"fill:none;stroke:#424242;stroke-linecap:square;stroke-width:2.7;\"/>\r\n   </g>\r\n   <g id=\"line2d_25\">\r\n    <path clip-path=\"url(#p5be4b671e0)\" d=\"M 0 0 \r\n\" style=\"fill:none;stroke:#424242;stroke-linecap:square;stroke-width:2.7;\"/>\r\n   </g>\r\n   <g id=\"line2d_26\">\r\n    <path clip-path=\"url(#p5be4b671e0)\" d=\"M 0 0 \r\n\" style=\"fill:none;stroke:#424242;stroke-linecap:square;stroke-width:2.7;\"/>\r\n   </g>\r\n   <g id=\"patch_12\">\r\n    <path d=\"M 40.603125 224.64 \r\nL 40.603125 7.2 \r\n\" style=\"fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;\"/>\r\n   </g>\r\n   <g id=\"patch_13\">\r\n    <path d=\"M 375.403125 224.64 \r\nL 375.403125 7.2 \r\n\" style=\"fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;\"/>\r\n   </g>\r\n   <g id=\"patch_14\">\r\n    <path d=\"M 40.603125 224.64 \r\nL 375.403125 224.64 \r\n\" style=\"fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;\"/>\r\n   </g>\r\n   <g id=\"patch_15\">\r\n    <path d=\"M 40.603125 7.2 \r\nL 375.403125 7.2 \r\n\" style=\"fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;\"/>\r\n   </g>\r\n  </g>\r\n </g>\r\n <defs>\r\n  <clipPath id=\"p5be4b671e0\">\r\n   <rect height=\"217.44\" width=\"334.8\" x=\"40.603125\" y=\"7.2\"/>\r\n  </clipPath>\r\n </defs>\r\n</svg>\r\n",
      "image/png": "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\n"
     },
     "metadata": {
      "needs_background": "light"
     }
    }
   ],
   "source": [
    "members_data = {memb: df[\"Members\"].to_list().count(memb) for memb in set(df[\"Members\"])}\n",
    "print(members_data)\n",
    "members_data=sorted(members_data.items(), key=operator.itemgetter(0))\n",
    "print(members_data)\n",
    "members_data=dict(members_data)\n",
    "print(members_data)\n",
    "del_data=[]\n",
    "for i in members_data:\n",
    "  if members_data[i]<5: \n",
    "   del_data.append(i)\n",
    "for j in del_data:\n",
    "  del members_data[j]\n",
    "print(members_data)\n",
    "import matplotlib.pyplot as plt\n",
    "comp_df = pd.DataFrame.from_dict(data=members_data, orient=\"index\", columns=[\"Members\"])\n",
    "comp_df[\"Num\"]=comp_df.index\n",
    "sns.barplot(data=comp_df, x=\"Num\", y=\"Members\")"
   ]
  },
  {
   "source": [
    "### В какой год больше всего групп сформироввалось"
   ],
   "cell_type": "markdown",
   "metadata": {}
  },
  {
   "cell_type": "code",
   "execution_count": 69,
   "metadata": {},
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "<AxesSubplot:xlabel='year', ylabel='number'>"
      ]
     },
     "metadata": {},
     "execution_count": 69
    },
    {
     "output_type": "display_data",
     "data": {
      "text/plain": "<Figure size 432x288 with 1 Axes>",
      "image/svg+xml": "<?xml version=\"1.0\" encoding=\"utf-8\" standalone=\"no\"?>\r\n<!DOCTYPE svg PUBLIC \"-//W3C//DTD SVG 1.1//EN\"\r\n  \"http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd\">\r\n<svg height=\"262.19625pt\" version=\"1.1\" viewBox=\"0 0 382.603125 262.19625\" width=\"382.603125pt\" xmlns=\"http://www.w3.org/2000/svg\" xmlns:xlink=\"http://www.w3.org/1999/xlink\">\r\n <metadata>\r\n  <rdf:RDF xmlns:cc=\"http://creativecommons.org/ns#\" xmlns:dc=\"http://purl.org/dc/elements/1.1/\" xmlns:rdf=\"http://www.w3.org/1999/02/22-rdf-syntax-ns#\">\r\n   <cc:Work>\r\n    <dc:type rdf:resource=\"http://purl.org/dc/dcmitype/StillImage\"/>\r\n    <dc:date>2021-04-21T13:14:39.018546</dc:date>\r\n    <dc:format>image/svg+xml</dc:format>\r\n    <dc:creator>\r\n     <cc:Agent>\r\n      <dc:title>Matplotlib v3.4.1, https://matplotlib.org/</dc:title>\r\n     </cc:Agent>\r\n    </dc:creator>\r\n   </cc:Work>\r\n  </rdf:RDF>\r\n </metadata>\r\n <defs>\r\n  <style type=\"text/css\">*{stroke-linecap:butt;stroke-linejoin:round;}</style>\r\n </defs>\r\n <g id=\"figure_1\">\r\n  <g id=\"patch_1\">\r\n   <path d=\"M 0 262.19625 \r\nL 382.603125 262.19625 \r\nL 382.603125 0 \r\nL 0 0 \r\nz\r\n\" style=\"fill:none;\"/>\r\n  </g>\r\n  <g id=\"axes_1\">\r\n   <g id=\"patch_2\">\r\n    <path d=\"M 40.603125 224.64 \r\nL 375.403125 224.64 \r\nL 375.403125 7.2 \r\nL 40.603125 7.2 \r\nz\r\n\" style=\"fill:#ffffff;\"/>\r\n   </g>\r\n   <g id=\"matplotlib.axis_1\">\r\n    <g id=\"xtick_1\">\r\n     <g id=\"line2d_1\">\r\n      <defs>\r\n       <path d=\"M 0 0 \r\nL 0 3.5 \r\n\" id=\"m145f3dd433\" style=\"stroke:#000000;stroke-width:0.8;\"/>\r\n      </defs>\r\n      <g>\r\n       <use style=\"stroke:#000000;stroke-width:0.8;\" x=\"55.821307\" xlink:href=\"#m145f3dd433\" y=\"224.64\"/>\r\n      </g>\r\n     </g>\r\n     <g id=\"text_1\">\r\n      <!-- 1995 -->\r\n      <g transform=\"translate(43.096307 239.238437)scale(0.1 -0.1)\">\r\n       <defs>\r\n        <path d=\"M 794 531 \r\nL 1825 531 \r\nL 1825 4091 \r\nL 703 3866 \r\nL 703 4441 \r\nL 1819 4666 \r\nL 2450 4666 \r\nL 2450 531 \r\nL 3481 531 \r\nL 3481 0 \r\nL 794 0 \r\nL 794 531 \r\nz\r\n\" id=\"DejaVuSans-31\" transform=\"scale(0.015625)\"/>\r\n        <path d=\"M 703 97 \r\nL 703 672 \r\nQ 941 559 1184 500 \r\nQ 1428 441 1663 441 \r\nQ 2288 441 2617 861 \r\nQ 2947 1281 2994 2138 \r\nQ 2813 1869 2534 1725 \r\nQ 2256 1581 1919 1581 \r\nQ 1219 1581 811 2004 \r\nQ 403 2428 403 3163 \r\nQ 403 3881 828 4315 \r\nQ 1253 4750 1959 4750 \r\nQ 2769 4750 3195 4129 \r\nQ 3622 3509 3622 2328 \r\nQ 3622 1225 3098 567 \r\nQ 2575 -91 1691 -91 \r\nQ 1453 -91 1209 -44 \r\nQ 966 3 703 97 \r\nz\r\nM 1959 2075 \r\nQ 2384 2075 2632 2365 \r\nQ 2881 2656 2881 3163 \r\nQ 2881 3666 2632 3958 \r\nQ 2384 4250 1959 4250 \r\nQ 1534 4250 1286 3958 \r\nQ 1038 3666 1038 3163 \r\nQ 1038 2656 1286 2365 \r\nQ 1534 2075 1959 2075 \r\nz\r\n\" id=\"DejaVuSans-39\" transform=\"scale(0.015625)\"/>\r\n        <path d=\"M 691 4666 \r\nL 3169 4666 \r\nL 3169 4134 \r\nL 1269 4134 \r\nL 1269 2991 \r\nQ 1406 3038 1543 3061 \r\nQ 1681 3084 1819 3084 \r\nQ 2600 3084 3056 2656 \r\nQ 3513 2228 3513 1497 \r\nQ 3513 744 3044 326 \r\nQ 2575 -91 1722 -91 \r\nQ 1428 -91 1123 -41 \r\nQ 819 9 494 109 \r\nL 494 744 \r\nQ 775 591 1075 516 \r\nQ 1375 441 1709 441 \r\nQ 2250 441 2565 725 \r\nQ 2881 1009 2881 1497 \r\nQ 2881 1984 2565 2268 \r\nQ 2250 2553 1709 2553 \r\nQ 1456 2553 1204 2497 \r\nQ 953 2441 691 2322 \r\nL 691 4666 \r\nz\r\n\" id=\"DejaVuSans-35\" transform=\"scale(0.015625)\"/>\r\n       </defs>\r\n       <use xlink:href=\"#DejaVuSans-31\"/>\r\n       <use x=\"63.623047\" xlink:href=\"#DejaVuSans-39\"/>\r\n       <use x=\"127.246094\" xlink:href=\"#DejaVuSans-39\"/>\r\n       <use x=\"190.869141\" xlink:href=\"#DejaVuSans-35\"/>\r\n      </g>\r\n     </g>\r\n    </g>\r\n    <g id=\"xtick_2\">\r\n     <g id=\"line2d_2\">\r\n      <g>\r\n       <use style=\"stroke:#000000;stroke-width:0.8;\" x=\"116.694034\" xlink:href=\"#m145f3dd433\" y=\"224.64\"/>\r\n      </g>\r\n     </g>\r\n     <g id=\"text_2\">\r\n      <!-- 2000 -->\r\n      <g transform=\"translate(103.969034 239.238437)scale(0.1 -0.1)\">\r\n       <defs>\r\n        <path d=\"M 1228 531 \r\nL 3431 531 \r\nL 3431 0 \r\nL 469 0 \r\nL 469 531 \r\nQ 828 903 1448 1529 \r\nQ 2069 2156 2228 2338 \r\nQ 2531 2678 2651 2914 \r\nQ 2772 3150 2772 3378 \r\nQ 2772 3750 2511 3984 \r\nQ 2250 4219 1831 4219 \r\nQ 1534 4219 1204 4116 \r\nQ 875 4013 500 3803 \r\nL 500 4441 \r\nQ 881 4594 1212 4672 \r\nQ 1544 4750 1819 4750 \r\nQ 2544 4750 2975 4387 \r\nQ 3406 4025 3406 3419 \r\nQ 3406 3131 3298 2873 \r\nQ 3191 2616 2906 2266 \r\nQ 2828 2175 2409 1742 \r\nQ 1991 1309 1228 531 \r\nz\r\n\" id=\"DejaVuSans-32\" transform=\"scale(0.015625)\"/>\r\n        <path d=\"M 2034 4250 \r\nQ 1547 4250 1301 3770 \r\nQ 1056 3291 1056 2328 \r\nQ 1056 1369 1301 889 \r\nQ 1547 409 2034 409 \r\nQ 2525 409 2770 889 \r\nQ 3016 1369 3016 2328 \r\nQ 3016 3291 2770 3770 \r\nQ 2525 4250 2034 4250 \r\nz\r\nM 2034 4750 \r\nQ 2819 4750 3233 4129 \r\nQ 3647 3509 3647 2328 \r\nQ 3647 1150 3233 529 \r\nQ 2819 -91 2034 -91 \r\nQ 1250 -91 836 529 \r\nQ 422 1150 422 2328 \r\nQ 422 3509 836 4129 \r\nQ 1250 4750 2034 4750 \r\nz\r\n\" id=\"DejaVuSans-30\" transform=\"scale(0.015625)\"/>\r\n       </defs>\r\n       <use xlink:href=\"#DejaVuSans-32\"/>\r\n       <use x=\"63.623047\" xlink:href=\"#DejaVuSans-30\"/>\r\n       <use x=\"127.246094\" xlink:href=\"#DejaVuSans-30\"/>\r\n       <use x=\"190.869141\" xlink:href=\"#DejaVuSans-30\"/>\r\n      </g>\r\n     </g>\r\n    </g>\r\n    <g id=\"xtick_3\">\r\n     <g id=\"line2d_3\">\r\n      <g>\r\n       <use style=\"stroke:#000000;stroke-width:0.8;\" x=\"177.566761\" xlink:href=\"#m145f3dd433\" y=\"224.64\"/>\r\n      </g>\r\n     </g>\r\n     <g id=\"text_3\">\r\n      <!-- 2005 -->\r\n      <g transform=\"translate(164.841761 239.238437)scale(0.1 -0.1)\">\r\n       <use xlink:href=\"#DejaVuSans-32\"/>\r\n       <use x=\"63.623047\" xlink:href=\"#DejaVuSans-30\"/>\r\n       <use x=\"127.246094\" xlink:href=\"#DejaVuSans-30\"/>\r\n       <use x=\"190.869141\" xlink:href=\"#DejaVuSans-35\"/>\r\n      </g>\r\n     </g>\r\n    </g>\r\n    <g id=\"xtick_4\">\r\n     <g id=\"line2d_4\">\r\n      <g>\r\n       <use style=\"stroke:#000000;stroke-width:0.8;\" x=\"238.439489\" xlink:href=\"#m145f3dd433\" y=\"224.64\"/>\r\n      </g>\r\n     </g>\r\n     <g id=\"text_4\">\r\n      <!-- 2010 -->\r\n      <g transform=\"translate(225.714489 239.238437)scale(0.1 -0.1)\">\r\n       <use xlink:href=\"#DejaVuSans-32\"/>\r\n       <use x=\"63.623047\" xlink:href=\"#DejaVuSans-30\"/>\r\n       <use x=\"127.246094\" xlink:href=\"#DejaVuSans-31\"/>\r\n       <use x=\"190.869141\" xlink:href=\"#DejaVuSans-30\"/>\r\n      </g>\r\n     </g>\r\n    </g>\r\n    <g id=\"xtick_5\">\r\n     <g id=\"line2d_5\">\r\n      <g>\r\n       <use style=\"stroke:#000000;stroke-width:0.8;\" x=\"299.312216\" xlink:href=\"#m145f3dd433\" y=\"224.64\"/>\r\n      </g>\r\n     </g>\r\n     <g id=\"text_5\">\r\n      <!-- 2015 -->\r\n      <g transform=\"translate(286.587216 239.238437)scale(0.1 -0.1)\">\r\n       <use xlink:href=\"#DejaVuSans-32\"/>\r\n       <use x=\"63.623047\" xlink:href=\"#DejaVuSans-30\"/>\r\n       <use x=\"127.246094\" xlink:href=\"#DejaVuSans-31\"/>\r\n       <use x=\"190.869141\" xlink:href=\"#DejaVuSans-35\"/>\r\n      </g>\r\n     </g>\r\n    </g>\r\n    <g id=\"xtick_6\">\r\n     <g id=\"line2d_6\">\r\n      <g>\r\n       <use style=\"stroke:#000000;stroke-width:0.8;\" x=\"360.184943\" xlink:href=\"#m145f3dd433\" y=\"224.64\"/>\r\n      </g>\r\n     </g>\r\n     <g id=\"text_6\">\r\n      <!-- 2020 -->\r\n      <g transform=\"translate(347.459943 239.238437)scale(0.1 -0.1)\">\r\n       <use xlink:href=\"#DejaVuSans-32\"/>\r\n       <use x=\"63.623047\" xlink:href=\"#DejaVuSans-30\"/>\r\n       <use x=\"127.246094\" xlink:href=\"#DejaVuSans-32\"/>\r\n       <use x=\"190.869141\" xlink:href=\"#DejaVuSans-30\"/>\r\n      </g>\r\n     </g>\r\n    </g>\r\n    <g id=\"text_7\">\r\n     <!-- year -->\r\n     <g transform=\"translate(196.847656 252.916562)scale(0.1 -0.1)\">\r\n      <defs>\r\n       <path d=\"M 2059 -325 \r\nQ 1816 -950 1584 -1140 \r\nQ 1353 -1331 966 -1331 \r\nL 506 -1331 \r\nL 506 -850 \r\nL 844 -850 \r\nQ 1081 -850 1212 -737 \r\nQ 1344 -625 1503 -206 \r\nL 1606 56 \r\nL 191 3500 \r\nL 800 3500 \r\nL 1894 763 \r\nL 2988 3500 \r\nL 3597 3500 \r\nL 2059 -325 \r\nz\r\n\" id=\"DejaVuSans-79\" transform=\"scale(0.015625)\"/>\r\n       <path d=\"M 3597 1894 \r\nL 3597 1613 \r\nL 953 1613 \r\nQ 991 1019 1311 708 \r\nQ 1631 397 2203 397 \r\nQ 2534 397 2845 478 \r\nQ 3156 559 3463 722 \r\nL 3463 178 \r\nQ 3153 47 2828 -22 \r\nQ 2503 -91 2169 -91 \r\nQ 1331 -91 842 396 \r\nQ 353 884 353 1716 \r\nQ 353 2575 817 3079 \r\nQ 1281 3584 2069 3584 \r\nQ 2775 3584 3186 3129 \r\nQ 3597 2675 3597 1894 \r\nz\r\nM 3022 2063 \r\nQ 3016 2534 2758 2815 \r\nQ 2500 3097 2075 3097 \r\nQ 1594 3097 1305 2825 \r\nQ 1016 2553 972 2059 \r\nL 3022 2063 \r\nz\r\n\" id=\"DejaVuSans-65\" transform=\"scale(0.015625)\"/>\r\n       <path d=\"M 2194 1759 \r\nQ 1497 1759 1228 1600 \r\nQ 959 1441 959 1056 \r\nQ 959 750 1161 570 \r\nQ 1363 391 1709 391 \r\nQ 2188 391 2477 730 \r\nQ 2766 1069 2766 1631 \r\nL 2766 1759 \r\nL 2194 1759 \r\nz\r\nM 3341 1997 \r\nL 3341 0 \r\nL 2766 0 \r\nL 2766 531 \r\nQ 2569 213 2275 61 \r\nQ 1981 -91 1556 -91 \r\nQ 1019 -91 701 211 \r\nQ 384 513 384 1019 \r\nQ 384 1609 779 1909 \r\nQ 1175 2209 1959 2209 \r\nL 2766 2209 \r\nL 2766 2266 \r\nQ 2766 2663 2505 2880 \r\nQ 2244 3097 1772 3097 \r\nQ 1472 3097 1187 3025 \r\nQ 903 2953 641 2809 \r\nL 641 3341 \r\nQ 956 3463 1253 3523 \r\nQ 1550 3584 1831 3584 \r\nQ 2591 3584 2966 3190 \r\nQ 3341 2797 3341 1997 \r\nz\r\n\" id=\"DejaVuSans-61\" transform=\"scale(0.015625)\"/>\r\n       <path d=\"M 2631 2963 \r\nQ 2534 3019 2420 3045 \r\nQ 2306 3072 2169 3072 \r\nQ 1681 3072 1420 2755 \r\nQ 1159 2438 1159 1844 \r\nL 1159 0 \r\nL 581 0 \r\nL 581 3500 \r\nL 1159 3500 \r\nL 1159 2956 \r\nQ 1341 3275 1631 3429 \r\nQ 1922 3584 2338 3584 \r\nQ 2397 3584 2469 3576 \r\nQ 2541 3569 2628 3553 \r\nL 2631 2963 \r\nz\r\n\" id=\"DejaVuSans-72\" transform=\"scale(0.015625)\"/>\r\n      </defs>\r\n      <use xlink:href=\"#DejaVuSans-79\"/>\r\n      <use x=\"59.179688\" xlink:href=\"#DejaVuSans-65\"/>\r\n      <use x=\"120.703125\" xlink:href=\"#DejaVuSans-61\"/>\r\n      <use x=\"181.982422\" xlink:href=\"#DejaVuSans-72\"/>\r\n     </g>\r\n    </g>\r\n   </g>\r\n   <g id=\"matplotlib.axis_2\">\r\n    <g id=\"ytick_1\">\r\n     <g id=\"line2d_7\">\r\n      <defs>\r\n       <path d=\"M 0 0 \r\nL -3.5 0 \r\n\" id=\"mcdc6adc32e\" style=\"stroke:#000000;stroke-width:0.8;\"/>\r\n      </defs>\r\n      <g>\r\n       <use style=\"stroke:#000000;stroke-width:0.8;\" x=\"40.603125\" xlink:href=\"#mcdc6adc32e\" y=\"218.874545\"/>\r\n      </g>\r\n     </g>\r\n     <g id=\"text_8\">\r\n      <!-- 0 -->\r\n      <g transform=\"translate(27.240625 222.673764)scale(0.1 -0.1)\">\r\n       <use xlink:href=\"#DejaVuSans-30\"/>\r\n      </g>\r\n     </g>\r\n    </g>\r\n    <g id=\"ytick_2\">\r\n     <g id=\"line2d_8\">\r\n      <g>\r\n       <use style=\"stroke:#000000;stroke-width:0.8;\" x=\"40.603125\" xlink:href=\"#mcdc6adc32e\" y=\"177.692727\"/>\r\n      </g>\r\n     </g>\r\n     <g id=\"text_9\">\r\n      <!-- 10 -->\r\n      <g transform=\"translate(20.878125 181.491946)scale(0.1 -0.1)\">\r\n       <use xlink:href=\"#DejaVuSans-31\"/>\r\n       <use x=\"63.623047\" xlink:href=\"#DejaVuSans-30\"/>\r\n      </g>\r\n     </g>\r\n    </g>\r\n    <g id=\"ytick_3\">\r\n     <g id=\"line2d_9\">\r\n      <g>\r\n       <use style=\"stroke:#000000;stroke-width:0.8;\" x=\"40.603125\" xlink:href=\"#mcdc6adc32e\" y=\"136.510909\"/>\r\n      </g>\r\n     </g>\r\n     <g id=\"text_10\">\r\n      <!-- 20 -->\r\n      <g transform=\"translate(20.878125 140.310128)scale(0.1 -0.1)\">\r\n       <use xlink:href=\"#DejaVuSans-32\"/>\r\n       <use x=\"63.623047\" xlink:href=\"#DejaVuSans-30\"/>\r\n      </g>\r\n     </g>\r\n    </g>\r\n    <g id=\"ytick_4\">\r\n     <g id=\"line2d_10\">\r\n      <g>\r\n       <use style=\"stroke:#000000;stroke-width:0.8;\" x=\"40.603125\" xlink:href=\"#mcdc6adc32e\" y=\"95.329091\"/>\r\n      </g>\r\n     </g>\r\n     <g id=\"text_11\">\r\n      <!-- 30 -->\r\n      <g transform=\"translate(20.878125 99.12831)scale(0.1 -0.1)\">\r\n       <defs>\r\n        <path d=\"M 2597 2516 \r\nQ 3050 2419 3304 2112 \r\nQ 3559 1806 3559 1356 \r\nQ 3559 666 3084 287 \r\nQ 2609 -91 1734 -91 \r\nQ 1441 -91 1130 -33 \r\nQ 819 25 488 141 \r\nL 488 750 \r\nQ 750 597 1062 519 \r\nQ 1375 441 1716 441 \r\nQ 2309 441 2620 675 \r\nQ 2931 909 2931 1356 \r\nQ 2931 1769 2642 2001 \r\nQ 2353 2234 1838 2234 \r\nL 1294 2234 \r\nL 1294 2753 \r\nL 1863 2753 \r\nQ 2328 2753 2575 2939 \r\nQ 2822 3125 2822 3475 \r\nQ 2822 3834 2567 4026 \r\nQ 2313 4219 1838 4219 \r\nQ 1578 4219 1281 4162 \r\nQ 984 4106 628 3988 \r\nL 628 4550 \r\nQ 988 4650 1302 4700 \r\nQ 1616 4750 1894 4750 \r\nQ 2613 4750 3031 4423 \r\nQ 3450 4097 3450 3541 \r\nQ 3450 3153 3228 2886 \r\nQ 3006 2619 2597 2516 \r\nz\r\n\" id=\"DejaVuSans-33\" transform=\"scale(0.015625)\"/>\r\n       </defs>\r\n       <use xlink:href=\"#DejaVuSans-33\"/>\r\n       <use x=\"63.623047\" xlink:href=\"#DejaVuSans-30\"/>\r\n      </g>\r\n     </g>\r\n    </g>\r\n    <g id=\"ytick_5\">\r\n     <g id=\"line2d_11\">\r\n      <g>\r\n       <use style=\"stroke:#000000;stroke-width:0.8;\" x=\"40.603125\" xlink:href=\"#mcdc6adc32e\" y=\"54.147273\"/>\r\n      </g>\r\n     </g>\r\n     <g id=\"text_12\">\r\n      <!-- 40 -->\r\n      <g transform=\"translate(20.878125 57.946491)scale(0.1 -0.1)\">\r\n       <defs>\r\n        <path d=\"M 2419 4116 \r\nL 825 1625 \r\nL 2419 1625 \r\nL 2419 4116 \r\nz\r\nM 2253 4666 \r\nL 3047 4666 \r\nL 3047 1625 \r\nL 3713 1625 \r\nL 3713 1100 \r\nL 3047 1100 \r\nL 3047 0 \r\nL 2419 0 \r\nL 2419 1100 \r\nL 313 1100 \r\nL 313 1709 \r\nL 2253 4666 \r\nz\r\n\" id=\"DejaVuSans-34\" transform=\"scale(0.015625)\"/>\r\n       </defs>\r\n       <use xlink:href=\"#DejaVuSans-34\"/>\r\n       <use x=\"63.623047\" xlink:href=\"#DejaVuSans-30\"/>\r\n      </g>\r\n     </g>\r\n    </g>\r\n    <g id=\"ytick_6\">\r\n     <g id=\"line2d_12\">\r\n      <g>\r\n       <use style=\"stroke:#000000;stroke-width:0.8;\" x=\"40.603125\" xlink:href=\"#mcdc6adc32e\" y=\"12.965455\"/>\r\n      </g>\r\n     </g>\r\n     <g id=\"text_13\">\r\n      <!-- 50 -->\r\n      <g transform=\"translate(20.878125 16.764673)scale(0.1 -0.1)\">\r\n       <use xlink:href=\"#DejaVuSans-35\"/>\r\n       <use x=\"63.623047\" xlink:href=\"#DejaVuSans-30\"/>\r\n      </g>\r\n     </g>\r\n    </g>\r\n    <g id=\"text_14\">\r\n     <!-- number -->\r\n     <g transform=\"translate(14.798438 135.434062)rotate(-90)scale(0.1 -0.1)\">\r\n      <defs>\r\n       <path d=\"M 3513 2113 \r\nL 3513 0 \r\nL 2938 0 \r\nL 2938 2094 \r\nQ 2938 2591 2744 2837 \r\nQ 2550 3084 2163 3084 \r\nQ 1697 3084 1428 2787 \r\nQ 1159 2491 1159 1978 \r\nL 1159 0 \r\nL 581 0 \r\nL 581 3500 \r\nL 1159 3500 \r\nL 1159 2956 \r\nQ 1366 3272 1645 3428 \r\nQ 1925 3584 2291 3584 \r\nQ 2894 3584 3203 3211 \r\nQ 3513 2838 3513 2113 \r\nz\r\n\" id=\"DejaVuSans-6e\" transform=\"scale(0.015625)\"/>\r\n       <path d=\"M 544 1381 \r\nL 544 3500 \r\nL 1119 3500 \r\nL 1119 1403 \r\nQ 1119 906 1312 657 \r\nQ 1506 409 1894 409 \r\nQ 2359 409 2629 706 \r\nQ 2900 1003 2900 1516 \r\nL 2900 3500 \r\nL 3475 3500 \r\nL 3475 0 \r\nL 2900 0 \r\nL 2900 538 \r\nQ 2691 219 2414 64 \r\nQ 2138 -91 1772 -91 \r\nQ 1169 -91 856 284 \r\nQ 544 659 544 1381 \r\nz\r\nM 1991 3584 \r\nL 1991 3584 \r\nz\r\n\" id=\"DejaVuSans-75\" transform=\"scale(0.015625)\"/>\r\n       <path d=\"M 3328 2828 \r\nQ 3544 3216 3844 3400 \r\nQ 4144 3584 4550 3584 \r\nQ 5097 3584 5394 3201 \r\nQ 5691 2819 5691 2113 \r\nL 5691 0 \r\nL 5113 0 \r\nL 5113 2094 \r\nQ 5113 2597 4934 2840 \r\nQ 4756 3084 4391 3084 \r\nQ 3944 3084 3684 2787 \r\nQ 3425 2491 3425 1978 \r\nL 3425 0 \r\nL 2847 0 \r\nL 2847 2094 \r\nQ 2847 2600 2669 2842 \r\nQ 2491 3084 2119 3084 \r\nQ 1678 3084 1418 2786 \r\nQ 1159 2488 1159 1978 \r\nL 1159 0 \r\nL 581 0 \r\nL 581 3500 \r\nL 1159 3500 \r\nL 1159 2956 \r\nQ 1356 3278 1631 3431 \r\nQ 1906 3584 2284 3584 \r\nQ 2666 3584 2933 3390 \r\nQ 3200 3197 3328 2828 \r\nz\r\n\" id=\"DejaVuSans-6d\" transform=\"scale(0.015625)\"/>\r\n       <path d=\"M 3116 1747 \r\nQ 3116 2381 2855 2742 \r\nQ 2594 3103 2138 3103 \r\nQ 1681 3103 1420 2742 \r\nQ 1159 2381 1159 1747 \r\nQ 1159 1113 1420 752 \r\nQ 1681 391 2138 391 \r\nQ 2594 391 2855 752 \r\nQ 3116 1113 3116 1747 \r\nz\r\nM 1159 2969 \r\nQ 1341 3281 1617 3432 \r\nQ 1894 3584 2278 3584 \r\nQ 2916 3584 3314 3078 \r\nQ 3713 2572 3713 1747 \r\nQ 3713 922 3314 415 \r\nQ 2916 -91 2278 -91 \r\nQ 1894 -91 1617 61 \r\nQ 1341 213 1159 525 \r\nL 1159 0 \r\nL 581 0 \r\nL 581 4863 \r\nL 1159 4863 \r\nL 1159 2969 \r\nz\r\n\" id=\"DejaVuSans-62\" transform=\"scale(0.015625)\"/>\r\n      </defs>\r\n      <use xlink:href=\"#DejaVuSans-6e\"/>\r\n      <use x=\"63.378906\" xlink:href=\"#DejaVuSans-75\"/>\r\n      <use x=\"126.757812\" xlink:href=\"#DejaVuSans-6d\"/>\r\n      <use x=\"224.169922\" xlink:href=\"#DejaVuSans-62\"/>\r\n      <use x=\"287.646484\" xlink:href=\"#DejaVuSans-65\"/>\r\n      <use x=\"349.169922\" xlink:href=\"#DejaVuSans-72\"/>\r\n     </g>\r\n    </g>\r\n   </g>\r\n   <g id=\"line2d_13\">\r\n    <path clip-path=\"url(#p802f6721b4)\" d=\"M 55.821307 214.756364 \r\nL 67.995852 214.756364 \r\nL 80.170398 206.52 \r\nL 92.344943 214.756364 \r\nL 104.519489 210.638182 \r\nL 128.86858 214.756364 \r\nL 153.21767 214.756364 \r\nL 165.392216 210.638182 \r\nL 177.566761 202.401818 \r\nL 189.741307 210.638182 \r\nL 201.915852 190.047273 \r\nL 214.090398 198.283636 \r\nL 226.264943 185.929091 \r\nL 238.439489 169.456364 \r\nL 250.614034 144.747273 \r\nL 262.78858 111.801818 \r\nL 274.963125 169.456364 \r\nL 287.13767 103.565455 \r\nL 299.312216 120.038182 \r\nL 311.486761 99.447273 \r\nL 323.661307 17.083636 \r\nL 335.835852 82.974545 \r\nL 348.010398 111.801818 \r\nL 360.184943 202.401818 \r\n\" style=\"fill:none;stroke:#1f77b4;stroke-linecap:square;stroke-width:1.5;\"/>\r\n   </g>\r\n   <g id=\"patch_3\">\r\n    <path d=\"M 40.603125 224.64 \r\nL 40.603125 7.2 \r\n\" style=\"fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;\"/>\r\n   </g>\r\n   <g id=\"patch_4\">\r\n    <path d=\"M 375.403125 224.64 \r\nL 375.403125 7.2 \r\n\" style=\"fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;\"/>\r\n   </g>\r\n   <g id=\"patch_5\">\r\n    <path d=\"M 40.603125 224.64 \r\nL 375.403125 224.64 \r\n\" style=\"fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;\"/>\r\n   </g>\r\n   <g id=\"patch_6\">\r\n    <path d=\"M 40.603125 7.2 \r\nL 375.403125 7.2 \r\n\" style=\"fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;\"/>\r\n   </g>\r\n  </g>\r\n </g>\r\n <defs>\r\n  <clipPath id=\"p802f6721b4\">\r\n   <rect height=\"217.44\" width=\"334.8\" x=\"40.603125\" y=\"7.2\"/>\r\n  </clipPath>\r\n </defs>\r\n</svg>\r\n",
      "image/png": "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\n"
     },
     "metadata": {
      "needs_background": "light"
     }
    }
   ],
   "source": [
    "\n",
    "dates_list = df.Debut\n",
    "dates_list=sorted(dates_list)\n",
    "date_data = {age: dates_list.count(age) for age in (dates_list)}\n",
    "score_df = pd.DataFrame.from_dict(data=date_data, orient=\"index\", columns=[\"number\"])\n",
    "score_df['year'] = score_df.index\n",
    "sns.lineplot(data=score_df, x=\"year\", y=\"number\")"
   ]
  },
  {
   "source": [
    "### В какой год больше всего групп распалось"
   ],
   "cell_type": "markdown",
   "metadata": {}
  },
  {
   "cell_type": "code",
   "execution_count": 81,
   "metadata": {},
   "outputs": [
    {
     "output_type": "stream",
     "name": "stdout",
     "text": [
      "      number  year\n2001       1  2001\n2002       1  2002\n2006       1  2006\n2010       1  2010\n2013       2  2013\n2014       2  2014\n2015       9  2015\n2016      11  2016\n2017      25  2017\n2018      13  2018\n2019      23  2019\n2020       3  2020\n"
     ]
    },
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "<AxesSubplot:xlabel='year', ylabel='number'>"
      ]
     },
     "metadata": {},
     "execution_count": 81
    },
    {
     "output_type": "display_data",
     "data": {
      "text/plain": "<Figure size 432x288 with 1 Axes>",
      "image/svg+xml": "<?xml version=\"1.0\" encoding=\"utf-8\" standalone=\"no\"?>\r\n<!DOCTYPE svg PUBLIC \"-//W3C//DTD SVG 1.1//EN\"\r\n  \"http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd\">\r\n<svg height=\"262.19625pt\" version=\"1.1\" viewBox=\"0 0 384.880256 262.19625\" width=\"384.880256pt\" xmlns=\"http://www.w3.org/2000/svg\" xmlns:xlink=\"http://www.w3.org/1999/xlink\">\r\n <metadata>\r\n  <rdf:RDF xmlns:cc=\"http://creativecommons.org/ns#\" xmlns:dc=\"http://purl.org/dc/elements/1.1/\" xmlns:rdf=\"http://www.w3.org/1999/02/22-rdf-syntax-ns#\">\r\n   <cc:Work>\r\n    <dc:type rdf:resource=\"http://purl.org/dc/dcmitype/StillImage\"/>\r\n    <dc:date>2021-04-21T14:02:50.494386</dc:date>\r\n    <dc:format>image/svg+xml</dc:format>\r\n    <dc:creator>\r\n     <cc:Agent>\r\n      <dc:title>Matplotlib v3.4.1, https://matplotlib.org/</dc:title>\r\n     </cc:Agent>\r\n    </dc:creator>\r\n   </cc:Work>\r\n  </rdf:RDF>\r\n </metadata>\r\n <defs>\r\n  <style type=\"text/css\">*{stroke-linecap:butt;stroke-linejoin:round;}</style>\r\n </defs>\r\n <g id=\"figure_1\">\r\n  <g id=\"patch_1\">\r\n   <path d=\"M 0 262.19625 \r\nL 384.880256 262.19625 \r\nL 384.880256 0 \r\nL 0 0 \r\nz\r\n\" style=\"fill:none;\"/>\r\n  </g>\r\n  <g id=\"axes_1\">\r\n   <g id=\"patch_2\">\r\n    <path d=\"M 40.603125 224.64 \r\nL 375.403125 224.64 \r\nL 375.403125 7.2 \r\nL 40.603125 7.2 \r\nz\r\n\" style=\"fill:#ffffff;\"/>\r\n   </g>\r\n   <g id=\"matplotlib.axis_1\">\r\n    <g id=\"xtick_1\">\r\n     <g id=\"line2d_1\">\r\n      <defs>\r\n       <path d=\"M 0 0 \r\nL 0 3.5 \r\n\" id=\"m37f988fa58\" style=\"stroke:#000000;stroke-width:0.8;\"/>\r\n      </defs>\r\n      <g>\r\n       <use style=\"stroke:#000000;stroke-width:0.8;\" x=\"79.850015\" xlink:href=\"#m37f988fa58\" y=\"224.64\"/>\r\n      </g>\r\n     </g>\r\n     <g id=\"text_1\">\r\n      <!-- 2002.5 -->\r\n      <g transform=\"translate(62.354702 239.238437)scale(0.1 -0.1)\">\r\n       <defs>\r\n        <path d=\"M 1228 531 \r\nL 3431 531 \r\nL 3431 0 \r\nL 469 0 \r\nL 469 531 \r\nQ 828 903 1448 1529 \r\nQ 2069 2156 2228 2338 \r\nQ 2531 2678 2651 2914 \r\nQ 2772 3150 2772 3378 \r\nQ 2772 3750 2511 3984 \r\nQ 2250 4219 1831 4219 \r\nQ 1534 4219 1204 4116 \r\nQ 875 4013 500 3803 \r\nL 500 4441 \r\nQ 881 4594 1212 4672 \r\nQ 1544 4750 1819 4750 \r\nQ 2544 4750 2975 4387 \r\nQ 3406 4025 3406 3419 \r\nQ 3406 3131 3298 2873 \r\nQ 3191 2616 2906 2266 \r\nQ 2828 2175 2409 1742 \r\nQ 1991 1309 1228 531 \r\nz\r\n\" id=\"DejaVuSans-32\" transform=\"scale(0.015625)\"/>\r\n        <path d=\"M 2034 4250 \r\nQ 1547 4250 1301 3770 \r\nQ 1056 3291 1056 2328 \r\nQ 1056 1369 1301 889 \r\nQ 1547 409 2034 409 \r\nQ 2525 409 2770 889 \r\nQ 3016 1369 3016 2328 \r\nQ 3016 3291 2770 3770 \r\nQ 2525 4250 2034 4250 \r\nz\r\nM 2034 4750 \r\nQ 2819 4750 3233 4129 \r\nQ 3647 3509 3647 2328 \r\nQ 3647 1150 3233 529 \r\nQ 2819 -91 2034 -91 \r\nQ 1250 -91 836 529 \r\nQ 422 1150 422 2328 \r\nQ 422 3509 836 4129 \r\nQ 1250 4750 2034 4750 \r\nz\r\n\" id=\"DejaVuSans-30\" transform=\"scale(0.015625)\"/>\r\n        <path d=\"M 684 794 \r\nL 1344 794 \r\nL 1344 0 \r\nL 684 0 \r\nL 684 794 \r\nz\r\n\" id=\"DejaVuSans-2e\" transform=\"scale(0.015625)\"/>\r\n        <path d=\"M 691 4666 \r\nL 3169 4666 \r\nL 3169 4134 \r\nL 1269 4134 \r\nL 1269 2991 \r\nQ 1406 3038 1543 3061 \r\nQ 1681 3084 1819 3084 \r\nQ 2600 3084 3056 2656 \r\nQ 3513 2228 3513 1497 \r\nQ 3513 744 3044 326 \r\nQ 2575 -91 1722 -91 \r\nQ 1428 -91 1123 -41 \r\nQ 819 9 494 109 \r\nL 494 744 \r\nQ 775 591 1075 516 \r\nQ 1375 441 1709 441 \r\nQ 2250 441 2565 725 \r\nQ 2881 1009 2881 1497 \r\nQ 2881 1984 2565 2268 \r\nQ 2250 2553 1709 2553 \r\nQ 1456 2553 1204 2497 \r\nQ 953 2441 691 2322 \r\nL 691 4666 \r\nz\r\n\" id=\"DejaVuSans-35\" transform=\"scale(0.015625)\"/>\r\n       </defs>\r\n       <use xlink:href=\"#DejaVuSans-32\"/>\r\n       <use x=\"63.623047\" xlink:href=\"#DejaVuSans-30\"/>\r\n       <use x=\"127.246094\" xlink:href=\"#DejaVuSans-30\"/>\r\n       <use x=\"190.869141\" xlink:href=\"#DejaVuSans-32\"/>\r\n       <use x=\"254.492188\" xlink:href=\"#DejaVuSans-2e\"/>\r\n       <use x=\"286.279297\" xlink:href=\"#DejaVuSans-35\"/>\r\n      </g>\r\n     </g>\r\n    </g>\r\n    <g id=\"xtick_2\">\r\n     <g id=\"line2d_2\">\r\n      <g>\r\n       <use style=\"stroke:#000000;stroke-width:0.8;\" x=\"119.897862\" xlink:href=\"#m37f988fa58\" y=\"224.64\"/>\r\n      </g>\r\n     </g>\r\n     <g id=\"text_2\">\r\n      <!-- 2005.0 -->\r\n      <g transform=\"translate(102.402549 239.238437)scale(0.1 -0.1)\">\r\n       <use xlink:href=\"#DejaVuSans-32\"/>\r\n       <use x=\"63.623047\" xlink:href=\"#DejaVuSans-30\"/>\r\n       <use x=\"127.246094\" xlink:href=\"#DejaVuSans-30\"/>\r\n       <use x=\"190.869141\" xlink:href=\"#DejaVuSans-35\"/>\r\n       <use x=\"254.492188\" xlink:href=\"#DejaVuSans-2e\"/>\r\n       <use x=\"286.279297\" xlink:href=\"#DejaVuSans-30\"/>\r\n      </g>\r\n     </g>\r\n    </g>\r\n    <g id=\"xtick_3\">\r\n     <g id=\"line2d_3\">\r\n      <g>\r\n       <use style=\"stroke:#000000;stroke-width:0.8;\" x=\"159.945709\" xlink:href=\"#m37f988fa58\" y=\"224.64\"/>\r\n      </g>\r\n     </g>\r\n     <g id=\"text_3\">\r\n      <!-- 2007.5 -->\r\n      <g transform=\"translate(142.450396 239.238437)scale(0.1 -0.1)\">\r\n       <defs>\r\n        <path d=\"M 525 4666 \r\nL 3525 4666 \r\nL 3525 4397 \r\nL 1831 0 \r\nL 1172 0 \r\nL 2766 4134 \r\nL 525 4134 \r\nL 525 4666 \r\nz\r\n\" id=\"DejaVuSans-37\" transform=\"scale(0.015625)\"/>\r\n       </defs>\r\n       <use xlink:href=\"#DejaVuSans-32\"/>\r\n       <use x=\"63.623047\" xlink:href=\"#DejaVuSans-30\"/>\r\n       <use x=\"127.246094\" xlink:href=\"#DejaVuSans-30\"/>\r\n       <use x=\"190.869141\" xlink:href=\"#DejaVuSans-37\"/>\r\n       <use x=\"254.492188\" xlink:href=\"#DejaVuSans-2e\"/>\r\n       <use x=\"286.279297\" xlink:href=\"#DejaVuSans-35\"/>\r\n      </g>\r\n     </g>\r\n    </g>\r\n    <g id=\"xtick_4\">\r\n     <g id=\"line2d_4\">\r\n      <g>\r\n       <use style=\"stroke:#000000;stroke-width:0.8;\" x=\"199.993556\" xlink:href=\"#m37f988fa58\" y=\"224.64\"/>\r\n      </g>\r\n     </g>\r\n     <g id=\"text_4\">\r\n      <!-- 2010.0 -->\r\n      <g transform=\"translate(182.498243 239.238437)scale(0.1 -0.1)\">\r\n       <defs>\r\n        <path d=\"M 794 531 \r\nL 1825 531 \r\nL 1825 4091 \r\nL 703 3866 \r\nL 703 4441 \r\nL 1819 4666 \r\nL 2450 4666 \r\nL 2450 531 \r\nL 3481 531 \r\nL 3481 0 \r\nL 794 0 \r\nL 794 531 \r\nz\r\n\" id=\"DejaVuSans-31\" transform=\"scale(0.015625)\"/>\r\n       </defs>\r\n       <use xlink:href=\"#DejaVuSans-32\"/>\r\n       <use x=\"63.623047\" xlink:href=\"#DejaVuSans-30\"/>\r\n       <use x=\"127.246094\" xlink:href=\"#DejaVuSans-31\"/>\r\n       <use x=\"190.869141\" xlink:href=\"#DejaVuSans-30\"/>\r\n       <use x=\"254.492188\" xlink:href=\"#DejaVuSans-2e\"/>\r\n       <use x=\"286.279297\" xlink:href=\"#DejaVuSans-30\"/>\r\n      </g>\r\n     </g>\r\n    </g>\r\n    <g id=\"xtick_5\">\r\n     <g id=\"line2d_5\">\r\n      <g>\r\n       <use style=\"stroke:#000000;stroke-width:0.8;\" x=\"240.041403\" xlink:href=\"#m37f988fa58\" y=\"224.64\"/>\r\n      </g>\r\n     </g>\r\n     <g id=\"text_5\">\r\n      <!-- 2012.5 -->\r\n      <g transform=\"translate(222.54609 239.238437)scale(0.1 -0.1)\">\r\n       <use xlink:href=\"#DejaVuSans-32\"/>\r\n       <use x=\"63.623047\" xlink:href=\"#DejaVuSans-30\"/>\r\n       <use x=\"127.246094\" xlink:href=\"#DejaVuSans-31\"/>\r\n       <use x=\"190.869141\" xlink:href=\"#DejaVuSans-32\"/>\r\n       <use x=\"254.492188\" xlink:href=\"#DejaVuSans-2e\"/>\r\n       <use x=\"286.279297\" xlink:href=\"#DejaVuSans-35\"/>\r\n      </g>\r\n     </g>\r\n    </g>\r\n    <g id=\"xtick_6\">\r\n     <g id=\"line2d_6\">\r\n      <g>\r\n       <use style=\"stroke:#000000;stroke-width:0.8;\" x=\"280.089249\" xlink:href=\"#m37f988fa58\" y=\"224.64\"/>\r\n      </g>\r\n     </g>\r\n     <g id=\"text_6\">\r\n      <!-- 2015.0 -->\r\n      <g transform=\"translate(262.593937 239.238437)scale(0.1 -0.1)\">\r\n       <use xlink:href=\"#DejaVuSans-32\"/>\r\n       <use x=\"63.623047\" xlink:href=\"#DejaVuSans-30\"/>\r\n       <use x=\"127.246094\" xlink:href=\"#DejaVuSans-31\"/>\r\n       <use x=\"190.869141\" xlink:href=\"#DejaVuSans-35\"/>\r\n       <use x=\"254.492188\" xlink:href=\"#DejaVuSans-2e\"/>\r\n       <use x=\"286.279297\" xlink:href=\"#DejaVuSans-30\"/>\r\n      </g>\r\n     </g>\r\n    </g>\r\n    <g id=\"xtick_7\">\r\n     <g id=\"line2d_7\">\r\n      <g>\r\n       <use style=\"stroke:#000000;stroke-width:0.8;\" x=\"320.137096\" xlink:href=\"#m37f988fa58\" y=\"224.64\"/>\r\n      </g>\r\n     </g>\r\n     <g id=\"text_7\">\r\n      <!-- 2017.5 -->\r\n      <g transform=\"translate(302.641784 239.238437)scale(0.1 -0.1)\">\r\n       <use xlink:href=\"#DejaVuSans-32\"/>\r\n       <use x=\"63.623047\" xlink:href=\"#DejaVuSans-30\"/>\r\n       <use x=\"127.246094\" xlink:href=\"#DejaVuSans-31\"/>\r\n       <use x=\"190.869141\" xlink:href=\"#DejaVuSans-37\"/>\r\n       <use x=\"254.492188\" xlink:href=\"#DejaVuSans-2e\"/>\r\n       <use x=\"286.279297\" xlink:href=\"#DejaVuSans-35\"/>\r\n      </g>\r\n     </g>\r\n    </g>\r\n    <g id=\"xtick_8\">\r\n     <g id=\"line2d_8\">\r\n      <g>\r\n       <use style=\"stroke:#000000;stroke-width:0.8;\" x=\"360.184943\" xlink:href=\"#m37f988fa58\" y=\"224.64\"/>\r\n      </g>\r\n     </g>\r\n     <g id=\"text_8\">\r\n      <!-- 2020.0 -->\r\n      <g transform=\"translate(342.689631 239.238437)scale(0.1 -0.1)\">\r\n       <use xlink:href=\"#DejaVuSans-32\"/>\r\n       <use x=\"63.623047\" xlink:href=\"#DejaVuSans-30\"/>\r\n       <use x=\"127.246094\" xlink:href=\"#DejaVuSans-32\"/>\r\n       <use x=\"190.869141\" xlink:href=\"#DejaVuSans-30\"/>\r\n       <use x=\"254.492188\" xlink:href=\"#DejaVuSans-2e\"/>\r\n       <use x=\"286.279297\" xlink:href=\"#DejaVuSans-30\"/>\r\n      </g>\r\n     </g>\r\n    </g>\r\n    <g id=\"text_9\">\r\n     <!-- year -->\r\n     <g transform=\"translate(196.847656 252.916562)scale(0.1 -0.1)\">\r\n      <defs>\r\n       <path d=\"M 2059 -325 \r\nQ 1816 -950 1584 -1140 \r\nQ 1353 -1331 966 -1331 \r\nL 506 -1331 \r\nL 506 -850 \r\nL 844 -850 \r\nQ 1081 -850 1212 -737 \r\nQ 1344 -625 1503 -206 \r\nL 1606 56 \r\nL 191 3500 \r\nL 800 3500 \r\nL 1894 763 \r\nL 2988 3500 \r\nL 3597 3500 \r\nL 2059 -325 \r\nz\r\n\" id=\"DejaVuSans-79\" transform=\"scale(0.015625)\"/>\r\n       <path d=\"M 3597 1894 \r\nL 3597 1613 \r\nL 953 1613 \r\nQ 991 1019 1311 708 \r\nQ 1631 397 2203 397 \r\nQ 2534 397 2845 478 \r\nQ 3156 559 3463 722 \r\nL 3463 178 \r\nQ 3153 47 2828 -22 \r\nQ 2503 -91 2169 -91 \r\nQ 1331 -91 842 396 \r\nQ 353 884 353 1716 \r\nQ 353 2575 817 3079 \r\nQ 1281 3584 2069 3584 \r\nQ 2775 3584 3186 3129 \r\nQ 3597 2675 3597 1894 \r\nz\r\nM 3022 2063 \r\nQ 3016 2534 2758 2815 \r\nQ 2500 3097 2075 3097 \r\nQ 1594 3097 1305 2825 \r\nQ 1016 2553 972 2059 \r\nL 3022 2063 \r\nz\r\n\" id=\"DejaVuSans-65\" transform=\"scale(0.015625)\"/>\r\n       <path d=\"M 2194 1759 \r\nQ 1497 1759 1228 1600 \r\nQ 959 1441 959 1056 \r\nQ 959 750 1161 570 \r\nQ 1363 391 1709 391 \r\nQ 2188 391 2477 730 \r\nQ 2766 1069 2766 1631 \r\nL 2766 1759 \r\nL 2194 1759 \r\nz\r\nM 3341 1997 \r\nL 3341 0 \r\nL 2766 0 \r\nL 2766 531 \r\nQ 2569 213 2275 61 \r\nQ 1981 -91 1556 -91 \r\nQ 1019 -91 701 211 \r\nQ 384 513 384 1019 \r\nQ 384 1609 779 1909 \r\nQ 1175 2209 1959 2209 \r\nL 2766 2209 \r\nL 2766 2266 \r\nQ 2766 2663 2505 2880 \r\nQ 2244 3097 1772 3097 \r\nQ 1472 3097 1187 3025 \r\nQ 903 2953 641 2809 \r\nL 641 3341 \r\nQ 956 3463 1253 3523 \r\nQ 1550 3584 1831 3584 \r\nQ 2591 3584 2966 3190 \r\nQ 3341 2797 3341 1997 \r\nz\r\n\" id=\"DejaVuSans-61\" transform=\"scale(0.015625)\"/>\r\n       <path d=\"M 2631 2963 \r\nQ 2534 3019 2420 3045 \r\nQ 2306 3072 2169 3072 \r\nQ 1681 3072 1420 2755 \r\nQ 1159 2438 1159 1844 \r\nL 1159 0 \r\nL 581 0 \r\nL 581 3500 \r\nL 1159 3500 \r\nL 1159 2956 \r\nQ 1341 3275 1631 3429 \r\nQ 1922 3584 2338 3584 \r\nQ 2397 3584 2469 3576 \r\nQ 2541 3569 2628 3553 \r\nL 2631 2963 \r\nz\r\n\" id=\"DejaVuSans-72\" transform=\"scale(0.015625)\"/>\r\n      </defs>\r\n      <use xlink:href=\"#DejaVuSans-79\"/>\r\n      <use x=\"59.179688\" xlink:href=\"#DejaVuSans-65\"/>\r\n      <use x=\"120.703125\" xlink:href=\"#DejaVuSans-61\"/>\r\n      <use x=\"181.982422\" xlink:href=\"#DejaVuSans-72\"/>\r\n     </g>\r\n    </g>\r\n   </g>\r\n   <g id=\"matplotlib.axis_2\">\r\n    <g id=\"ytick_1\">\r\n     <g id=\"line2d_9\">\r\n      <defs>\r\n       <path d=\"M 0 0 \r\nL -3.5 0 \r\n\" id=\"m6c6ba5542c\" style=\"stroke:#000000;stroke-width:0.8;\"/>\r\n      </defs>\r\n      <g>\r\n       <use style=\"stroke:#000000;stroke-width:0.8;\" x=\"40.603125\" xlink:href=\"#m6c6ba5542c\" y=\"222.992727\"/>\r\n      </g>\r\n     </g>\r\n     <g id=\"text_10\">\r\n      <!-- 0 -->\r\n      <g transform=\"translate(27.240625 226.791946)scale(0.1 -0.1)\">\r\n       <use xlink:href=\"#DejaVuSans-30\"/>\r\n      </g>\r\n     </g>\r\n    </g>\r\n    <g id=\"ytick_2\">\r\n     <g id=\"line2d_10\">\r\n      <g>\r\n       <use style=\"stroke:#000000;stroke-width:0.8;\" x=\"40.603125\" xlink:href=\"#m6c6ba5542c\" y=\"181.810909\"/>\r\n      </g>\r\n     </g>\r\n     <g id=\"text_11\">\r\n      <!-- 5 -->\r\n      <g transform=\"translate(27.240625 185.610128)scale(0.1 -0.1)\">\r\n       <use xlink:href=\"#DejaVuSans-35\"/>\r\n      </g>\r\n     </g>\r\n    </g>\r\n    <g id=\"ytick_3\">\r\n     <g id=\"line2d_11\">\r\n      <g>\r\n       <use style=\"stroke:#000000;stroke-width:0.8;\" x=\"40.603125\" xlink:href=\"#m6c6ba5542c\" y=\"140.629091\"/>\r\n      </g>\r\n     </g>\r\n     <g id=\"text_12\">\r\n      <!-- 10 -->\r\n      <g transform=\"translate(20.878125 144.42831)scale(0.1 -0.1)\">\r\n       <use xlink:href=\"#DejaVuSans-31\"/>\r\n       <use x=\"63.623047\" xlink:href=\"#DejaVuSans-30\"/>\r\n      </g>\r\n     </g>\r\n    </g>\r\n    <g id=\"ytick_4\">\r\n     <g id=\"line2d_12\">\r\n      <g>\r\n       <use style=\"stroke:#000000;stroke-width:0.8;\" x=\"40.603125\" xlink:href=\"#m6c6ba5542c\" y=\"99.447273\"/>\r\n      </g>\r\n     </g>\r\n     <g id=\"text_13\">\r\n      <!-- 15 -->\r\n      <g transform=\"translate(20.878125 103.246491)scale(0.1 -0.1)\">\r\n       <use xlink:href=\"#DejaVuSans-31\"/>\r\n       <use x=\"63.623047\" xlink:href=\"#DejaVuSans-35\"/>\r\n      </g>\r\n     </g>\r\n    </g>\r\n    <g id=\"ytick_5\">\r\n     <g id=\"line2d_13\">\r\n      <g>\r\n       <use style=\"stroke:#000000;stroke-width:0.8;\" x=\"40.603125\" xlink:href=\"#m6c6ba5542c\" y=\"58.265455\"/>\r\n      </g>\r\n     </g>\r\n     <g id=\"text_14\">\r\n      <!-- 20 -->\r\n      <g transform=\"translate(20.878125 62.064673)scale(0.1 -0.1)\">\r\n       <use xlink:href=\"#DejaVuSans-32\"/>\r\n       <use x=\"63.623047\" xlink:href=\"#DejaVuSans-30\"/>\r\n      </g>\r\n     </g>\r\n    </g>\r\n    <g id=\"ytick_6\">\r\n     <g id=\"line2d_14\">\r\n      <g>\r\n       <use style=\"stroke:#000000;stroke-width:0.8;\" x=\"40.603125\" xlink:href=\"#m6c6ba5542c\" y=\"17.083636\"/>\r\n      </g>\r\n     </g>\r\n     <g id=\"text_15\">\r\n      <!-- 25 -->\r\n      <g transform=\"translate(20.878125 20.882855)scale(0.1 -0.1)\">\r\n       <use xlink:href=\"#DejaVuSans-32\"/>\r\n       <use x=\"63.623047\" xlink:href=\"#DejaVuSans-35\"/>\r\n      </g>\r\n     </g>\r\n    </g>\r\n    <g id=\"text_16\">\r\n     <!-- number -->\r\n     <g transform=\"translate(14.798438 135.434062)rotate(-90)scale(0.1 -0.1)\">\r\n      <defs>\r\n       <path d=\"M 3513 2113 \r\nL 3513 0 \r\nL 2938 0 \r\nL 2938 2094 \r\nQ 2938 2591 2744 2837 \r\nQ 2550 3084 2163 3084 \r\nQ 1697 3084 1428 2787 \r\nQ 1159 2491 1159 1978 \r\nL 1159 0 \r\nL 581 0 \r\nL 581 3500 \r\nL 1159 3500 \r\nL 1159 2956 \r\nQ 1366 3272 1645 3428 \r\nQ 1925 3584 2291 3584 \r\nQ 2894 3584 3203 3211 \r\nQ 3513 2838 3513 2113 \r\nz\r\n\" id=\"DejaVuSans-6e\" transform=\"scale(0.015625)\"/>\r\n       <path d=\"M 544 1381 \r\nL 544 3500 \r\nL 1119 3500 \r\nL 1119 1403 \r\nQ 1119 906 1312 657 \r\nQ 1506 409 1894 409 \r\nQ 2359 409 2629 706 \r\nQ 2900 1003 2900 1516 \r\nL 2900 3500 \r\nL 3475 3500 \r\nL 3475 0 \r\nL 2900 0 \r\nL 2900 538 \r\nQ 2691 219 2414 64 \r\nQ 2138 -91 1772 -91 \r\nQ 1169 -91 856 284 \r\nQ 544 659 544 1381 \r\nz\r\nM 1991 3584 \r\nL 1991 3584 \r\nz\r\n\" id=\"DejaVuSans-75\" transform=\"scale(0.015625)\"/>\r\n       <path d=\"M 3328 2828 \r\nQ 3544 3216 3844 3400 \r\nQ 4144 3584 4550 3584 \r\nQ 5097 3584 5394 3201 \r\nQ 5691 2819 5691 2113 \r\nL 5691 0 \r\nL 5113 0 \r\nL 5113 2094 \r\nQ 5113 2597 4934 2840 \r\nQ 4756 3084 4391 3084 \r\nQ 3944 3084 3684 2787 \r\nQ 3425 2491 3425 1978 \r\nL 3425 0 \r\nL 2847 0 \r\nL 2847 2094 \r\nQ 2847 2600 2669 2842 \r\nQ 2491 3084 2119 3084 \r\nQ 1678 3084 1418 2786 \r\nQ 1159 2488 1159 1978 \r\nL 1159 0 \r\nL 581 0 \r\nL 581 3500 \r\nL 1159 3500 \r\nL 1159 2956 \r\nQ 1356 3278 1631 3431 \r\nQ 1906 3584 2284 3584 \r\nQ 2666 3584 2933 3390 \r\nQ 3200 3197 3328 2828 \r\nz\r\n\" id=\"DejaVuSans-6d\" transform=\"scale(0.015625)\"/>\r\n       <path d=\"M 3116 1747 \r\nQ 3116 2381 2855 2742 \r\nQ 2594 3103 2138 3103 \r\nQ 1681 3103 1420 2742 \r\nQ 1159 2381 1159 1747 \r\nQ 1159 1113 1420 752 \r\nQ 1681 391 2138 391 \r\nQ 2594 391 2855 752 \r\nQ 3116 1113 3116 1747 \r\nz\r\nM 1159 2969 \r\nQ 1341 3281 1617 3432 \r\nQ 1894 3584 2278 3584 \r\nQ 2916 3584 3314 3078 \r\nQ 3713 2572 3713 1747 \r\nQ 3713 922 3314 415 \r\nQ 2916 -91 2278 -91 \r\nQ 1894 -91 1617 61 \r\nQ 1341 213 1159 525 \r\nL 1159 0 \r\nL 581 0 \r\nL 581 4863 \r\nL 1159 4863 \r\nL 1159 2969 \r\nz\r\n\" id=\"DejaVuSans-62\" transform=\"scale(0.015625)\"/>\r\n      </defs>\r\n      <use xlink:href=\"#DejaVuSans-6e\"/>\r\n      <use x=\"63.378906\" xlink:href=\"#DejaVuSans-75\"/>\r\n      <use x=\"126.757812\" xlink:href=\"#DejaVuSans-6d\"/>\r\n      <use x=\"224.169922\" xlink:href=\"#DejaVuSans-62\"/>\r\n      <use x=\"287.646484\" xlink:href=\"#DejaVuSans-65\"/>\r\n      <use x=\"349.169922\" xlink:href=\"#DejaVuSans-72\"/>\r\n     </g>\r\n    </g>\r\n   </g>\r\n   <g id=\"line2d_15\">\r\n    <path clip-path=\"url(#p661d7599c6)\" d=\"M 55.821307 214.756364 \r\nL 71.840446 214.756364 \r\nL 135.917001 214.756364 \r\nL 199.993556 214.756364 \r\nL 248.050972 206.52 \r\nL 264.070111 206.52 \r\nL 280.089249 148.865455 \r\nL 296.108388 132.392727 \r\nL 312.127527 17.083636 \r\nL 328.146666 115.92 \r\nL 344.165804 33.556364 \r\nL 360.184943 198.283636 \r\n\" style=\"fill:none;stroke:#1f77b4;stroke-linecap:square;stroke-width:1.5;\"/>\r\n   </g>\r\n   <g id=\"patch_3\">\r\n    <path d=\"M 40.603125 224.64 \r\nL 40.603125 7.2 \r\n\" style=\"fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;\"/>\r\n   </g>\r\n   <g id=\"patch_4\">\r\n    <path d=\"M 375.403125 224.64 \r\nL 375.403125 7.2 \r\n\" style=\"fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;\"/>\r\n   </g>\r\n   <g id=\"patch_5\">\r\n    <path d=\"M 40.603125 224.64 \r\nL 375.403125 224.64 \r\n\" style=\"fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;\"/>\r\n   </g>\r\n   <g id=\"patch_6\">\r\n    <path d=\"M 40.603125 7.2 \r\nL 375.403125 7.2 \r\n\" style=\"fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;\"/>\r\n   </g>\r\n  </g>\r\n </g>\r\n <defs>\r\n  <clipPath id=\"p661d7599c6\">\r\n   <rect height=\"217.44\" width=\"334.8\" x=\"40.603125\" y=\"7.2\"/>\r\n  </clipPath>\r\n </defs>\r\n</svg>\r\n",
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAYEAAAEGCAYAAACD7ClEAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjQuMSwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy/Z1A+gAAAACXBIWXMAAAsTAAALEwEAmpwYAAAlbUlEQVR4nO3deXRkZ3nn8e9TWkpLlXqRqtSLe7Fbahu3MV6aHkwcGwaSAZKwDEmwScAQgsMEJnAmmRMyOTNhyMnJCslkOUkc7MQhQDgJhjgZCHgcxx2CIW47XtReerGltqXu1tattbWV3vnj3quullVSSVX31vb7nKPTtenex1fleupdH3POISIitSlW6gBERKR0lARERGqYkoCISA1TEhARqWFKAiIiNay+1AHko6Ojw+3du7fUYYiIVJTHHnts2DmXWu01FZEE9u7dy5EjR0odhohIRTGzvrVeo+4gEZEapiQgIlLDlARERGqYkoCISA1TEhARqWGhJQEz22VmD5nZM2Z21Mw+7j/+KTPrN7Mn/J+3hRWDiIisLswpogvAzzvnHjezJPCYmT3gP/e7zrnfCfHcIiKSh9BaAs650865x/3bE8CzwM6wzicikm1uYZEvP3qKzKK2y19NJGMCZrYXuB74nv/Qx8zsKTO7x8y25PidO83siJkdGRoaiiJMEaki//TcIL/4laf51xPDpQ6lrIWeBMwsAXwF+IRzbhz4Y2AfcB1wGvjMSr/nnLvLOXfQOXcwlVp11bOIyCv0jkwBcHxwssSRlLdQk4CZNeAlgC845+4DcM6ddc5lnHOLwJ8Bh8KMQURqU5+fBE4oCawqzNlBBtwNPOuc+2zW49uzXvYuoCesGESkdvWNTANwYnCixJGUtzBnB30f8D7gaTN7wn/sfwC3m9l1gAN6gZ8JMQYRqVFBEjg+OIlzDu97qSwXWhJwzn0bWOmqfz2sc4qIAMwuZBgYu8DmlgbOT88zMjVHRyJe6rDKklYMi0jVeWn0As7BG69MAxoXWI2SgIhUnVOj3qDwm17lJQHNEMpNSUBEqk7vsDce8Lor2mltrOOkkkBOSgIiUnX6RqZIxOtpb22kK53guGYI5aQkICJVp290mj3tLZgZXemkxgRWoSQgIlWnb8RLAgBd6QRnx2cZn5kvcVTlSUlARKrKQmaRl89Ns6e9FYDudALQDKFclAREpKqcHpthPuPYs/ViSwDgxFklgZUoCYhIVQlWCgctgV1bW2isj3FiSElgJUoCIlJVgt1D93Z4LYG6mHFFRyvHz2qG0EqUBESkqpwanaaxPkZnsmnpse7OZOQtgReGJrnhVx/gZJm3QJQERKSq9A5PsWdrC7HYxa3LulIJXj53gQtzmcji+M7JEUan5nhmYDyyc26EkoCIVJXs6aGB7s4EzhHpt/Kj/of/4MRsZOfcCCUBEakazjn6RqeWBoUDXSWYJnp0YAyAwYmZyM65EUoCIlI1BidmmZlffEVLYG97K3UxiywJzGcWee60NxA9NK6WgIhIJJZPDw001sfY094S2R5Cx89OMpdZBNQdJCISmWB6aLBQLFt3OhFZS6DH7wrqTifUHSQiEpVTI9PUxYydW5pf8VxXOkHvyDRzC4uhx/HMwDitjXW89vKtagmIiESld2SKy7Y001D3yo+27nSSzKKjz28thKmnf4yrd7Sxra2J89PzzC5ENzV1vZQERKRq9I1Ms3uFriC4OEMo7CpjmUXHM6fHObBjE+mkV9d4eHIu1HMWQklARKqCc47ekSn2LhsUDuxLJTALf5roi8NTTM9luGbnJtJtXhIYHC/fcYH6UgcgIlIM56fnmZhZeMX00EBzYx07NzeH3hII1gcc2NFGZtEB5T1DSElARKpC3+jK00OzRTFD6OjAOI31MbrSCc5Ned1A5ZwE1B0kIlUhGPDN1RIAb1zg5NDk0jf0MPT0j/GqbUka6mK0J+LEDIbKuDtISUBEqkKwUCzXwDB4M4TmFrzKY2FwztHTP8aBnZsAbxvr9kRcLQERkbD1jkyxfVMTTQ11OV+zL5ghFFKVsZfPXWB8ZoEDO9qWHksnlQREREJ3apXpoYGljeRC2k20p98bFL5mx6alx7wkoO4gEZFQ9Y5M55weGtjU3EA6GQ+tJXB0YJy6mHHltuTSY6lknMEy3kROSUBEKt7k7ALDk7PsXmVQONDdmQivJTAwRnc6cUmXVDrZxPDkbKiD0YVQEhCRinfKHxReqyUAXpWxk4OTOFfcD+VgUPianZsueTzdFmfRwehUea4aVhIQkYqXz/TQQFdnksnZBc4Uedrm4MQsw5NzlwwKA0tbR5TruICSgIhUvGChWD7dQV2pcGYIBSuFl7cEUn7B+3KdIRRaEjCzXWb2kJk9Y2ZHzezj/uNbzewBMzvu/7slrBhEpDb0jUyxtbWRtqaGNV/b3RlOqcme/nHM4FXbV24JlGuFsTBbAgvAzzvnrgZeB3zUzK4GPgk86JzrBh7074uIbNhKxeVzaW9tZHNLQ9H3EOrpH+PyjlYS8Ut340nVaneQc+60c+5x//YE8CywE3gHcK//snuBd4YVg4jUhr48pocGzIzutDc4XExHB8YvWR8QaGqoY1NzQ+11B2Uzs73A9cD3gE7n3Gn/qTNAZ47fudPMjpjZkaGhoSjCFJEKNLuQYWDswpoLxbJ1pRNFrTd8bmqO/vMXXjEoHEiX8VqB0JOAmSWArwCfcM6NZz/nvDlaK87Tcs7d5Zw76Jw7mEqlwg5TRCrUS6MXcA72duSfBPalEpybnmdksjgfzEcHvI+25YPCgVQZrxoONQmYWQNeAviCc+4+/+GzZrbdf347MBhmDCJS3YLpobu35tcdBNDd6a3oLda4QE9WDYGVlPP+QWHODjLgbuBZ59xns566H7jDv30H8HdhxSAi1a9vaaHY+rqDoHgzhHr6x7hsSzObWxpXfD7d1sTgxGzRF6gVQ5gtge8D3gf8RzN7wv95G/AbwA+Y2XHgzf59EZEN6RuZIhGvZ2vryh/AK9mxqYnWxrqiJYFcg8KBdDLO3MIi4zMLRTlfMYVWWcw5923Acjz9prDOKyK1pW/Umx7qdT7kx8zYV6QqYxMz87w4PMV/vn5nztcE00SHJmbY1Lz2WoYoacWwiFS09UwPzVasGULPnvaOkWtQGLxN5ICynCGkJCAiFWsh41UJy2e7iOW60gnOjs8yPjNfUAxBDYEDO1ceFAZvEzkoz60jlAREpGKdHpthPuPWNSgc6E57M4QK7RLqGRgjnYwvfdtfSTlvIqckICIVq3cD00MDxZohdLR/POfU0EAiXk9zQ526g0REimlpeug6FooFdm1pprE+VlASmJnPcGJoctXxAPAGotNt5blWQElARCpW38gUjfUxOlfpismlvi7GFR2tBSWB585MkFl0HFhlemgglSjPVcNKAiJSsfpGptmztYVYLP/podkKnSG0VFh+lUHhgFoCIiJFtp4tpFfSlU7w8rkLXJjLbOj3jw6MsbmlgZ2bm9d8bTrZxJCSgIhIcTjn6BudYs8G1ggEutNJnIOTGyw83+MPCuezUC2VjDMxs8DM/MYSTliUBESkIg1OzDIzv7ih6aGBYIbQRpLAfGaR589MrLpdRLalaaJlNkNISUBEKlLvsD89tICWwN6OFupitqF6w8fPTjKXWeTAGjODAum2oNZweQ0OKwmISEUKissX0hKI19exZ2vLhmYIBdtHX7PGGoHAxQVjagmIiBSsb2SKupixI49B2dVsdIbQ0f4xWhvr8t636GJ3kFoCIiIF6xuZ5rItzTTUFfYx1pVO0DcyzdzC4rp+r2dgnKt3tOU9PXVLSyP1MVNLQESkGPpGptdVVziX7s4EC4tuqUJZPjKLjmdPj+e1SCwQi5lfZlJJQESkIM45ekemNrSF9HJdqfVvJPfi8BTTc5k1t4tYTklARKQIzk/PMzGzUNBCscC+tJdI1lNv+OhA/iuFs6WTcY0JiIgUKpgZVMhCsUBLYz07NzevqyXQ0z9GvD5GVyqxrnOlkk0MT6olICJSkKD/vpDpodm6OxPragn09I9z1bYk9esclE4n44xMzbGQWd8gdJiUBESk4vQOey2BXUUYGAboSiV4YWiSzKJb87XOOY4OjOW9SCxbui2OczA8ObeRMEOhJCAiFadvdIrtm5poaqgryvG6OxPMLnilKtfy8rkLjM8s5L1dRLalWsNltGpYSUBEKk6xpocG1lNlbD3bRy9XjvsHKQmISMXpG5kuyvTQQDBNNJ9xgZ6BMepjxv7O5LrPU44F55UERKSiTM4uMDw5y+4iDQoDbGppIJWM59kSGKcrndhQV1RHovwKzisJiEhFORXUFS5iSwCgO732DKFgUHi9i8QCDXUxtrY2qiUgIrJRwfTQYiwUy9aVTnBycBLncs8QGpyYZXhyLu+dQ1fiLRhTEhAR2ZDekWChWHGTQHc6weTsAmdWWdF7cVB4Yy0B8LaOGFJ3kIjIxpwanaK9tZFkU0NRj7svjxlCPf3jmMGrthfSEiivWsNKAiJSUXqHp4s6KBzoTvszhFapMnZ0YIzLO1ppjddv+DzptjhDk7OrdjtFSUlARCrKqdHiTg8NdCQa2dTcwIlV6g0fHRjf0CKxbOlknPmM49z0fEHHKRYlARGpGLMLGQbGLhR1oVjAzOhOJziRoyUwOjVH//kLG1oklq3cVg0rCYhIxXhp9ALOeQXiw9CVTuRsCSxtH11oS6CtvFYNh5YEzOweMxs0s56sxz5lZv1m9oT/87awzi8i1SeYHrp7a/G7g8BLAqNTc4yssN1zT/84AFcXMD0Uyq/gfJgtgb8A3rLC47/rnLvO//l6iOcXkSrTt7RQLLyWAKw8Q+jowBiXbWlmc0tjQedIJctr1XBoScA5dxgYDev4IlJ7+kamSMbr2dpa2AdxLt2dufcQKsagMHhFbBLx+srpDjKzOjN7qIjn/JiZPeV3F20p4nFFpMr1jnjTQ80slOPv2NRES2PdK1oCEzPzvDg8VfCgcCCdjJfNWoE1k4BzLgMsmlnhKRD+GNgHXAecBj6T64VmdqeZHTGzI0NDQ0U4tYhUurCmhwbMzBscXpYEnhnwxgM2UkhmJV7B+crqDpoEnjazu83s94Of9Z7MOXfWOZdxzi0CfwYcWuW1dznnDjrnDqZSqfWeSkSqzEJmkZdGw1kolq0r9cok0BMkgQIHhQPptvJZNZzvsrf7/J+CmNl259xp/+67gJ7VXi8iEjg9NsPCogttUDjQ1Zngvn/vZ3xmnjZ/a4qjA2Okk/GlOf6FSifjZTM7KK8k4Jy718yagd3Ouefz+R0z+xLwBqDDzF4GfgV4g5ldBzigF/iZDcQsIjWoN+TpoYGulDdD6OTgJNfv9oYtj/aPF7Rp3HLpZJzpuQyTswskCtiCohjyOruZ/QjwO0AjcLn/Qf5p59zbc/2Oc+72FR6+eyNBiogsTQ8NaaFYIHuG0PW7t3BhLsPxwQn+04HOop3j4oKxGRJ+0imVfMcEPoXXf38ewDn3BHBFKBGJiKygb2SKeH2MziJ1yeSya0szjXUxTvrjAs+dGWfRFW9QGLK3jih9l1C+SWDeOTe27LHFYgcjIpJLr19cPhYLZ3pooL4uxhWp1qW1AkeLPCgM5bVqON8kcNTM3gvUmVm3mf0B8J0Q4xIRucSpkWn2hDg9NNu+rGmiRwfG2NzSwM7NzUU7/lJLYJUCNlHJNwn8V+AAMAt8CRgHPhFSTCIil3DO0Tc6VfRqYrl0pxO8dG6amfkMPf3eSuFiLlBra66nsT5WFtNE850dNA38spn9pnfXTYQblojIRYMTs8zML4Y+PTTQlU7gHDx3ZoLnz0zwwZv3FvX4ZkYqUR7TRPNqCZjZa83saeApvEVjT5rZjeGGJiLi6R32p4dG1B0UVBn7Rs9p5jKLHCjCnkHLpdvKY9Vwvt1BdwM/65zb65zbC3wU+PPQohIRydI3Gu7uocvt7WghZnD/EwMAXFPEQeFAuewflG8SyDjn/iW445z7NrAQTkgiIpfqG5miLmbsKOLg7Gri9XXsbW/l9NgMrY11oexXlE42lUV30KpjAmZ2g3/zYTP7U7xBYQe8B/jncEMTEfH0jUxz2ZZmGuqiK4a4L53gheEpDuzYFMq01HQyzvnpeWYXMsTr64p+/HytNTC8fJfPX8m67Yoci4jIivoinB4a6E4neOCZsxwo0vbRywWrhocmZrlsSzTdXCtZNQk4594YVSAiIitxztE7MsV1uzZHet6gylgYg8Jw6arhsk0CATPbDLwf2Jv9O865nwslKhER3/npeSZmFiJbIxC4uauDW/enuGV/RyjHXyozWeIKY/luX/d14LvA02i7CBGJULB7aNTdQem2Ju79qZwlTwo/fjLoDirtNNF8k0CTc+6/hRqJiMgKTkU8PTQq7Yk4MSv9/kH5DrV/3sw+bGbbzWxr8BNqZCIiQO+wlwR2ba2uJFAXM9oT8YrpDpoDfhv4ZS7OCnJoO2kRCVnf6BTbNzXR1FC6aZRhSZdBreF8k8DPA13OueEwgxERWc6bHlpdrYBAOhlnaLIyuoNOANNhBiIispK+kSn2hFxSslTSyaaK6Q6aAp4ws4fwtpMGNEVURMI1ObvA8OQce0IuKVkq6bY4w5OzZBYddSEXy8kl3yTwNf9HRCQyfcH00KptCcRZdDAyNbu0eCxq+dYTuDfsQEREljvlF5ev1jGB1FKFsTJPAmb2IivsFeSc0+wgEQlNb5Ungez9g0ol3+6gg1m3m4AfA7ROQERCdWp0ivbWRpJNDaUOJRSpRFBwvnTTRPOaHeScG8n66XfO/R7wQ+GGJiK1rnd4mt1V2gqA8tg/KN/uoBuy7sbwWgb5tiJERDbk1Og0hy6v3k6HpoY6NjU3lHTriHw/yD/DxTGBBaAXr0tIRCQUM/MZBsYuVO14QKDUZSbzTQJvBd7NpVtJ3wZ8OoSYRER4+dw0zlXvoHCg1AXn810x/DXgR4B5YNL/mQopJhGpcc45vvi9lwDoSiVLHE24Sl1rON+WwGXOubeEGomIiO8z3zrGPf/6Iu+/aQ/XhFTesVx4m8jN4pzDLPpVw/m2BL5jZq8ONRIREeD3HzzOHz50gtsP7eJTP3KgJB+MUUol48wtLDJ+YaEk58+3JXAz8AF/0dgsYIBzzl0bWmQiUnP+5OGTfPaBY7z7hsv4tXe+mliJ9tOJUrotqDU8w6aW6NdDrGdgWEQkNHd/+0V+4xvP8fbX7OC3fvTamkgAcLHM5ODELN2d0Y9/5Lt3UF/YgYhI7fr8d/v41X94hrdes43P/vhrSrajZiksLRgr0QyhfMcE1s3M7jGzQTPryXpsq5k9YGbH/X+3hHV+EakMX370FP/zaz28+VVp/s9t11NfF9rHUllKl3jVcJhX+y+A5TOKPgk86JzrBh7074tIjbrv8Zf55H1Pc8v+FH/0EzfQWF9bCQAgEa+nuaGuZNNEQ7vizrnDwOiyh98BBNtS3wu8M6zzi0h5+4enBviFv3mSm65o56733Ui8vvpqCOfDzEi3lW7VcNRpt9M5d9q/fQbozPVCM7vTzI6Y2ZGhoaFoohORSHzz6Bk+/tdPcHDPVj53x8GqLCK/HqUsOF+ytpdzzrFCjYKs5+9yzh10zh1MpVIRRiYiYfqn587ysS8+zrWXbeKeD76WlkbtRVnKVcNRJ4GzZrYdwP93MOLzi0gJHT42xEf+6nGu2tbGX3zwEIm4EgB4M4SGqnBgeCX3A3f4t+8A/i7i84tIiTxycoQP/+UR9qUSfP5Dh9jUXJ2FYjYi3RZnYnaBC3OZyM8d5hTRLwGPAFea2ctm9iHgN4AfMLPjwJv9+yJS5Y70jvKhex9lT3sLf/WhQ2xuaSx1SGUlqC9cinGB0Npizrnbczz1prDOKSLl599PneMDf/4o29qa+Kuf/g+0+yUV5aJU1qrhPe2tkZ679iblikhkevrHeP89/0Z7opEvfvh1S9945VKlXDCmJCAioXhpdJqfvPt7tDU18MUPv45tm5QAckmXcOsIDc2LSCjuf3KA89Pz3PdfXs/Ozc2lDqesbWlppD5mJZkmqpaAiITi4WNDHNjRxhWpRKlDKXuxmHnTRJUERKQaTMzM83jfOW7Zr4We+QoqjEVNSUBEiu6RkyMsLDpu6VYSyFcq2cTgePRjAkoCIlJ0Dx8borWxjhv3aLf4fJVqEzklAREpKucch48PcdO+9prcGnqj0sk4I1NzzGcWIz2v/kIiUlS9I9O8NHpB4wHrFKyhGJ6MtjWgJCAiRXX4mLf1u8YD1idVogVjSgIiUlSHjw2xp72FvR3Rbn9Q6bILzkdJSUBEimZuYZFHXhhRK2AD0m2lWTWsJCAiRXOkb5TpuYzGAzagIxHHTN1BIlLBDh8bpj5m3LSvvdShVJyGuhhbWxoZ0sCwiFSqh48NceOeLaoYtkGpZFwtARGpTIMTMzx7elxdQQVItzUxpDEBEalE/3JsGIBblQQ2rBT7BykJiEhRHD4+RHtrI1dvbyt1KBUr7e8kurjoIjunkoCIFGxx0fEvx4e5ZX+KWMxKHU7FSifjLCw6zk3PRXZOJQERKdjRgXFGp+a4ZX9HqUOpaKmlgvPRdQkpCYhIwQ4f97aK+H4tEivIxQVjSgIiUkEeft6rItaRiJc6lIp2seB8dDOElAREpCATM/M8fkpVxIohre4gEak031EVsaJpbqwjGa+PtLiMkoCIFOSwqogVVSriCmNKAiKyYReriHWoiliReAvGNCYgIhUgqCJ2q6aGFk062aQxARGpDEtVxDQoXDRpfxM556JZNawkICIbFlQR29OuKmLFkkrGuTCfYXJ2IZLzKQmIyIbMLmT4zklVESu2qBeMKQmIyIY81nuOC/OqIlZsS2sFIqoroCQgIhvy8PEhVRELwcWC89HMECpJ+R8z6wUmgAyw4Jw7WIo4RGTjDh8bVhWxEAQtgajWCpSyJfBG59x1SgAilSeoInbrleoKKra25noa62M1kQREpEIFVcQ0KFx8ZhZphbFSJQEHfMvMHjOzO1d6gZndaWZHzOzI0NBQxOGJyGoOHx+iI6EqYmGJctVwqZLAzc65G4C3Ah81s1uWv8A5d5dz7qBz7mAqpW8bIuUiqCL2/d2qIhaWdLKpumcHOef6/X8Hga8Ch0oRh4isX8/AmKqIhSzdVsXdQWbWambJ4Dbwg0BP1HGIyMYEW0Woilh4Uok4YxfmmZnPhH6uUszt6gS+ambB+b/onPvHEsQhIhtw+NiwqoiFLFg1PDQxy66tLaGeK/Ik4Jx7AXhN1OcVkcIFVcTuvOWKUodS1bIrjIWdBDRFVETytlRFTFtFhCqVDFoC4c8QUhIQkbwFVcRu2K0qYmHK7g4Km5KAiOTFOcfDx1RFLArtrXFiFs1OovpLikheXhye4uVzqiIWhbqY0ZGIR7JWQElARPKiKmLR8tYKaExARMrE4ePDqiIWoahqDSsJiMiaZhcyPHJyhFvVCohMVJvIKQmIyJqWqohplXBkUsk4I5OzZBbDLTivJCAia3r4+BANdaoiFqV0Ms6ig5HJcFsDSgIisqagilirqohFJpW1ajhMSgIisqrBca+KmGYFRStYMBb2DCGldRFZ1eHjqiJWCldtS/L3H7uZK1LhzsZSEhCRVR0+pipipdDSWM+rL9sU+nnUHSQiOS0uOr59QlXEqpmSgIjkFFQR0/qA6qUkICI5BVtF3Nyt/YKqlZKAiOR0+Ngw1+xUFbFqpoFhkSrlnGN8ZgHnNrbidHouoypiNUBJQKQKnJua49jZCY6dneD5sxMcOzPJ82cnGLswX/CxNR5Q3ZQERCrI5OwCx4MP+zOTSx/62RWokk31XNmZ5Ieu3c7l7a3U1218Vs+m5gYOXb61GKFLmVISEClDM/MZTg5N+t/uJzl2xvuwf/nchaXXNDXE2N+Z5Nb9Ka7sTLJ/W5IrO5N0tsUx03ROyY+SgEgJLWQW6R2Z9r/ZX+zO6R2eItg8sqHO2JdKcMPuLdx+aDf7O5Ps70ywa0uL5u5LwZQERCKwuOjoP3+B5/1v9MGH/gtDU8xlFgGIGextb2V/Z5IffvX2pW/2eztaaajTRD4Jh5KASBE55xicmL34rf7MBMcGJzl+doLpuczS63ZubmZ/Z4Jbr/S7cjqTdKUTNDXUlTB6qUVKAiIblM+MnI5EnCu3JXjPa3ct9dt3pxMkmxpKGLnIRUoCImvId0bOVduS/PC12/0+e6/fvl2LrKTMVXUS+IMHj3P/kwOlDkMq2PRchv7zmpEj1auqk0AqGae7M1HqMKSCxevr6EonNCNHqlZVJ4HbDu3mtkO7Sx2GiEjZ0rwzEZEapiQgIlLDlARERGpYSZKAmb3FzJ43sxNm9slSxCAiIiVIAmZWB/wR8FbgauB2M7s66jhERKQ0LYFDwAnn3AvOuTngr4F3lCAOEZGaV4oksBN4Kev+y/5jlzCzO83siJkdGRoaiiw4EZFaUrYDw865u5xzB51zB1MpVTYSEQlDKRaL9QO7su5f5j+W02OPPTZsZn2hRrVxHcBwqYNYheIrjOIrjOIrXCEx7lnrBbbRItQbZWb1wDHgTXgf/o8C73XOHY00kCIxsyPOuYOljiMXxVcYxVcYxVe4sGOMvCXgnFsws48B3wTqgHsqNQGIiFS6kuwd5Jz7OvD1UpxbREQuKtuB4QpyV6kDWIPiK4ziK4ziK1yoMUY+JiAiIuVDLQERkRqmJCAiUsucczX9g7dm4SHgGeAo8HH/8a3AA8Bx/98t/uMG/D5wAngKuMF//DrgEf8YTwHvyXG+DwBDwBP+z09HEZ//XCbrvPfnOF8c+LL/+98D9kZ0/d6YFdsTwAzwzhJcv6v8v+Ms8AvLjvUW4Hk/9k+W6PqtGF+u46xwvjcAY1nX739FeP16gaf98x7Jcb6c79+Qr9+Vy95/48AnSnD9fsL/734a+A7wmjDff845JQFgOxc/iJJ4axiuBn4ruNDAJ4Hf9G+/DfiG/2Z9HfA9//H9QLd/ewdwGti8wvk+APxh1PH5z03mcb6fBf7Ev30b8OWo4ss65lZgFGgpwfVLA68Ffo1LPyTqgJPAFUAj8CRwdQmuX674VjzOCud7A/APUV8//7leoGON8635/ggrvmV/6zPAnhJcv9dzMSG8lYufL6G8/5xTEljpj/Z3wA/gZdztWX/I5/3bfwrcnvX6pdctO86T+Elh2eMfYB0fYsWMj/ySwDeBm/zb9XgrFS3K6wfcCXwhx/FDvX5Zr/sUl37I3gR8M+v+LwG/FPX1yxVfruOs8PgbWMeHWDHjI78kkNf/X2FeP+AHgX/N8Vwk189/fAvQH/b7T2MCWcxsL3A9XjOq0zl32n/qDNDp315zAzwzO4SXrU/mONW7zewpM/tbM9uV4zVhxNfkb8r3XTN7Z47TLP2+c24Br+nbHlF8gduAL61yqjCvXy55bXxI+NdvvcdZyU1m9qSZfcPMDmzwuBuJzwHfMrPHzOzOHK/J9zqHEV9grfdfVNfvQ3itIgjx/ack4DOzBPAVvH7A8eznnJdWXZ7H2Q58Hvigc25xhZf8PV4/3bV4fYH3RhjfHuctP38v8Htmti+fc0cYX3D9Xo33jWYlpbx+oSni9ct5HN/jeO+D1wB/AHwtwvhuds7dgNfN8VEzuyWfc0cYH2bWCLwd+JscL4nk+pnZG/GSwC/mc/xCKAkAZtaA9wf6gnPuPv/hs/4HUvDBNOg/nnMDPDNrA/4v8MvOue+udC7n3Ihzbta/+zngxqjic84F/74A/DPet5Llln7f3+dpEzASRXy+Hwe+6pybX+lcEVy/XPLd+DDs67fe41zCOTfunJv0b38daDCzjijiy3r/DQJfxaststy6N5gsVny+twKPO+fO5vhvCP36mdm1eO/tdzjngvdOaO+/mk8CZmbA3cCzzrnPZj11P3CHf/sOvL684PH3m+d1wJhz7rT/DeKrwF865/52lfNtz7r7duDZiOLbYmZx/5gdwPfhzVhYLvu4Pwr8k/9NJdT4sn7vdlZpikdw/XJ5FOg2s8v9v/Vt/jGWC/v6rfc4y1+3zX9t0G0ZY5UPiSLG12pmyeA2Xr97zwovXev9EUp8WdZ6/4V6/cxsN3Af8D7n3LGs14fy/gM0MAzcjNcUe4qL077ehteP9iDeFK7/B2z1X2945TFP4k3jOug//pPAPJdOM7vOf+7TwNv927+ON1XsSbypY1dFFN/r/ftP+v9+KOsc2fE14TWFTwD/BlwRRXz+c3vxvsnElp0jyuu3Da+/dRw4799u8597G97sjpN4rb1SXL8V48t1HP93PgJ8xL/9sazr913g9RHFd4V/zif982dfv+z4cr4/Ivj7tuJ9oG9ado4or9/ngHNZrz2Sdayiv/+cc9o2QkSkltV8d5CISC1TEhARqWFKAiIiNUxJQESkhikJiIjUMCUBEZEapiQgEhEzqyt1DCLLKQmIrMDMPm1mn8i6/2tm9nEz++9m9qh5G9j976znv+ZvjHbUsjZHM7NJM/uMmT2JtxOkSFlREhBZ2T3A+wHMLIa3TP8M0I235811wI1Zm6D9lHPuRuAg8HNmFuzc2Iq3J/xrnHPfjjB+kbzUlzoAkXLknOs1sxEzux5vm99/xytG8oP+bYAEXlI4jPfB/y7/8V3+4yN41dy+EmXsIuuhJCCS2+fwithsw2sZvAn4defcn2a/yMzeALwZr5jHtJn9M94eLgAzzrlMRPGKrJu6g0Ry+ypeXdfX4tU3+CbwU/7e8JjZTjNL423Xe85PAFfhlUUUqQhqCYjk4JybM7OHgPP+t/lvmdmrgEf83YQn8XaP/UfgI2b2LF7ZwBVrSYiUI+0iKpKDPyD8OPBjzrnjpY5HJAzqDhJZgZldjbcn+4NKAFLN1BIQEalhagmIiNQwJQERkRqmJCAiUsOUBEREapiSgIhIDfv/GEzvd0PyvqQAAAAASUVORK5CYII=\n"
     },
     "metadata": {
      "needs_background": "light"
     }
    }
   ],
   "source": [
    "dates = df.disband\n",
    "dates_list = []\n",
    "num = 0\n",
    "for i in dates:\n",
    "  if i !=1:\n",
    "   dates_list.append(i)\n",
    "  num = num+1\n",
    "dates_list=sorted(dates_list)\n",
    "date_data = {age: dates_list.count(age) for age in (dates_list)}\n",
    "score_df = pd.DataFrame.from_dict(data=date_data, orient=\"index\", columns=[\"number\"])\n",
    "score_df['year'] = score_df.index\n",
    "print(score_df)\n",
    "sns.lineplot(data=score_df, x=\"year\", y=\"number\")"
   ]
  },
  {
   "source": [
    "### Сколько живут группы"
   ],
   "cell_type": "markdown",
   "metadata": {}
  },
  {
   "cell_type": "code",
   "execution_count": 88,
   "metadata": {},
   "outputs": [
    {
     "output_type": "stream",
     "name": "stdout",
     "text": [
      "{0: 2, 1: 21, 2: 35, 3: 43, 4: 45, 5: 29, 6: 29, 7: 32, 8: 8, 9: 14, 10: 8, 11: 9, 12: 2, 13: 4, 14: 6, 15: 3, 16: 2, 17: 1, 18: 1, 22: 2, 23: 1, 24: 1, 26: 1}\n"
     ]
    },
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "<AxesSubplot:xlabel='Num', ylabel='Age'>"
      ]
     },
     "metadata": {},
     "execution_count": 88
    },
    {
     "output_type": "display_data",
     "data": {
      "text/plain": "<Figure size 432x288 with 1 Axes>",
      "image/svg+xml": "<?xml version=\"1.0\" encoding=\"utf-8\" standalone=\"no\"?>\r\n<!DOCTYPE svg PUBLIC \"-//W3C//DTD SVG 1.1//EN\"\r\n  \"http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd\">\r\n<svg height=\"262.19625pt\" version=\"1.1\" viewBox=\"0 0 382.603125 262.19625\" width=\"382.603125pt\" xmlns=\"http://www.w3.org/2000/svg\" xmlns:xlink=\"http://www.w3.org/1999/xlink\">\r\n <metadata>\r\n  <rdf:RDF xmlns:cc=\"http://creativecommons.org/ns#\" xmlns:dc=\"http://purl.org/dc/elements/1.1/\" xmlns:rdf=\"http://www.w3.org/1999/02/22-rdf-syntax-ns#\">\r\n   <cc:Work>\r\n    <dc:type rdf:resource=\"http://purl.org/dc/dcmitype/StillImage\"/>\r\n    <dc:date>2021-04-21T14:22:58.377477</dc:date>\r\n    <dc:format>image/svg+xml</dc:format>\r\n    <dc:creator>\r\n     <cc:Agent>\r\n      <dc:title>Matplotlib v3.4.1, https://matplotlib.org/</dc:title>\r\n     </cc:Agent>\r\n    </dc:creator>\r\n   </cc:Work>\r\n  </rdf:RDF>\r\n </metadata>\r\n <defs>\r\n  <style type=\"text/css\">*{stroke-linecap:butt;stroke-linejoin:round;}</style>\r\n </defs>\r\n <g id=\"figure_1\">\r\n  <g id=\"patch_1\">\r\n   <path d=\"M 0 262.19625 \r\nL 382.603125 262.19625 \r\nL 382.603125 0 \r\nL 0 0 \r\nz\r\n\" style=\"fill:none;\"/>\r\n  </g>\r\n  <g id=\"axes_1\">\r\n   <g id=\"patch_2\">\r\n    <path d=\"M 40.603125 224.64 \r\nL 375.403125 224.64 \r\nL 375.403125 7.2 \r\nL 40.603125 7.2 \r\nz\r\n\" style=\"fill:#ffffff;\"/>\r\n   </g>\r\n   <g id=\"patch_3\">\r\n    <path clip-path=\"url(#p672b085371)\" d=\"M 43.393125 224.64 \r\nL 65.713125 224.64 \r\nL 65.713125 128 \r\nL 43.393125 128 \r\nz\r\n\" style=\"fill:#ea96a3;\"/>\r\n   </g>\r\n   <g id=\"patch_4\">\r\n    <path clip-path=\"url(#p672b085371)\" d=\"M 71.293125 224.64 \r\nL 93.613125 224.64 \r\nL 93.613125 63.573333 \r\nL 71.293125 63.573333 \r\nz\r\n\" style=\"fill:#e19153;\"/>\r\n   </g>\r\n   <g id=\"patch_5\">\r\n    <path clip-path=\"url(#p672b085371)\" d=\"M 99.193125 224.64 \r\nL 121.513125 224.64 \r\nL 121.513125 26.758095 \r\nL 99.193125 26.758095 \r\nz\r\n\" style=\"fill:#b89c49;\"/>\r\n   </g>\r\n   <g id=\"patch_6\">\r\n    <path clip-path=\"url(#p672b085371)\" d=\"M 127.093125 224.64 \r\nL 149.413125 224.64 \r\nL 149.413125 17.554286 \r\nL 127.093125 17.554286 \r\nz\r\n\" style=\"fill:#98a246;\"/>\r\n   </g>\r\n   <g id=\"patch_7\">\r\n    <path clip-path=\"url(#p672b085371)\" d=\"M 154.993125 224.64 \r\nL 177.313125 224.64 \r\nL 177.313125 91.184762 \r\nL 154.993125 91.184762 \r\nz\r\n\" style=\"fill:#60ae47;\"/>\r\n   </g>\r\n   <g id=\"patch_8\">\r\n    <path clip-path=\"url(#p672b085371)\" d=\"M 182.893125 224.64 \r\nL 205.213125 224.64 \r\nL 205.213125 91.184762 \r\nL 182.893125 91.184762 \r\nz\r\n\" style=\"fill:#4aae8a;\"/>\r\n   </g>\r\n   <g id=\"patch_9\">\r\n    <path clip-path=\"url(#p672b085371)\" d=\"M 210.793125 224.64 \r\nL 233.113125 224.64 \r\nL 233.113125 77.379048 \r\nL 210.793125 77.379048 \r\nz\r\n\" style=\"fill:#4baba4;\"/>\r\n   </g>\r\n   <g id=\"patch_10\">\r\n    <path clip-path=\"url(#p672b085371)\" d=\"M 238.693125 224.64 \r\nL 261.013125 224.64 \r\nL 261.013125 187.824762 \r\nL 238.693125 187.824762 \r\nz\r\n\" style=\"fill:#4fabbc;\"/>\r\n   </g>\r\n   <g id=\"patch_11\">\r\n    <path clip-path=\"url(#p672b085371)\" d=\"M 266.593125 224.64 \r\nL 288.913125 224.64 \r\nL 288.913125 160.213333 \r\nL 266.593125 160.213333 \r\nz\r\n\" style=\"fill:#6daee2;\"/>\r\n   </g>\r\n   <g id=\"patch_12\">\r\n    <path clip-path=\"url(#p672b085371)\" d=\"M 294.493125 224.64 \r\nL 316.813125 224.64 \r\nL 316.813125 187.824762 \r\nL 294.493125 187.824762 \r\nz\r\n\" style=\"fill:#b6a8eb;\"/>\r\n   </g>\r\n   <g id=\"patch_13\">\r\n    <path clip-path=\"url(#p672b085371)\" d=\"M 322.393125 224.64 \r\nL 344.713125 224.64 \r\nL 344.713125 183.222857 \r\nL 322.393125 183.222857 \r\nz\r\n\" style=\"fill:#df8fe7;\"/>\r\n   </g>\r\n   <g id=\"patch_14\">\r\n    <path clip-path=\"url(#p672b085371)\" d=\"M 350.293125 224.64 \r\nL 372.613125 224.64 \r\nL 372.613125 197.028571 \r\nL 350.293125 197.028571 \r\nz\r\n\" style=\"fill:#e890c6;\"/>\r\n   </g>\r\n   <g id=\"matplotlib.axis_1\">\r\n    <g id=\"xtick_1\">\r\n     <g id=\"line2d_1\">\r\n      <defs>\r\n       <path d=\"M 0 0 \r\nL 0 3.5 \r\n\" id=\"m7b223e7a23\" style=\"stroke:#000000;stroke-width:0.8;\"/>\r\n      </defs>\r\n      <g>\r\n       <use style=\"stroke:#000000;stroke-width:0.8;\" x=\"54.553125\" xlink:href=\"#m7b223e7a23\" y=\"224.64\"/>\r\n      </g>\r\n     </g>\r\n     <g id=\"text_1\">\r\n      <!-- 1 -->\r\n      <g transform=\"translate(51.371875 239.238437)scale(0.1 -0.1)\">\r\n       <defs>\r\n        <path d=\"M 794 531 \r\nL 1825 531 \r\nL 1825 4091 \r\nL 703 3866 \r\nL 703 4441 \r\nL 1819 4666 \r\nL 2450 4666 \r\nL 2450 531 \r\nL 3481 531 \r\nL 3481 0 \r\nL 794 0 \r\nL 794 531 \r\nz\r\n\" id=\"DejaVuSans-31\" transform=\"scale(0.015625)\"/>\r\n       </defs>\r\n       <use xlink:href=\"#DejaVuSans-31\"/>\r\n      </g>\r\n     </g>\r\n    </g>\r\n    <g id=\"xtick_2\">\r\n     <g id=\"line2d_2\">\r\n      <g>\r\n       <use style=\"stroke:#000000;stroke-width:0.8;\" x=\"82.453125\" xlink:href=\"#m7b223e7a23\" y=\"224.64\"/>\r\n      </g>\r\n     </g>\r\n     <g id=\"text_2\">\r\n      <!-- 2 -->\r\n      <g transform=\"translate(79.271875 239.238437)scale(0.1 -0.1)\">\r\n       <defs>\r\n        <path d=\"M 1228 531 \r\nL 3431 531 \r\nL 3431 0 \r\nL 469 0 \r\nL 469 531 \r\nQ 828 903 1448 1529 \r\nQ 2069 2156 2228 2338 \r\nQ 2531 2678 2651 2914 \r\nQ 2772 3150 2772 3378 \r\nQ 2772 3750 2511 3984 \r\nQ 2250 4219 1831 4219 \r\nQ 1534 4219 1204 4116 \r\nQ 875 4013 500 3803 \r\nL 500 4441 \r\nQ 881 4594 1212 4672 \r\nQ 1544 4750 1819 4750 \r\nQ 2544 4750 2975 4387 \r\nQ 3406 4025 3406 3419 \r\nQ 3406 3131 3298 2873 \r\nQ 3191 2616 2906 2266 \r\nQ 2828 2175 2409 1742 \r\nQ 1991 1309 1228 531 \r\nz\r\n\" id=\"DejaVuSans-32\" transform=\"scale(0.015625)\"/>\r\n       </defs>\r\n       <use xlink:href=\"#DejaVuSans-32\"/>\r\n      </g>\r\n     </g>\r\n    </g>\r\n    <g id=\"xtick_3\">\r\n     <g id=\"line2d_3\">\r\n      <g>\r\n       <use style=\"stroke:#000000;stroke-width:0.8;\" x=\"110.353125\" xlink:href=\"#m7b223e7a23\" y=\"224.64\"/>\r\n      </g>\r\n     </g>\r\n     <g id=\"text_3\">\r\n      <!-- 3 -->\r\n      <g transform=\"translate(107.171875 239.238437)scale(0.1 -0.1)\">\r\n       <defs>\r\n        <path d=\"M 2597 2516 \r\nQ 3050 2419 3304 2112 \r\nQ 3559 1806 3559 1356 \r\nQ 3559 666 3084 287 \r\nQ 2609 -91 1734 -91 \r\nQ 1441 -91 1130 -33 \r\nQ 819 25 488 141 \r\nL 488 750 \r\nQ 750 597 1062 519 \r\nQ 1375 441 1716 441 \r\nQ 2309 441 2620 675 \r\nQ 2931 909 2931 1356 \r\nQ 2931 1769 2642 2001 \r\nQ 2353 2234 1838 2234 \r\nL 1294 2234 \r\nL 1294 2753 \r\nL 1863 2753 \r\nQ 2328 2753 2575 2939 \r\nQ 2822 3125 2822 3475 \r\nQ 2822 3834 2567 4026 \r\nQ 2313 4219 1838 4219 \r\nQ 1578 4219 1281 4162 \r\nQ 984 4106 628 3988 \r\nL 628 4550 \r\nQ 988 4650 1302 4700 \r\nQ 1616 4750 1894 4750 \r\nQ 2613 4750 3031 4423 \r\nQ 3450 4097 3450 3541 \r\nQ 3450 3153 3228 2886 \r\nQ 3006 2619 2597 2516 \r\nz\r\n\" id=\"DejaVuSans-33\" transform=\"scale(0.015625)\"/>\r\n       </defs>\r\n       <use xlink:href=\"#DejaVuSans-33\"/>\r\n      </g>\r\n     </g>\r\n    </g>\r\n    <g id=\"xtick_4\">\r\n     <g id=\"line2d_4\">\r\n      <g>\r\n       <use style=\"stroke:#000000;stroke-width:0.8;\" x=\"138.253125\" xlink:href=\"#m7b223e7a23\" y=\"224.64\"/>\r\n      </g>\r\n     </g>\r\n     <g id=\"text_4\">\r\n      <!-- 4 -->\r\n      <g transform=\"translate(135.071875 239.238437)scale(0.1 -0.1)\">\r\n       <defs>\r\n        <path d=\"M 2419 4116 \r\nL 825 1625 \r\nL 2419 1625 \r\nL 2419 4116 \r\nz\r\nM 2253 4666 \r\nL 3047 4666 \r\nL 3047 1625 \r\nL 3713 1625 \r\nL 3713 1100 \r\nL 3047 1100 \r\nL 3047 0 \r\nL 2419 0 \r\nL 2419 1100 \r\nL 313 1100 \r\nL 313 1709 \r\nL 2253 4666 \r\nz\r\n\" id=\"DejaVuSans-34\" transform=\"scale(0.015625)\"/>\r\n       </defs>\r\n       <use xlink:href=\"#DejaVuSans-34\"/>\r\n      </g>\r\n     </g>\r\n    </g>\r\n    <g id=\"xtick_5\">\r\n     <g id=\"line2d_5\">\r\n      <g>\r\n       <use style=\"stroke:#000000;stroke-width:0.8;\" x=\"166.153125\" xlink:href=\"#m7b223e7a23\" y=\"224.64\"/>\r\n      </g>\r\n     </g>\r\n     <g id=\"text_5\">\r\n      <!-- 5 -->\r\n      <g transform=\"translate(162.971875 239.238437)scale(0.1 -0.1)\">\r\n       <defs>\r\n        <path d=\"M 691 4666 \r\nL 3169 4666 \r\nL 3169 4134 \r\nL 1269 4134 \r\nL 1269 2991 \r\nQ 1406 3038 1543 3061 \r\nQ 1681 3084 1819 3084 \r\nQ 2600 3084 3056 2656 \r\nQ 3513 2228 3513 1497 \r\nQ 3513 744 3044 326 \r\nQ 2575 -91 1722 -91 \r\nQ 1428 -91 1123 -41 \r\nQ 819 9 494 109 \r\nL 494 744 \r\nQ 775 591 1075 516 \r\nQ 1375 441 1709 441 \r\nQ 2250 441 2565 725 \r\nQ 2881 1009 2881 1497 \r\nQ 2881 1984 2565 2268 \r\nQ 2250 2553 1709 2553 \r\nQ 1456 2553 1204 2497 \r\nQ 953 2441 691 2322 \r\nL 691 4666 \r\nz\r\n\" id=\"DejaVuSans-35\" transform=\"scale(0.015625)\"/>\r\n       </defs>\r\n       <use xlink:href=\"#DejaVuSans-35\"/>\r\n      </g>\r\n     </g>\r\n    </g>\r\n    <g id=\"xtick_6\">\r\n     <g id=\"line2d_6\">\r\n      <g>\r\n       <use style=\"stroke:#000000;stroke-width:0.8;\" x=\"194.053125\" xlink:href=\"#m7b223e7a23\" y=\"224.64\"/>\r\n      </g>\r\n     </g>\r\n     <g id=\"text_6\">\r\n      <!-- 6 -->\r\n      <g transform=\"translate(190.871875 239.238437)scale(0.1 -0.1)\">\r\n       <defs>\r\n        <path d=\"M 2113 2584 \r\nQ 1688 2584 1439 2293 \r\nQ 1191 2003 1191 1497 \r\nQ 1191 994 1439 701 \r\nQ 1688 409 2113 409 \r\nQ 2538 409 2786 701 \r\nQ 3034 994 3034 1497 \r\nQ 3034 2003 2786 2293 \r\nQ 2538 2584 2113 2584 \r\nz\r\nM 3366 4563 \r\nL 3366 3988 \r\nQ 3128 4100 2886 4159 \r\nQ 2644 4219 2406 4219 \r\nQ 1781 4219 1451 3797 \r\nQ 1122 3375 1075 2522 \r\nQ 1259 2794 1537 2939 \r\nQ 1816 3084 2150 3084 \r\nQ 2853 3084 3261 2657 \r\nQ 3669 2231 3669 1497 \r\nQ 3669 778 3244 343 \r\nQ 2819 -91 2113 -91 \r\nQ 1303 -91 875 529 \r\nQ 447 1150 447 2328 \r\nQ 447 3434 972 4092 \r\nQ 1497 4750 2381 4750 \r\nQ 2619 4750 2861 4703 \r\nQ 3103 4656 3366 4563 \r\nz\r\n\" id=\"DejaVuSans-36\" transform=\"scale(0.015625)\"/>\r\n       </defs>\r\n       <use xlink:href=\"#DejaVuSans-36\"/>\r\n      </g>\r\n     </g>\r\n    </g>\r\n    <g id=\"xtick_7\">\r\n     <g id=\"line2d_7\">\r\n      <g>\r\n       <use style=\"stroke:#000000;stroke-width:0.8;\" x=\"221.953125\" xlink:href=\"#m7b223e7a23\" y=\"224.64\"/>\r\n      </g>\r\n     </g>\r\n     <g id=\"text_7\">\r\n      <!-- 7 -->\r\n      <g transform=\"translate(218.771875 239.238437)scale(0.1 -0.1)\">\r\n       <defs>\r\n        <path d=\"M 525 4666 \r\nL 3525 4666 \r\nL 3525 4397 \r\nL 1831 0 \r\nL 1172 0 \r\nL 2766 4134 \r\nL 525 4134 \r\nL 525 4666 \r\nz\r\n\" id=\"DejaVuSans-37\" transform=\"scale(0.015625)\"/>\r\n       </defs>\r\n       <use xlink:href=\"#DejaVuSans-37\"/>\r\n      </g>\r\n     </g>\r\n    </g>\r\n    <g id=\"xtick_8\">\r\n     <g id=\"line2d_8\">\r\n      <g>\r\n       <use style=\"stroke:#000000;stroke-width:0.8;\" x=\"249.853125\" xlink:href=\"#m7b223e7a23\" y=\"224.64\"/>\r\n      </g>\r\n     </g>\r\n     <g id=\"text_8\">\r\n      <!-- 8 -->\r\n      <g transform=\"translate(246.671875 239.238437)scale(0.1 -0.1)\">\r\n       <defs>\r\n        <path d=\"M 2034 2216 \r\nQ 1584 2216 1326 1975 \r\nQ 1069 1734 1069 1313 \r\nQ 1069 891 1326 650 \r\nQ 1584 409 2034 409 \r\nQ 2484 409 2743 651 \r\nQ 3003 894 3003 1313 \r\nQ 3003 1734 2745 1975 \r\nQ 2488 2216 2034 2216 \r\nz\r\nM 1403 2484 \r\nQ 997 2584 770 2862 \r\nQ 544 3141 544 3541 \r\nQ 544 4100 942 4425 \r\nQ 1341 4750 2034 4750 \r\nQ 2731 4750 3128 4425 \r\nQ 3525 4100 3525 3541 \r\nQ 3525 3141 3298 2862 \r\nQ 3072 2584 2669 2484 \r\nQ 3125 2378 3379 2068 \r\nQ 3634 1759 3634 1313 \r\nQ 3634 634 3220 271 \r\nQ 2806 -91 2034 -91 \r\nQ 1263 -91 848 271 \r\nQ 434 634 434 1313 \r\nQ 434 1759 690 2068 \r\nQ 947 2378 1403 2484 \r\nz\r\nM 1172 3481 \r\nQ 1172 3119 1398 2916 \r\nQ 1625 2713 2034 2713 \r\nQ 2441 2713 2670 2916 \r\nQ 2900 3119 2900 3481 \r\nQ 2900 3844 2670 4047 \r\nQ 2441 4250 2034 4250 \r\nQ 1625 4250 1398 4047 \r\nQ 1172 3844 1172 3481 \r\nz\r\n\" id=\"DejaVuSans-38\" transform=\"scale(0.015625)\"/>\r\n       </defs>\r\n       <use xlink:href=\"#DejaVuSans-38\"/>\r\n      </g>\r\n     </g>\r\n    </g>\r\n    <g id=\"xtick_9\">\r\n     <g id=\"line2d_9\">\r\n      <g>\r\n       <use style=\"stroke:#000000;stroke-width:0.8;\" x=\"277.753125\" xlink:href=\"#m7b223e7a23\" y=\"224.64\"/>\r\n      </g>\r\n     </g>\r\n     <g id=\"text_9\">\r\n      <!-- 9 -->\r\n      <g transform=\"translate(274.571875 239.238437)scale(0.1 -0.1)\">\r\n       <defs>\r\n        <path d=\"M 703 97 \r\nL 703 672 \r\nQ 941 559 1184 500 \r\nQ 1428 441 1663 441 \r\nQ 2288 441 2617 861 \r\nQ 2947 1281 2994 2138 \r\nQ 2813 1869 2534 1725 \r\nQ 2256 1581 1919 1581 \r\nQ 1219 1581 811 2004 \r\nQ 403 2428 403 3163 \r\nQ 403 3881 828 4315 \r\nQ 1253 4750 1959 4750 \r\nQ 2769 4750 3195 4129 \r\nQ 3622 3509 3622 2328 \r\nQ 3622 1225 3098 567 \r\nQ 2575 -91 1691 -91 \r\nQ 1453 -91 1209 -44 \r\nQ 966 3 703 97 \r\nz\r\nM 1959 2075 \r\nQ 2384 2075 2632 2365 \r\nQ 2881 2656 2881 3163 \r\nQ 2881 3666 2632 3958 \r\nQ 2384 4250 1959 4250 \r\nQ 1534 4250 1286 3958 \r\nQ 1038 3666 1038 3163 \r\nQ 1038 2656 1286 2365 \r\nQ 1534 2075 1959 2075 \r\nz\r\n\" id=\"DejaVuSans-39\" transform=\"scale(0.015625)\"/>\r\n       </defs>\r\n       <use xlink:href=\"#DejaVuSans-39\"/>\r\n      </g>\r\n     </g>\r\n    </g>\r\n    <g id=\"xtick_10\">\r\n     <g id=\"line2d_10\">\r\n      <g>\r\n       <use style=\"stroke:#000000;stroke-width:0.8;\" x=\"305.653125\" xlink:href=\"#m7b223e7a23\" y=\"224.64\"/>\r\n      </g>\r\n     </g>\r\n     <g id=\"text_10\">\r\n      <!-- 10 -->\r\n      <g transform=\"translate(299.290625 239.238437)scale(0.1 -0.1)\">\r\n       <defs>\r\n        <path d=\"M 2034 4250 \r\nQ 1547 4250 1301 3770 \r\nQ 1056 3291 1056 2328 \r\nQ 1056 1369 1301 889 \r\nQ 1547 409 2034 409 \r\nQ 2525 409 2770 889 \r\nQ 3016 1369 3016 2328 \r\nQ 3016 3291 2770 3770 \r\nQ 2525 4250 2034 4250 \r\nz\r\nM 2034 4750 \r\nQ 2819 4750 3233 4129 \r\nQ 3647 3509 3647 2328 \r\nQ 3647 1150 3233 529 \r\nQ 2819 -91 2034 -91 \r\nQ 1250 -91 836 529 \r\nQ 422 1150 422 2328 \r\nQ 422 3509 836 4129 \r\nQ 1250 4750 2034 4750 \r\nz\r\n\" id=\"DejaVuSans-30\" transform=\"scale(0.015625)\"/>\r\n       </defs>\r\n       <use xlink:href=\"#DejaVuSans-31\"/>\r\n       <use x=\"63.623047\" xlink:href=\"#DejaVuSans-30\"/>\r\n      </g>\r\n     </g>\r\n    </g>\r\n    <g id=\"xtick_11\">\r\n     <g id=\"line2d_11\">\r\n      <g>\r\n       <use style=\"stroke:#000000;stroke-width:0.8;\" x=\"333.553125\" xlink:href=\"#m7b223e7a23\" y=\"224.64\"/>\r\n      </g>\r\n     </g>\r\n     <g id=\"text_11\">\r\n      <!-- 11 -->\r\n      <g transform=\"translate(327.190625 239.238437)scale(0.1 -0.1)\">\r\n       <use xlink:href=\"#DejaVuSans-31\"/>\r\n       <use x=\"63.623047\" xlink:href=\"#DejaVuSans-31\"/>\r\n      </g>\r\n     </g>\r\n    </g>\r\n    <g id=\"xtick_12\">\r\n     <g id=\"line2d_12\">\r\n      <g>\r\n       <use style=\"stroke:#000000;stroke-width:0.8;\" x=\"361.453125\" xlink:href=\"#m7b223e7a23\" y=\"224.64\"/>\r\n      </g>\r\n     </g>\r\n     <g id=\"text_12\">\r\n      <!-- 14 -->\r\n      <g transform=\"translate(355.090625 239.238437)scale(0.1 -0.1)\">\r\n       <use xlink:href=\"#DejaVuSans-31\"/>\r\n       <use x=\"63.623047\" xlink:href=\"#DejaVuSans-34\"/>\r\n      </g>\r\n     </g>\r\n    </g>\r\n    <g id=\"text_13\">\r\n     <!-- Num -->\r\n     <g transform=\"translate(196.223437 252.916562)scale(0.1 -0.1)\">\r\n      <defs>\r\n       <path d=\"M 628 4666 \r\nL 1478 4666 \r\nL 3547 763 \r\nL 3547 4666 \r\nL 4159 4666 \r\nL 4159 0 \r\nL 3309 0 \r\nL 1241 3903 \r\nL 1241 0 \r\nL 628 0 \r\nL 628 4666 \r\nz\r\n\" id=\"DejaVuSans-4e\" transform=\"scale(0.015625)\"/>\r\n       <path d=\"M 544 1381 \r\nL 544 3500 \r\nL 1119 3500 \r\nL 1119 1403 \r\nQ 1119 906 1312 657 \r\nQ 1506 409 1894 409 \r\nQ 2359 409 2629 706 \r\nQ 2900 1003 2900 1516 \r\nL 2900 3500 \r\nL 3475 3500 \r\nL 3475 0 \r\nL 2900 0 \r\nL 2900 538 \r\nQ 2691 219 2414 64 \r\nQ 2138 -91 1772 -91 \r\nQ 1169 -91 856 284 \r\nQ 544 659 544 1381 \r\nz\r\nM 1991 3584 \r\nL 1991 3584 \r\nz\r\n\" id=\"DejaVuSans-75\" transform=\"scale(0.015625)\"/>\r\n       <path d=\"M 3328 2828 \r\nQ 3544 3216 3844 3400 \r\nQ 4144 3584 4550 3584 \r\nQ 5097 3584 5394 3201 \r\nQ 5691 2819 5691 2113 \r\nL 5691 0 \r\nL 5113 0 \r\nL 5113 2094 \r\nQ 5113 2597 4934 2840 \r\nQ 4756 3084 4391 3084 \r\nQ 3944 3084 3684 2787 \r\nQ 3425 2491 3425 1978 \r\nL 3425 0 \r\nL 2847 0 \r\nL 2847 2094 \r\nQ 2847 2600 2669 2842 \r\nQ 2491 3084 2119 3084 \r\nQ 1678 3084 1418 2786 \r\nQ 1159 2488 1159 1978 \r\nL 1159 0 \r\nL 581 0 \r\nL 581 3500 \r\nL 1159 3500 \r\nL 1159 2956 \r\nQ 1356 3278 1631 3431 \r\nQ 1906 3584 2284 3584 \r\nQ 2666 3584 2933 3390 \r\nQ 3200 3197 3328 2828 \r\nz\r\n\" id=\"DejaVuSans-6d\" transform=\"scale(0.015625)\"/>\r\n      </defs>\r\n      <use xlink:href=\"#DejaVuSans-4e\"/>\r\n      <use x=\"74.804688\" xlink:href=\"#DejaVuSans-75\"/>\r\n      <use x=\"138.183594\" xlink:href=\"#DejaVuSans-6d\"/>\r\n     </g>\r\n    </g>\r\n   </g>\r\n   <g id=\"matplotlib.axis_2\">\r\n    <g id=\"ytick_1\">\r\n     <g id=\"line2d_13\">\r\n      <defs>\r\n       <path d=\"M 0 0 \r\nL -3.5 0 \r\n\" id=\"m08b2a6502f\" style=\"stroke:#000000;stroke-width:0.8;\"/>\r\n      </defs>\r\n      <g>\r\n       <use style=\"stroke:#000000;stroke-width:0.8;\" x=\"40.603125\" xlink:href=\"#m08b2a6502f\" y=\"224.64\"/>\r\n      </g>\r\n     </g>\r\n     <g id=\"text_14\">\r\n      <!-- 0 -->\r\n      <g transform=\"translate(27.240625 228.439219)scale(0.1 -0.1)\">\r\n       <use xlink:href=\"#DejaVuSans-30\"/>\r\n      </g>\r\n     </g>\r\n    </g>\r\n    <g id=\"ytick_2\">\r\n     <g id=\"line2d_14\">\r\n      <g>\r\n       <use style=\"stroke:#000000;stroke-width:0.8;\" x=\"40.603125\" xlink:href=\"#m08b2a6502f\" y=\"178.620952\"/>\r\n      </g>\r\n     </g>\r\n     <g id=\"text_15\">\r\n      <!-- 10 -->\r\n      <g transform=\"translate(20.878125 182.420171)scale(0.1 -0.1)\">\r\n       <use xlink:href=\"#DejaVuSans-31\"/>\r\n       <use x=\"63.623047\" xlink:href=\"#DejaVuSans-30\"/>\r\n      </g>\r\n     </g>\r\n    </g>\r\n    <g id=\"ytick_3\">\r\n     <g id=\"line2d_15\">\r\n      <g>\r\n       <use style=\"stroke:#000000;stroke-width:0.8;\" x=\"40.603125\" xlink:href=\"#m08b2a6502f\" y=\"132.601905\"/>\r\n      </g>\r\n     </g>\r\n     <g id=\"text_16\">\r\n      <!-- 20 -->\r\n      <g transform=\"translate(20.878125 136.401124)scale(0.1 -0.1)\">\r\n       <use xlink:href=\"#DejaVuSans-32\"/>\r\n       <use x=\"63.623047\" xlink:href=\"#DejaVuSans-30\"/>\r\n      </g>\r\n     </g>\r\n    </g>\r\n    <g id=\"ytick_4\">\r\n     <g id=\"line2d_16\">\r\n      <g>\r\n       <use style=\"stroke:#000000;stroke-width:0.8;\" x=\"40.603125\" xlink:href=\"#m08b2a6502f\" y=\"86.582857\"/>\r\n      </g>\r\n     </g>\r\n     <g id=\"text_17\">\r\n      <!-- 30 -->\r\n      <g transform=\"translate(20.878125 90.382076)scale(0.1 -0.1)\">\r\n       <use xlink:href=\"#DejaVuSans-33\"/>\r\n       <use x=\"63.623047\" xlink:href=\"#DejaVuSans-30\"/>\r\n      </g>\r\n     </g>\r\n    </g>\r\n    <g id=\"ytick_5\">\r\n     <g id=\"line2d_17\">\r\n      <g>\r\n       <use style=\"stroke:#000000;stroke-width:0.8;\" x=\"40.603125\" xlink:href=\"#m08b2a6502f\" y=\"40.56381\"/>\r\n      </g>\r\n     </g>\r\n     <g id=\"text_18\">\r\n      <!-- 40 -->\r\n      <g transform=\"translate(20.878125 44.363028)scale(0.1 -0.1)\">\r\n       <use xlink:href=\"#DejaVuSans-34\"/>\r\n       <use x=\"63.623047\" xlink:href=\"#DejaVuSans-30\"/>\r\n      </g>\r\n     </g>\r\n    </g>\r\n    <g id=\"text_19\">\r\n     <!-- Age -->\r\n     <g transform=\"translate(14.798438 125.591094)rotate(-90)scale(0.1 -0.1)\">\r\n      <defs>\r\n       <path d=\"M 2188 4044 \r\nL 1331 1722 \r\nL 3047 1722 \r\nL 2188 4044 \r\nz\r\nM 1831 4666 \r\nL 2547 4666 \r\nL 4325 0 \r\nL 3669 0 \r\nL 3244 1197 \r\nL 1141 1197 \r\nL 716 0 \r\nL 50 0 \r\nL 1831 4666 \r\nz\r\n\" id=\"DejaVuSans-41\" transform=\"scale(0.015625)\"/>\r\n       <path d=\"M 2906 1791 \r\nQ 2906 2416 2648 2759 \r\nQ 2391 3103 1925 3103 \r\nQ 1463 3103 1205 2759 \r\nQ 947 2416 947 1791 \r\nQ 947 1169 1205 825 \r\nQ 1463 481 1925 481 \r\nQ 2391 481 2648 825 \r\nQ 2906 1169 2906 1791 \r\nz\r\nM 3481 434 \r\nQ 3481 -459 3084 -895 \r\nQ 2688 -1331 1869 -1331 \r\nQ 1566 -1331 1297 -1286 \r\nQ 1028 -1241 775 -1147 \r\nL 775 -588 \r\nQ 1028 -725 1275 -790 \r\nQ 1522 -856 1778 -856 \r\nQ 2344 -856 2625 -561 \r\nQ 2906 -266 2906 331 \r\nL 2906 616 \r\nQ 2728 306 2450 153 \r\nQ 2172 0 1784 0 \r\nQ 1141 0 747 490 \r\nQ 353 981 353 1791 \r\nQ 353 2603 747 3093 \r\nQ 1141 3584 1784 3584 \r\nQ 2172 3584 2450 3431 \r\nQ 2728 3278 2906 2969 \r\nL 2906 3500 \r\nL 3481 3500 \r\nL 3481 434 \r\nz\r\n\" id=\"DejaVuSans-67\" transform=\"scale(0.015625)\"/>\r\n       <path d=\"M 3597 1894 \r\nL 3597 1613 \r\nL 953 1613 \r\nQ 991 1019 1311 708 \r\nQ 1631 397 2203 397 \r\nQ 2534 397 2845 478 \r\nQ 3156 559 3463 722 \r\nL 3463 178 \r\nQ 3153 47 2828 -22 \r\nQ 2503 -91 2169 -91 \r\nQ 1331 -91 842 396 \r\nQ 353 884 353 1716 \r\nQ 353 2575 817 3079 \r\nQ 1281 3584 2069 3584 \r\nQ 2775 3584 3186 3129 \r\nQ 3597 2675 3597 1894 \r\nz\r\nM 3022 2063 \r\nQ 3016 2534 2758 2815 \r\nQ 2500 3097 2075 3097 \r\nQ 1594 3097 1305 2825 \r\nQ 1016 2553 972 2059 \r\nL 3022 2063 \r\nz\r\n\" id=\"DejaVuSans-65\" transform=\"scale(0.015625)\"/>\r\n      </defs>\r\n      <use xlink:href=\"#DejaVuSans-41\"/>\r\n      <use x=\"68.408203\" xlink:href=\"#DejaVuSans-67\"/>\r\n      <use x=\"131.884766\" xlink:href=\"#DejaVuSans-65\"/>\r\n     </g>\r\n    </g>\r\n   </g>\r\n   <g id=\"line2d_18\">\r\n    <path clip-path=\"url(#p672b085371)\" d=\"M 0 0 \r\n\" style=\"fill:none;stroke:#424242;stroke-linecap:square;stroke-width:2.7;\"/>\r\n   </g>\r\n   <g id=\"line2d_19\">\r\n    <path clip-path=\"url(#p672b085371)\" d=\"M 0 0 \r\n\" style=\"fill:none;stroke:#424242;stroke-linecap:square;stroke-width:2.7;\"/>\r\n   </g>\r\n   <g id=\"line2d_20\">\r\n    <path clip-path=\"url(#p672b085371)\" d=\"M 0 0 \r\n\" style=\"fill:none;stroke:#424242;stroke-linecap:square;stroke-width:2.7;\"/>\r\n   </g>\r\n   <g id=\"line2d_21\">\r\n    <path clip-path=\"url(#p672b085371)\" d=\"M 0 0 \r\n\" style=\"fill:none;stroke:#424242;stroke-linecap:square;stroke-width:2.7;\"/>\r\n   </g>\r\n   <g id=\"line2d_22\">\r\n    <path clip-path=\"url(#p672b085371)\" d=\"M 0 0 \r\n\" style=\"fill:none;stroke:#424242;stroke-linecap:square;stroke-width:2.7;\"/>\r\n   </g>\r\n   <g id=\"line2d_23\">\r\n    <path clip-path=\"url(#p672b085371)\" d=\"M 0 0 \r\n\" style=\"fill:none;stroke:#424242;stroke-linecap:square;stroke-width:2.7;\"/>\r\n   </g>\r\n   <g id=\"line2d_24\">\r\n    <path clip-path=\"url(#p672b085371)\" d=\"M 0 0 \r\n\" style=\"fill:none;stroke:#424242;stroke-linecap:square;stroke-width:2.7;\"/>\r\n   </g>\r\n   <g id=\"line2d_25\">\r\n    <path clip-path=\"url(#p672b085371)\" d=\"M 0 0 \r\n\" style=\"fill:none;stroke:#424242;stroke-linecap:square;stroke-width:2.7;\"/>\r\n   </g>\r\n   <g id=\"line2d_26\">\r\n    <path clip-path=\"url(#p672b085371)\" d=\"M 0 0 \r\n\" style=\"fill:none;stroke:#424242;stroke-linecap:square;stroke-width:2.7;\"/>\r\n   </g>\r\n   <g id=\"line2d_27\">\r\n    <path clip-path=\"url(#p672b085371)\" d=\"M 0 0 \r\n\" style=\"fill:none;stroke:#424242;stroke-linecap:square;stroke-width:2.7;\"/>\r\n   </g>\r\n   <g id=\"line2d_28\">\r\n    <path clip-path=\"url(#p672b085371)\" d=\"M 0 0 \r\n\" style=\"fill:none;stroke:#424242;stroke-linecap:square;stroke-width:2.7;\"/>\r\n   </g>\r\n   <g id=\"line2d_29\">\r\n    <path clip-path=\"url(#p672b085371)\" d=\"M 0 0 \r\n\" style=\"fill:none;stroke:#424242;stroke-linecap:square;stroke-width:2.7;\"/>\r\n   </g>\r\n   <g id=\"patch_15\">\r\n    <path d=\"M 40.603125 224.64 \r\nL 40.603125 7.2 \r\n\" style=\"fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;\"/>\r\n   </g>\r\n   <g id=\"patch_16\">\r\n    <path d=\"M 375.403125 224.64 \r\nL 375.403125 7.2 \r\n\" style=\"fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;\"/>\r\n   </g>\r\n   <g id=\"patch_17\">\r\n    <path d=\"M 40.603125 224.64 \r\nL 375.403125 224.64 \r\n\" style=\"fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;\"/>\r\n   </g>\r\n   <g id=\"patch_18\">\r\n    <path d=\"M 40.603125 7.2 \r\nL 375.403125 7.2 \r\n\" style=\"fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;\"/>\r\n   </g>\r\n  </g>\r\n </g>\r\n <defs>\r\n  <clipPath id=\"p672b085371\">\r\n   <rect height=\"217.44\" width=\"334.8\" x=\"40.603125\" y=\"7.2\"/>\r\n  </clipPath>\r\n </defs>\r\n</svg>\r\n",
      "image/png": "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\n"
     },
     "metadata": {
      "needs_background": "light"
     }
    }
   ],
   "source": [
    "dates = df.Debut\n",
    "debut_list = []\n",
    "num = 0\n",
    "for i in dates:\n",
    "  debut_list.append(i)\n",
    "  num = num+1\n",
    "\n",
    "dates2 = df.disband\n",
    "disband_list = []\n",
    "num = 0\n",
    "for j in dates2:\n",
    "  if  j ==1:\n",
    "    j=2021\n",
    "  disband_list.append(j)\n",
    "  num = num+1\n",
    "\n",
    "old_list=[]\n",
    "for k in range (0,num):\n",
    "  l=disband_list[k]-debut_list[k]\n",
    "  old_list.append(l)\n",
    "age_data = {memb: old_list.count(memb) for memb in set(old_list)}\n",
    "\n",
    "age_data=dict(age_data)\n",
    "print(age_data)\n",
    "del_data=[]\n",
    "for i in age_data:\n",
    "  if age_data[i]<5: \n",
    "   del_data.append(i)\n",
    "for j in del_data:\n",
    "  del age_data[j]\n",
    "\n",
    "import matplotlib.pyplot as plt\n",
    "comp_df = pd.DataFrame.from_dict(data=age_data, orient=\"index\", columns=[\"Age\"])\n",
    "comp_df[\"Num\"]=comp_df.index\n",
    "sns.barplot(data=comp_df, x=\"Num\", y=\"Age\")"
   ]
  },
  {
   "source": [
    "## Вывод: данные гипотезы абсолютно не изменились так как датасет изначально был хорошим и не требовал предобработки."
   ],
   "cell_type": "markdown",
   "metadata": {}
  },
  {
   "source": [
    "# Новые гипотезы"
   ],
   "cell_type": "markdown",
   "metadata": {}
  },
  {
   "source": [
    "### Мужские группы чаще имеют название фанбазы: гипотеза подтвердилась"
   ],
   "cell_type": "markdown",
   "metadata": {}
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "metadata": {},
   "outputs": [
    {
     "output_type": "display_data",
     "data": {
      "application/vnd.plotly.v1+json": {
       "config": {
        "plotlyServerURL": "https://plot.ly"
       },
       "data": [
        {
         "labels": [
          "M",
          "F"
         ],
         "type": "pie",
         "values": [
          61,
          46
         ]
        }
       ],
       "layout": {
        "template": {
         "data": {
          "bar": [
           {
            "error_x": {
             "color": "#2a3f5f"
            },
            "error_y": {
             "color": "#2a3f5f"
            },
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             }
            },
            "type": "bar"
           }
          ],
          "barpolar": [
           {
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             }
            },
            "type": "barpolar"
           }
          ],
          "carpet": [
           {
            "aaxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "baxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "type": "carpet"
           }
          ],
          "choropleth": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "choropleth"
           }
          ],
          "contour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "contour"
           }
          ],
          "contourcarpet": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "contourcarpet"
           }
          ],
          "heatmap": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmap"
           }
          ],
          "heatmapgl": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmapgl"
           }
          ],
          "histogram": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "histogram"
           }
          ],
          "histogram2d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2d"
           }
          ],
          "histogram2dcontour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2dcontour"
           }
          ],
          "mesh3d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "mesh3d"
           }
          ],
          "parcoords": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "parcoords"
           }
          ],
          "pie": [
           {
            "automargin": true,
            "type": "pie"
           }
          ],
          "scatter": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter"
           }
          ],
          "scatter3d": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter3d"
           }
          ],
          "scattercarpet": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattercarpet"
           }
          ],
          "scattergeo": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergeo"
           }
          ],
          "scattergl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergl"
           }
          ],
          "scattermapbox": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattermapbox"
           }
          ],
          "scatterpolar": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolar"
           }
          ],
          "scatterpolargl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolargl"
           }
          ],
          "scatterternary": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterternary"
           }
          ],
          "surface": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "surface"
           }
          ],
          "table": [
           {
            "cells": {
             "fill": {
              "color": "#EBF0F8"
             },
             "line": {
              "color": "white"
             }
            },
            "header": {
             "fill": {
              "color": "#C8D4E3"
             },
             "line": {
              "color": "white"
             }
            },
            "type": "table"
           }
          ]
         },
         "layout": {
          "annotationdefaults": {
           "arrowcolor": "#2a3f5f",
           "arrowhead": 0,
           "arrowwidth": 1
          },
          "autotypenumbers": "strict",
          "coloraxis": {
           "colorbar": {
            "outlinewidth": 0,
            "ticks": ""
           }
          },
          "colorscale": {
           "diverging": [
            [
             0,
             "#8e0152"
            ],
            [
             0.1,
             "#c51b7d"
            ],
            [
             0.2,
             "#de77ae"
            ],
            [
             0.3,
             "#f1b6da"
            ],
            [
             0.4,
             "#fde0ef"
            ],
            [
             0.5,
             "#f7f7f7"
            ],
            [
             0.6,
             "#e6f5d0"
            ],
            [
             0.7,
             "#b8e186"
            ],
            [
             0.8,
             "#7fbc41"
            ],
            [
             0.9,
             "#4d9221"
            ],
            [
             1,
             "#276419"
            ]
           ],
           "sequential": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ],
           "sequentialminus": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ]
          },
          "colorway": [
           "#636efa",
           "#EF553B",
           "#00cc96",
           "#ab63fa",
           "#FFA15A",
           "#19d3f3",
           "#FF6692",
           "#B6E880",
           "#FF97FF",
           "#FECB52"
          ],
          "font": {
           "color": "#2a3f5f"
          },
          "geo": {
           "bgcolor": "white",
           "lakecolor": "white",
           "landcolor": "#E5ECF6",
           "showlakes": true,
           "showland": true,
           "subunitcolor": "white"
          },
          "hoverlabel": {
           "align": "left"
          },
          "hovermode": "closest",
          "mapbox": {
           "style": "light"
          },
          "paper_bgcolor": "white",
          "plot_bgcolor": "#E5ECF6",
          "polar": {
           "angularaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "radialaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "scene": {
           "xaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "yaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "zaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           }
          },
          "shapedefaults": {
           "line": {
            "color": "#2a3f5f"
           }
          },
          "ternary": {
           "aaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "baxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "caxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "title": {
           "x": 0.05
          },
          "xaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          },
          "yaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          }
         }
        }
       }
      }
     },
     "metadata": {}
    }
   ],
   "source": [
    "fan_df = df.loc[df[\"Fanclub Name\"] != \"-\"]\n",
    "\n",
    "male_df = fan_df.loc[fan_df[\"Gender\"] == 0]\n",
    "m_num = male_df.shape[0]\n",
    "fem_df = fan_df.loc[fan_df[\"Gender\"] == 1]\n",
    "f_num = fem_df.shape[0]\n",
    "\n",
    "\n",
    "labels = [\"M\",\"F\"]\n",
    "values = [m_num, f_num]\n",
    "fig = go.Figure(data=[go.Pie(labels=labels, values=values)])\n",
    "fig.show()"
   ]
  },
  {
   "source": [
    "### Большинство групп сформированных в 2017 году сейчас не активны : гипотеза не подтвердилась, большинство активны"
   ],
   "cell_type": "markdown",
   "metadata": {}
  },
  {
   "cell_type": "code",
   "execution_count": 90,
   "metadata": {},
   "outputs": [
    {
     "output_type": "display_data",
     "data": {
      "application/vnd.plotly.v1+json": {
       "config": {
        "plotlyServerURL": "https://plot.ly"
       },
       "data": [
        {
         "labels": [
          "Active",
          "Inactive"
         ],
         "type": "pie",
         "values": [
          39,
          10
         ]
        }
       ],
       "layout": {
        "template": {
         "data": {
          "bar": [
           {
            "error_x": {
             "color": "#2a3f5f"
            },
            "error_y": {
             "color": "#2a3f5f"
            },
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             }
            },
            "type": "bar"
           }
          ],
          "barpolar": [
           {
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             }
            },
            "type": "barpolar"
           }
          ],
          "carpet": [
           {
            "aaxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "baxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "type": "carpet"
           }
          ],
          "choropleth": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "choropleth"
           }
          ],
          "contour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "contour"
           }
          ],
          "contourcarpet": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "contourcarpet"
           }
          ],
          "heatmap": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmap"
           }
          ],
          "heatmapgl": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmapgl"
           }
          ],
          "histogram": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "histogram"
           }
          ],
          "histogram2d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2d"
           }
          ],
          "histogram2dcontour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2dcontour"
           }
          ],
          "mesh3d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "mesh3d"
           }
          ],
          "parcoords": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "parcoords"
           }
          ],
          "pie": [
           {
            "automargin": true,
            "type": "pie"
           }
          ],
          "scatter": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter"
           }
          ],
          "scatter3d": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter3d"
           }
          ],
          "scattercarpet": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattercarpet"
           }
          ],
          "scattergeo": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergeo"
           }
          ],
          "scattergl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergl"
           }
          ],
          "scattermapbox": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattermapbox"
           }
          ],
          "scatterpolar": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolar"
           }
          ],
          "scatterpolargl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolargl"
           }
          ],
          "scatterternary": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterternary"
           }
          ],
          "surface": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "surface"
           }
          ],
          "table": [
           {
            "cells": {
             "fill": {
              "color": "#EBF0F8"
             },
             "line": {
              "color": "white"
             }
            },
            "header": {
             "fill": {
              "color": "#C8D4E3"
             },
             "line": {
              "color": "white"
             }
            },
            "type": "table"
           }
          ]
         },
         "layout": {
          "annotationdefaults": {
           "arrowcolor": "#2a3f5f",
           "arrowhead": 0,
           "arrowwidth": 1
          },
          "autotypenumbers": "strict",
          "coloraxis": {
           "colorbar": {
            "outlinewidth": 0,
            "ticks": ""
           }
          },
          "colorscale": {
           "diverging": [
            [
             0,
             "#8e0152"
            ],
            [
             0.1,
             "#c51b7d"
            ],
            [
             0.2,
             "#de77ae"
            ],
            [
             0.3,
             "#f1b6da"
            ],
            [
             0.4,
             "#fde0ef"
            ],
            [
             0.5,
             "#f7f7f7"
            ],
            [
             0.6,
             "#e6f5d0"
            ],
            [
             0.7,
             "#b8e186"
            ],
            [
             0.8,
             "#7fbc41"
            ],
            [
             0.9,
             "#4d9221"
            ],
            [
             1,
             "#276419"
            ]
           ],
           "sequential": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ],
           "sequentialminus": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ]
          },
          "colorway": [
           "#636efa",
           "#EF553B",
           "#00cc96",
           "#ab63fa",
           "#FFA15A",
           "#19d3f3",
           "#FF6692",
           "#B6E880",
           "#FF97FF",
           "#FECB52"
          ],
          "font": {
           "color": "#2a3f5f"
          },
          "geo": {
           "bgcolor": "white",
           "lakecolor": "white",
           "landcolor": "#E5ECF6",
           "showlakes": true,
           "showland": true,
           "subunitcolor": "white"
          },
          "hoverlabel": {
           "align": "left"
          },
          "hovermode": "closest",
          "mapbox": {
           "style": "light"
          },
          "paper_bgcolor": "white",
          "plot_bgcolor": "#E5ECF6",
          "polar": {
           "angularaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "radialaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "scene": {
           "xaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "yaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "zaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           }
          },
          "shapedefaults": {
           "line": {
            "color": "#2a3f5f"
           }
          },
          "ternary": {
           "aaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "baxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "caxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "title": {
           "x": 0.05
          },
          "xaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          },
          "yaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          }
         }
        }
       }
      }
     },
     "metadata": {}
    }
   ],
   "source": [
    "semn_df = df.loc[df[\"Debut\"] == 2017]\n",
    "\n",
    "al_df = semn_df.loc[semn_df[\"disband\"] == 1]\n",
    "a_num = al_df.shape[0]\n",
    "ded_df = semn_df.loc[semn_df[\"disband\"] != 1]\n",
    "d_num = ded_df.shape[0]\n",
    "\n",
    "\n",
    "labels = [\"Active\",\"Inactive\"]\n",
    "values = [a_num, d_num]\n",
    "fig = go.Figure(data=[go.Pie(labels=labels, values=values)])\n",
    "fig.show()"
   ]
  },
  {
   "source": [
    "### Количество участников в мужских группах больше чем в женских: подвердилось в мужских группах в среднем 6 участников а женских 5"
   ],
   "cell_type": "markdown",
   "metadata": {}
  },
  {
   "cell_type": "code",
   "execution_count": 91,
   "metadata": {},
   "outputs": [
    {
     "output_type": "stream",
     "name": "stdout",
     "text": [
      "5.065789473684211\n5.938775510204081\n"
     ]
    },
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "<AxesSubplot:xlabel='Gender', ylabel='Members'>"
      ]
     },
     "metadata": {},
     "execution_count": 91
    },
    {
     "output_type": "display_data",
     "data": {
      "text/plain": "<Figure size 432x288 with 1 Axes>",
      "image/svg+xml": "<?xml version=\"1.0\" encoding=\"utf-8\" standalone=\"no\"?>\r\n<!DOCTYPE svg PUBLIC \"-//W3C//DTD SVG 1.1//EN\"\r\n  \"http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd\">\r\n<svg height=\"262.19625pt\" version=\"1.1\" viewBox=\"0 0 376.240625 262.19625\" width=\"376.240625pt\" xmlns=\"http://www.w3.org/2000/svg\" xmlns:xlink=\"http://www.w3.org/1999/xlink\">\r\n <metadata>\r\n  <rdf:RDF xmlns:cc=\"http://creativecommons.org/ns#\" xmlns:dc=\"http://purl.org/dc/elements/1.1/\" xmlns:rdf=\"http://www.w3.org/1999/02/22-rdf-syntax-ns#\">\r\n   <cc:Work>\r\n    <dc:type rdf:resource=\"http://purl.org/dc/dcmitype/StillImage\"/>\r\n    <dc:date>2021-04-21T15:11:51.813845</dc:date>\r\n    <dc:format>image/svg+xml</dc:format>\r\n    <dc:creator>\r\n     <cc:Agent>\r\n      <dc:title>Matplotlib v3.4.1, https://matplotlib.org/</dc:title>\r\n     </cc:Agent>\r\n    </dc:creator>\r\n   </cc:Work>\r\n  </rdf:RDF>\r\n </metadata>\r\n <defs>\r\n  <style type=\"text/css\">*{stroke-linecap:butt;stroke-linejoin:round;}</style>\r\n </defs>\r\n <g id=\"figure_1\">\r\n  <g id=\"patch_1\">\r\n   <path d=\"M 0 262.19625 \r\nL 376.240625 262.19625 \r\nL 376.240625 0 \r\nL 0 0 \r\nz\r\n\" style=\"fill:none;\"/>\r\n  </g>\r\n  <g id=\"axes_1\">\r\n   <g id=\"patch_2\">\r\n    <path d=\"M 34.240625 224.64 \r\nL 369.040625 224.64 \r\nL 369.040625 7.2 \r\nL 34.240625 7.2 \r\nz\r\n\" style=\"fill:#ffffff;\"/>\r\n   </g>\r\n   <g id=\"patch_3\">\r\n    <path clip-path=\"url(#p063cb63451)\" d=\"M 50.980625 224.64 \r\nL 184.900625 224.64 \r\nL 184.900625 30.455437 \r\nL 50.980625 30.455437 \r\nz\r\n\" style=\"fill:#3274a1;\"/>\r\n   </g>\r\n   <g id=\"patch_4\">\r\n    <path clip-path=\"url(#p063cb63451)\" d=\"M 218.380625 224.64 \r\nL 352.300625 224.64 \r\nL 352.300625 59.000111 \r\nL 218.380625 59.000111 \r\nz\r\n\" style=\"fill:#e1812c;\"/>\r\n   </g>\r\n   <g id=\"matplotlib.axis_1\">\r\n    <g id=\"xtick_1\">\r\n     <g id=\"line2d_1\">\r\n      <defs>\r\n       <path d=\"M 0 0 \r\nL 0 3.5 \r\n\" id=\"m7e7e10d93e\" style=\"stroke:#000000;stroke-width:0.8;\"/>\r\n      </defs>\r\n      <g>\r\n       <use style=\"stroke:#000000;stroke-width:0.8;\" x=\"117.940625\" xlink:href=\"#m7e7e10d93e\" y=\"224.64\"/>\r\n      </g>\r\n     </g>\r\n     <g id=\"text_1\">\r\n      <!-- 0 -->\r\n      <g transform=\"translate(114.759375 239.238438)scale(0.1 -0.1)\">\r\n       <defs>\r\n        <path d=\"M 2034 4250 \r\nQ 1547 4250 1301 3770 \r\nQ 1056 3291 1056 2328 \r\nQ 1056 1369 1301 889 \r\nQ 1547 409 2034 409 \r\nQ 2525 409 2770 889 \r\nQ 3016 1369 3016 2328 \r\nQ 3016 3291 2770 3770 \r\nQ 2525 4250 2034 4250 \r\nz\r\nM 2034 4750 \r\nQ 2819 4750 3233 4129 \r\nQ 3647 3509 3647 2328 \r\nQ 3647 1150 3233 529 \r\nQ 2819 -91 2034 -91 \r\nQ 1250 -91 836 529 \r\nQ 422 1150 422 2328 \r\nQ 422 3509 836 4129 \r\nQ 1250 4750 2034 4750 \r\nz\r\n\" id=\"DejaVuSans-30\" transform=\"scale(0.015625)\"/>\r\n       </defs>\r\n       <use xlink:href=\"#DejaVuSans-30\"/>\r\n      </g>\r\n     </g>\r\n    </g>\r\n    <g id=\"xtick_2\">\r\n     <g id=\"line2d_2\">\r\n      <g>\r\n       <use style=\"stroke:#000000;stroke-width:0.8;\" x=\"285.340625\" xlink:href=\"#m7e7e10d93e\" y=\"224.64\"/>\r\n      </g>\r\n     </g>\r\n     <g id=\"text_2\">\r\n      <!-- 1 -->\r\n      <g transform=\"translate(282.159375 239.238438)scale(0.1 -0.1)\">\r\n       <defs>\r\n        <path d=\"M 794 531 \r\nL 1825 531 \r\nL 1825 4091 \r\nL 703 3866 \r\nL 703 4441 \r\nL 1819 4666 \r\nL 2450 4666 \r\nL 2450 531 \r\nL 3481 531 \r\nL 3481 0 \r\nL 794 0 \r\nL 794 531 \r\nz\r\n\" id=\"DejaVuSans-31\" transform=\"scale(0.015625)\"/>\r\n       </defs>\r\n       <use xlink:href=\"#DejaVuSans-31\"/>\r\n      </g>\r\n     </g>\r\n    </g>\r\n    <g id=\"text_3\">\r\n     <!-- Gender -->\r\n     <g transform=\"translate(183.214844 252.916563)scale(0.1 -0.1)\">\r\n      <defs>\r\n       <path d=\"M 3809 666 \r\nL 3809 1919 \r\nL 2778 1919 \r\nL 2778 2438 \r\nL 4434 2438 \r\nL 4434 434 \r\nQ 4069 175 3628 42 \r\nQ 3188 -91 2688 -91 \r\nQ 1594 -91 976 548 \r\nQ 359 1188 359 2328 \r\nQ 359 3472 976 4111 \r\nQ 1594 4750 2688 4750 \r\nQ 3144 4750 3555 4637 \r\nQ 3966 4525 4313 4306 \r\nL 4313 3634 \r\nQ 3963 3931 3569 4081 \r\nQ 3175 4231 2741 4231 \r\nQ 1884 4231 1454 3753 \r\nQ 1025 3275 1025 2328 \r\nQ 1025 1384 1454 906 \r\nQ 1884 428 2741 428 \r\nQ 3075 428 3337 486 \r\nQ 3600 544 3809 666 \r\nz\r\n\" id=\"DejaVuSans-47\" transform=\"scale(0.015625)\"/>\r\n       <path d=\"M 3597 1894 \r\nL 3597 1613 \r\nL 953 1613 \r\nQ 991 1019 1311 708 \r\nQ 1631 397 2203 397 \r\nQ 2534 397 2845 478 \r\nQ 3156 559 3463 722 \r\nL 3463 178 \r\nQ 3153 47 2828 -22 \r\nQ 2503 -91 2169 -91 \r\nQ 1331 -91 842 396 \r\nQ 353 884 353 1716 \r\nQ 353 2575 817 3079 \r\nQ 1281 3584 2069 3584 \r\nQ 2775 3584 3186 3129 \r\nQ 3597 2675 3597 1894 \r\nz\r\nM 3022 2063 \r\nQ 3016 2534 2758 2815 \r\nQ 2500 3097 2075 3097 \r\nQ 1594 3097 1305 2825 \r\nQ 1016 2553 972 2059 \r\nL 3022 2063 \r\nz\r\n\" id=\"DejaVuSans-65\" transform=\"scale(0.015625)\"/>\r\n       <path d=\"M 3513 2113 \r\nL 3513 0 \r\nL 2938 0 \r\nL 2938 2094 \r\nQ 2938 2591 2744 2837 \r\nQ 2550 3084 2163 3084 \r\nQ 1697 3084 1428 2787 \r\nQ 1159 2491 1159 1978 \r\nL 1159 0 \r\nL 581 0 \r\nL 581 3500 \r\nL 1159 3500 \r\nL 1159 2956 \r\nQ 1366 3272 1645 3428 \r\nQ 1925 3584 2291 3584 \r\nQ 2894 3584 3203 3211 \r\nQ 3513 2838 3513 2113 \r\nz\r\n\" id=\"DejaVuSans-6e\" transform=\"scale(0.015625)\"/>\r\n       <path d=\"M 2906 2969 \r\nL 2906 4863 \r\nL 3481 4863 \r\nL 3481 0 \r\nL 2906 0 \r\nL 2906 525 \r\nQ 2725 213 2448 61 \r\nQ 2172 -91 1784 -91 \r\nQ 1150 -91 751 415 \r\nQ 353 922 353 1747 \r\nQ 353 2572 751 3078 \r\nQ 1150 3584 1784 3584 \r\nQ 2172 3584 2448 3432 \r\nQ 2725 3281 2906 2969 \r\nz\r\nM 947 1747 \r\nQ 947 1113 1208 752 \r\nQ 1469 391 1925 391 \r\nQ 2381 391 2643 752 \r\nQ 2906 1113 2906 1747 \r\nQ 2906 2381 2643 2742 \r\nQ 2381 3103 1925 3103 \r\nQ 1469 3103 1208 2742 \r\nQ 947 2381 947 1747 \r\nz\r\n\" id=\"DejaVuSans-64\" transform=\"scale(0.015625)\"/>\r\n       <path d=\"M 2631 2963 \r\nQ 2534 3019 2420 3045 \r\nQ 2306 3072 2169 3072 \r\nQ 1681 3072 1420 2755 \r\nQ 1159 2438 1159 1844 \r\nL 1159 0 \r\nL 581 0 \r\nL 581 3500 \r\nL 1159 3500 \r\nL 1159 2956 \r\nQ 1341 3275 1631 3429 \r\nQ 1922 3584 2338 3584 \r\nQ 2397 3584 2469 3576 \r\nQ 2541 3569 2628 3553 \r\nL 2631 2963 \r\nz\r\n\" id=\"DejaVuSans-72\" transform=\"scale(0.015625)\"/>\r\n      </defs>\r\n      <use xlink:href=\"#DejaVuSans-47\"/>\r\n      <use x=\"77.490234\" xlink:href=\"#DejaVuSans-65\"/>\r\n      <use x=\"139.013672\" xlink:href=\"#DejaVuSans-6e\"/>\r\n      <use x=\"202.392578\" xlink:href=\"#DejaVuSans-64\"/>\r\n      <use x=\"265.869141\" xlink:href=\"#DejaVuSans-65\"/>\r\n      <use x=\"327.392578\" xlink:href=\"#DejaVuSans-72\"/>\r\n     </g>\r\n    </g>\r\n   </g>\r\n   <g id=\"matplotlib.axis_2\">\r\n    <g id=\"ytick_1\">\r\n     <g id=\"line2d_3\">\r\n      <defs>\r\n       <path d=\"M 0 0 \r\nL -3.5 0 \r\n\" id=\"mf1b629062f\" style=\"stroke:#000000;stroke-width:0.8;\"/>\r\n      </defs>\r\n      <g>\r\n       <use style=\"stroke:#000000;stroke-width:0.8;\" x=\"34.240625\" xlink:href=\"#mf1b629062f\" y=\"224.64\"/>\r\n      </g>\r\n     </g>\r\n     <g id=\"text_4\">\r\n      <!-- 0 -->\r\n      <g transform=\"translate(20.878125 228.439219)scale(0.1 -0.1)\">\r\n       <use xlink:href=\"#DejaVuSans-30\"/>\r\n      </g>\r\n     </g>\r\n    </g>\r\n    <g id=\"ytick_2\">\r\n     <g id=\"line2d_4\">\r\n      <g>\r\n       <use style=\"stroke:#000000;stroke-width:0.8;\" x=\"34.240625\" xlink:href=\"#mf1b629062f\" y=\"191.942256\"/>\r\n      </g>\r\n     </g>\r\n     <g id=\"text_5\">\r\n      <!-- 1 -->\r\n      <g transform=\"translate(20.878125 195.741474)scale(0.1 -0.1)\">\r\n       <use xlink:href=\"#DejaVuSans-31\"/>\r\n      </g>\r\n     </g>\r\n    </g>\r\n    <g id=\"ytick_3\">\r\n     <g id=\"line2d_5\">\r\n      <g>\r\n       <use style=\"stroke:#000000;stroke-width:0.8;\" x=\"34.240625\" xlink:href=\"#mf1b629062f\" y=\"159.244511\"/>\r\n      </g>\r\n     </g>\r\n     <g id=\"text_6\">\r\n      <!-- 2 -->\r\n      <g transform=\"translate(20.878125 163.04373)scale(0.1 -0.1)\">\r\n       <defs>\r\n        <path d=\"M 1228 531 \r\nL 3431 531 \r\nL 3431 0 \r\nL 469 0 \r\nL 469 531 \r\nQ 828 903 1448 1529 \r\nQ 2069 2156 2228 2338 \r\nQ 2531 2678 2651 2914 \r\nQ 2772 3150 2772 3378 \r\nQ 2772 3750 2511 3984 \r\nQ 2250 4219 1831 4219 \r\nQ 1534 4219 1204 4116 \r\nQ 875 4013 500 3803 \r\nL 500 4441 \r\nQ 881 4594 1212 4672 \r\nQ 1544 4750 1819 4750 \r\nQ 2544 4750 2975 4387 \r\nQ 3406 4025 3406 3419 \r\nQ 3406 3131 3298 2873 \r\nQ 3191 2616 2906 2266 \r\nQ 2828 2175 2409 1742 \r\nQ 1991 1309 1228 531 \r\nz\r\n\" id=\"DejaVuSans-32\" transform=\"scale(0.015625)\"/>\r\n       </defs>\r\n       <use xlink:href=\"#DejaVuSans-32\"/>\r\n      </g>\r\n     </g>\r\n    </g>\r\n    <g id=\"ytick_4\">\r\n     <g id=\"line2d_6\">\r\n      <g>\r\n       <use style=\"stroke:#000000;stroke-width:0.8;\" x=\"34.240625\" xlink:href=\"#mf1b629062f\" y=\"126.546767\"/>\r\n      </g>\r\n     </g>\r\n     <g id=\"text_7\">\r\n      <!-- 3 -->\r\n      <g transform=\"translate(20.878125 130.345986)scale(0.1 -0.1)\">\r\n       <defs>\r\n        <path d=\"M 2597 2516 \r\nQ 3050 2419 3304 2112 \r\nQ 3559 1806 3559 1356 \r\nQ 3559 666 3084 287 \r\nQ 2609 -91 1734 -91 \r\nQ 1441 -91 1130 -33 \r\nQ 819 25 488 141 \r\nL 488 750 \r\nQ 750 597 1062 519 \r\nQ 1375 441 1716 441 \r\nQ 2309 441 2620 675 \r\nQ 2931 909 2931 1356 \r\nQ 2931 1769 2642 2001 \r\nQ 2353 2234 1838 2234 \r\nL 1294 2234 \r\nL 1294 2753 \r\nL 1863 2753 \r\nQ 2328 2753 2575 2939 \r\nQ 2822 3125 2822 3475 \r\nQ 2822 3834 2567 4026 \r\nQ 2313 4219 1838 4219 \r\nQ 1578 4219 1281 4162 \r\nQ 984 4106 628 3988 \r\nL 628 4550 \r\nQ 988 4650 1302 4700 \r\nQ 1616 4750 1894 4750 \r\nQ 2613 4750 3031 4423 \r\nQ 3450 4097 3450 3541 \r\nQ 3450 3153 3228 2886 \r\nQ 3006 2619 2597 2516 \r\nz\r\n\" id=\"DejaVuSans-33\" transform=\"scale(0.015625)\"/>\r\n       </defs>\r\n       <use xlink:href=\"#DejaVuSans-33\"/>\r\n      </g>\r\n     </g>\r\n    </g>\r\n    <g id=\"ytick_5\">\r\n     <g id=\"line2d_7\">\r\n      <g>\r\n       <use style=\"stroke:#000000;stroke-width:0.8;\" x=\"34.240625\" xlink:href=\"#mf1b629062f\" y=\"93.849023\"/>\r\n      </g>\r\n     </g>\r\n     <g id=\"text_8\">\r\n      <!-- 4 -->\r\n      <g transform=\"translate(20.878125 97.648241)scale(0.1 -0.1)\">\r\n       <defs>\r\n        <path d=\"M 2419 4116 \r\nL 825 1625 \r\nL 2419 1625 \r\nL 2419 4116 \r\nz\r\nM 2253 4666 \r\nL 3047 4666 \r\nL 3047 1625 \r\nL 3713 1625 \r\nL 3713 1100 \r\nL 3047 1100 \r\nL 3047 0 \r\nL 2419 0 \r\nL 2419 1100 \r\nL 313 1100 \r\nL 313 1709 \r\nL 2253 4666 \r\nz\r\n\" id=\"DejaVuSans-34\" transform=\"scale(0.015625)\"/>\r\n       </defs>\r\n       <use xlink:href=\"#DejaVuSans-34\"/>\r\n      </g>\r\n     </g>\r\n    </g>\r\n    <g id=\"ytick_6\">\r\n     <g id=\"line2d_8\">\r\n      <g>\r\n       <use style=\"stroke:#000000;stroke-width:0.8;\" x=\"34.240625\" xlink:href=\"#mf1b629062f\" y=\"61.151278\"/>\r\n      </g>\r\n     </g>\r\n     <g id=\"text_9\">\r\n      <!-- 5 -->\r\n      <g transform=\"translate(20.878125 64.950497)scale(0.1 -0.1)\">\r\n       <defs>\r\n        <path d=\"M 691 4666 \r\nL 3169 4666 \r\nL 3169 4134 \r\nL 1269 4134 \r\nL 1269 2991 \r\nQ 1406 3038 1543 3061 \r\nQ 1681 3084 1819 3084 \r\nQ 2600 3084 3056 2656 \r\nQ 3513 2228 3513 1497 \r\nQ 3513 744 3044 326 \r\nQ 2575 -91 1722 -91 \r\nQ 1428 -91 1123 -41 \r\nQ 819 9 494 109 \r\nL 494 744 \r\nQ 775 591 1075 516 \r\nQ 1375 441 1709 441 \r\nQ 2250 441 2565 725 \r\nQ 2881 1009 2881 1497 \r\nQ 2881 1984 2565 2268 \r\nQ 2250 2553 1709 2553 \r\nQ 1456 2553 1204 2497 \r\nQ 953 2441 691 2322 \r\nL 691 4666 \r\nz\r\n\" id=\"DejaVuSans-35\" transform=\"scale(0.015625)\"/>\r\n       </defs>\r\n       <use xlink:href=\"#DejaVuSans-35\"/>\r\n      </g>\r\n     </g>\r\n    </g>\r\n    <g id=\"ytick_7\">\r\n     <g id=\"line2d_9\">\r\n      <g>\r\n       <use style=\"stroke:#000000;stroke-width:0.8;\" x=\"34.240625\" xlink:href=\"#mf1b629062f\" y=\"28.453534\"/>\r\n      </g>\r\n     </g>\r\n     <g id=\"text_10\">\r\n      <!-- 6 -->\r\n      <g transform=\"translate(20.878125 32.252753)scale(0.1 -0.1)\">\r\n       <defs>\r\n        <path d=\"M 2113 2584 \r\nQ 1688 2584 1439 2293 \r\nQ 1191 2003 1191 1497 \r\nQ 1191 994 1439 701 \r\nQ 1688 409 2113 409 \r\nQ 2538 409 2786 701 \r\nQ 3034 994 3034 1497 \r\nQ 3034 2003 2786 2293 \r\nQ 2538 2584 2113 2584 \r\nz\r\nM 3366 4563 \r\nL 3366 3988 \r\nQ 3128 4100 2886 4159 \r\nQ 2644 4219 2406 4219 \r\nQ 1781 4219 1451 3797 \r\nQ 1122 3375 1075 2522 \r\nQ 1259 2794 1537 2939 \r\nQ 1816 3084 2150 3084 \r\nQ 2853 3084 3261 2657 \r\nQ 3669 2231 3669 1497 \r\nQ 3669 778 3244 343 \r\nQ 2819 -91 2113 -91 \r\nQ 1303 -91 875 529 \r\nQ 447 1150 447 2328 \r\nQ 447 3434 972 4092 \r\nQ 1497 4750 2381 4750 \r\nQ 2619 4750 2861 4703 \r\nQ 3103 4656 3366 4563 \r\nz\r\n\" id=\"DejaVuSans-36\" transform=\"scale(0.015625)\"/>\r\n       </defs>\r\n       <use xlink:href=\"#DejaVuSans-36\"/>\r\n      </g>\r\n     </g>\r\n    </g>\r\n    <g id=\"text_11\">\r\n     <!-- Members -->\r\n     <g transform=\"translate(14.798437 139.091875)rotate(-90)scale(0.1 -0.1)\">\r\n      <defs>\r\n       <path d=\"M 628 4666 \r\nL 1569 4666 \r\nL 2759 1491 \r\nL 3956 4666 \r\nL 4897 4666 \r\nL 4897 0 \r\nL 4281 0 \r\nL 4281 4097 \r\nL 3078 897 \r\nL 2444 897 \r\nL 1241 4097 \r\nL 1241 0 \r\nL 628 0 \r\nL 628 4666 \r\nz\r\n\" id=\"DejaVuSans-4d\" transform=\"scale(0.015625)\"/>\r\n       <path d=\"M 3328 2828 \r\nQ 3544 3216 3844 3400 \r\nQ 4144 3584 4550 3584 \r\nQ 5097 3584 5394 3201 \r\nQ 5691 2819 5691 2113 \r\nL 5691 0 \r\nL 5113 0 \r\nL 5113 2094 \r\nQ 5113 2597 4934 2840 \r\nQ 4756 3084 4391 3084 \r\nQ 3944 3084 3684 2787 \r\nQ 3425 2491 3425 1978 \r\nL 3425 0 \r\nL 2847 0 \r\nL 2847 2094 \r\nQ 2847 2600 2669 2842 \r\nQ 2491 3084 2119 3084 \r\nQ 1678 3084 1418 2786 \r\nQ 1159 2488 1159 1978 \r\nL 1159 0 \r\nL 581 0 \r\nL 581 3500 \r\nL 1159 3500 \r\nL 1159 2956 \r\nQ 1356 3278 1631 3431 \r\nQ 1906 3584 2284 3584 \r\nQ 2666 3584 2933 3390 \r\nQ 3200 3197 3328 2828 \r\nz\r\n\" id=\"DejaVuSans-6d\" transform=\"scale(0.015625)\"/>\r\n       <path d=\"M 3116 1747 \r\nQ 3116 2381 2855 2742 \r\nQ 2594 3103 2138 3103 \r\nQ 1681 3103 1420 2742 \r\nQ 1159 2381 1159 1747 \r\nQ 1159 1113 1420 752 \r\nQ 1681 391 2138 391 \r\nQ 2594 391 2855 752 \r\nQ 3116 1113 3116 1747 \r\nz\r\nM 1159 2969 \r\nQ 1341 3281 1617 3432 \r\nQ 1894 3584 2278 3584 \r\nQ 2916 3584 3314 3078 \r\nQ 3713 2572 3713 1747 \r\nQ 3713 922 3314 415 \r\nQ 2916 -91 2278 -91 \r\nQ 1894 -91 1617 61 \r\nQ 1341 213 1159 525 \r\nL 1159 0 \r\nL 581 0 \r\nL 581 4863 \r\nL 1159 4863 \r\nL 1159 2969 \r\nz\r\n\" id=\"DejaVuSans-62\" transform=\"scale(0.015625)\"/>\r\n       <path d=\"M 2834 3397 \r\nL 2834 2853 \r\nQ 2591 2978 2328 3040 \r\nQ 2066 3103 1784 3103 \r\nQ 1356 3103 1142 2972 \r\nQ 928 2841 928 2578 \r\nQ 928 2378 1081 2264 \r\nQ 1234 2150 1697 2047 \r\nL 1894 2003 \r\nQ 2506 1872 2764 1633 \r\nQ 3022 1394 3022 966 \r\nQ 3022 478 2636 193 \r\nQ 2250 -91 1575 -91 \r\nQ 1294 -91 989 -36 \r\nQ 684 19 347 128 \r\nL 347 722 \r\nQ 666 556 975 473 \r\nQ 1284 391 1588 391 \r\nQ 1994 391 2212 530 \r\nQ 2431 669 2431 922 \r\nQ 2431 1156 2273 1281 \r\nQ 2116 1406 1581 1522 \r\nL 1381 1569 \r\nQ 847 1681 609 1914 \r\nQ 372 2147 372 2553 \r\nQ 372 3047 722 3315 \r\nQ 1072 3584 1716 3584 \r\nQ 2034 3584 2315 3537 \r\nQ 2597 3491 2834 3397 \r\nz\r\n\" id=\"DejaVuSans-73\" transform=\"scale(0.015625)\"/>\r\n      </defs>\r\n      <use xlink:href=\"#DejaVuSans-4d\"/>\r\n      <use x=\"86.279297\" xlink:href=\"#DejaVuSans-65\"/>\r\n      <use x=\"147.802734\" xlink:href=\"#DejaVuSans-6d\"/>\r\n      <use x=\"245.214844\" xlink:href=\"#DejaVuSans-62\"/>\r\n      <use x=\"308.691406\" xlink:href=\"#DejaVuSans-65\"/>\r\n      <use x=\"370.214844\" xlink:href=\"#DejaVuSans-72\"/>\r\n      <use x=\"411.328125\" xlink:href=\"#DejaVuSans-73\"/>\r\n     </g>\r\n    </g>\r\n   </g>\r\n   <g id=\"line2d_10\">\r\n    <path clip-path=\"url(#p063cb63451)\" d=\"M 117.940625 43.807015 \r\nL 117.940625 17.554286 \r\n\" style=\"fill:none;stroke:#424242;stroke-linecap:square;stroke-width:2.7;\"/>\r\n   </g>\r\n   <g id=\"line2d_11\">\r\n    <path clip-path=\"url(#p063cb63451)\" d=\"M 285.340625 69.325714 \r\nL 285.340625 48.029157 \r\n\" style=\"fill:none;stroke:#424242;stroke-linecap:square;stroke-width:2.7;\"/>\r\n   </g>\r\n   <g id=\"patch_5\">\r\n    <path d=\"M 34.240625 224.64 \r\nL 34.240625 7.2 \r\n\" style=\"fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;\"/>\r\n   </g>\r\n   <g id=\"patch_6\">\r\n    <path d=\"M 369.040625 224.64 \r\nL 369.040625 7.2 \r\n\" style=\"fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;\"/>\r\n   </g>\r\n   <g id=\"patch_7\">\r\n    <path d=\"M 34.240625 224.64 \r\nL 369.040625 224.64 \r\n\" style=\"fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;\"/>\r\n   </g>\r\n   <g id=\"patch_8\">\r\n    <path d=\"M 34.240625 7.2 \r\nL 369.040625 7.2 \r\n\" style=\"fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;\"/>\r\n   </g>\r\n  </g>\r\n </g>\r\n <defs>\r\n  <clipPath id=\"p063cb63451\">\r\n   <rect height=\"217.44\" width=\"334.8\" x=\"34.240625\" y=\"7.2\"/>\r\n  </clipPath>\r\n </defs>\r\n</svg>\r\n",
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAXgAAAEGCAYAAABvtY4XAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjQuMSwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy/Z1A+gAAAACXBIWXMAAAsTAAALEwEAmpwYAAAOLElEQVR4nO3de4yldX3H8feHXRClFGJ24hpwXa2URC1yGbEGQpWmBGuFtppUCFVb0m2sAqbYrYakav2r0JreiHWLKFTEGiqGYAvSAqUogrOwBZZLSlEu204YQkAuKbjw7R9zFmaXZebszvzmDL95v5LJzLk9z5fN8t4nz3nOb1JVSJL6s8eoB5AktWHgJalTBl6SOmXgJalTBl6SOrVy1APMtGrVqlq7du2ox5Ckl42NGzc+XFVjO3tsSQV+7dq1TExMjHoMSXrZSHLfSz3mKRpJ6pSBl6ROGXhJ6pSBl6ROGXhJ6pSBl6ROGXhJ6pSBl6ROLakPOmlhrF+/nsnJSVavXs3ZZ5896nEkjYiB79Dk5CRbtmwZ9RiSRsxTNJLUKQMvSZ0y8JLUKQMvSZ0y8JLUKQMvSZ1qGvgk+ye5JMldSe5M8s6W+5MkvaD1dfB/BVxRVR9Ishfwqsb7kyQNNAt8kv2AY4CPAFTVM8AzrfYnSdpey1M0bwCmgK8kuSXJeUn2abg/SdIMLQO/Ejgc+GJVHQY8CXxqxyclWZdkIsnE1NRUw3EkaXlpGfgHgQer6sbB7UuYDv52qmpDVY1X1fjY2FjDcSRpeWl2Dr6qJpM8kOTgqrob+GXgjlb7Azjijy5sufmXjX0ffpwVwP0PP+6fCbDxnA+NegRpJFpfRXMacNHgCpp7gd9pvD9J0kDTwFfVJmC85T4kSTvnJ1klqVMGXpI6ZeAlqVMGXpI6ZeAlqVMGXpI6ZeAlqVMGXpI6ZeAlqVMGXpI6ZeAlqVOtFxvTCDy31z7bfZe0PBn4Dj150HGjHkHSEmDgJS2q9evXMzk5yerVqzn77LNHPU7XDLykRTU5OcmWLVtGPcay4JusktQpAy9JnTLwktQpAy9JnTLwktQpAy9JnTLwktQpAy9JnTLwktSppp9kTfJj4HHgWWBrVY233J8k6QWLsVTBu6vq4UXYj7Sk3f+nvzDqEZaErY+8GljJ1kfu888EWPMntzXbtqdoJKlTrQNfwHeTbEyybmdPSLIuyUSSiampqcbjSNLy0TrwR1fV4cB7gI8lOWbHJ1TVhqoar6rxsbGxxuNI0vLRNPBVtWXw/SHgUuDIlvuTJL2gWeCT7JNk320/A8cBt7fanyRpey2vonkNcGmSbfv5elVd0XB/kqQZmgW+qu4F3tZq+5Kk2XmZpCR1ysBLUqcMvCR1ajGWKpCk563a+zlg6+C7WjLwkhbVJw95dNQjLBueopGkThl4SeqUgZekThl4SeqUgZekThl4SeqUgZekThl4SeqUgZekThl4SeqUgZekThl4SeqUgZekThl4SeqUgZekThl4SeqUgZekThl4SeqUgZekTjUPfJIVSW5JcnnrfUmSXrAYR/BnAHcuwn4kSTM0DXySA4H3Aue13I8k6cVaH8H/JbAeeO6lnpBkXZKJJBNTU1ONx5Gk5aNZ4JP8GvBQVW2c7XlVtaGqxqtqfGxsrNU4krTsDBX4JEcl2Wfw8ylJvpDk9XO87CjghCQ/Br4BHJvka/OaVpI0tGGP4L8IPJXkbcCZwH8DF872gqr6dFUdWFVrgQ8CV1fVKfMZVpI0vGEDv7WqCjgR+NuqOhfYt91YkqT5Wjnk8x5P8mngFOCYJHsAew67k6q6Frh2l6eTJO22YY/gfwt4Gji1qiaBA4Fzmk0lSZq3OY/gk6wALq6qd2+7r6ruZ45z8JKk0ZrzCL6qngWeS7LfIswjSVogw56DfwK4LclVwJPb7qyq05tMJUmat2ED/63BlyTpZWKowFfVBUleCaypqrsbzyRJWgDDfpL1fcAm4IrB7UOTXNZwLknSPA17meRngSOBRwGqahPwxiYTSZIWxLCB/2lVPbbDfS+5QqQkafSGfZN1c5KTgRVJDgJOB77fbixJ0nwNewR/GvAWpj/NejHwE+ATjWaSJC2AYa+ieQo4K8mfTd+sx9uOJUmar2Gvonl7ktuAW5n+wNN/Jjmi7WiSpPkY9hz8l4E/qKr/AEhyNPAV4JBWg0mS5mfYc/DPbos7QFVdD2xtM5IkaSHMegSf5PDBj/+e5EtMv8FaTC8ffG3b0SRJ8zHXKZq/2OH2Z2b8XAs8iyRpAc0a+JlrwEuSXl6GepM1yf7Ah4C1M1/jcsGStHQNexXNPwM/AG7DJQok6WVh2MDvXVV/2HQSSdKCGvYyyX9I8ntJXpvk1du+mk4mSZqXYY/gnwHOAc7ihatnCpcMlqQla9jAnwm8qaoebjmMJGnhDHuK5h7gqV3ZcJK9k9w0WLdmc5LP7fp4kqTdNewR/JPApiTXML1kMDDnZZJPA8dW1RNJ9gSuT/IvVfWD3R9XkjSsYQP/7cHX0KqqgCcGN/ccfPnpV0laJMOuB39BklcCa6rq7mE3nmQFsBF4E3BuVd24k+esA9YBrFmzZthNS5LmMOx68O8DNgFXDG4fmuSyuV5XVc9W1aHAgcCRSd66k+dsqKrxqhofGxvbldklSbMY9k3WzwJHAo8CVNUmduESyap6FLgGOH5XhpMk7b5hA//Tqnpsh/tmXbIgydhgDRsGp3d+BbhrlyeUJO2WYd9k3ZzkZGBFkoOA04Hvz/Ga1wIXDM7D7wF8s6ou3/1RJUm7YtjAn8b0p1ifZvqXflwJfH62F1TVrcBh85pOkrTbhr2K5immA39W23EkSQtlrl/ZN+uVMlV1wsKOI0laKHMdwb8TeIDp0zI3Amk+kSRpQcwV+NVMX/1yEnAy8B3g4qra3HowSdL8zHqZ5OCDSldU1YeBX2R60bFrk3x8UaaTJO22Od9kTfIK4L1MH8WvBf4auLTtWJKk+ZrrTdYLgbcy/TtZP1dVty/KVJKkeZvrCP4UppcKPgM4PXn+PdYwvWDkzzacTZI0D7MGvqqGXcpAkrTEGHBJ6pSBl6ROGXhJ6pSBl6ROGXhJ6pSBl6ROGXhJ6pSBl6ROGXhJ6pSBl6ROGXhJ6pSBl6ROGXhJ6pSBl6RONQt8ktcluSbJHUk2Jzmj1b4kSS8256/sm4etwJlVdXOSfYGNSa6qqjsa7lOSNNDsCL6q/reqbh78/DhwJ3BAq/1Jkra3KOfgk6wFDgNu3Mlj65JMJJmYmppajHEkaVloHvgkPwP8E/CJqvrJjo9X1YaqGq+q8bGxsdbjSNKy0TTwSfZkOu4XVdW3Wu5LkrS9llfRBPgycGdVfaHVfiRJO9fyCP4o4LeBY5NsGnz9asP9SZJmaHaZZFVdD6TV9iVJs/OTrJLUKQMvSZ0y8JLUKQMvSZ0y8JLUKQMvSZ0y8JLUKQMvSZ0y8JLUKQMvSZ0y8JLUKQMvSZ0y8JLUKQMvSZ0y8JLUKQMvSZ0y8JLUKQMvSZ0y8JLUKQMvSZ0y8JLUKQMvSZ0y8JLUKQMvSZ1qFvgk5yd5KMntrfYhSXppLY/gvwoc33D7kqRZNAt8VV0HPNJq+5Kk2Y38HHySdUkmkkxMTU2NehxJ6sbIA19VG6pqvKrGx8bGRj2OJHVj5IGXJLVh4CWpUy0vk7wYuAE4OMmDSU5ttS9J0outbLXhqjqp1bYlSXPzFI0kdcrAS1KnDLwkdcrAS1KnDLwkdcrAS1KnDLwkdcrAS1KnDLwkdcrAS1KnDLwkdcrAS1KnDLwkdcrAS1KnDLwkdcrAS1KnDLwkdcrAS1KnDLwkdcrAS1KnDLwkdcrAS1KnDLwkdcrAS1KnmgY+yfFJ7k5yT5JPtdyXJGl7zQKfZAVwLvAe4M3ASUne3Gp/kqTttTyCPxK4p6rurapngG8AJzbcnyRphpUNt30A8MCM2w8C79jxSUnWAesGN59IcnfDmZaTVcDDox5iKciff3jUI+jF/Pu5zWcy3y28/qUeaBn4oVTVBmDDqOfoTZKJqhof9RzSzvj3c3G0PEWzBXjdjNsHDu6TJC2CloH/IXBQkjck2Qv4IHBZw/1JkmZodoqmqrYm+ThwJbACOL+qNrfan17E015ayvz7uQhSVaOeQZLUgJ9klaROGXhJ6pSB75BLRGipSnJ+koeS3D7qWZYDA98Zl4jQEvdV4PhRD7FcGPj+uESElqyqug54ZNRzLBcGvj87WyLigBHNImmEDLwkdcrA98clIiQBBr5HLhEhCTDw3amqrcC2JSLuBL7pEhFaKpJcDNwAHJzkwSSnjnqmnrlUgSR1yiN4SeqUgZekThl4SeqUgZekThl4SeqUgVf3krwmydeT3JtkY5IbkvzGAmz3XUkuX4gZpRYMvLqWJMC3geuq6o1VdQTTH/46cASzNPsVmdLOGHj17ljgmar6u213VNV9VfU3SVYkOSfJD5PcmuT34fkj82uTXJLkriQXDf6h2LbW/l1JbgZ+c9s2k+wzWOv8piS3JDlxcP9HklyW5Grg3xb1v1zLnkcU6t1bgJtf4rFTgceq6u1JXgF8L8l3B48dNnjt/wDfA45KMgH8PdP/aNwD/OOMbZ0FXF1Vv5tkf+CmJP86eOxw4JCqcplcLSoDr2UlybnA0cAzwH3AIUk+MHh4P+CgwWM3VdWDg9dsAtYCTwA/qqr/Gtz/NWDd4LXHASck+eTg9t7AmsHPVxl3jYKBV+82A+/fdqOqPpZkFTAB3A+cVlVXznxBkncBT8+461nm/n8lwPur6u4dtvUO4MndHV6aD8/Bq3dXA3sn+eiM+141+H4l8NEkewIk+fkk+8yyrbuAtUl+bnD7pBmPXQmcNuNc/WELMr00DwZeXavp1fR+HfilJD9KchNwAfDHwHnAHcDNg18C/SVmOVKvqv9j+pTMdwZvsj404+HPA3sCtybZPLgtjZSrSUpSpzyCl6ROGXhJ6pSBl6ROGXhJ6pSBl6ROGXhJ6pSBl6RO/T8N8DiOMWHU1QAAAABJRU5ErkJggg==\n"
     },
     "metadata": {
      "needs_background": "light"
     }
    }
   ],
   "source": [
    "fem_df = df.loc[df[\"Gender\"] == 1]\n",
    "print(fem_df[\"Members\"].mean())\n",
    "man_df = df.loc[df[\"Gender\"] == 0]\n",
    "print(man_df[\"Members\"].mean())\n",
    "sns.barplot(data=df, x=\"Gender\", y=\"Members\")"
   ]
  },
  {
   "source": [
    "### Популярное количество участников в год растет: подтвердилось, с каждым годом группы имеют все больше участников"
   ],
   "cell_type": "markdown",
   "metadata": {}
  },
  {
   "cell_type": "code",
   "execution_count": 92,
   "metadata": {},
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "<AxesSubplot:xlabel='Debut', ylabel='Members'>"
      ]
     },
     "metadata": {},
     "execution_count": 92
    },
    {
     "output_type": "display_data",
     "data": {
      "text/plain": "<Figure size 432x288 with 1 Axes>",
      "image/svg+xml": "<?xml version=\"1.0\" encoding=\"utf-8\" standalone=\"no\"?>\r\n<!DOCTYPE svg PUBLIC \"-//W3C//DTD SVG 1.1//EN\"\r\n  \"http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd\">\r\n<svg height=\"262.19625pt\" version=\"1.1\" viewBox=\"0 0 376.240625 262.19625\" width=\"376.240625pt\" xmlns=\"http://www.w3.org/2000/svg\" xmlns:xlink=\"http://www.w3.org/1999/xlink\">\r\n <metadata>\r\n  <rdf:RDF xmlns:cc=\"http://creativecommons.org/ns#\" xmlns:dc=\"http://purl.org/dc/elements/1.1/\" xmlns:rdf=\"http://www.w3.org/1999/02/22-rdf-syntax-ns#\">\r\n   <cc:Work>\r\n    <dc:type rdf:resource=\"http://purl.org/dc/dcmitype/StillImage\"/>\r\n    <dc:date>2021-04-21T15:35:02.219753</dc:date>\r\n    <dc:format>image/svg+xml</dc:format>\r\n    <dc:creator>\r\n     <cc:Agent>\r\n      <dc:title>Matplotlib v3.4.1, https://matplotlib.org/</dc:title>\r\n     </cc:Agent>\r\n    </dc:creator>\r\n   </cc:Work>\r\n  </rdf:RDF>\r\n </metadata>\r\n <defs>\r\n  <style type=\"text/css\">*{stroke-linecap:butt;stroke-linejoin:round;}</style>\r\n </defs>\r\n <g id=\"figure_1\">\r\n  <g id=\"patch_1\">\r\n   <path d=\"M 0 262.19625 \r\nL 376.240625 262.19625 \r\nL 376.240625 0 \r\nL 0 0 \r\nz\r\n\" style=\"fill:none;\"/>\r\n  </g>\r\n  <g id=\"axes_1\">\r\n   <g id=\"patch_2\">\r\n    <path d=\"M 34.240625 224.64 \r\nL 369.040625 224.64 \r\nL 369.040625 7.2 \r\nL 34.240625 7.2 \r\nz\r\n\" style=\"fill:#ffffff;\"/>\r\n   </g>\r\n   <g id=\"PolyCollection_1\">\r\n    <path clip-path=\"url(#p23b3963e6c)\" d=\"M 73.807898 130.039481 \r\nL 73.807898 186.517403 \r\nL 73.807898 130.039481 \r\nL 73.807898 130.039481 \r\nz\r\n\" style=\"fill:#1f77b4;fill-opacity:0.2;stroke:#1f77b4;stroke-opacity:0.2;\"/>\r\n    <path clip-path=\"url(#p23b3963e6c)\" d=\"M 98.156989 130.039481 \r\nL 98.156989 214.756364 \r\nL 98.156989 130.039481 \r\nL 98.156989 130.039481 \r\nz\r\n\" style=\"fill:#1f77b4;fill-opacity:0.2;stroke:#1f77b4;stroke-opacity:0.2;\"/>\r\n    <path clip-path=\"url(#p23b3963e6c)\" d=\"M 159.029716 186.517403 \r\nL 159.029716 214.756364 \r\nL 171.204261 186.517403 \r\nL 183.378807 158.278442 \r\nL 195.553352 166.346716 \r\nL 207.727898 180.86961 \r\nL 219.902443 172.397922 \r\nL 232.076989 160.631688 \r\nL 244.251534 148.865455 \r\nL 256.42608 144.158961 \r\nL 268.600625 155.925195 \r\nL 280.77517 144.158961 \r\nL 292.949716 122.97974 \r\nL 305.124261 137.853883 \r\nL 317.298807 106.42537 \r\nL 329.473352 114.636411 \r\nL 341.647898 136.556164 \r\nL 353.822443 101.800519 \r\nL 353.822443 17.083636 \r\nL 353.822443 17.083636 \r\nL 341.647898 102.886633 \r\nL 329.473352 69.282928 \r\nL 317.298807 68.37481 \r\nL 305.124261 66.720914 \r\nL 292.949716 73.561558 \r\nL 280.77517 119.928924 \r\nL 268.600625 111.213506 \r\nL 256.42608 111.575544 \r\nL 244.251534 120.626494 \r\nL 232.076989 101.800519 \r\nL 219.902443 137.099221 \r\nL 207.727898 113.096104 \r\nL 195.553352 142.141892 \r\nL 183.378807 158.278442 \r\nL 171.204261 17.083636 \r\nL 159.029716 186.517403 \r\nz\r\n\" style=\"fill:#1f77b4;fill-opacity:0.2;stroke:#1f77b4;stroke-opacity:0.2;\"/>\r\n   </g>\r\n   <g id=\"matplotlib.axis_1\">\r\n    <g id=\"xtick_1\">\r\n     <g id=\"line2d_1\">\r\n      <defs>\r\n       <path d=\"M 0 0 \r\nL 0 3.5 \r\n\" id=\"m2952ddb556\" style=\"stroke:#000000;stroke-width:0.8;\"/>\r\n      </defs>\r\n      <g>\r\n       <use style=\"stroke:#000000;stroke-width:0.8;\" x=\"49.458807\" xlink:href=\"#m2952ddb556\" y=\"224.64\"/>\r\n      </g>\r\n     </g>\r\n     <g id=\"text_1\">\r\n      <!-- 1995 -->\r\n      <g transform=\"translate(36.733807 239.238437)scale(0.1 -0.1)\">\r\n       <defs>\r\n        <path d=\"M 794 531 \r\nL 1825 531 \r\nL 1825 4091 \r\nL 703 3866 \r\nL 703 4441 \r\nL 1819 4666 \r\nL 2450 4666 \r\nL 2450 531 \r\nL 3481 531 \r\nL 3481 0 \r\nL 794 0 \r\nL 794 531 \r\nz\r\n\" id=\"DejaVuSans-31\" transform=\"scale(0.015625)\"/>\r\n        <path d=\"M 703 97 \r\nL 703 672 \r\nQ 941 559 1184 500 \r\nQ 1428 441 1663 441 \r\nQ 2288 441 2617 861 \r\nQ 2947 1281 2994 2138 \r\nQ 2813 1869 2534 1725 \r\nQ 2256 1581 1919 1581 \r\nQ 1219 1581 811 2004 \r\nQ 403 2428 403 3163 \r\nQ 403 3881 828 4315 \r\nQ 1253 4750 1959 4750 \r\nQ 2769 4750 3195 4129 \r\nQ 3622 3509 3622 2328 \r\nQ 3622 1225 3098 567 \r\nQ 2575 -91 1691 -91 \r\nQ 1453 -91 1209 -44 \r\nQ 966 3 703 97 \r\nz\r\nM 1959 2075 \r\nQ 2384 2075 2632 2365 \r\nQ 2881 2656 2881 3163 \r\nQ 2881 3666 2632 3958 \r\nQ 2384 4250 1959 4250 \r\nQ 1534 4250 1286 3958 \r\nQ 1038 3666 1038 3163 \r\nQ 1038 2656 1286 2365 \r\nQ 1534 2075 1959 2075 \r\nz\r\n\" id=\"DejaVuSans-39\" transform=\"scale(0.015625)\"/>\r\n        <path d=\"M 691 4666 \r\nL 3169 4666 \r\nL 3169 4134 \r\nL 1269 4134 \r\nL 1269 2991 \r\nQ 1406 3038 1543 3061 \r\nQ 1681 3084 1819 3084 \r\nQ 2600 3084 3056 2656 \r\nQ 3513 2228 3513 1497 \r\nQ 3513 744 3044 326 \r\nQ 2575 -91 1722 -91 \r\nQ 1428 -91 1123 -41 \r\nQ 819 9 494 109 \r\nL 494 744 \r\nQ 775 591 1075 516 \r\nQ 1375 441 1709 441 \r\nQ 2250 441 2565 725 \r\nQ 2881 1009 2881 1497 \r\nQ 2881 1984 2565 2268 \r\nQ 2250 2553 1709 2553 \r\nQ 1456 2553 1204 2497 \r\nQ 953 2441 691 2322 \r\nL 691 4666 \r\nz\r\n\" id=\"DejaVuSans-35\" transform=\"scale(0.015625)\"/>\r\n       </defs>\r\n       <use xlink:href=\"#DejaVuSans-31\"/>\r\n       <use x=\"63.623047\" xlink:href=\"#DejaVuSans-39\"/>\r\n       <use x=\"127.246094\" xlink:href=\"#DejaVuSans-39\"/>\r\n       <use x=\"190.869141\" xlink:href=\"#DejaVuSans-35\"/>\r\n      </g>\r\n     </g>\r\n    </g>\r\n    <g id=\"xtick_2\">\r\n     <g id=\"line2d_2\">\r\n      <g>\r\n       <use style=\"stroke:#000000;stroke-width:0.8;\" x=\"110.331534\" xlink:href=\"#m2952ddb556\" y=\"224.64\"/>\r\n      </g>\r\n     </g>\r\n     <g id=\"text_2\">\r\n      <!-- 2000 -->\r\n      <g transform=\"translate(97.606534 239.238437)scale(0.1 -0.1)\">\r\n       <defs>\r\n        <path d=\"M 1228 531 \r\nL 3431 531 \r\nL 3431 0 \r\nL 469 0 \r\nL 469 531 \r\nQ 828 903 1448 1529 \r\nQ 2069 2156 2228 2338 \r\nQ 2531 2678 2651 2914 \r\nQ 2772 3150 2772 3378 \r\nQ 2772 3750 2511 3984 \r\nQ 2250 4219 1831 4219 \r\nQ 1534 4219 1204 4116 \r\nQ 875 4013 500 3803 \r\nL 500 4441 \r\nQ 881 4594 1212 4672 \r\nQ 1544 4750 1819 4750 \r\nQ 2544 4750 2975 4387 \r\nQ 3406 4025 3406 3419 \r\nQ 3406 3131 3298 2873 \r\nQ 3191 2616 2906 2266 \r\nQ 2828 2175 2409 1742 \r\nQ 1991 1309 1228 531 \r\nz\r\n\" id=\"DejaVuSans-32\" transform=\"scale(0.015625)\"/>\r\n        <path d=\"M 2034 4250 \r\nQ 1547 4250 1301 3770 \r\nQ 1056 3291 1056 2328 \r\nQ 1056 1369 1301 889 \r\nQ 1547 409 2034 409 \r\nQ 2525 409 2770 889 \r\nQ 3016 1369 3016 2328 \r\nQ 3016 3291 2770 3770 \r\nQ 2525 4250 2034 4250 \r\nz\r\nM 2034 4750 \r\nQ 2819 4750 3233 4129 \r\nQ 3647 3509 3647 2328 \r\nQ 3647 1150 3233 529 \r\nQ 2819 -91 2034 -91 \r\nQ 1250 -91 836 529 \r\nQ 422 1150 422 2328 \r\nQ 422 3509 836 4129 \r\nQ 1250 4750 2034 4750 \r\nz\r\n\" id=\"DejaVuSans-30\" transform=\"scale(0.015625)\"/>\r\n       </defs>\r\n       <use xlink:href=\"#DejaVuSans-32\"/>\r\n       <use x=\"63.623047\" xlink:href=\"#DejaVuSans-30\"/>\r\n       <use x=\"127.246094\" xlink:href=\"#DejaVuSans-30\"/>\r\n       <use x=\"190.869141\" xlink:href=\"#DejaVuSans-30\"/>\r\n      </g>\r\n     </g>\r\n    </g>\r\n    <g id=\"xtick_3\">\r\n     <g id=\"line2d_3\">\r\n      <g>\r\n       <use style=\"stroke:#000000;stroke-width:0.8;\" x=\"171.204261\" xlink:href=\"#m2952ddb556\" y=\"224.64\"/>\r\n      </g>\r\n     </g>\r\n     <g id=\"text_3\">\r\n      <!-- 2005 -->\r\n      <g transform=\"translate(158.479261 239.238437)scale(0.1 -0.1)\">\r\n       <use xlink:href=\"#DejaVuSans-32\"/>\r\n       <use x=\"63.623047\" xlink:href=\"#DejaVuSans-30\"/>\r\n       <use x=\"127.246094\" xlink:href=\"#DejaVuSans-30\"/>\r\n       <use x=\"190.869141\" xlink:href=\"#DejaVuSans-35\"/>\r\n      </g>\r\n     </g>\r\n    </g>\r\n    <g id=\"xtick_4\">\r\n     <g id=\"line2d_4\">\r\n      <g>\r\n       <use style=\"stroke:#000000;stroke-width:0.8;\" x=\"232.076989\" xlink:href=\"#m2952ddb556\" y=\"224.64\"/>\r\n      </g>\r\n     </g>\r\n     <g id=\"text_4\">\r\n      <!-- 2010 -->\r\n      <g transform=\"translate(219.351989 239.238437)scale(0.1 -0.1)\">\r\n       <use xlink:href=\"#DejaVuSans-32\"/>\r\n       <use x=\"63.623047\" xlink:href=\"#DejaVuSans-30\"/>\r\n       <use x=\"127.246094\" xlink:href=\"#DejaVuSans-31\"/>\r\n       <use x=\"190.869141\" xlink:href=\"#DejaVuSans-30\"/>\r\n      </g>\r\n     </g>\r\n    </g>\r\n    <g id=\"xtick_5\">\r\n     <g id=\"line2d_5\">\r\n      <g>\r\n       <use style=\"stroke:#000000;stroke-width:0.8;\" x=\"292.949716\" xlink:href=\"#m2952ddb556\" y=\"224.64\"/>\r\n      </g>\r\n     </g>\r\n     <g id=\"text_5\">\r\n      <!-- 2015 -->\r\n      <g transform=\"translate(280.224716 239.238437)scale(0.1 -0.1)\">\r\n       <use xlink:href=\"#DejaVuSans-32\"/>\r\n       <use x=\"63.623047\" xlink:href=\"#DejaVuSans-30\"/>\r\n       <use x=\"127.246094\" xlink:href=\"#DejaVuSans-31\"/>\r\n       <use x=\"190.869141\" xlink:href=\"#DejaVuSans-35\"/>\r\n      </g>\r\n     </g>\r\n    </g>\r\n    <g id=\"xtick_6\">\r\n     <g id=\"line2d_6\">\r\n      <g>\r\n       <use style=\"stroke:#000000;stroke-width:0.8;\" x=\"353.822443\" xlink:href=\"#m2952ddb556\" y=\"224.64\"/>\r\n      </g>\r\n     </g>\r\n     <g id=\"text_6\">\r\n      <!-- 2020 -->\r\n      <g transform=\"translate(341.097443 239.238437)scale(0.1 -0.1)\">\r\n       <use xlink:href=\"#DejaVuSans-32\"/>\r\n       <use x=\"63.623047\" xlink:href=\"#DejaVuSans-30\"/>\r\n       <use x=\"127.246094\" xlink:href=\"#DejaVuSans-32\"/>\r\n       <use x=\"190.869141\" xlink:href=\"#DejaVuSans-30\"/>\r\n      </g>\r\n     </g>\r\n    </g>\r\n    <g id=\"text_7\">\r\n     <!-- Debut -->\r\n     <g transform=\"translate(186.410938 252.916562)scale(0.1 -0.1)\">\r\n      <defs>\r\n       <path d=\"M 1259 4147 \r\nL 1259 519 \r\nL 2022 519 \r\nQ 2988 519 3436 956 \r\nQ 3884 1394 3884 2338 \r\nQ 3884 3275 3436 3711 \r\nQ 2988 4147 2022 4147 \r\nL 1259 4147 \r\nz\r\nM 628 4666 \r\nL 1925 4666 \r\nQ 3281 4666 3915 4102 \r\nQ 4550 3538 4550 2338 \r\nQ 4550 1131 3912 565 \r\nQ 3275 0 1925 0 \r\nL 628 0 \r\nL 628 4666 \r\nz\r\n\" id=\"DejaVuSans-44\" transform=\"scale(0.015625)\"/>\r\n       <path d=\"M 3597 1894 \r\nL 3597 1613 \r\nL 953 1613 \r\nQ 991 1019 1311 708 \r\nQ 1631 397 2203 397 \r\nQ 2534 397 2845 478 \r\nQ 3156 559 3463 722 \r\nL 3463 178 \r\nQ 3153 47 2828 -22 \r\nQ 2503 -91 2169 -91 \r\nQ 1331 -91 842 396 \r\nQ 353 884 353 1716 \r\nQ 353 2575 817 3079 \r\nQ 1281 3584 2069 3584 \r\nQ 2775 3584 3186 3129 \r\nQ 3597 2675 3597 1894 \r\nz\r\nM 3022 2063 \r\nQ 3016 2534 2758 2815 \r\nQ 2500 3097 2075 3097 \r\nQ 1594 3097 1305 2825 \r\nQ 1016 2553 972 2059 \r\nL 3022 2063 \r\nz\r\n\" id=\"DejaVuSans-65\" transform=\"scale(0.015625)\"/>\r\n       <path d=\"M 3116 1747 \r\nQ 3116 2381 2855 2742 \r\nQ 2594 3103 2138 3103 \r\nQ 1681 3103 1420 2742 \r\nQ 1159 2381 1159 1747 \r\nQ 1159 1113 1420 752 \r\nQ 1681 391 2138 391 \r\nQ 2594 391 2855 752 \r\nQ 3116 1113 3116 1747 \r\nz\r\nM 1159 2969 \r\nQ 1341 3281 1617 3432 \r\nQ 1894 3584 2278 3584 \r\nQ 2916 3584 3314 3078 \r\nQ 3713 2572 3713 1747 \r\nQ 3713 922 3314 415 \r\nQ 2916 -91 2278 -91 \r\nQ 1894 -91 1617 61 \r\nQ 1341 213 1159 525 \r\nL 1159 0 \r\nL 581 0 \r\nL 581 4863 \r\nL 1159 4863 \r\nL 1159 2969 \r\nz\r\n\" id=\"DejaVuSans-62\" transform=\"scale(0.015625)\"/>\r\n       <path d=\"M 544 1381 \r\nL 544 3500 \r\nL 1119 3500 \r\nL 1119 1403 \r\nQ 1119 906 1312 657 \r\nQ 1506 409 1894 409 \r\nQ 2359 409 2629 706 \r\nQ 2900 1003 2900 1516 \r\nL 2900 3500 \r\nL 3475 3500 \r\nL 3475 0 \r\nL 2900 0 \r\nL 2900 538 \r\nQ 2691 219 2414 64 \r\nQ 2138 -91 1772 -91 \r\nQ 1169 -91 856 284 \r\nQ 544 659 544 1381 \r\nz\r\nM 1991 3584 \r\nL 1991 3584 \r\nz\r\n\" id=\"DejaVuSans-75\" transform=\"scale(0.015625)\"/>\r\n       <path d=\"M 1172 4494 \r\nL 1172 3500 \r\nL 2356 3500 \r\nL 2356 3053 \r\nL 1172 3053 \r\nL 1172 1153 \r\nQ 1172 725 1289 603 \r\nQ 1406 481 1766 481 \r\nL 2356 481 \r\nL 2356 0 \r\nL 1766 0 \r\nQ 1100 0 847 248 \r\nQ 594 497 594 1153 \r\nL 594 3053 \r\nL 172 3053 \r\nL 172 3500 \r\nL 594 3500 \r\nL 594 4494 \r\nL 1172 4494 \r\nz\r\n\" id=\"DejaVuSans-74\" transform=\"scale(0.015625)\"/>\r\n      </defs>\r\n      <use xlink:href=\"#DejaVuSans-44\"/>\r\n      <use x=\"77.001953\" xlink:href=\"#DejaVuSans-65\"/>\r\n      <use x=\"138.525391\" xlink:href=\"#DejaVuSans-62\"/>\r\n      <use x=\"202.001953\" xlink:href=\"#DejaVuSans-75\"/>\r\n      <use x=\"265.380859\" xlink:href=\"#DejaVuSans-74\"/>\r\n     </g>\r\n    </g>\r\n   </g>\r\n   <g id=\"matplotlib.axis_2\">\r\n    <g id=\"ytick_1\">\r\n     <g id=\"line2d_7\">\r\n      <defs>\r\n       <path d=\"M 0 0 \r\nL -3.5 0 \r\n\" id=\"m1f66c2d7b9\" style=\"stroke:#000000;stroke-width:0.8;\"/>\r\n      </defs>\r\n      <g>\r\n       <use style=\"stroke:#000000;stroke-width:0.8;\" x=\"34.240625\" xlink:href=\"#m1f66c2d7b9\" y=\"214.756364\"/>\r\n      </g>\r\n     </g>\r\n     <g id=\"text_8\">\r\n      <!-- 2 -->\r\n      <g transform=\"translate(20.878125 218.555582)scale(0.1 -0.1)\">\r\n       <use xlink:href=\"#DejaVuSans-32\"/>\r\n      </g>\r\n     </g>\r\n    </g>\r\n    <g id=\"ytick_2\">\r\n     <g id=\"line2d_8\">\r\n      <g>\r\n       <use style=\"stroke:#000000;stroke-width:0.8;\" x=\"34.240625\" xlink:href=\"#m1f66c2d7b9\" y=\"186.517403\"/>\r\n      </g>\r\n     </g>\r\n     <g id=\"text_9\">\r\n      <!-- 3 -->\r\n      <g transform=\"translate(20.878125 190.316621)scale(0.1 -0.1)\">\r\n       <defs>\r\n        <path d=\"M 2597 2516 \r\nQ 3050 2419 3304 2112 \r\nQ 3559 1806 3559 1356 \r\nQ 3559 666 3084 287 \r\nQ 2609 -91 1734 -91 \r\nQ 1441 -91 1130 -33 \r\nQ 819 25 488 141 \r\nL 488 750 \r\nQ 750 597 1062 519 \r\nQ 1375 441 1716 441 \r\nQ 2309 441 2620 675 \r\nQ 2931 909 2931 1356 \r\nQ 2931 1769 2642 2001 \r\nQ 2353 2234 1838 2234 \r\nL 1294 2234 \r\nL 1294 2753 \r\nL 1863 2753 \r\nQ 2328 2753 2575 2939 \r\nQ 2822 3125 2822 3475 \r\nQ 2822 3834 2567 4026 \r\nQ 2313 4219 1838 4219 \r\nQ 1578 4219 1281 4162 \r\nQ 984 4106 628 3988 \r\nL 628 4550 \r\nQ 988 4650 1302 4700 \r\nQ 1616 4750 1894 4750 \r\nQ 2613 4750 3031 4423 \r\nQ 3450 4097 3450 3541 \r\nQ 3450 3153 3228 2886 \r\nQ 3006 2619 2597 2516 \r\nz\r\n\" id=\"DejaVuSans-33\" transform=\"scale(0.015625)\"/>\r\n       </defs>\r\n       <use xlink:href=\"#DejaVuSans-33\"/>\r\n      </g>\r\n     </g>\r\n    </g>\r\n    <g id=\"ytick_3\">\r\n     <g id=\"line2d_9\">\r\n      <g>\r\n       <use style=\"stroke:#000000;stroke-width:0.8;\" x=\"34.240625\" xlink:href=\"#m1f66c2d7b9\" y=\"158.278442\"/>\r\n      </g>\r\n     </g>\r\n     <g id=\"text_10\">\r\n      <!-- 4 -->\r\n      <g transform=\"translate(20.878125 162.07766)scale(0.1 -0.1)\">\r\n       <defs>\r\n        <path d=\"M 2419 4116 \r\nL 825 1625 \r\nL 2419 1625 \r\nL 2419 4116 \r\nz\r\nM 2253 4666 \r\nL 3047 4666 \r\nL 3047 1625 \r\nL 3713 1625 \r\nL 3713 1100 \r\nL 3047 1100 \r\nL 3047 0 \r\nL 2419 0 \r\nL 2419 1100 \r\nL 313 1100 \r\nL 313 1709 \r\nL 2253 4666 \r\nz\r\n\" id=\"DejaVuSans-34\" transform=\"scale(0.015625)\"/>\r\n       </defs>\r\n       <use xlink:href=\"#DejaVuSans-34\"/>\r\n      </g>\r\n     </g>\r\n    </g>\r\n    <g id=\"ytick_4\">\r\n     <g id=\"line2d_10\">\r\n      <g>\r\n       <use style=\"stroke:#000000;stroke-width:0.8;\" x=\"34.240625\" xlink:href=\"#m1f66c2d7b9\" y=\"130.039481\"/>\r\n      </g>\r\n     </g>\r\n     <g id=\"text_11\">\r\n      <!-- 5 -->\r\n      <g transform=\"translate(20.878125 133.838699)scale(0.1 -0.1)\">\r\n       <use xlink:href=\"#DejaVuSans-35\"/>\r\n      </g>\r\n     </g>\r\n    </g>\r\n    <g id=\"ytick_5\">\r\n     <g id=\"line2d_11\">\r\n      <g>\r\n       <use style=\"stroke:#000000;stroke-width:0.8;\" x=\"34.240625\" xlink:href=\"#m1f66c2d7b9\" y=\"101.800519\"/>\r\n      </g>\r\n     </g>\r\n     <g id=\"text_12\">\r\n      <!-- 6 -->\r\n      <g transform=\"translate(20.878125 105.599738)scale(0.1 -0.1)\">\r\n       <defs>\r\n        <path d=\"M 2113 2584 \r\nQ 1688 2584 1439 2293 \r\nQ 1191 2003 1191 1497 \r\nQ 1191 994 1439 701 \r\nQ 1688 409 2113 409 \r\nQ 2538 409 2786 701 \r\nQ 3034 994 3034 1497 \r\nQ 3034 2003 2786 2293 \r\nQ 2538 2584 2113 2584 \r\nz\r\nM 3366 4563 \r\nL 3366 3988 \r\nQ 3128 4100 2886 4159 \r\nQ 2644 4219 2406 4219 \r\nQ 1781 4219 1451 3797 \r\nQ 1122 3375 1075 2522 \r\nQ 1259 2794 1537 2939 \r\nQ 1816 3084 2150 3084 \r\nQ 2853 3084 3261 2657 \r\nQ 3669 2231 3669 1497 \r\nQ 3669 778 3244 343 \r\nQ 2819 -91 2113 -91 \r\nQ 1303 -91 875 529 \r\nQ 447 1150 447 2328 \r\nQ 447 3434 972 4092 \r\nQ 1497 4750 2381 4750 \r\nQ 2619 4750 2861 4703 \r\nQ 3103 4656 3366 4563 \r\nz\r\n\" id=\"DejaVuSans-36\" transform=\"scale(0.015625)\"/>\r\n       </defs>\r\n       <use xlink:href=\"#DejaVuSans-36\"/>\r\n      </g>\r\n     </g>\r\n    </g>\r\n    <g id=\"ytick_6\">\r\n     <g id=\"line2d_12\">\r\n      <g>\r\n       <use style=\"stroke:#000000;stroke-width:0.8;\" x=\"34.240625\" xlink:href=\"#m1f66c2d7b9\" y=\"73.561558\"/>\r\n      </g>\r\n     </g>\r\n     <g id=\"text_13\">\r\n      <!-- 7 -->\r\n      <g transform=\"translate(20.878125 77.360777)scale(0.1 -0.1)\">\r\n       <defs>\r\n        <path d=\"M 525 4666 \r\nL 3525 4666 \r\nL 3525 4397 \r\nL 1831 0 \r\nL 1172 0 \r\nL 2766 4134 \r\nL 525 4134 \r\nL 525 4666 \r\nz\r\n\" id=\"DejaVuSans-37\" transform=\"scale(0.015625)\"/>\r\n       </defs>\r\n       <use xlink:href=\"#DejaVuSans-37\"/>\r\n      </g>\r\n     </g>\r\n    </g>\r\n    <g id=\"ytick_7\">\r\n     <g id=\"line2d_13\">\r\n      <g>\r\n       <use style=\"stroke:#000000;stroke-width:0.8;\" x=\"34.240625\" xlink:href=\"#m1f66c2d7b9\" y=\"45.322597\"/>\r\n      </g>\r\n     </g>\r\n     <g id=\"text_14\">\r\n      <!-- 8 -->\r\n      <g transform=\"translate(20.878125 49.121816)scale(0.1 -0.1)\">\r\n       <defs>\r\n        <path d=\"M 2034 2216 \r\nQ 1584 2216 1326 1975 \r\nQ 1069 1734 1069 1313 \r\nQ 1069 891 1326 650 \r\nQ 1584 409 2034 409 \r\nQ 2484 409 2743 651 \r\nQ 3003 894 3003 1313 \r\nQ 3003 1734 2745 1975 \r\nQ 2488 2216 2034 2216 \r\nz\r\nM 1403 2484 \r\nQ 997 2584 770 2862 \r\nQ 544 3141 544 3541 \r\nQ 544 4100 942 4425 \r\nQ 1341 4750 2034 4750 \r\nQ 2731 4750 3128 4425 \r\nQ 3525 4100 3525 3541 \r\nQ 3525 3141 3298 2862 \r\nQ 3072 2584 2669 2484 \r\nQ 3125 2378 3379 2068 \r\nQ 3634 1759 3634 1313 \r\nQ 3634 634 3220 271 \r\nQ 2806 -91 2034 -91 \r\nQ 1263 -91 848 271 \r\nQ 434 634 434 1313 \r\nQ 434 1759 690 2068 \r\nQ 947 2378 1403 2484 \r\nz\r\nM 1172 3481 \r\nQ 1172 3119 1398 2916 \r\nQ 1625 2713 2034 2713 \r\nQ 2441 2713 2670 2916 \r\nQ 2900 3119 2900 3481 \r\nQ 2900 3844 2670 4047 \r\nQ 2441 4250 2034 4250 \r\nQ 1625 4250 1398 4047 \r\nQ 1172 3844 1172 3481 \r\nz\r\n\" id=\"DejaVuSans-38\" transform=\"scale(0.015625)\"/>\r\n       </defs>\r\n       <use xlink:href=\"#DejaVuSans-38\"/>\r\n      </g>\r\n     </g>\r\n    </g>\r\n    <g id=\"ytick_8\">\r\n     <g id=\"line2d_14\">\r\n      <g>\r\n       <use style=\"stroke:#000000;stroke-width:0.8;\" x=\"34.240625\" xlink:href=\"#m1f66c2d7b9\" y=\"17.083636\"/>\r\n      </g>\r\n     </g>\r\n     <g id=\"text_15\">\r\n      <!-- 9 -->\r\n      <g transform=\"translate(20.878125 20.882855)scale(0.1 -0.1)\">\r\n       <use xlink:href=\"#DejaVuSans-39\"/>\r\n      </g>\r\n     </g>\r\n    </g>\r\n    <g id=\"text_16\">\r\n     <!-- Members -->\r\n     <g transform=\"translate(14.798437 139.091875)rotate(-90)scale(0.1 -0.1)\">\r\n      <defs>\r\n       <path d=\"M 628 4666 \r\nL 1569 4666 \r\nL 2759 1491 \r\nL 3956 4666 \r\nL 4897 4666 \r\nL 4897 0 \r\nL 4281 0 \r\nL 4281 4097 \r\nL 3078 897 \r\nL 2444 897 \r\nL 1241 4097 \r\nL 1241 0 \r\nL 628 0 \r\nL 628 4666 \r\nz\r\n\" id=\"DejaVuSans-4d\" transform=\"scale(0.015625)\"/>\r\n       <path d=\"M 3328 2828 \r\nQ 3544 3216 3844 3400 \r\nQ 4144 3584 4550 3584 \r\nQ 5097 3584 5394 3201 \r\nQ 5691 2819 5691 2113 \r\nL 5691 0 \r\nL 5113 0 \r\nL 5113 2094 \r\nQ 5113 2597 4934 2840 \r\nQ 4756 3084 4391 3084 \r\nQ 3944 3084 3684 2787 \r\nQ 3425 2491 3425 1978 \r\nL 3425 0 \r\nL 2847 0 \r\nL 2847 2094 \r\nQ 2847 2600 2669 2842 \r\nQ 2491 3084 2119 3084 \r\nQ 1678 3084 1418 2786 \r\nQ 1159 2488 1159 1978 \r\nL 1159 0 \r\nL 581 0 \r\nL 581 3500 \r\nL 1159 3500 \r\nL 1159 2956 \r\nQ 1356 3278 1631 3431 \r\nQ 1906 3584 2284 3584 \r\nQ 2666 3584 2933 3390 \r\nQ 3200 3197 3328 2828 \r\nz\r\n\" id=\"DejaVuSans-6d\" transform=\"scale(0.015625)\"/>\r\n       <path d=\"M 2631 2963 \r\nQ 2534 3019 2420 3045 \r\nQ 2306 3072 2169 3072 \r\nQ 1681 3072 1420 2755 \r\nQ 1159 2438 1159 1844 \r\nL 1159 0 \r\nL 581 0 \r\nL 581 3500 \r\nL 1159 3500 \r\nL 1159 2956 \r\nQ 1341 3275 1631 3429 \r\nQ 1922 3584 2338 3584 \r\nQ 2397 3584 2469 3576 \r\nQ 2541 3569 2628 3553 \r\nL 2631 2963 \r\nz\r\n\" id=\"DejaVuSans-72\" transform=\"scale(0.015625)\"/>\r\n       <path d=\"M 2834 3397 \r\nL 2834 2853 \r\nQ 2591 2978 2328 3040 \r\nQ 2066 3103 1784 3103 \r\nQ 1356 3103 1142 2972 \r\nQ 928 2841 928 2578 \r\nQ 928 2378 1081 2264 \r\nQ 1234 2150 1697 2047 \r\nL 1894 2003 \r\nQ 2506 1872 2764 1633 \r\nQ 3022 1394 3022 966 \r\nQ 3022 478 2636 193 \r\nQ 2250 -91 1575 -91 \r\nQ 1294 -91 989 -36 \r\nQ 684 19 347 128 \r\nL 347 722 \r\nQ 666 556 975 473 \r\nQ 1284 391 1588 391 \r\nQ 1994 391 2212 530 \r\nQ 2431 669 2431 922 \r\nQ 2431 1156 2273 1281 \r\nQ 2116 1406 1581 1522 \r\nL 1381 1569 \r\nQ 847 1681 609 1914 \r\nQ 372 2147 372 2553 \r\nQ 372 3047 722 3315 \r\nQ 1072 3584 1716 3584 \r\nQ 2034 3584 2315 3537 \r\nQ 2597 3491 2834 3397 \r\nz\r\n\" id=\"DejaVuSans-73\" transform=\"scale(0.015625)\"/>\r\n      </defs>\r\n      <use xlink:href=\"#DejaVuSans-4d\"/>\r\n      <use x=\"86.279297\" xlink:href=\"#DejaVuSans-65\"/>\r\n      <use x=\"147.802734\" xlink:href=\"#DejaVuSans-6d\"/>\r\n      <use x=\"245.214844\" xlink:href=\"#DejaVuSans-62\"/>\r\n      <use x=\"308.691406\" xlink:href=\"#DejaVuSans-65\"/>\r\n      <use x=\"370.214844\" xlink:href=\"#DejaVuSans-72\"/>\r\n      <use x=\"411.328125\" xlink:href=\"#DejaVuSans-73\"/>\r\n     </g>\r\n    </g>\r\n   </g>\r\n   <g id=\"line2d_15\">\r\n    <path clip-path=\"url(#p23b3963e6c)\" d=\"M 49.458807 186.517403 \r\nL 61.633352 130.039481 \r\nL 73.807898 148.865455 \r\nL 85.982443 101.800519 \r\nL 98.156989 172.397922 \r\nL 122.50608 158.278442 \r\nL 146.85517 214.756364 \r\nL 159.029716 200.636883 \r\nL 171.204261 115.92 \r\nL 183.378807 158.278442 \r\nL 195.553352 154.244304 \r\nL 207.727898 146.982857 \r\nL 219.902443 154.748571 \r\nL 232.076989 132.392727 \r\nL 244.251534 134.745974 \r\nL 256.42608 128.953367 \r\nL 268.600625 134.745974 \r\nL 280.77517 132.056549 \r\nL 292.949716 100.623896 \r\nL 305.124261 105.695549 \r\nL 317.298807 87.392886 \r\nL 329.473352 93.243259 \r\nL 341.647898 120.264456 \r\nL 353.822443 59.442078 \r\n\" style=\"fill:none;stroke:#1f77b4;stroke-linecap:square;stroke-width:1.5;\"/>\r\n   </g>\r\n   <g id=\"patch_3\">\r\n    <path d=\"M 34.240625 224.64 \r\nL 34.240625 7.2 \r\n\" style=\"fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;\"/>\r\n   </g>\r\n   <g id=\"patch_4\">\r\n    <path d=\"M 369.040625 224.64 \r\nL 369.040625 7.2 \r\n\" style=\"fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;\"/>\r\n   </g>\r\n   <g id=\"patch_5\">\r\n    <path d=\"M 34.240625 224.64 \r\nL 369.040625 224.64 \r\n\" style=\"fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;\"/>\r\n   </g>\r\n   <g id=\"patch_6\">\r\n    <path d=\"M 34.240625 7.2 \r\nL 369.040625 7.2 \r\n\" style=\"fill:none;stroke:#000000;stroke-linecap:square;stroke-linejoin:miter;stroke-width:0.8;\"/>\r\n   </g>\r\n  </g>\r\n </g>\r\n <defs>\r\n  <clipPath id=\"p23b3963e6c\">\r\n   <rect height=\"217.44\" width=\"334.8\" x=\"34.240625\" y=\"7.2\"/>\r\n  </clipPath>\r\n </defs>\r\n</svg>\r\n",
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAXgAAAEGCAYAAABvtY4XAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjQuMSwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy/Z1A+gAAAACXBIWXMAAAsTAAALEwEAmpwYAABODUlEQVR4nO2dd5hb13mn3w91ZjCY3thmhp0UxU51y5bcu2Q7jh03SU5Wm43tOF47u944u944m2RT1tnYieN4XSS5xk0uimNLtmy5UI0UKVLsfYac3gcd996zfwAYTgFmMBhcDACe93nwEAQu7jlnAHw49yu/T5RSaDQajab8cCz3BDQajUZjD9rAazQaTZmiDbxGo9GUKdrAazQaTZmiDbxGo9GUKa7lnsB0mpqaVGdn53JPQ6PRaEqGgwcPDimlmtM9V1QGvrOzkwMHDiz3NDQajaZkEJFLmZ7TLhqNRqMpU7SB12g0mjJFG3iNRqMpU7SB12g0mjJFG3iNRqMpU2w18CLyQRF5QUSOicgf2TmWRqPRaGZim4EXkeuB/wDcCOwEXi8iG+waT6PRaDQzsXMHvxV4WikVUkoZwBPAm20cT1PmxAxruaeg0eQdy1LETXs+23Ya+BeA20WkUUSqgNcCa2YfJCL3i8gBETkwODho43Q0pc6pvglMS/cv0JQX4+E4PaNhW85tm4FXSp0A/hp4FPgxcBgw0xz3OaXUPqXUvubmtNW2Gg2mpYgaFoald/Ga8iIcM4mV4A4epdQXlFJ7lVIvBkaB03aOpylfDMsiZlgYpt7Ba8qLYMyw7dx2Z9G0JP9tJ+F//5qd42nKF8uCmGlhaBeNpsyYjNpn4O0WG/uOiDQCceB9Sqkxm8fTlCmGZRE3FIZNl7IazXIRihr4vfaYYlsNvFLqdjvPr7l2MC1FzDR1kFVTVsRNi6iNmxZdyaopCUxLYViKSHxOnF6jKVlihkXcxvRfbeA1JYFpKZwOIapz4TVlRNSwiNt4VaoNvKYkiBoWbodDG3hNWRGNm4iNXkdt4DUlQcw08bgcROPawGvKh0DUwOOyzwxrA68pCeKGwu10EDW1D15TPgRjBm6nNvCaa5yoYeFxOoibFkrpTBpNeRCIaAOv0RA3LZwOQSl0sZOmLIgnC/ccYt8Y2sBrSoKUgRfQufCasiBmWNho2wFt4DUlQty0cAio5H2NptQphPy1NvCaose0FJYCEb2D15QPUcNExN49vDbwmqLHsK5eyiq0D15THkxGDFx2OuDRBl5TAkzfsQtia2m3RlMo7E6RBG3gNSWAaSlSJt7pECK62ElTBgSjpjbwGo1pKVKuyoQejS520pQ2hmkRS2aG2Yk28Jqix7AUqdomlxYc05QBUcMqiPHVBl5T9FiWmgqyOh1CVEsGa0qcQqRIgjbwmhIgalg4kj4ap0Nsa1Cs0RSKQrkZtYHXFD1Rw5wy8A4RDEth6VRJTQkTiNqfQQPawGtKgHiaYFTc0rt4TelSFgZeRD4kIsdE5AUR+bqIVNg5nqY8iRlqhoHX1ayaUqcQKZJgo4EXkVXAHwL7lFLXA07g7XaNpylfEjo0M3fwuppVU6oYppX2qtQO7P4JcQGVIuICqoAem8fTlCGz84UVYJjawGtKk0ImCdhm4JVSV4C/A7qAXmBcKfXo7ONE5H4ROSAiBwYHB+2ajqaEMZJKkjMe0z54TYlSCJngFHa6aOqBu4C1wErAJyLvmn2cUupzSql9Sql9zc3Ndk1HU6IYpjWlJJnCIaJ7s2pKlkgB6zjsdNG8HLiglBpUSsWB7wK32jiepgwxlZqz23FpuQJNCROIGrgchUlgtHOULuBmEamSxPbrZcAJG8fTlCHpsmWcDilYJaBGk28KlUED9vrgnwa+DTwHHE2O9Tm7xtOUJ8Y0JckUDhEi2sBrSpRA1MDjKoyBd9l5cqXUx4GP2zmGpryZrkOTwqX1aDQlSiFTJEFXsmqKnES++8wvg9aj0ZQqMbNwGTSgDbymyDEthVIznTQigqUSuyGNppQodOxIG3hNURMz0l/OCqKrWTUlR6Fdi9rAa4qaqGGmNfAKpQ28puSYLGCKJGgDrylyYml0aCApOKblCjQlRiFTJEEbeE2RE5+lJJlCoSWDNaVHKGbgdhYuzKoNvKaoyZRSJogOsmpKCtNSROIWLr2D12gSTG/XNx2nbr6tKTESncnmPj4ciDIciNoypjbwmqJFKYVhzVWSBHCKNvCa0iJTiuT3Dvfwuw8dmJMOnA+0gdcULYkc+JlKkimcDimoKp9Gs1RihjVHdgPgwnCQjS3VaT/nS0UbeE3Rkk5JMoUWHNOUGoGogXtWimTctOgeCbGxxW/LmNrAa4qW+fquJnbw2sBrSofJyNxG210jIeKmYlNrtS1jagOvKVrSKUmmcDoEw7KwdLGTpkRIlyJ5diAAwMZWvYPXXGOYZmYXTQpdzaopBUxLETXmpkieGwxQ5XGysrbClnG1gdcULabKvIOHZDWrNvCaEiBTH9azAwE6G322BFhBG3hNEWNaCplnD6+rWTWRuEn3SIiBiQhjoRihmFGUBXDpEgLipsWFoSDrmny2jWtrww+NZilE4+kLQ6aj9WiuTeKmRe9YmPNDQYTEj33qo6IAt9OBz+vE53Hh87io8DjxuBx4nA7cTrFtx5yJqGHOuRrtGglhWIq12sBrrkViWXS+0T74awvLUgwFopwZCGCYFnWVnrSfEdNSxA2LoWiMXjPC9Ax0h4DH5UwYe5cDb9Lwe10OXE4HTofgdAiuaf8uVV4gXaPtVIBVG3jNNclCBt6BEDN0sdO1wlgoxtn+AJNRg9pKN+4Kd8ZjE0baCWkOUUphWgpTKUJRg0A4Ee+xLDX1Q3D1U5e4t2tNHbVVmcdbiGDMnJNBc24wgM/jpLXGm/N5F0IbeE3REsugQ5PC6RAi2sCXPcGowYWhAAOTUao9bpqql2YQRQSXU7I2fpOROD3j4aUZ+Egcr8s547EzAwHW21TBmsK2IKuIbBaRw9NuEyLyR3aNpyk/DDO9VHAKLThW3kQNk7MDAZ69OMJ4yKC5uoJKj3PhF+YZn9fFwGSEeI7BW9NSRGalSMZNi4tDQTY021PglMK2HbxS6hSwC0BEnMAV4GG7xtOUH1HDwufJ/BHVcgXliWkpesfDXBgMooD6Ks+8V3J24xBBKRgNxmipWXy+eroUyVSAdUNLiRr4WbwMOKeUulSg8TQlTkpJcsEdvJYrKCuihsnz3WOEYia1Fe6CaqfPR6XbSe94OGcDP5tUgHW9zTv4Qv313g58Pd0TInK/iBwQkQODg4MFmo6m2EkpSc5HwkWjffDlxETYIBg1afR5i8a4A1R5XIyG4jkpmEbNuSmSZwcSAdYVNlWwprD9LygiHuCNwLfSPa+U+pxSap9Sal9zc7Pd09GUCIa1sEyBQwRL6WrWcmIkGKXCVXg/e7aMBGKLfk0gkiZFctD+ACsUZgf/GuA5pVR/AcbSlAlWls0PBDB0NWtZoJRicDK2LIHUbKj2urg8Glr062anSBYqwAqFMfC/Qwb3jEaTiWwLmBSJbBtN6ROKmZgLxF2WE6/LSShuEogai3pdMDpTJrhQAVaw2cCLiA94BfBdO8fRlB/ZShAkdvDawJcDgUh8XnG5YsDpEAYnI1kfb1mKSNycYeALFWAFmw28UiqolGpUSo3bOY6m/JhPC346iR28dtGUA4OBWFH73wGqPS6ujEay7kMQM+emSBYqwApaTVJTpJiWNa+SZAotGVweWJZiNFi8/vcULqeDuGkxEYlndXy6NN5CBVhBG3hNkZKQKVj4OIfo5tvlQDBmYCq1rAVN2eJ1OeifyM5NMztFspABVtAGXlOkRI3sgm0uh0PLFZQBE+F4SRh3SEgX9E9Es5IuCEXNGSmSl4YLF2AFbeA1RUo8y2wKhwNt4MuAoUBx579PJ1F/oRgPL+ymmYzO7MN6bjARYNUGXnNNs5CSZAotV1D6GKbFWDhOhbt0zFGl28mVsfCCx81OkTw7EMDnddKWg+RBLpTOX1RzTRGLL8JFY2offCkTjJqgKHiXpaVQ6XYyEojNG/+xLEU0bs008IMB1jcXJsAK2sBripS4lV3AzSGJwJXKsvJVU3yMh2MFNe7DgeiSM69EBIfML10Qm+WjL3SAFbSB1xQh2ShJppCklKsudipdBiajVBUoPfKFK+O898Fn+U9fPcijx/ty1niHRLD1ylhm6YJEbOjq57LQAVbQBl5ThGSjJDkdnQtfusQMi8moMafbkR1E4ib/8LMzNFV7qfI4+fTjZ7n/ywf54fM9OamSel1OglGTYAbpgtmNtgsdYAXdsk9ThCSUJLO/ZFckLn8r3KWRhaG5SjBqLOKdXhoPPXmRvokIf/Wm7WxbWcPBrlG+eeAyn/vVeb55oJu7dq3itdvbqJqnycxsnA5haDKKzzv3NbNTJAsdYAVt4DVFSGI3nv2OXO/gS5eRYGyOlK4dvHBlnB8e6eX1O1Zw/apaAPZ1NLC3vZ4Xeib45oFuHnzyIt9+rps37FjJG3aspKZy4R6sPq+Ly2Nh1jRU4ZjlUgzOSpEsdIAVtIHXFCHmIgOmiR28NvClyGDAfv97JG7yqcfP0FZTwT23dM54TkTYvqqW7atqOd0/yTcPdPONZ7v53uErvOb6Fbxp1yrqfZ6M53Y7HUxEYkxGjDlNuQPTUiRTAda7dq3M+/rmQxt4TdFhmtkJjaVwIFpwrASJxE0icXPevrv54MtPXaJ3PMJfvmn7vG68Ta1+/vR113FxKMi3Dl7m+4ev8MiRHl5xXRvvuLGd2gw7erfDSf9kZIaBT6hIWlQmx0sFWAuhIDkdHWTVFB2LzYhxOISILnYqORarq54Lx3rG+eHzPbx++wq2J10zC9HZ5OOPX7WZf37nXu7Y3MJPjvXxmV+czXi8z+uibzwyY5ORSpFMuWOWI8AK2sBripBslSRT6N6spclIMIbHxr6rqayZlhov75nlmsmGlXWV/OFLN/KmXat48twwvePpK1edjrnSBbNTJJcjwArawGuKkFiWQmMpXA7RejQlRqI9X3TKhWEHKdfMB1+6cUkyxK/fsQKnQ/jB4Z6Mx1S4nPRMky6IGdYMN+PZgQAbChxghSwNvIjcluzOhIi8S0Q+KSId9k5Nc60SzVIqOEVCj0bv4EuJcNwkbli4bNrBp1wzr9u+gu2r65Z0rsZqLy/e1MxjJ/qZzKADX+VxMhS8Kl0QjF5ttB03LS4OBwvunoHsd/D/DIREZCfwYeAc8JBts9Jc0yx2B+90yJyycE1xMxmOY1cCfCRu8qmfnaHZ752TNZMrd+9aRdSw+PcX+tI+L5JwKo4GE9IF01MklyvACtkbeEMlxD7uAv5RKfVPgN++aWmuZeJWdkqSKRwiGJbKuo2aZvkZDtrXnu+rT1+iZzzCB1+2NNfMdNY2+di9po5HjvRklDfweVxTCpPTVSSXK8AK2Rv4SRH5b8C7gH8TEQewYBWAiNSJyLdF5KSInBCRW5YyWc21QbZKkrOJW3oXXwpYlmI4ELOl8vh47wTfP9zDa7evYMcSXTOzuXv3KkZDcZ44NZj2+Qq3k0DUIBA1CBsmruRn+MwyBVghewP/NiAK/K5Sqg9YDfxtFq/7B+DHSqktwE7gRE6z1FxTxMzF7eBBV7OWEqn2fOl+xH91ZpDfffBZHtx/kYEs2+KliBom//DT0zT7vdybJ9fMdHavqaOzsYrvHb6SUb3UKULPaAiUXE2RXKYAK2Rh4EXECXxdKfVJpdSvAJRSXUqpeX3wIlILvBj4QvI1MaXU2NKnXPwcuTzGh/71sC6+yQGlVMYv/0KUm6KkUmrKp1tOTIYz689857nLBKIG3z10mf/w5QP8r387znOXRrGyqG7+ylNd9IxH+MM8umamIyLcvWsVl0ZCHOoaS3uMz+tiYDJKKkVyOQOskIWBV0qZgJU02IthLTAIfElEDonI51OZONMRkftF5ICIHBgcTH/pU2p8/ZkuHj50hfNDweWeSslhLFJJMoUCjDKTK5iIGDzfPcZYqLyM/GAgktY9c34wwLnBIO+6qYP/9559vGXPak72TfLxHx7j979ykO8dvkIgkr446kTvBN8/fIXXXN/Gzjy7Zqbz4k3NNFR5ePjwlbTPu50O4tMqsbMJsMZMi5oKe6p5s3XRBICjIvIFEflU6rbAa1zAHuCflVK7gSDw0dkHKaU+p5Tap5Ta19zcvKjJFyv7zw0DcKpvcplnUnqYi1SSnI5RZj74oclEY4qTvRNlczVoWoqxkJE2//2x4/24ncIdm5tp8Vfwnls6+dK9N/DhV2yirtLNF359gXseeIZPPX5mKnAJSddMMmvm3ls7bZ2/2+ng9TtWcLh7jAtDgbTHVHtdU/ILZwfmD7CmXD21VZn1bpZCtj8b303eFsNl4LJS6unk/79NGgNfblweDXFpONEE4HS/NvCLxbQUi1OiSeCQ8urNalmK3vEwjdVexsMxukZCrFuGNLt8E4gaKNQcf3TUMPn56QFuWdeIv+Jq/obb6eCOzS3csbmF84MBfnS0l1+cHuSx4/1sbvXzuh0rODsQ4MpYmP911/WLkvrNlVdf38Y3D3bzvUM9fOgVm+Y8P/3q5Ozg/AHWcNykvsptm9R1Vn8NpdSDIlIJtCulTmX5mj4R6RaRzcnXvAw4voS5lgRPJnfvVR4nJ/UOftEktOAXj6vM5AomInHiZiIWUVfl4eJQkCa/l5qKhSVsi5mJcDxtAP3Jc8MEoyavvK4t42vXNVfz/pdu5N7b1vL4yX5+dLSPTz52GoBXb2tj55o6u6Y9A3+Fm5dvbeXfX+jjPbd00FjtzXjsQgHWcNy09Yc720rWNwCHgR8n/79LRH6QxUs/AHxVRI4Au4C/zG2apcP+c8M0+jzcsblZ7+BzwLJy2b+nqlnLZwc/MBmd0mlxiODzujjVO1HymUIDE+nlCR470U9rjZftqxcO9VV7Xbxx5yo+8849/Pld1/PWvau577bO7OcwGWE8vLS4xl07V6GU4odHejMes1CANRU4rquy70c7Wx/8/wRuBMYAlFKHgXULvUgpdTjpX9+hlLpbKTWa4zxLAqUU+88NcfP6Rra01dA1EiIUs18xr5zINRPG6RCiZeSn7p+IzOgSVOVxEYiaXBnN3AO02ImbFpPR+Bx3RN94hCOXx3n51tZFF7jtWlPHe27pzNo1E4oZNPg8NPg8DE5Gcu7J2lZbwS3rGvnxC70Zv+MLBVhDMZMWv3eqIMoOsj1zXCk1Puux8vg25ZHzQ0H6J6Lctr6JTa1+lLoaZNFkh2EuTkkyhVOEWJno0UyE45jW3FTR+ioP5waDGXuAFjuBSPr0yJ+e6EeAl21ptX0O4bjJmoYqtq6o4fpVtQSjBhMZ9GUW4u7dqwjGTH56oj/t86nv/saW9EX/UcOkrbYyp7GzJVsDf0xE3gE4RWSjiHwa2G/jvEqSVPbMresb2dyWeFN1Js3iiJm5VbGWkx5N30QEr3OuG8PpECrcTk72TZSkLMNoKIZzVns+01L87GQ/u9vrafZn9mXng9SPZl2lGxGhpaaCG9Y2UFvpYjCw+N38lrYatrb5+f7hnrSus7ODAaq9Llpr5q4rNRe70iNTZGvgPwBsI1HN+nVgAvgjm+ZUsjx5boiVtRV0NFbR3lCF1+XQfvhFEjMsnDlU/IkIlqLk0wkN02JwMkqVN31WRbXXxUQkTt/44qo8l4JSCtNSGKaVkMHNpVABEuuaVYB0qHuUoUCMV15n/+59MhJnRW3lDAXLCreTbStruX5lLYFofIameza8afcqBiaj7D83NOe5cwMB1jf70gZYg1GDFr/XNjXNFNlm0YSAj4nIXyf+q7TVmoVlKZ48N8xLt7QiIjgFNrZWc6pfu2gWQ8ywyLUHs5AQHbNJw6ogjIfjWErN64uuq/BwemCSep9nSRWbhmnRNRJiMpKQDrCSgm2mUlgq0XhFqUQRmQhTBWj1VR42t/kXldoXiZuE4+YcX/mjx/qprXRz49qGnNeRLaZSaXfTqd18TaWb0/2TDAai1Fe6szK+N65tZEVtBd87fIUXbWiaMuapAGumHqwx06K1ANo02WbR3CAiR4EjJAqenheRvfZOrbQ40TfBaCjOresbpx7b1OrnVN/EMs6q9IjmoEOTQqEKKldgWSrvWS294xG8C/xCuZwO3A4HZwYmc95NB6MGh7vG6B4JETMsrGSBmcvpoMLlxOdxUVvpocHnpdHnpaEq8W+jz0sgavDsxRGGJrO/ikgXNxgLxXjm4gh3bm62NdAIiR+Yao9rRo79bCrcTravquW6Nj8TkTgTWezmnQ7hrp0rOd0f4Hjv1e96KsC6IY3/3bQUbqcUJOU127/qF4A/UEp1KqU6gfcBX7JtViVIKv/91g1XDfyWNj/9E9GyKzW3E2ORWvDTERINuwvF5dFQXl1wMcNiKBDFl8WuvKbSzXAgxuBkdNHjDExEePbiCIalaPB5qXA78bqceFwO3E4HLqcDp0My/tDWVLipcrs4cmWcs/2TWbnFhtO05/v5qQFMS/GKeXLf80UwZrCmYeGApojQVlfJjWsbqa5wMRSILri+l21txe918fChq/IFUxWsaTJoAlGDFbWVOHL8nC+GbA28mRIaA1BK/RoozVC+Tew/N8y6Jh8rpkXFN7Umfr1PazdN1uSiJJlCUTjJYNNSdI2E6R0P5615dGojkK3qYG2lm1N9k1NdhBbCMC1O9k3wwpVxaircM9IwF4vH5aDJ5+XKWJjnukYzdjqC9O35lFJT1ajtDVU5zyMbLJUonqv3ZR/ErfQ42bG6li1tfsYj8Xn/xhVuJ6/ZvoJnLoxMte2bL8BqWBbNaR63g3kNvIjsEZE9wBMi8i8icoeIvEREPgP8oiAzLAHipsXT54e5ZZp7BriaSaMDrVmhVMLFkm4HH4mb/L9fnZ/3slmQggVZR0MxDMvC63TSNZwfUbm+iciiepS6nQ5EEiJdCxGIGjzXNUrfeISm6vzkXosIDT4vSsGBi6NcHg2ldRmF4yZxc2Z7vlN9k3SPhnlFAYKrwahBa20FHtfi1iwirKirZMfqOgLR+d01r9+e6Nv6vaQI2dmBybQB1rhp4XU58C/hx3UxLDTK/5n1/49Pu196eVo2ceTyOMGYya3rm2Y83lZTgb/CxWmdKpkVhjVXoyTFsZ4JfvB8Dy1+L3ftWpX2GGcBm293jYSocruocDvon4iypiE+r393IaKGyXAwRuMiRadqKtz0TURo8Xtp8s8N2iml6B+PcLJ/kkq3k8ZF7GKzpcrjwutycqY/wGgoxsaWmQHYdAqQj57op8Lt4PaNTXOeyzcx02JFTe755vVVbhp8XgIRg+oMaY31Pg93bm7hZycGeNu+NVwaDqX9nAajBh2NVQXThp/3J00pdec8t5cWZIYlwJPJFKnZO3gRYXOrX+/gs8S0VMZtQ+rS98ClzMXQhTLwgajBeChOpceJiOB1Obi0xF38WDCGkL17JoWIUFvh4VR/gNistcdNi5N9k5zom6C2wm2rEJfTITRVe5kIGxy4OMJw4GpsYCgYnRE4DsUMfnVmkNs3NNsuDpbaMddU5j6OiLCu2UfEMOYNat+1ayUx0+KfnziXDLDO9b+blppXuybfZLVqEakD3gN0Tn+NUuoPbZlVibH/3DBbV9TQ4Ju7+9rU5udHR3tRKvPuVJNgPiXJnvGEgX/hyjiRuJk2Rc8pkrU/ein0joVnuDiqvS4GJmNMRnLfxfeMR6hy52aEPC4HwZjBxeEAm1prgETO97GeCWKGRaPPW7DPXk2Fm5hhcfjyGB31VXQ0+RgOxPB7r/5dfn12iEjcKoh7ZiISZ0PL0rsp+SvcrKyrZHAySm1l+qusjkYfe9rrefrCCDA3wBo1THxe55JiH4slW6fUj0gY96PAwWm3a55I3OTApdEZ6ZHT2dzqZywUT3Z50cyHYSkyJRb0jEVwORJ57kcuj6U9xumQObvYfBMzLHrHw/inXaqLCJUuJxdzbPASiZuMh+NLymmvq3RzeTTMaDBGz2iYAxdHE4HFKk/BNxYel4PmZAD24KVRTHNmXOWx4/2srq9kS1v6Ev58oVSieUxTnnbMHY0+jAVSY9+8O+GWSRdgDUQNVtbZK00wm2x/SiqUUv/Z1pmUKM9dGiVmWJkN/DTJgkIUNpQyppUosElH73iYvR31HLk8zoFLo9y4du7f2+kQAlF7d/BDk1EsxZxMn+qKRLn7RCS+6Pzm0aR7ZimICH6vm+cvj6FUwrDnmm6aD1IB2FDMmPHD1T0S4mTfJPfd2mn7D08oZtJU7cmb1nqF28naRh8Xh4M0ZIhl7Fhdy6bW6vQ/rIqMr7OLbA38l0XkPwCPkJArAEApNWLLrEqI/eeGcTokYyXe1VTJSV68qTw6VtlFpp2RYVr0T0SSlYJw8NJoWpeX0yEYVqJox44cY6UUXSOhGe6G6VS6XVwcCrJjkS3jroyF8+KLrnA7cYgsOlvETuZUrh7vx+kQXrqlxfaxI4bJpjxfJaysr6R7LETctNJmIokIf3H3dmbb9kjcxF/ptqVX7Hxk+0mIAX8LPMlV98wBuyZVSuw/N8SO1bUZfa8NPg/Nfq8WHcsCw7RwpNnLDiR3zSvrKtnb3sDAZJTu0XDm89hUzToejhOOmxkNaLXXxXAguig9k3DMZDIyV0I3V4rJuM8mblr8/NQAN3Y2UJchW0gplZc4imFauBxCbWV+q0XdTgcbmqoZj2QuXkwVjk0nGDNYXVf4K/hsPw0fBjYkK1nXJm8L6sGXO4GowfOXxzO6Z1JsbvVr0bEsiBpW2p13KoNmZV0lezvqATh4Kf3Fo5D5SmCpdI+EFjTEFcldfLYMB6M5F3aVGs9cGGE8HJ9XWGw0FCMYM5bcRyEQM1hVX2mLm6qlpgKfx5X1D1Eq86YuTRKG3WRr4M8CpdtpwCaeuTCMaak5+e+z2dTq53R/oCQlXgtJ3EyvJJnKoFlZW0Gz30tHQ1XGdEm7qlnDsUSe+kIyAtVeF8PBKOOh7HbxV0bDBc2qWE4eO9FPo8/D7vb6tM/HzcQP/M7VdVPFUbliWoqWNHUB+cDhEDa2+BcsfkoRjps0+DwLagzZQbYGPggcTlazfip1s3NipcD+s8N4XI6pXWUmNrdVE46bdJdwN55CkElJsncsUeGZutze11nP8Z6JjLs8O/Ro+ibCOEWyCgxWuV1cGFq4ujQYNQjHzGX54heaoUCUQ12jvGxra8Zd9UQkzobmaup9HratrGE0HJtqa7cYwjGTmsqlSTEsRN204qcF5xM3C549kyJbA/894C9INPnQaZJJ9p8bZm97/YKX7ZvbErnJ2g8/P5mUJHvGw6ysq5gyrnvb6zEsxfOXZzcZS5BvH7xhWlwZDWed4+7zuhgJxRfcxQ8Hosua6VJIfnaiH0vBK7amd8+EYyY+j3Mq06zZX8GGpmqGg4tPLw7FDVbbbFBTxU/h+PzFT5ZSiJD3WEC2ZGXglVIPAt8EnlJKPZi6LfQ6EbkoIkdF5LCIlFVQdjQY43jvxIL+d4CNyYo27Yefn3gGJcmesciMHdDWFTVUup0cTOOmcYgQM/KbKjkSjGXUyMmEz+Pk3FAg45dfKUXPWOSacM9YSvHYiX52rKqlrTa92yQQi7Ox1T8jBtPeWEVbTQWji1BjNa2Eln59Afzd/go3q+or5235F4qZNOdJ+ycXstWDfwNwGPhx8v+7ROQHWY5xp1Jql1JqX25TLE6eOj9XHjgTPq+LNQ2VuvnHAsTTtOuLmxYDkxFWTlPpdDkd7G6v4+ClkTkG1ClCJI8GPpUa6VtkGmOVx8V4KHOHoEDUIBI3l+2LD4lm1w89eZHHTw7YKtJ29Mo4/RPRjJWrE+E4rf6KOZk1IsLGVj9VbmdWrhBISfFWFOzvulDxUyH6rs5Htp/a/wncSFJBUil1WERKNovml6cHcTmEWzfkLnT0m3ND+DzOrHOeN7f6tejYPFiWSlayzjTw/RORZIrkzJ3f3o569p8b5tJwiM4m39Tj+dajmYwaTEbiNFUvPmBX5XFyfijI7jXuOb77oUC0IHrg6bg4FOTbz13mV2cGpwrLvvr0Jd68ZzUv39qS95jAo8f68Xmdc7SaILHjjpkWa5t9aV6ZSEvctqqWA5dGiBoLxyvipkVrhqsEO5iv+CnVd3W53DOQvQ8+rpSa7fDM5lukgEdF5KCI3J/uABG5X0QOiMiBwcHBLKezND72vaPc/+WD9I5nzqWeTf/EzO41+88Nc+Pahqx3Cpta/ZwbnCsIlen81xpmBldGb7L36IpZu6C9yUyMg10z3TROhxCN58/A946F8aRpgJ0NiV18jLFZvviUe6ZQkrEpTvZN8OePHOcD3zjE0xeGuWvXKh649wb+++uuo8Hn4bNPnOP3HjrAd567vOQ0xRSBiMGT54e4Y1P6H46xcIzOpqp5C70qPYlOSxOR+LwpsFHDpMrjLPjfdWV9JU6nzMn6CUYNWmsqljXOkq2BPyYi7wCcIrJRRD5NIuC6EC9SSu0BXgO8T0RePPsApdTnlFL7lFL7mpvtr/QcDkTpHkk0afjYwy9k3fJsYOJqsKdvPML5weCC6ZHT2dzmx7AUFzOoDk4//7WIaam0RU7Tc+Cn01jtZW2TjwMXZ+bD53MHHzVMescjGSVis6HK45rji5+IGMQMa8Gen4kfgvCS0gWVUhzqGuVjDx/lj799hBO9E7zjxna+eM8NvPe2tTRWe7lxbQN/85Yd/OWbtrO20ccD+y/y3gef5StPXVp0E+oUhmlxdiDAQ09dJG6qtO6ZhEa8sLp+4YYfdVUetrTWMBKMZvzOBqIGa+oLJ8WbIlPxU9yyaLUpVTNbsv3kfgD4GAmZgq8DPwH+fKEXKaWuJP8dEJGHSbh5fpnbVPPD4e4xAF5zfRv//kIfP3i+J6O+eCaePJ9eHng+UpIFJ/smp+5rrmJYCiuNkmTPeASfx0lNGiO7r6Oe7x66QjBqTAUrnQ4hlic9mlQ7vKUUIlV5XAwFIoyG4lNqo0OT0ayu/H58rI/P/OIcTofQ3lDF+mYf65qqWd9SzdpG37xl75ZSPH1+mG8evMzZgQANVR5+97a1vGpbW9rXiQjbV9WyfVUtZ/on+dbBy3zzQDffO3yFV21r4027V80r2jUSjHGqb4KTfZOc6p/kzMDVq9UbOutZn6Z13Vg4xrYVtVlfBa+sryQQi9MzFpmja58y+o3+whcTQaL46dJIaErpNFFJ65ghSrccZDW6UipEwsB/LNsTi4gPcCilJpP3Xwl8IqdZ5pFDXWM4HcLfvnUnPeMR/uyHx7l9Y3Naqd9M7D87TF2Vm+tW1GT9mvXN1bgckvDD78xl5uWNaam0gls9Y2FW1FWm3ZXt7ajnWwcvc7h7jNuS8RSHCJa66v/MFctKBFfz0RjZ53FzfjBAfVU9SiWE06oz6NmkCMUMvvp0Fxtbqtm5uo7zQwGevTjKT08MAImK3ZV1laxv9rG+uZp1zdWsa/JR5XHyyzNDfPtgN92jYVbUVvD+Ozfw0i0tWRvSja1+/uS1W+keCfHt5y7zyJEefnS0lzu3tPBbe1bT7PdyYSjIyZRB75ucUkt1OYT1zdW8elsbW9r8bG7z05zmhyEUM6jxumn2L058a32zn1DMmiPqFoyatPgrlq2mwOEQNrX6Odw9SoXbOaUcuVxxlhTzGviFMmWUUm+c5+lW4OHkF9MFfE0p9eNFzzDPHO4eY3Orn2qvi795yw5e/+lf8YkfHuP/vn13Vq9XSrH/3DC3rGtc1JvncTlY2+TTzT8yYFqKdBa+ZyzMlrb0P6Rb2mrweRLpkrdNC5gLqYyc3L/sY+E4UcPKKCy2GCo9ToYCUUZDcRwCcXPhH5+HD11hPBznf7z+uqkrPqUUI8EY5wYDnBsMcn4owIm+SX55ZujqWG4n4bhJZ2MVH3nlZl60oSnnH7o1DVV86OWbeMeN7Tx86AqPHe/nZycSYmHxZDFZU7WXzW1+3rBzJVta/axrrl5QD0cpRTBmsLe9YdEG0OkQtq7wc/DSKKGYMeW7jxgmW+uW98p4qvgpamBYqmB9V+djoR38LUA3CbfM06T9CqZHKXWeIturWpbi+e4x3rBrJZDwi//BHRv4h5+d4Y27VvLSLQs3IOgaCXFlLMzvv2TxSUSb2vy8cCV9cc61jmFZzHatxk2LoUCUFRlEmpwOYXd7/Rx1ScXS9Wi6R0NU5UkADBISBucGJvFXuvEssJMeCcZ4+NAVXrShaYY7T0RorPYm/eZX3YMT4Tjnh4KcHwzQMxbmxrWN3NBZnzdfdGtNBb//kvW87YY1/OhoL5G4xZY2P1va/Dl1J5qIGLTVVFBblduPp9eVCLoevDQ6dVXidTvycrW1FFLFT89cGFmWYG86FppBG/AK4HeAdwD/BnxdKXXM7onZwfmhAJNRg91r6qYe+4M71/Ojo7386cMv8JMPNSxYrbj/XCL//ZZFBFhTbG5NdHeavvPQJDCMuUHWvlSK5Dx5xHs76vn12SEuDAVZl/TzCkurZg1GDUYC0ZxSIzNR4XYyFIwSipvUVszvDvz6M10YluLdN3dkde6aSje71tSxa9rn2g7qqzy886bs5pQJ01IYlsXaprk++cXgr3CzbWUNR66M4xRhXZNv2d0hqXmtrq+k0u0sig5uC/VkNZVSP1ZK3QPcTEJ07Bci8v6CzC7PHOoaA2B3e93UY16Xk7/+rR30TkT4mx+fWvAc+88N0+L3sj5D3u58bGr1oxScHdAFT7OJmXOVJHunMmgyG9qpdMlpVa0KllS40zceWTDDJRf8XhcOZF6XSfdoiEeP9/Ga69uWTb/ETsbDsQUDxNmSkjNAJe4XCxtb/FllBhWCBT/FIuIVkTcDXwHeB3wKeNjuidnBoe4x/BUu1s3aPexpr+feWzv58lOXeOZC5h4mSimePDfEbRuacvp1nt7dSTOTWBolyZ6xRA78fDv4ep+H9c2+GeqSS5EMjpsWV8bCefG9z8brcmbUQU/x0JMX8bqcvP2G9ryPv9ykUkNX1ufvh6u9sYqda+oK3khjPhwOKYqrCVjAwIvIQySafOwB/kwpdYNS6s9T6Y+lxuGuMXaurkv7x//IKzezur6Sj37nSEad59P9AYYCsUWlR06nvaGKCrdDG/g0pFOS7BkPU+11UbNAJeC+jgZO9k1MlbM7ltB8eyQQXXIGTq4c753gqfMjvGXv6mWtfrSL8UicjS3VeZURkALpzpQqC/2l3wVsBD4I7BeRieRtUkQm7J9e/gjHTE71T2b0U/q8Lv7qzds5PxTk04+fSXvM/nOJbIVsBMbS4UzqSOtMmrnE0ujQ9I5HWJFF2fnejnosBYe6E7t4l8ORU7HTVEu+ZchdVkrxpd9coKHKw107VxZ8fLsJxQxqK12LTovULI2FfPAOpZQ/eauZdvMrpbJPAi8Cjl4Zx7TUvIGo2zc281t7V/PZJ85zrGdutsv+c8O0N1Qtyb+2SXd3SkvMmCsV3DMWzsoPvanVj9/rmnLTOBzkZOAnwgaB6PLosz91fpiTfZO846b2vLXvKxYSaZEmG1r8RRF4vJYo3gaOeeZwcne3a1qANR1/+rqt1Fd5+K/fOTIjUGdaiqfOD3NbFuqR87G5rZr+iShji5BAvRaYrSQZMywGJ6OszGIHn0qXfK5rFEupxA5+kXo0pqU4PxRYFuNqmBYPPnmJNfWVvDyDXnopMxGJs7KuoizdTsXONWTgx1jTUDlvuTUkNC8+cdc2Xrgywed/fWHq8XODASYjRk7pkdNJ5TWf1tLBU1iWwrJmSgL0TURQzNWgycTejnrGQnHODwYTejTm4nzwl4aDjIXiVC9D7vJjJ/q5Mhbmnls7C+77t6t/7fTzG5ais3HxWWeapXPNGPhDXWPsWjN/a70Ur7m+jVdta+XvHzvNhWQD5SPJ7kG3rFvqDj6ZSaPdNFMYlkLN0qHJJDKWiT3tdQiJZtyJSksrayG5ockIF4aDi5KryBfhmMnXnuli28oabuxsKMiYllJMRuIMByNMRuIMBTILeC0F01KMBKNsaKkuO7dTqXBNGPj+iQi945GsC0FEhE/cdT0el4OPfucIlqU4cnmMTa3VSw4StdVU4K9wcaqvpGLUtmKpuTo0KSnnbIKskLjy2tBSPeWHVyq7YqdwzORE7yR1FZ4liYrlyvcOX2EsFOfeWztt909H4ibDwYR7sN7nYdeaem7d0MSq+gqG5lFpzAXTUoyEoqxvri6anPBrkWvCwKcKnBZT6ddaU8Gfvm4rT18Y4aEnL3Ksd2JR8sCZEJFk8w/tokmRzhCn9NKz7YMKCXXJU32TTITjWeXCm5bieO84TocsqJ+S7rU/Pd7PD57vybmoajQY47uHLnPb+saMejtLxbQU4+E4Q4EIoNjc6ueW9U1sXVFDXZVnKrOrvb6KoWBuTa7TjTkcjLKxxU9Hk3bNLCfXRL384e4x3E5h28rFfYl+e98avn+4h088chxL5Z4eOZvNbX4eOdI7Qz/lWsY008kEZ5dBM529HQ18/dluDnWPcf2qGuKmNa9r4MJQkMmIMUd6diFO90/yz0+cm6pI/umJfj5w5wY2LlIG+uvPdhE3Fe+5pXNRr8uGUMwgHDdxOoQVtRW01lRQ7XWl/byJCOtbqnE4hEvDIRp8uV/NGKbFSDjGlrYaVuWxoEmTG9fEDv5w9yjXrahZtB9QRPirN2/H43LgELhpif73FJvb/IyH41MSq9c6pprtgU/s4DOJjGViQ0s1NRUuDlwaWXAHPzQZoWskSP0ClaXTGQ/H+fTjZ/jIt55nJBDjw6/YxJ+8divj4Tgf+fbzfP5X57MusLo8GuInx/p49bb8ShKMhWMMB6J4XQ6uX1XLLesa2dDix18xt23gdESEtU0+OpuqGE4Wey0Ww7QYCcW4Thv3oqHsd/CmpThyeZy37l2d0+s7Gn381Zu38+szQ3lL80pl0pzqm6S1png0NJYLw5rp4ogaJkOB6LwSBelwOoQ9HfU8d2mU99zSMSVpO5twzOR47wR1ldntVE1L8eMXevny05eIxC3u3r2Kt9+wZkowbseqWh588iLff76HJ88P8wd3bGBvx/wB/YeevJSUJFizqDVmQinFcDBGa42XziZfTmJ2CSNfjVOEs4MBGqq8WWf1xE2LsVCM61fWFrQnqmZ+yt7An+6fJBQzF8x/n4837V7Nhub8aU1fTZWc5MWb7G9TWOzEDWuGkmTfVB/WxRuKve31/OLUIJeGQmxN49dO+d3dDmdWJfMneif47BPnOD8UZMfqWv7ji9fT3jAzaOjzuviDOzbwkk3N/OPPz/I/f3iMOzY183u3r0u7KTjZO8GT54d5503tC2rTZEPKuLfVVrC51b9kHZT2Rh8iwun+SRp9Cxv5uGkxFo6xfXVtUYl+aa4BA59q0ZdtimQhaPB5aPZ7tSZNkpihZhilnqSBz8V1sae9HgGOXBnnjs0tc56/kKxnWMjvPhqK8cD+izx+coCmag//9dVbuG1947xujm0ra/nU23fzrQPdfOvgZQ52jfJ7L1rHnZubr2rVK8UX91+kvsrN3YtsFZkOpRRDwSir6yvZ0Lx0455iTUMVDhFO9k/QUOnJqK4ZMxLdlXasqqVJG/eio/wNfNcYdVVuOhuLK1Vrc6vWpEkRt2ZWsfYuMgd+OjWVbja1+jlyeYyoMdMfPjgZ4dJIKG0LuRSmpfi3oz189ekuYobFW/eu5rf3rck6fuN2OnjHTR3ctqGJf/r5Wf7+p6f5+akB3nfHBtpqK3j6wggneid43x0blpwbbiV37u31Vaxvqc57wH5VfSVOgWO9EzRUzTXyUcNkMmKwc3UtDTk0/tDYT/kb+O4xdq2pK7pslc1tfr769CUsSxWNtOhyETUspv8JesbC1FS4cq4q3ddZz9ee7mJgMsqWFYnHQjGD4z0T1Fd50n4WTEtxqHuUB35zkUsjIfa013H/7etzDhZ2NPr432/Zwb+/0MeD+y/yvq8/xztvbOexE/2srq/kFdctTZLASrbv62isYl2Tz7bPd1uyH+6xnnHqqjxTbq1I3CQYM9jdXpcXN5PGHsrawAeiBqcHJnnN9rblnsocNrf6icQtukdDdFzjZdxxY9YOfjyypMySve31fPXpLp65MMyLNzVjmBbHeybwuGb63U1LcfTKOL8+O8RT54cZD8dp8Xv5k9du5ea1DUs2mg4RXrd9BTetbeCzT5zjS/svAvAnr926JEmCVIXo2mYfnY32GfcUrbUVOBwJwb66Sg+mpQjFDHa312t9mSLHdgMvIk7gAHBFKfV6u8ebzpHuMZRaXIFTodg0rfnHtW7gY6aFd5rh7RkPs31Vbc7nW99STW2le6rL0/mhAMGoQYPPi2FaHLkyzm/ODvHk+WEmIwYVbgc3dDZw2/ombuhsWHTR00I0VXv52Gu3sv/cMN2jIW5em7skwfQK0UIWETX7K9ixCo5emcDlEHZ31C97D1TNwhRiB/9B4ARQcHnhQ1MB1rpCD70gG1sSXaVO90/yym3Fd4VRSGKGSWXSHx2JmwwFYkvawTtE2NtRz9MXhrkyGuLicJCe0QhfebqLp84NMxk1qHQ7uaGzgRdtaGRPR73tEsEiwm0bllYJnaoQ3dTqZ01D4WNKTf4K9nQ4cTpkWUTZNIvH1ndJRFYDrwP+AvjPdo6VjsPdY6xr8hWlj9DndbGmoZJTBVKVPN2fyLkvtktqy1JY6qqSZCpFcrE58LPZ11HP4ycHeN/XDnF2IEAgadRvWtvAbRua2N1etyy677lSLBWixfb50cyP3T/D/xf4L0DGJHIRuR+4H6C9PX99KJVSHO4e4/Yl7prsJKFJY28mzZWxMH/1oxM8cqSXV29r47Pv3mvreIvFsBTTXcg947ln0Exn95p6vC4HJ/smuHltI7dvbGLXmvq8u18KwVSF6IoaVpRhI26Nfdhm4EXk9cCAUuqgiNyR6Til1OeAzwHs27cvb3J2PeMRBiejSypwsptNrX5+cWqQWA7dhxYiHDP5l1+e47NPnJuKQzx6vI/ukdCyXN5nwrQU03UKepdQ5DQdEfjce/ayuq6KrpEQFW5nSRp3XSGqWQp2fuJvA94oIheBbwAvFZGv2DjeDA51JTs4FaH/PcXmNj+GpaY05/OBUopHjvTw8k8+wf/96RletrWVn334JXzmnXsQEb781KW8jZUPZuvQ9IyFqa1041uijzccN9mxqo71LdXcuLYBr0sYDuamsbJcTK8Q1cZdkwu2GXil1H9TSq1WSnUCbwceV0q9y67xZnO4awyPy2GbDGs+yHfzj2M947ztc0/x/q8doqbSzb/efzP/9I49rK6vYmVdJa++vo1vPNNFKGbkZbx8YJpqxoewZyycVZu++YgZFpUeJ3VVCX+xz+ti15p6NrRUMxaOEYgUz/ozETMsxsOJClFd/q/JldK7Zs2Sw91jXL+ypqgvy9c1VeNyyJL98MOBKP/tu0d5/ad/zZn+Sf7iTdfzyAdeNEf98r5bO5mIGHz3uStLGi+fGJbFdAdVz3hkyX7myWicjoaqGfnhDoewur6KGzobqPA4GApGinY3HzVMJiJxdq7W5f+apVEQ66eU+kUhc+DjpsXRK+Psbi8e/Zl0eFwO1jb5ct7Bx02LL/z6Anf83S/41oFu7rt1Lb/4yJ2886aOtIU0ezvq2b6qlgf2X7SlRVsumNPmEYmbjASXliJpWgqHCE0ZOm/5vC52rq5jY4u/KHfzkbhJIJqoENXl/5qlUpbJrKf6JokaVlH731NsavPzwpXxRb/uidODfOKHxzg3GOT2jU18/A3XsaFlfsVLEeHeWzv58Lee59dnh7h94/IrWcYNaypFsncqRTL3XetkNM6qusp5lSJTu/kGn4dTfZMMBiLUzyOoVSgicVNXiGrySvH6L5ZAMRc4zWZzq5+ukVDWjSIuDAX5vQef5Z4vPoNpKT7/nn089N4bFzTuKV6/cwVN1R4e+M3FJcw6f0SnGfhUo+0VOebAK6UwTJV1o5AqT2I3v6W1hvFInMlIPKdx80E4ZhKJm+zu0MZdkz/Kcgd/qGuUpmoPq0ugq8ymVj9KQddIiBvmKWGfjMT5x8fP8sXfXMDjdPDR12zhvts6F12s43U5ecdNHXz68TNcHArSucw9M+OmmnInXc2Bz20HH4yZNFV7FtXswuEQVtZXUu/zcKp/kpFQlIaqwrpGQjGDmGmxq71uUT1oNZqFKMsdfLEqSKZjSzKTpms4lPZ5y1J880A3d/7dE/zLL89z965V/PyP7+D3X7I+50rMd93UjlOEB5+8mOu080bMtHCmXDRjEeqq3Dl1IwKIGkbOOf6VHifXr6yh2utiIly4nXwwahC3LPa012vjrsk7ZWfgx0Nxzg8Giz7AmmJNQxUVbgeXRubmwh+8NMrdn/kN/+XbR1jTUMn333cbf/vWnbQsMbOipaaC1+1YwbcOXCYQXd4gYyxu4Uh+CnvGwzlLFEQNk0q3a0nuDZfTwbaVtSAJl4ndBKIGFoo97fVLzvvXaNJRdgb++ctjQGn43yHRR3Rji59L03bwfeMRPvSvh3nLP++nfyLC379tJ9/5/VvZmcc13XfbWgJRg+8cvJy3c+ZC3DRn7OBzdc9MRgw6G6uWfNVW4XayY3UtobhB3Mx/hXGKQMRAUOxeU5/zFYtGsxBl98k63D2GCOxYnbvcbKHZ1Orn56cGiMRNPv+r8/zTz89hKsX77lzPH9yxwZbd3a41dexaU8cD+y/y7ps7lq3pSMy0qPK4CMdMRkKxnAKspqVwOYXGPKUV+ivcbFtZw5HL41n1JF0sE+E4Lqewc039krs6aTTzUXY7+ENdo2xori4pf+bmtmpGgjFe9n+e4O8ePc1LNjXz0w+9hD9+1RZbL93vu62TC0NBnjgzaNsY82EmlSRFhN4liIxNRuKsrq/Ma5pjs7+CjS2J9yWfNQMTkThul7BzTZ027hrbKSsDn1KQLBX3TIrtq+oAqPa6+Orv3cRn372X9gL0kH3N9Sto8XuXLWVyeiVpT4458EopTKVoq8l/xtSahipW1lcwEoot+VxKJboweV0Obdw1BaOsXDRdIyFGQ/GSCbCmuHldA3//27t4w84VBS228bgcvOvmDj752GnODgTYkGxCUijMaVLBvTnmwAejJs1+L5We/BtMkUR8JBxLSAfk2sEoapiMR+J01FfR2eRb9oIqzbVDWX3SDpdQgdN0RIQNLdXL8sV/x03teJwOHlqGlEnDskh5P3rGwzRUeRZtqCOGyeo6+652nA7hupU1OIRFi7QppRgLx4gYJnvW1LOh1a+Nu6aglNWn7VDXGJVuJ5taC7sTLWWaqr28YedKvn3wMuMFzP8GsCxIhS97xiJZV6CmiMRNqr1OairtvRD1upxsX11HJG5mrd0fNy2Gg1EafR5u6Gyg3ld8XcU05U9ZGfjD3WNsX12rd0mL5L7bOgnFTL51oLug4xrWVWOZSw58MGbQ0egrSEFbtdfF9atqGQ/HFlShnAjHCUTjbFtZy9YVNSXVGlBTXpSNJYwaJsd7JthdYu6ZYuD6VbXc0FnPQ09eKqiErmklmn2EYgZjofiidvCmpXA5hIYC7owbq71savMzEoqmzawxLcVQMEJ1hYsb1zbSUlNREtXUmvKlbAz88Z4JYqbF7iJu0VfM3HvrWrpGQjx+cqBgY8bMhNBYbw6NticicdbUVxX8am1VXSWr6yvnZNaEYgajoRgbW/xsX1Wrs2Q0RUHZGPirAdbSyqApFl65rZUVtRU8sP9CwcaMGQkdmpSKZLY58EopTEstSxs7EWF9s5/6Kg/j4RiWUgwHozhFuGFtA6vrq5ataEyjmU1ZGfi2mgradO/KnHA7Hbz7lg5+c3aY03lqIbgQMcPC4ZCpHPhsG20HogatNRXLtkt2OoStK2pwOR0MB6K0N1Sxu6Oeaq0noykyysrAl1p6ZLHxOze043U5+FKBCp9SSpI9Y2EafJ6sDXbUsFi1zFLQHpeDnavr2NvZwLrm6rzLGWg0+aAsDPxwIMql4RC7tP99SdT7PLxp9yoePnSZsTxUby5E3EhowfcuotF2JG7i97qoqVj+3XKlx6mbc2iKmrIw8KWmIFnM3HNrJ5G4xTeetT9lMmaaOCTRqi9b/3swZtCeB9VIjeZawDYDLyIVIvKMiDwvIsdE5M/sGutw1xiOElOQLFa2rqjh5nUNfPnJSxg2yuVCohgoapiMheNZGXjDtHA58qcaqdGUO3bu4KPAS5VSO4FdwKtF5GY7BjrUPcbmthqtq50n7rttLVfGwvz0RL9tY6SUJHvHo0B2AdaJSJz2hirt79ZossQ2A68SBJL/dSdvea+isSzF8zrAmldevrWVVXWVfNHGYGuqoGoqRXKBHHilEkVRLTU6S0qjyRZbffAi4hSRw8AA8JhS6uk0x9wvIgdE5MDg4OJ1yU2l+NPXXcdb9qxa+oTnoaXm2nELOB3CPbd28MyFEY71jNsyhkIhXG20vVB662TEoK12+VIjNZpSxFYDr5QylVK7gNXAjSJyfZpjPqeU2qeU2tfc3LzoMdxOB799wxr2dTYsfcLz0HqN7Rzftq+dSreTB/dftHWc3rEITdULp0jGTDOnZiAazbVMQbJolFJjwM+BVxdiPM3Sqa1y8+Y9q/je4R6GA1HbxslGZCwcM/FXunPWY9dorlXszKJpFpG65P1K4BXASbvG0+Sfe2/tJGbYmzLZMxZeMMAajMfpaLC/w5VGU27YuYNfAfxcRI4Az5LwwT9i43iaPLOx1c/tG5v48pOXiNuQMhmMGkxEjHldL3HTwu1w0uC7dmIgGk2+sDOL5ohSardSaodS6nql1CfsGktjH/fe2knfRIQfv9CX93P3TyQ1aOYx8BOROB2NOjVSo8mFsqhk1djHnZtb6Gis4gEbgq39kwnffiaZAiupud7s17t3jSYXtIHXzIvDIdxzSycHL41yJCkJkS/6JyIImRttT0YMVujUSI0mZ7SB1yzIb+1bjc/j5IE8Fz71T0RprPbicaX/GMZNS6dGajRLQBt4zYLUVLh56741/PBIDwOTkbydt38iwsoMbfpCMYPaKjd+nRqp0eSMNvCarHjPLR3ETcXXnu7K2zn7JiIZc+BDMVOnRmo0S0QbeE1WrGuu5o7NzXzlqS5ixtJTJsdCMYJRM+0OPm5aeN0O6qsK11BboylHtIHXZM19t61lKBDlR0d7l3yurpEQkD7AmlKN1L1NNZqloQ28Jmtu39DEumYfX/rNBZRamjDosxdHgbmNtnVqpEaTP7SB12SNwyHcd2snz18e51D3WM7n+c3ZIT756Gm2raxhzazeqpPJylavS6dGajRLRRt4zaJ4857V+L2unFMmz/RP8vtfOcjaJh/vv3P9nNZ7OjVSo8kf2sBrFoXP6+K3b1jDj4720je+uJTJwcko9z3wLBVuJ//y7r1zOnCFYgb1VW6qvbozl0aTD7SB1yyae27pxFSKrz59KevXhGMmv/fgswwFonzhnn2sqp+7Sw/FTdobffmcqkZzTaMNvGbRtDdW8bItrXzt6S4icXPB401L8Uf/eogjV8b51Nt3s2N13Zxj4qaF1+WgrlIXNmk0+UIbeE1O3HdbJ8PBGD98vmfBY//3v5/gJ8f6+dPXXccrt7WlPWYyEqezwadTIzWaPKINvCYnbl3fyKbWah7Yf3HelMkvP3WJ//erC9xzSwfvva0z7TGpBtxNOjVSo8kr2sBrckJEuPfWtRzrmZjKaZ/Nz08O8PHvv8DLtrTwP96wbU7GTIpA1GBVfWVG0TGNRpMb+hulyZk37V5FbaWbB/ZfmPPcsZ5x3v+159i6ooZP/c7ueRt2xE0ro2SwRqPJHW3gNTlT6XHy9hvX8JNj/VwZC0893jse5r0PPEtNpZsv3nsDvnnSHlOpkfMdo9FockMbeM2SePfNHSil+PKTiZTJQNTgvQ8cIBg1+eK9N9BaM39D7VDcpEOnRmo0tmCbgReRNSLycxE5LiLHROSDdo2lWT5W11fxqm1tfOPZLgJRg/d/7TlO90/yT+/cw9YVNfO+1rAUFS4HtTo1UqOxBTt38AbwYaXUdcDNwPtE5Dobx9MsE/fe2slYKM6bP/MbfnFqkE/ctY2XbGpe8HUi0KFTIzUa27DNwCulepVSzyXvTwIngFV2jadZPm5c28DWFTWc7g/wH1+8jnfe1JHV62or3TTX6NRIjcYuChLZEpFOYDfwdJrn7gfuB2hvby/EdIqSlhI2dCLCX77pevafG+Y/vWR9Vq/xOB1sbqvB7dRhII3GLmSput4LDiBSDTwB/IVS6rvzHbtv3z514MABW+ej0Wg05YSIHFRK7Uv3nK3bJxFxA98BvrqQcddoNBpNfrEzi0aALwAnlFKftGscjUaj0aTHzh38bcC7gZeKyOHk7bU2jqfRaDSaadgWZFVK/RrQ+W8ajUazTOgUBo1GoylTtIHXaDSaMkUbeI1GoylTtIHXaDSaMsX2QqfFICKDQPadnGfSBAzlcTqlgF5z+XOtrRf0mhdLh1IqrfhTURn4pSAiBzJVc5Ures3lz7W2XtBrzifaRaPRaDRlijbwGo1GU6aUk4H/3HJPYBnQay5/rrX1gl5z3igbH7xGo9FoZlJOO3iNRqPRTEMbeI1GoylTitbAi8gXRWRARF6Y9thOEXlSRI6KyA9FpCb5uEdEvpR8/HkRuWPaa34hIqemKVq2FH412ZGpUbmINIjIYyJyJvlvffJxEZFPichZETkiInumneue5PFnROSe5VrTQuR5zea09/kHy7WmhchhzVuSn/uoiHxk1rlenfx8nxWRjy7HehYiz+u9mPyeHxaRou0OlMOa35n8PB8Vkf0isnPauXJ/j5VSRXkDXgzsAV6Y9tizwEuS998L/Hny/vuALyXvtwAHAUfy/78A9i33erJc8wpgT/K+HzgNXAf8DfDR5OMfBf46ef+1wL+TUO28GXg6+XgDcD75b33yfv1yr8/ONSefCyz3emxacwtwA/AXwEemnccJnAPWAR7geeC65V6fXetNPncRaFruNdmw5ltT31HgNdO+y0t6j4t2B6+U+iUwMuvhTcAvk/cfA96SvH8d8HjydQPAGFByhRIqc6Pyu4AHk4c9CNydvH8X8JBK8BRQJyIrgFcBjymlRpRSoyT+Vq8u3EqyJ49rLhkWu2al1IBS6lkgPutUNwJnlVLnlVIx4BvJcxQVeVxvyZDDmvcnv6sATwGrk/eX9B4XrYHPwDGuLu6twJrk/eeBN4qIS0TWAnunPQfwpeQl3X8XkZLQqJeZjcpblVK9yaf6gNbk/VVA97SXXU4+lunxomaJawaoEJEDIvKUiNxt/4yXTpZrzkTJvc9LXC+AAh4VkYMicr89s8wvOaz5d0lcpcIS32PbGn7YxHuBT4nIfwd+AMSSj38R2AocIKFlsx8wk8+9Uyl1RUT8JPrDvht4qKCzXiSSaFT+HeCPlFIT03+TlFJKRMoutzVPa+5IvtfrgMdF5KhS6pxNU14y19r7nKf1vij5HrcAj4nIyeTVflGy2DWLyJ0kDPyL8jF+Se3glVInlVKvVErtBb5OwjeFUspQSn1IKbVLKXUXUEfC54VS6kry30ngayQueYoWSd+ovD/lhkj+O5B8/Aozr1RWJx/L9HhRkqc1T3+vz5OIvey2ffI5ssg1Z6Jk3uc8rXf6ezwAPEwRf58Xu2YR2QF8HrhLKTWcfHhJ73FJGfjkrzYi4gD+FPhs8v9VIuJL3n8FYCiljiddNk3Jx93A64EX0p68CEi6j9I1Kv8BkMqEuQf4/rTH3yMJbgbGk5d/PwFeKSL1ySj9K5OPFR35WnNyrd7kOZtI9AQ+XpBFLJIc1pyJZ4GNIrJWRDzA25PnKCrytV4R8SWvxEl+319JkX6fF7tmEWkHvgu8Wyl1etrxS3uP8xk5zueNxA69l0Sg5TKJy5YPktiZnwb+N1crcTuBUyQCGT8lcakO4CORUXOEhP/+HwDncq9tnjW/iISP8QhwOHl7LdAI/Aw4k1xfQ/J4Af6JxJXMUaZlC5FwZ51N3u5b7rXZvWYSWQhHScRjjgK/u9xry+Oa25LfgQkSCQSXgZrkc69Nfh/OAR9b7rXZuV4SmSTPJ2/HinW9Oa7588DotGMPTDtXzu+xlirQaDSaMqWkXDQajUajyR5t4DUajaZM0QZeo9FoyhRt4DUajaZM0QZeo9FoyhRt4DXXFHJVcfKYJJRHP5ysq5jvNXeIyCOLHOduEbluabPVaJaGNvCaa42wSlQ8bwNeQUK57+M2jHM3CRE8jWbZ0AZec82iEuXu9wPvT1bGOkXkb0Xk2aQ293+cdniNiPxbUpf7s6ldv4gEUgeIyG+JyAMicivwRuBvk1cL6wu6MI0mSamJjWk0eUUpdV5EnCQ0yO8iIX1wQ1L24Dci8mjy0BtJ7MgvAT8G3gx8O8M590ui4cgjSqm0x2g0hUDv4DWaq7yShM7NYRLSro3AxuRzz6iEJrdJQkYjL2p/Go2d6B285pomKS1sklD1E+ADSqmfzDrmDhK6ItNRs/4FqLBnlhpNbugdvOaaRUSaSSiS/qNKiDL9BPhPSeVRRGRTSqUUuDGp6OcA3gb8Ovl4v4hsTT7+pmmnnyTRqk2jWTa0gddca1Sm0iRJqPk9CvxZ8rnPk5AYfk4Szd7/hatXuc8C/0hCsfQCCS1ySPTVfIREk5lUpx5ItFb7YxE5pIOsmuVCq0lqNBpNmaJ38BqNRlOmaAOv0Wg0ZYo28BqNRlOmaAOv0Wg0ZYo28BqNRlOmaAOv0Wg0ZYo28BqNRlOm/H9YCZWPlQxH/gAAAABJRU5ErkJggg==\n"
     },
     "metadata": {
      "needs_background": "light"
     }
    }
   ],
   "source": [
    "dates_list = df.Debut\n",
    "dates_list=sorted(dates_list)\n",
    "date_data = {age: dates_list.count(age) for age in (dates_list)}\n",
    "score_df = pd.DataFrame.from_dict(data=date_data, orient=\"index\", columns=[\"number\"])\n",
    "score_df['year'] = score_df.index\n",
    "sns.lineplot(data=df, x=\"Debut\", y=\"Members\")"
   ]
  },
  {
   "source": [
    "### Большинство групп до 2007 не имеют название фандома: подтвердилось, мода на название фандома сравнительно новая."
   ],
   "cell_type": "markdown",
   "metadata": {}
  },
  {
   "cell_type": "code",
   "execution_count": 93,
   "metadata": {},
   "outputs": [
    {
     "output_type": "display_data",
     "data": {
      "application/vnd.plotly.v1+json": {
       "config": {
        "plotlyServerURL": "https://plot.ly"
       },
       "data": [
        {
         "labels": [
          "Have",
          "Don't"
         ],
         "type": "pie",
         "values": [
          107,
          192
         ]
        }
       ],
       "layout": {
        "template": {
         "data": {
          "bar": [
           {
            "error_x": {
             "color": "#2a3f5f"
            },
            "error_y": {
             "color": "#2a3f5f"
            },
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             }
            },
            "type": "bar"
           }
          ],
          "barpolar": [
           {
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             }
            },
            "type": "barpolar"
           }
          ],
          "carpet": [
           {
            "aaxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "baxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "type": "carpet"
           }
          ],
          "choropleth": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "choropleth"
           }
          ],
          "contour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "contour"
           }
          ],
          "contourcarpet": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "contourcarpet"
           }
          ],
          "heatmap": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmap"
           }
          ],
          "heatmapgl": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmapgl"
           }
          ],
          "histogram": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "histogram"
           }
          ],
          "histogram2d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2d"
           }
          ],
          "histogram2dcontour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2dcontour"
           }
          ],
          "mesh3d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "mesh3d"
           }
          ],
          "parcoords": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "parcoords"
           }
          ],
          "pie": [
           {
            "automargin": true,
            "type": "pie"
           }
          ],
          "scatter": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter"
           }
          ],
          "scatter3d": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter3d"
           }
          ],
          "scattercarpet": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattercarpet"
           }
          ],
          "scattergeo": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergeo"
           }
          ],
          "scattergl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergl"
           }
          ],
          "scattermapbox": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattermapbox"
           }
          ],
          "scatterpolar": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolar"
           }
          ],
          "scatterpolargl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolargl"
           }
          ],
          "scatterternary": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterternary"
           }
          ],
          "surface": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "surface"
           }
          ],
          "table": [
           {
            "cells": {
             "fill": {
              "color": "#EBF0F8"
             },
             "line": {
              "color": "white"
             }
            },
            "header": {
             "fill": {
              "color": "#C8D4E3"
             },
             "line": {
              "color": "white"
             }
            },
            "type": "table"
           }
          ]
         },
         "layout": {
          "annotationdefaults": {
           "arrowcolor": "#2a3f5f",
           "arrowhead": 0,
           "arrowwidth": 1
          },
          "autotypenumbers": "strict",
          "coloraxis": {
           "colorbar": {
            "outlinewidth": 0,
            "ticks": ""
           }
          },
          "colorscale": {
           "diverging": [
            [
             0,
             "#8e0152"
            ],
            [
             0.1,
             "#c51b7d"
            ],
            [
             0.2,
             "#de77ae"
            ],
            [
             0.3,
             "#f1b6da"
            ],
            [
             0.4,
             "#fde0ef"
            ],
            [
             0.5,
             "#f7f7f7"
            ],
            [
             0.6,
             "#e6f5d0"
            ],
            [
             0.7,
             "#b8e186"
            ],
            [
             0.8,
             "#7fbc41"
            ],
            [
             0.9,
             "#4d9221"
            ],
            [
             1,
             "#276419"
            ]
           ],
           "sequential": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ],
           "sequentialminus": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ]
          },
          "colorway": [
           "#636efa",
           "#EF553B",
           "#00cc96",
           "#ab63fa",
           "#FFA15A",
           "#19d3f3",
           "#FF6692",
           "#B6E880",
           "#FF97FF",
           "#FECB52"
          ],
          "font": {
           "color": "#2a3f5f"
          },
          "geo": {
           "bgcolor": "white",
           "lakecolor": "white",
           "landcolor": "#E5ECF6",
           "showlakes": true,
           "showland": true,
           "subunitcolor": "white"
          },
          "hoverlabel": {
           "align": "left"
          },
          "hovermode": "closest",
          "mapbox": {
           "style": "light"
          },
          "paper_bgcolor": "white",
          "plot_bgcolor": "#E5ECF6",
          "polar": {
           "angularaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "radialaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "scene": {
           "xaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "yaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "zaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           }
          },
          "shapedefaults": {
           "line": {
            "color": "#2a3f5f"
           }
          },
          "ternary": {
           "aaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "baxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "caxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "title": {
           "x": 0.05
          },
          "xaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          },
          "yaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          }
         }
        }
       }
      }
     },
     "metadata": {}
    }
   ],
   "source": [
    "fan_df = df.loc[df[\"Debut\"] < 2007]\n",
    "\n",
    "act_df = df.loc[df[\"Fanclub Name\"] != \"-\"]\n",
    "act_num = act_df.shape[0]\n",
    "nact_df = df.loc[df[\"Fanclub Name\"] == \"-\"]\n",
    "nact_num = nact_df.shape[0]\n",
    "\n",
    "\n",
    "labels = [\"Have\",\"Don't\"]\n",
    "values = [act_num, nact_num]\n",
    "fig = go.Figure(data=[go.Pie(labels=labels, values=values)])\n",
    "fig.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ]
}