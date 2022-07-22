{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Datatab_Netflix_Analysis.py",
      "provenance": [],
      "collapsed_sections": [],
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/ImranDemirci/Netflix-Original-Films-IMDB-Scores_DataAnalysis/blob/main/Datatab_Netflix_Analysis.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "**pandas, numpy, matplolib ve seaborn kütüphanelerini yükleyip, NetflixOriginals.csv dosyasını dataframe olarak açıyoruz.**"
      ],
      "metadata": {
        "id": "ZXBhFBEQlB8c"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import pandas as pd\n",
        "import numpy as np\n",
        "import matplotlib.pyplot as plt\n",
        "import seaborn as sns\n",
        "\n",
        "\n",
        "NetflixOriginals = pd.read_csv(\"NetflixOriginals.csv\",  encoding='ISO-8859-1')\n",
        "NetflixOriginals.head()\n",
        "NetflixOriginals.info()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "92766O6VlhVi",
        "outputId": "47afa146-179d-4400-e343-0c0164b89eff"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "<class 'pandas.core.frame.DataFrame'>\n",
            "RangeIndex: 584 entries, 0 to 583\n",
            "Data columns (total 6 columns):\n",
            " #   Column      Non-Null Count  Dtype  \n",
            "---  ------      --------------  -----  \n",
            " 0   Title       584 non-null    object \n",
            " 1   Genre       584 non-null    object \n",
            " 2   Premiere    584 non-null    object \n",
            " 3   Runtime     584 non-null    int64  \n",
            " 4   IMDB Score  584 non-null    float64\n",
            " 5   Language    584 non-null    object \n",
            "dtypes: float64(1), int64(1), object(4)\n",
            "memory usage: 27.5+ KB\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Uzun soluklu filmlerin hangi dillerde oluşturulduğunu görselleştiriyoruz."
      ],
      "metadata": {
        "id": "SkWpvmTzllMI"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "uzun_soluklu = NetflixOriginals[(NetflixOriginals[\"Runtime\"] > (NetflixOriginals[\"Runtime\"].mean()))].groupby(\"Language\").agg({\"Runtime\": \"count\"}).sort_values(by = \"Runtime\", ascending= False)\n",
        "uzun_soluklu.reset_index(inplace=True)\n",
        "\n",
        "plt.figure(figsize=(19,9))\n",
        "us = sns.barplot(x=\"Language\", y=\"Runtime\", data=uzun_soluklu)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 551
        },
        "id": "dVgSIno3l9bE",
        "outputId": "26f26c7c-488c-484a-d096-baa4fbcf2254"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 1368x648 with 1 Axes>"
            ],
            "image/png": "iVBORw0KGgoAAAANSUhEUgAABFoAAAIWCAYAAABndOm+AAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADh0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uMy4yLjIsIGh0dHA6Ly9tYXRwbG90bGliLm9yZy+WH4yJAAAgAElEQVR4nOzdeZgtV1kv/u9LwhBmISEXmQ4gosgQMRdRUBkUQkADgiCigD8wDkwqeq9c/En06hVUHBBFmW4QAUUGCYgKRBBBEAIECCAQICEJkIRBhjAmWfePtXbOTqe7T3ef1adPw+fzPP303rWrar+7hlVV36rau1prAQAAAGD/XW6nCwAAAAD4eiFoAQAAAJhE0AIAAAAwiaAFAAAAYBJBCwAAAMAkghYAAACASQ7d6QL2x+GHH9727Nmz02UAAAAA30De9ra3fbK1dsRqr+3qoGXPnj055ZRTdroMAAAA4BtIVZ251mtuHQIAAACYRNACAAAAMImgBQAAAGASQQsAAADAJIIWAAAAgEkELQAAAACTCFoAAAAAJhG0AAAAAEwiaAEAAACYRNACAAAAMImgBQAAAGASQQsAAADAJIIWAAAAgEkELQAAAACTCFoAAAAAJhG0AAAAAEwiaAEAAACYRNACAAAAMImgBQAAAGASQQsAAADAJIIWAAAAgEkO3ekCZjr/aX+90yUkSY74+Z/c6RIAAACAHeCKFgAAAIBJBC0AAAAAkwhaAAAAACYRtAAAAABMImgBAAAAmETQAgAAADCJoAUAAABgEkELAAAAwCSCFgAAAIBJBC0AAAAAkwhaAAAAACYRtAAAAABMImgBAAAAmETQAgAAADCJoAUAAABgEkELAAAAwCSCFgAAAIBJBC0AAAAAkwhaAAAAACYRtAAAAABMImgBAAAAmETQAgAAADCJoAUAAABgEkELAAAAwCSCFgAAAIBJBC0AAAAAkwhaAAAAACYRtAAAAABMImgBAAAAmETQAgAAADCJoAUAAABgEkELAAAAwCSCFgAAAIBJBC0AAAAAkwhaAAAAACYRtAAAAABMImgBAAAAmETQAgAAADCJoAUAAABgEkELAAAAwCSCFgAAAIBJBC0AAAAAkwhaAAAAACYRtAAAAABMImgBAAAAmETQAgAAADCJoAUAAABgEkELAAAAwCSCFgAAAIBJBC0AAAAAkwhaAAAAACYRtAAAAABMImgBAAAAmETQAgAAADCJoAUAAABgEkELAAAAwCSCFgAAAIBJBC0AAAAAkwhaAAAAACYRtAAAAABMsm1BS1XdoKpeW1Xvrar3VNVjRvdrVdWrq+qD4/83je5VVU+pqtOr6l1Vddvtqg0AAABgO2znFS0XJnlsa+0WSW6f5BFVdYskv5bk5NbazZKcPJ4nyT2S3Gz8HZ/kadtYGwAAAMB02xa0tNY+3lp7+3j8+STvS3K9JMclec7o7TlJ7j0eH5fkr1r35iTXrKrrbld9AAAAALMdkO9oqao9Sb4zyX8kObK19vHx0ieSHDkeXy/JWUuDnT26rRzX8VV1SlWdcv75529bzQAAAACbte1BS1VdNcmLk/xia+1zy6+11lqStpnxtdae3lo7urV29BFHHDGxUgAAAID9s61BS1VdPj1keV5r7SWj87mLW4LG//NG93OS3GBp8OuPbgAAAAC7wnb+6lAleVaS97XW/nDppZOSPGQ8fkiSly11f/D49aHbJ/ns0i1GAAAAAAe9Q7dx3HdI8lNJ3l1Vp45u/yvJE5O8sKoeluTMJPcfr70yybFJTk/yxSQ/vY21AQAAAEy3bUFLa+0NSWqNl++6Sv8tySO2qx4AAACA7XZAfnUIAAAA4BuBoAUAAABgEkELAAAAwCSCFgAAAIBJBC0AAAAAkwhaAAAAACYRtAAAAABMImgBAAAAmETQAgAAADCJoAUAAABgEkELAAAAwCSCFgAAAIBJBC0AAAAAkwhaAAAAACYRtAAAAABMImgBAAAAmETQAgAAADCJoAUAAABgEkELAAAAwCSCFgAAAIBJBC0AAAAAkwhaAAAAACYRtAAAAABMImgBAAAAmETQAgAAADCJoAUAAABgEkELAAAAwCSCFgAAAIBJBC0AAAAAkwhaAAAAACYRtAAAAABMImgBAAAAmETQAgAAADCJoAUAAABgEkELAAAAwCSCFgAAAIBJBC0AAAAAkwhaAAAAACYRtAAAAABMImgBAAAAmETQAgAAADCJoAUAAABgEkELAAAAwCSCFgAAAIBJBC0AAAAAkwhaAAAAACYRtAAAAABMImgBAAAAmETQAgAAADCJoAUAAABgEkELAAAAwCSCFgAAAIBJBC0AAAAAkwhaAAAAACYRtAAAAABMImgBAAAAmETQAgAAADCJoAUAAABgEkELAAAAwCSCFgAAAIBJBC0AAAAAkwhaAAAAACYRtAAAAABMImgBAAAAmETQAgAAADCJoAUAAABgEkELAAAAwCSCFgAAAIBJBC0AAAAAkwhaAAAAACYRtAAAAABMImgBAAAAmETQAgAAADCJoAUAAABgEkELAAAAwCSCFgAAAIBJBC0AAAAAkwhaAAAAACYRtAAAAABMImgBAAAAmETQAgAAADCJoAUAAABgEkELAAAAwCSCFgAAAIBJBC0AAAAAkwhaAAAAACYRtAAAAABMImgBAAAAmETQAgAAADCJoAUAAABgEkELAAAAwCTbFrRU1bOr6ryqOm2p2wlVdU5VnTr+jl167XFVdXpVvb+q7r5ddQEAAABsl+28ouXEJMes0v2PWmtHjb9XJklV3SLJjyf5jjHMn1fVIdtYGwAAAMB02xa0tNZen+TTG+z9uCR/01r7SmvtI0lOT3K77aoNAAAAYDvsxHe0PLKq3jVuLfqm0e16Sc5a6ufs0Q0AAABg1zjQQcvTktw0yVFJPp7kyZsdQVUdX1WnVNUp559//uz6AAAAALbsgAYtrbVzW2sXtdYuTvKM7L096JwkN1jq9fqj22rjeHpr7ejW2tFHHHHE9hYMAAAAsAkHNGipqusuPb1PksUvEp2U5Mer6opVdeMkN0vylgNZGwAAAMD+OnS7RlxVL0hypySHV9XZSZ6Q5E5VdVSSluSMJD+bJK2191TVC5O8N8mFSR7RWrtou2oDAAAA2A7bFrS01h64SudnrdP/7yT5ne2qBwAAAGC77cSvDgEAAAB8XRK0AAAAAEwiaAEAAACYRNACAAAAMImgBQAAAGASQQsAAADAJIIWAAAAgEkELQAAAACTCFoAAAAAJhG0AAAAAEwiaAEAAACYRNACAAAAMImgBQAAAGASQQsAAADAJIIWAAAAgEkELQAAAACTCFoAAAAAJhG0AAAAAEwiaAEAAACYRNACAAAAMImgBQAAAGASQQsAAADAJIIWAAAAgEkELQAAAACTCFoAAAAAJhG0AAAAAEwiaAEAAACYRNACAAAAMImgBQAAAGASQQsAAADAJIIWAAAAgEkELQAAAACTCFoAAAAAJtlU0FJVV96uQgAAAAB2uw0FLVX1vVX13iT/OZ7fpqr+fFsrAwAAANhlNnpFyx8luXuSTyVJa+2dSb5/u4oCAAAA2I02fOtQa+2sFZ0umlwLAAAAwK526Ab7O6uqvjdJq6rLJ3lMkvdtX1kAAAAAu89Gr2j5uSSPSHK9JOckOWo8BwAAAGDY0BUtrbVPJnnQNtcCAAAAsKttKGipqhsneVSSPcvDtNZ+ZHvKAgAAANh9NvodLX+f5FlJXp7k4u0rBwAAAGD32mjQ8uXW2lO2tRIAAACAXW6jQcufVNUTkrwqyVcWHVtrb9+WqgAAAAB2oY0GLbdK8lNJ7pK9tw618RwAAACAbDxo+bEkN2mtfXU7iwEAAADYzS63wf5OS3LN7SwEAAAAYLfb6BUt10zyn1X11lz6O1r8vDMAAADAsNGg5QnbWgUAAADA14ENBS2ttX/d7kIAAAAAdrt1g5aqekNr7Y5V9fn0Xxm65KUkrbV29W2tDgAAAGAXWTdoaa3dcfy/2oEpBwAAAGD32tCvDlXVczfSDQAAAOAb2UZ/3vk7lp9U1aFJvmt+OQAAAAC717pBS1U9bnw/y62r6nPj7/NJzk3ysgNSIQAAAMAusW7Q0lr73fH9LL/fWrv6+Ltaa+3arbXHHaAaAQAAAHaFjf688+Oq6npJbrQ8TGvt9dtVGAAAAMBus6GgpaqemOTHk7w3yUWjc0siaAEAAAAYNhS0JLlPkpu31r6yncUAAAAA7GYb/dWhDye5/HYWAgAAALDbbfSKli8mObWqTk5yyVUtrbVHb0tVAAAAALvQRoOWk8YfAAAAAGvY6K8OPWe7CwEAAADY7Tb6q0MfSf+VoUtprd1kekUAAAAAu9RGbx06eunxlZL8WJJrzS8HAAAAYPfa0K8OtdY+tfR3Tmvtj5Pcc5trAwAAANhVNnrr0G2Xnl4u/QqXjV4NAwAAAPANYaNhyZOXHl+Y5Iz024cAAAAAGDb6q0N3Xn5eVYck+fEkH9iOogAAAAB2o3W/o6Wqrl5Vj6uqp1bVD1X3yCSnJ7n/gSkRAAAAYHfY1xUtz03ymSRvSvIzSR6fpJLcp7V26jbXBgAAALCr7CtouUlr7VZJUlXPTPLxJDdsrX152ysDAAAA2GX29fPOX1s8aK1dlORsIQsAAADA6vZ1Rcttqupz43ElOWw8rySttXb1ba0OAAAAYBdZN2hprR1yoAoBAAAA2O32desQAAAAABskaAEAAACYRNACAAAAMImgBQAAAGASQQsAAADAJIIWAAAAgEkELQAAAACTCFoAAAAAJhG0AAAAAEwiaAEAAACYRNACAAAAMImgBQAAAGASQQsAAADAJIIWAAAAgEkELQAAAACTCFoAAAAAJhG0AAAAAEyybUFLVT27qs6rqtOWul2rql5dVR8c/79pdK+qekpVnV5V76qq225XXQAAAADbZTuvaDkxyTEruv1akpNbazdLcvJ4niT3SHKz8Xd8kqdtY10AAAAA22LbgpbW2uuTfHpF5+OSPGc8fk6Sey91/6vWvTnJNavquttVGwAAAMB2ONDf0XJka+3j4/Enkhw5Hl8vyVlL/Z09ul1GVR1fVadU1Snnn3/+9lUKAAAAsEk79mW4rbWWpG1huKe31o5urR19xBFHbENlAAAAAFtzoIOWcxe3BI3/543u5yS5wVJ/1x/dAAAAAHaNAx20nJTkIePxQ5K8bKn7g8evD90+yWeXbjECAAAA2BUO3a4RV9ULktwpyeFVdXaSJyR5YpIXVtXDkpyZ5P6j91cmOTbJ6Um+mOSnt6suAAAAgO2ybUFLa+2Ba7x011X6bUkesV21AAAAABwIO/ZluAAAAABfbwQtAAAAAJMIWgAAAAAmEbQAAAAATCJoAQAAAJhE0AIAAAAwiaAFAAAAYBJBCwAAAMAkghYAAACASQQtAAAAAJMIWgAAAAAmEbQAAAAATCJoAQAAAJhE0AIAAAAwiaAFAAAAYBJBCwAAAMAkghYAAACASQQtAAAAAJMIWgAAAAAmEbQAAAAATCJoAQAAAJhE0AIAAAAwiaAFAAAAYBJBCwAAAMAkghYAAACASQQtAAAAAJMIWgAAAAAmEbQAAAAATCJoAQAAAJhE0AIAAAAwiaAFAAAAYBJBCwAAAMAkghYAAACASQQtAAAAAJMIWgAAAAAmEbQAAAAATCJoAQAAAJhE0AIAAAAwiaAFAAAAYBJBCwAAAMAkghYAAACASQQtAAAAAJMIWgAAAAAmEbQAAAAATCJoAQAAAJhE0AIAAAAwiaAFAAAAYBJBCwAAAMAkghYAAACASQQtAAAAAJMIWgAAAAAmEbQAAAAATCJoAQAAAJhE0AIAAAAwiaAFAAAAYBJBCwAAAMAkghYAAACASQQtAAAAAJMIWgAAAAAmEbQAAAAATCJoAQAAAJhE0AIAAAAwiaAFAAAAYBJBCwAAAMAkghYAAACASQQtAAAAAJMIWgAAAAAmEbQAAAAATCJoAQAAAJhE0AIAAAAwiaAFAAAAYBJBCwAAAMAkghYAAACASQQtAAAAAJMIWgAAAAAmEbQAAAAATCJoAQAAAJhE0AIAAAAwiaAFAAAAYBJBCwAAAMAkghYAAACASQQtAAAAAJMIWgAAAAAmEbQAAAAATCJoAQAAAJhE0AIAAAAwiaAFAAAAYBJBCwAAAMAkghYAAACASQQtAAAAAJMIWgAAAAAmOXQn3rSqzkjy+SQXJbmwtXZ0VV0ryd8m2ZPkjCT3b619ZifqAwAAANiKnbyi5c6ttaNaa0eP57+W5OTW2s2SnDyeAwAAAOwaB9OtQ8clec54/Jwk997BWgAAAAA2baeClpbkVVX1tqo6fnQ7srX28fH4E0mOXG3Aqjq+qk6pqlPOP//8A1ErAAAAwIbsyHe0JLlja+2cqrpOkldX1X8uv9haa1XVVhuwtfb0JE9PkqOPPnrVfgAAAAB2wo5c0dJaO2f8Py/JS5PcLsm5VXXdJBn/z9uJ2gAAAAC26oAHLVV1laq62uJxkrslOS3JSUkeMnp7SJKXHejaAAAAAPbHTtw6dGSSl1bV4v2f31r7p6p6a5IXVtXDkpyZ5P47UBsAAADAlh3woKW19uEkt1ml+6eS3PVA1wMAAAAwy8H0884AAAAAu5qgBQAAAGASQQsAAADAJIIWAAAAgEkELQAAAACTCFoAAAAAJhG0AAAAAEwiaAEAAACYRNACAAAAMImgBQAAAGASQQsAAADAJIIWAAAAgEkELQAAAACTCFoAAAAAJhG0AAAAAEwiaAEAAACYRNACAAAAMImgBQAAAGASQQsAAADAJIIWAAAAgEkELQAAAACTCFoAAAAAJhG0AAAAAEwiaAEAAACYRNACAAAAMImgBQAAAGASQQsAAADAJIIWAAAAgEkELQAAAACTCFoAAAAAJhG0AAAAAExy6E4X8I3q3Kc9eadLSJIc+fOP3ekSAAAA4OuGK1oAAAAAJhG0AAAAAEwiaAEAAACYRNACAAAAMImgBQAAAGASQQsAAADAJIIWAAAAgEkELQAAAACTCFoAAAAAJhG0AAAAAEwiaAEAAACYRNACAAAAMImgBQAAAGASQQsAAADAJIIWAAAAgEkELQAAAACTCFoAAAAAJhG0AAAAAEwiaAEAAACYRNACAAAAMImgBQAAAGASQQsAAADAJIIWAAAAgEkELQAAAACTCFoAAAAAJhG0AAAAAEwiaAEAAACY5NCdLoCD21l/+qCdLiFJcoNHPW+nSwAAAIB9ckULAAAAwCSCFgAAAIBJBC0AAAAAkwhaAAAAACYRtAAAAABMImgBAAAAmETQAgAAADCJoAUAAABgEkELAAAAwCSCFgAAAIBJBC0AAAAAkxy60wXALG//ix/e6RKSJLf9uZfvdAkAAADsEFe0AAAAAEwiaAEAAACYRNACAAAAMInvaIED7DXPPHanS0iS/ODDX7nTJQAAAHzdcUULAAAAwCSuaAFW9aL/e8xOl5Akud9P/9NOlwAAALBhrmgBAAAAmETQAgAAADCJoAUAAABgEt/RAux6z/qru+90CUmShz34n3e6BAAAYIe5ogUAAABgEkELAAAAwCSCFgAAAIBJfEcLwAHyBy84OL5L5lce6LtkAABgu7iiBQAAAGASV7QAcBm/+OJjdrqEJMkf3/ef1n39Hi972AGqZH3/eNyzdroEAAAOEq5oAQAAAJjEFS0AcAAc+9Lf3ukS8sr7/Po++7nnS556ACrZt3/40Ueu+/q9XnzigSlkH15x34fudAkAwEHGFS0AAAAAkxx0V7RU1TFJ/iTJIUme2Vp74g6XBACwZfd60Qt3uoQkySvud/91Xz/uRa88QJWs72X3O3anSwCA/XJQXdFSVYck+bMk90hyiyQPrKpb7GxVAAAAABtzsF3Rcrskp7fWPpwkVfU3SY5L8t4drQoAgIPGfV78hp0uIS+97x332c/9X3xw7MK+8L7rn7c84aUfO0CVrO+E+3zzPvt53ovPPwCV7NuD7nvEuq+/5vkHR50/+BPr15kk73jmeQegkn37zodfZ93Xz3ryJw5QJeu7wWP/27qvf+IPD471/r/98r6vVzj3T954ACrZtyMfc4d1Xz/vqQfHFZfXeeTGr7g8qK5oSXK9JGctPT97dAMAAAA46FVrbadruERV3S/JMa21h4/nP5Xku1trj1zq5/gkx4+nN0/y/sllHJ7kk5PHuV12S627pc5k99Sqzvl2S627pc5k99Sqzvl2S627pc5k99S6W+pMdk+t6pxvt9S6W+pMdk+t6pxvt9S6HXXeqLW26mVjB9utQ+ckucHS8+uPbpdorT09ydO3q4CqOqW1dvR2jX+m3VLrbqkz2T21qnO+3VLrbqkz2T21qnO+3VLrbqkz2T217pY6k91Tqzrn2y217pY6k91Tqzrn2y21Hug6D7Zbh96a5GZVdeOqukKSH09y0g7XBAAAALAhB9UVLa21C6vqkUn+Of3nnZ/dWnvPDpcFAAAAsCEHVdCSJK21VybZya8V3rbbkrbBbql1t9SZ7J5a1Tnfbql1t9SZ7J5a1Tnfbql1t9SZ7J5ad0udye6pVZ3z7ZZad0udye6pVZ3z7ZZaD2idB9WX4QIAAADsZgfbd7QAAAAA7FpfV0FLVV1UVacu/f3afozrC+P/N1fVi9bpb09VnbbV91ntPZeeP7Sqnjoe/1xVPXiT43tdVR09Hr+yqq65yeEfX1Xvqap3jen53ZsZfgPj//d9vP6F9V5fY5iVy8Cerda3j/e5U1W9Yj/HsVjG9lTVT2yg/0uWtao6uqqessX3XUyj06rq76rqypsY9qiqOnYr77sVm10GZsyXTbzXb1XVD25huC8sPT62qj5QVTeaW93mbWV922lVde2ldf0TVXXO0vMr7GPYVdvufa1bW1nGqurIqnp+VX24qt5WVW+qqvtsZhwHSlW1qvrrpeeHVtX5s9arqrpmVf3C0vM1p2dVPbOqbrHB8S7atfdU1Tur6rFVtc99nKr6Xxvo58Squt9G6thAfZdsmxbbwM227fvaL5lpM9uLfe2zrJgGn6iqf9iPulbdR1ulff1wVb1/rXlYVbevqmesXA6r6rer6p+q6opbrO9tVXXFqjqjqt699Lm3tN0e42xL47qg1tnHXa89r6rrVtWFY7n7UlX911rt5lrt5NLrq06/Vfq7ZNmYbatt1j7anoPueGIxrZee//HY5l1uqduG6t7HZ3/laKf3q+7aewxxelV9qsYxxBp1n1BVv7LWe6zxvls+hhjrwKvG428dbcRXxvrwmaq6xzrDbmWffb9rXVpfl+fvpo4L16jtMtucuvS+1adXvO+6+1brvOclx6Hrfd4tjnutfcH/qqr3bnJcmz7eXs9B9x0t++lLrbWjZo6wtfaxJPu1gzWpjr/Yz+E3dXBcVd+T5F5Jbtta+0pVHZ5kSyvXOjV978zxDWsuA1VV6bfLXbwN77s/9iT5iSTP3+gArbVTkpyyxfe7ZBpV1fOS/FySP9zXQFV1aJKjkhydnf0epYNCa+039mf4qrprkqckuXtr7cwN9H+wLr87prX2qfRlMlV1QpIvtNb+YF/DjWV5rXHuz7q12ntVkr9P8pzW2k+MbjdK8iMbHP7Q1tqFs+rZgAuS3LKqDmutfSnJDyU5ZzMj2EfN10zyC0n+fF/jaa09fBNvu9yuXSe9Pb16kifsY7j/leT/bOJ9tmq1bdNltoEbWf4O8H7JlrYXa+yzLI/rhCT7vbO91rRYal8fmvWXtXsk+acVw/56kjskOba19pV91bBY3pf+3zjJOWPfKUnu3Fr75EY/0zrapHEdk+Si8fhDrbVbrtbTeu3kkstMvx2w323WKg7G44lLpvUIKe6T5KwkP5DktaOf5XVsS9uOxfHCWHa3VPfyMUR6G/uRJGetU/em7ecxxDFJ/rmqrpTk5PRl6OpjnT0uyZfXGXZPNr/Pvt+1jscf2obl8jLbnBX7Vicmud3+vu9mj0M3Oe5V9wWrn2zf1Emi/T3eXunr6oqWtVQ/o/CbVfX26mcDvm10P6KqXj0S12dW1ZkjUFgedjn1+46qestIyd5VVTcbvR1SPdF/z0gdD9uGz3BJ2lv9SpUnjVo+UFXfN7ofVlV/U1Xvq6qXJjlsafgzVn62fbhukk8udjJaa59srX1sjOf3xnR8S1V9yxj/D1fVf1TVO6rqNVV15FLdzx41f7iqHr1U0yItv25Vvb72njX7vqV+fqf62ck3L8a5yem2p3pS/VdJTktyg6r61ap665iHv7nU3/tWm49V9S3jM71zLEM3HaO/alW9qKr+s6qeV4ut0uY9Mcn3jc//S6OWfxvv9faqukwDXUtnI6rqdtXPkL+jqv69qm4+uj+0ql5S/azcB6vq91Z5739L8i1Vda2q+vsxTd5cVbce4zihqp5bVW9M8twkv5XkAaPWB9SKsxBj/u0Zj///Me3fUFUvWLH8Lq60OryqzhiPD6mq31+aNz87ul93TPsvVNVnx3r6vKq62/jcp1fV56rq1CQ/ulTLep9prWXyJ2vvOv6Xo6ZDqp8NPW0s9780+j2xxhnSqvqNUfdpVfX0xbJQa6+r35/kGUnu1Vr70Oj2y2P406rqF0e3DS2/o9+/r34W9T1VdfxS9y/UBtejqrpqVZ1ce9vK45bqWCzn7xvL/ZW3+NnXm8+XaQeW5vPbq59Rv+pa9a+cL4vPP/7fqfp6dVKS964Y5ibV15//Xpdet36g9p4leUdVXW0Mspl1/y5Jvrq88W6tndla+9N1psWlah3P/7WqXjaW2SdW1YPGtH13jTapttAOr+GVSe45Hj8wyQuWptV67c1JVfUvSU5ea1lKb+9uOqbp7683PWuprdiM1tp5SY5P8sjqHlpLZ9Or6hVjmj4xyWGjlueN1x485sU7q+q5S6P9/vF5P1z7eXXLUh2XCRpWLH+L9vdN1dvwnxndl/dL1mznq+qBY9qfVlVPmlDyutuLFZ9jeZ/l0dXPKh5WVX+z1Nstxjz+WlX9Y03YRxvv8cH0ZfgRST6a/iuW35vkL6uf4fzI0jz80SS/lOS3k9y5qk5O8lNJrpbkLVX17VX1f6vqvWPY/xzr62+P5f0jSc6pqjcleYDc9LwAABsoSURBVH9VvSXJ65N8bIz/0CQvrxXb87HMfbT62eKvVt/nqKq6clW9cLzfS8f6fJl1oC69//Tl6mdxv1RVH1qafn9UVZ+vqi9W1V8vTb9jkiwOwC9fl97HfV+NbW2SD6YfJ1y3+hUiXx51HTaW09eNafy7SR6/VNtDxvt+afy/7Xjp9lV17qjn01X1hKVhNrX9GsvGi6vqren7uu9Kcs+q+oEkz0tynfT9qqtVb7POrH4V0AW1ypU1taJdS7Jog15fVUct9fflqvqLGctqbf544q5JXjMe3ynJe5I8Lb2NXrhCLe2z1d79ya9U1cer70+8O8kNk1x91HzBmB+Luj+6qL16e/i+MS+fu9G6k9woe48h7prkpSOw+Vj6sne9JH9b4xgiybcmedSY/u+tvu04rKpeO5a9C6rv5z161PW66uvNW8Yyv9hOb/QY4pgk/5gemHwoyQeXjnde1lp7bVWdXVVnjc9+QVX92Bj2L5IcM5bjD1S/IuTfxvT95Fg2Ppwe8i7quGD0866xTnxg1Pqo6uvRlcawn1mn1jWts57cdDx/d/U2a1/bnLX2ea5Yff1cXPHz4tq7D3hiVT1tvM+Hx/iePZabE5fe54yV68QBsuo6VVU/U70tf+eKz3Op45r91lr7uvlLT+hPXfp7wOh+RpJHjce/kOSZ4/FTkzxuPD4m/WzB4eP5F8b/PUlOG4//NMmDxuMrpDfue9IbjaNG9xcm+clJ9X80yVPHayck+ZXx+HVJnjweH5vkNePxL6f/JHaS3HrUdfTSNDh8E7VcddTwgfSzQT+wNJ7Hj8cPTvKK8fibkku+XPnhS/WdkOTfk1wxyeFJPpXk8ium8WOXxnlIkquNxy3JD4/Hv5fk1zc5DV865s/FSW4/Xr9b+jdOV/oOxCuSfP968zHJfyS5z3h8pSRXTt/IfTbJ9cd43pTkjpuc34vPf6fFdBzPr5zkSuPxzZKcssqyeMkw6WdtDx2PfzDJi8fjhyb5cJJrjLrPTHKDpfc9NMnLkvx8+rL9hNH9LklOXZp/b0ty2NI4n7pU6wkZy+V4ftqo87+PeXCl9B3WD+bSy+9iuTw8yRnj8fGLeZy+vJySfpbhsUmeOab3DcfnfesY/7XSz4z8XpLfGPNtMV3W+0yXWSaTfHuSl2fv8vnn6cv4dyV59dJnvOb4f2KS+43H11p6/bnZu9y+LivW1SRfS/LpJLdeGua7krw7yVXS1733JPnObHD5Xa4hvV06Lcm1N7MepZ9dPjT9rM5i3pw+3mvPGM8dxmvPXpqfG/7s68znG2eVdmDU8PokVxnd/2eS31ij/hOS/MryfFllPbsgyY2X16ckN0/yjiS3WWXdevnSZ77qmD53yibW/SSPTvJHa7y21rRYWeudkvxXegB+xfSztb85XntMkj/eaju8xnJw6yQvSl9/T83G25uzs3c5XG9ZOm3p/dacnllqKzbanq7o9l9Jjsxl261XJLnTyuGSfEf6Nm+xH7D4LCcm+btR3y2SnL6RmlbUcqlt04pl85JpsmJan5Dknenr9OHpbd03r+j/oVm9nf/m9H2II8a8+Jck995C3ZvZXlwynXPpfZaPpS97F6W3c6cm+USS94/uH01f3i+f/d9HuzC9fb1tLr2PdtKYhy9M8j/Sl8fD09f9/0oPXD4z+v3dpXXr9ent3fPTD8o+mr5d/lj68v6k9G3k72XvPsM/pJ/Bv8qYH6eNz/zeJB8d/Zya5Cvpy/09Rw13TG/D/nL0c8tcej+uLU2/i5I8IL3d/EySR6W3m7+Uvr1s6cv540ZtzxndrjOG/8KYNl9O8qXR7V3pgdMF6Qe+h43hL0o/W3zFMW1/KX05/Vx6u3K59G3WG9P3jT+SvdusH0nykvRl47z0+b5YNv9z6bNtavs15seinbggfR140Zj2Hxz1/WP6cnvv9BMblX61y8fT9/vulLXbtTamyZlJzh/T+lvHPDvgxxPpy+prl9bLZ6QHgldP3x4s9lsuTvLF9Hbj1NHPldL33X8rfRvzC2M6fTnJX6VfcfLq9Hnfxrw5fIznA+n7Iqel729ttO6Hjfc/fdT3A+O1z6evh1dPX5b+YXR/Yvqy/8j0dXKxTXtS9m67Xpi+zF0+fdvw1aVpcfp4vM9jiNHPos36wyS/mtWPd87M3nbuV5P813h8r+xdbh6e5E/GND4hydvT24PD09fLxfz+wujnseM9Txl13CN9+9fS15U3pQeFq9W6J3vX1cXf9+3js74iyQPH45/Lvrc5q+3znDje95bZu41+TvauBycm+Zv09eu4MY9uNfp9W/YuF2dkxTqxHX+59LZnT9Zep669NMxvL32eS4af8feNdOvQS8b/t2XvWe87pl/CltbaP1XVZ/Yx/jcleXxVXT/JS1prH6x+4u0jrbVTl8a/Z0b9VfXQ9Ns0VrP8eRbv9/3pl8qmtfauqnrXFutIa+0LVfVdSb4vyZ3Tk+fFvZ4vWPr/R+Px9Uc/183eDe3CP7SeFH+lqs5L3/E9e+n1tyZ5dlVdPsnfL03Lr2bvJV9vS99A7svKabgnyZmttTePTncbf+8Yz6+avtP00awyH0eae73W2kvHdPnyGG+SvKW1dvZ4fmr6fHjDBmrcl8sneWr1sygXpW/c13ONJM8ZZxbaGH7h5NbaZ0eN700/y3DYqDfpZyiflR4m3TdJWmv/Uv1+x6uPfk5q/XLczbhDkpeN6fXlqnr5Boa5W5Jb194zjddIb6jfmh4ifjJ9Z+yjVXV++rL5pvSDy3uNx3+dfvCa9PV7rc+02jJ51/TA461j/h6WvmP48iQ3qao/Td85edUqtd+5qv5Hekh2rfSdzsVnXrmufi19x+Fh6Tvyi1pf2lq7IEmq6iXj852UjS2/r0/y6Nr7vR83GN0/lc2tR5Xk/1S/4ubi9LNOizMrZ7XW3jge/3V6gPAHm/zsi8+wcj7fLKu0A9XPTt4iyRvHPLlC+nzeqre01pbbpiPSDx5/tLW22n28b0zyh9WvdnhJa+3s/V33q+rP0uf3V9N35FabFl9dpda3ttY+PsbxoexdDt+d3kYn+9cOX2JsP/aknyldeZvgeu3Nq1trn1581Ky9LK20XW3pZt0lyd+1cWvG0mdJ+jJ5cfoVRpu+ujJbvxXhZaP9/VJVvTbJ7dJ3sJet1s5fO8nrWmvnj+7PS99H+PtNvv9mtxereVf6wcPXknzP2L84IcnXWr9U/+L04OLI7P8+2iOSnJvkMa21hyz20dIP6l6dvo5cYbzX3dLbnU+O109PP5j4/Bjfu9PD3RPSDyRukd7GvTx9+/CK9AOQk5L8cJJjq+pX09fhT6afGEh6wPLt6ev18hndd4425WvZG0LeMf3ALa2101bsx7WMW4eq6guttb8d69dVx7C3St+23HO81/VH3bdLb/c/k76N+48kiysJzkyfD0dV/96J30kPQ1pr7UvVrw64KP1gauE26dugM5O8vLV2cVWdPj7vzcdn/58r2ojFlYQfbf3q6PeM97lj+kHnZrdfP5h+RVTSD2CvmOQm6VcnXDl9Gbp867dy3SM9JPvJMewhY/wfWvpMK9u1NqbJldOX35ck+d/pB8w7cTxxt4w2v/p3ZByb5Jdba5+vqv9IcvcxnS5M8qTW2uJq7WukBxHfnL7O3niM92FJ3pIeqj8hfV7cOn0ZWTgkPRT5zPhcn65+5dZG6r5u+rJ2QvrVZH9bVY9PX29+q7X2uar61/T9rqQHL48Y0/7jSb5tdN+Tvjyckr7ufTl7tyOLq7JekeQho03ZyDHEd6evA1nqb63jnaOqXwF0UfoykvT9hu8e3a+QHoA/I30eXZzkGmMd/VQu/RUdzxjTYnFS4Vbp7cdb0tvml6cHLxdm73xfWetatw6t9Vm/Jz1oTHo4ua9bq9fa5zkrfZvyr+nHJDcdtS+8vLXWxjQ5t7X27iQZ6/meXHabdSCttU7dsqp+O/125qtm7+1ZU31D3Do0LO6zvShb/G6a1trz0xPHLyV5ZVXdZcW492v8m7Tfn2dfWmsXtdZe11p7QnrKfN/FS8u9jf9/mn4m61ZJfjZ9w7ey1lXrba29Pr2ROSfJibX3S4i+1ka8uNpwm3DB0uNKP1t11Pj7ltbaszZS5yq2a77/UvqO4m3Sg7Z9fTfO/04/03HL9J29fU37Ly19/ke11r66j/FfsM5rF+bS7ciV1upxjWGW+6/0RHlR242TXDSWj0en7+Aslo+L0w/oH5Dk7a21W7TWHraB915YbbpU+vdoLN7/5q21E1prn0mfF69LPyPwzOURVb/H98/Tr6K4VfrGdLV5sHifi5PcP8ntagNfxJkNLL9Vdaf0Hc/vaa0tdoIXNWxmPXpQ+k7Ed42N+blL42kr+m1b+OyLz3Cp+dxae9Ua7UClH7wv+t3IfL5k+ap+P/jy+rNyWf5sesh6x9VG1Fp7YvoZq8PSw57Fzt9m1v33pJ9dX4zzEek7l0dkjWmxRq3L73nx0vOLl95/y+3wKk5K3yl7wYru67U3yzWvtyytNL0traqbjHGdl621Uyst17jV20S34jLr3Sr9bOc+yGa3F6u5Z5I/ywjOa+93fyzXfWF63fu7j/al9Db6/lW1aKu/svR/ub2/R/pBzuL1c9MPqh9dVXdOX7cW8/pySW6f3rbeP307/dnx2gWjv/umnxR4Rmvthq2196UfnJ2f1bfny+1jbeVzj3bzE+mh6YnpB9yHpodaC8vT9K5Z4ztVxvR7fC69j1tJPrZYBtK/z+iMMcg3LY1reVrdMKu3ERdm7/J7Ufo0bVvcfl0u/aqZo9KX0eulh4h3Sb+654pJvne02XdIPxA8LD3w+tjSft/CynZtMU2+mB7QHZc+3y/IzhxPLH8Xzt3TDw7fXf3W6zvm0rcPLbfDi/3Jj6VPmyuM8R6SjbUtW667tXZR+kHt4kqVn02fb/846r5D9q4Px6YfBJ+VHvxcaexf3DPJiUv7F8llp/kbx2fc6DHE8rR8T/o2arXjneV19/ZL7/eY9CuxF9vZbxnv/xfpJ58Xn2mxXmd0Ozc94PuWMR1OTA9nvrJU68q2YKPfgTTleGmdfZ4LR72PTN8nOCmr718s75ssnu/0RR1rrVMnJnnkmI+/ma3tF+zTN1LQspo3pjecqaq7pW801jR23D7cWntK+lnQy9yXvMNen57ap6pumf2or6puXnvvvUz6ZaOLL+x8wNL/xdnla2Tvl489ZJPvdaP0BPQZ6TtIt93HIPvjn5P8fzW+56Gqrlf9ixNX1Vr7fJKzq+reo/8r1iZ+pWeDPp9+m8TCNZJ8vPWzpz+VvkFcz/K0f+gWa/i39AOjjJ2eT7bWPreBWs/ImF/V78O+8ej+xiQ/XFVXGtP6XiuG+a7xePm7Dv45yc+PKxpSVd86/t8o/YzKWdm7fHwie8/876mqW47+l3c2NvqZFk5Ocr/F8lD9ewhuVP2e0su11l6c5Ndz2eVz0Th/cnzWfX5/w9h5u2eSB1XVw0at965+f/5V0s+M/dsqg661/F4jyWdaa18cG8bbrzLsRlwjyXmtta+NA40bLb12w+pfcJf0duYN2cJnzyrzuaquskY78OYkd6i93wV1lcVysY4zsnf5+pFc+oqLlb6aPq0fXKv8ikBV3bS19u7W2pPSz3x/28p+NuBf0ncaf36p26INWXVabOE9FrbcDq/i2em3J717nfd46D5qWW1ZWtmGTFdVR6Tv9D517HyekX5m8nJVdYP0M/wLX1tM//R59WNVde0xnmttZ50bdNxoR6+dfon3Wzc43FuS/ED178E6JL1t/NdJNW24bR1h5w1aa69NX9+ukX72cCO2so/WWmtPTr/y5p6L4ddw6/SrWJZ9Kf3Wor9OPyD6dPpnfVX6zvgN0295uuGK4f45/QD/mPQDye9clJXerm10e778mW+RftZ7TaPdvCj9ts1n5tJt1CXjSr+i4ZvSw+zXZBVj+n0sfX1Z7OO+Psm1ltaRw7O3Tb16Lnum+v3p83exbTh+xes/NNary6UHBG/M1rZfr0qf3ovaj0pvs57aWntJ+sHgZ9Onx2eT3HZsox6a/p0NK/f71mvXnpl+tfhb0w8cV7NtxxPVLym4dfZO6wcmeXhrbU9rbU/6ftcPrbFveo30K0Qy6lte/m6XHiw+YPx9fkXdFyX5sfRQZ7FPtNG6rz2OIRZ1HzXG86n0ebQn/ba0GnVfMT1g+9n0kzdXyN5l6IJ97F9cP/2k3EaPIZa/6+b56e3kzyy9/iPp06LSr2i/OONugeFK/6+9+4+1uq7jOP58gRgR9sMoirFiawuzNq2LLrQ1/rF06WpJ6maEucXol79WlpXrltmP5axl4UaIc9lAGX/gjzR1ggUrBS95FYjW1DUKkGxRoBfl8u6P9+d0Dpdzzzn33HOBA6/Hxjj7nu/3ez7f7/3++Hze3/fn86Xafp5P7tPtZKCqh+HP8e1kds45ZfklNM9Yry1rO/5I9SH5Jc1mblLnOYnchkrQududBGwv17ZLx+pHjnSUqdNqU1wBHoyIRq9k+w6wTNI8MmCwg2rKaD0XAfOUaZ47yMh+o3TZw+1W4HZJW4AtZHS4XZOBW5Sv4tpPVkYWkA3mNynTWfdRbdj2AiuU6ZKPUm1wt2IO8NWyX/eQ42KMiYh4SNJ7gD+UdLg9ZDrpYIPF5pGD6H2XfEr0qQbztqMfGJT0FBlhXQSsLFH5B2mcUQKl/7XyTQntvi6zl+y20U/2yx2ukbYa+Ho5z34ArCQbqZvI9Ma/AETEeuVAnv1kFP9pqk//bgLuVg54V1veJeTTj75SsdhVps8p5TuZrDR8huq4LXeQx+cGspJ0H9VGXKvbRCnz5rIPHyqNg1fJVNaXyfOqcmO9bshy/1a+cvEZ8rrQUkMoMg33XLIieyX5t3+isi8iYqPKwMI1ywx3/D4ILCzn/lby5toy5RPmfWR6/73K9M8NZB/6iq3AFyUtJVPAby0V45Fue72/8yeocx2IiF3KLpTLVH3N6rcox9kwfgmsKudT0/MnIvZKOh94WDlQXG2D8SpVn2xvIvv8z66zmkbrjxKo/Ymyi9WuUqavkWnZMzh0X7Srl/avw0PLvY2DK5cVrV5v6h5LEfGipHXKQSEfaLKOkajc/yeQ14RfUX07zjqy+8hm8t7YV7PcYqBfUl9EXCrpRuAxSYNkxf+yDpWvXf3kdXcKcENkt4sZzRaKiO3K9PfVZIPh/ohY1aEy9dL6tXU8cKeyC8PryPNrDfA28u/RKJW9nTpa5TjYQTZoHqB+43gc1S6YQ20GPkseQ1vKvKeTT5f/VZbbSV4TKm4AfgpcTgZ4niXrS/8FrpN0Hbntzd4Cs4g8vzaT58wmqvdOAavLsfla5WDOW8ggyqNlvh+TWTVQ9h/5UGKAzO7aG9ndpN5vX0Q2dE8m2wffJ++511C9Rk0kr1szgd01T9EF7I+IVyR9GfiFcrD2Fzm4fvUEWW84E7g7IjaUa8RI719XlN/oJwPXCyNiYQkGPEM+kT9A/v13kkGBXeTf4/UcGuwdel3TkPbEa4Dbya4c9Yxle6IH2FjuJZPIYN7CypflHraWzMQ5AbhaUqWb1OPk+TmNPA5q74fryS4+F5L3/7+VslTOlwNkV7K7yMDizeQx2Uq5TyTHzHknOV7Mc2SG4384uA2xppR7DVm3+zD50Ovcsi19ZEbMBaW8H+NQZwPTJG2kSRtCGYQfKA9Riewedw2wRDlIcpDHyUdKWc6Q9DI5htJLZTXfAH4t6SXyWP0HuY/fSl476tU5Xi3zXEn12LyYzPT7dJ35Dylr8a4hx+XSEvQazlXk9febZH1od4N5oX6dp1InuZ48nird6bpdZXt2lf/H5AGQqtfI40+puA9G9uGcTTYcOvrarGONMt1vVnTmVYV2DJM0ObIv/iQymLAgIvqaLWeHn6TTyHT3M4f5fgY5WFrd14CaWedpBK8sPxaNZR2tNKj/GhHLm87c+jqnk9fR80axjvHk2CIDyreJPQLMbKfLVp39t5zchz9st3w16z5o/0m6knz6f22DZS4j649fGu3vH06SppGBgFNKdkO9ebrqWK1Z92Et95FuQ5QA1PRWzoFuKmuDdUwiu9aFpEvIgXE/3mw565xjLaNlpN5BPlkfR6a0fq7J/GbWusXK1OeJ5NgnDrIchSQtJJ8OXnWky2JmVmPM6mgR8b1OratmndvIrJfRmERmrUwgs0S+0E6QpRi6/+ZGRKtdzxqq3X+SbiMHEW7UTasrKTOLbyQHnh2u2xB02bFao1vL3ZaIuPNIl6FVHSprD/lyDZFZOZd3YJ02Asd1RouZmZmZmZmZWScd74PhmpmZmZmZmZl1jAMtZmZmZmZmZmYd4kCLmZmZmZmZmVmHONBiZmZmR63y2m0zMzOzruFAi5mZmZmZmZlZhzjQYmZmZl1F0gWSHpe0UdIjkqaW6b2SlkpaI+lZSVfULHO9pK2S1kpaJukrZfoaSbPK5ymSni+fZ0j6vaS+8u+sMn2cpEWS/izpYUm/kTS3fNcj6TFJT0r6raS3H+ZdY2ZmZkcBB1rMzMys26wFPhgR7weWA9fWfHcK8FHgTODbkiZIOgO4EDgNOA+Y1cJvvACcExEfAC4GflamfxKYAZwKzANmA0iaANwCzI2IHmApcOMottHMzMy61AlHugBmZmZmIzQduKtkjJwIPFfz3f0RsQ/YJ+kFYCpwNrAqIgaAAUn3tvAbE4CfSzodGATeXaZ/CFgREQeAHZJWl+kzgfcBD0sCGA9sH81GmpmZWXdyoMXMzMy6zS3AzRFxj6Q5QG/Nd/tqPg/SvK6zn2qG78Sa6VcDO8ksmHHAQJP1CNgUEbObzGdmZmbHOHcdMjMzs27zBuDv5fP8FuZfB1wgaaKkycD5Nd89D/SUz3OH/Mb2krkyj8xQqazrwjJWy1RgTpm+FXiLpP93JZL03hFtlZmZmR0THGgxMzOzo9kkSdtq/l1DZrCskPQk8M9mK4iI9cA9QD/wAPA0sLt8fRPweUkbgSk1iy0C5kt6ihz3ZW+ZvhLYBmwG7gT6gN0R8QoZqPlRWeZPwFntb7aZmZl1K0XEkS6DmZmZ2ZiSNDki9kiaBPwOWBARfaNc15uBJ4CzI2JHJ8trZmZm3ctjtJiZmdnxYLGkU8lxWO5oN8hS3CfpjeRAvDc4yGJmZma1nNFiZmZmZmZmZtYhHqPFzMzMzMzMzKxDHGgxMzMzMzMzM+sQB1rMzMzMzMzMzDrEgRYzMzMzMzMzsw5xoMXMzMzMzMzMrEMcaDEzMzMzMzMz65D/ATLiCMOYOuwlAAAAAElFTkSuQmCC\n"
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# 2019 Ocak ile 2020 Haziran tarihleri arasında \"Documentary\" türünde çekilmiş filmlerin IMDB değerlerini gösteriyoruz."
      ],
      "metadata": {
        "id": "7j50FPdTmCxD"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "NetflixOriginals[\"Date\"] = pd.to_datetime(NetflixOriginals.Premiere)\n",
        "Documentary = NetflixOriginals.loc[(NetflixOriginals[\"Genre\"] == \"Documentary\") & (NetflixOriginals[\"Date\"] > \"2019-01-31\") & (NetflixOriginals[\"Date\"] < \"2020-06-01\")]\n",
        "Documentary"
      ],
      "metadata": {
        "id": "aeds3X-bmumo",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 1000
        },
        "outputId": "f9546030-29ff-44c8-8d36-06a182b03727"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "                                                 Title        Genre  \\\n",
              "0                                      Enter the Anime  Documentary   \n",
              "15                                      After the Raid  Documentary   \n",
              "20                   Hello Privilege. It's Me, Chelsea  Documentary   \n",
              "30                                         After Maria  Documentary   \n",
              "111                               Ghosts of Sugar Land  Documentary   \n",
              "263                             A Tale of Two Kitchens  Documentary   \n",
              "286                       The Legend of Cocaine Island  Documentary   \n",
              "290                   Travis Scott: Look Mom I Can Fly  Documentary   \n",
              "295                                            Birders  Documentary   \n",
              "303           Murder to Mercy: The Cyntoia Brown Story  Documentary   \n",
              "320                                     A 3 Minute Hug  Documentary   \n",
              "324          Antoine Griezmann: The Making of a Legend  Documentary   \n",
              "334                                  Life Overtakes Me  Documentary   \n",
              "353                                 It Takes a Lunatic  Documentary   \n",
              "367                       Bikram: Yogi, Guru, Predator  Documentary   \n",
              "378                                   Little Miss Sumo  Documentary   \n",
              "384                           Parchis: The Documentary  Documentary   \n",
              "392      A Life of Speed: The Juan Manuel Fangio Story  Documentary   \n",
              "394                                   All in My Family  Documentary   \n",
              "396                                           Becoming  Documentary   \n",
              "401       Have a Good Trip: Adventures in Psychedelics  Documentary   \n",
              "436                         Lorena, Light-Footed Woman  Documentary   \n",
              "437              Los Tigres del Norte at Folsom Prison  Documentary   \n",
              "442                ReMastered: Devil at the Crossroads  Documentary   \n",
              "443                       ReMastered: The Lion's Share  Documentary   \n",
              "444            ReMastered: The Miami Showband Massacre  Documentary   \n",
              "455                                    Circus of Books  Documentary   \n",
              "458                            El Pepe: A Supreme Life  Documentary   \n",
              "460                                             Evelyn  Documentary   \n",
              "462                                   Grass Is Greener  Documentary   \n",
              "466                               Knock Down the House  Documentary   \n",
              "476                                     The Great Hack  Documentary   \n",
              "484                                       LA Originals  Documentary   \n",
              "494                              The Edge of Democracy  Documentary   \n",
              "511          ReMastered: The Two Killings of Sam Cooke  Documentary   \n",
              "520                                   American Factory  Documentary   \n",
              "521                                   Fire in Paradise  Documentary   \n",
              "523                                     Miss Americana  Documentary   \n",
              "524                           Period. End of Sentence.  Documentary   \n",
              "527                                The Black Godfather  Documentary   \n",
              "536                     Homecoming: A Film by Beyonce   Documentary   \n",
              "545  Rolling Thunder Revue: A bob Dylan Story by Ma...  Documentary   \n",
              "546                                   Tell Me Who I Am  Documentary   \n",
              "554                   Brene Brown: The Call to Courage  Documentary   \n",
              "555                 Crip Camp: A Disability Revolution  Documentary   \n",
              "563                                      A Secret Love  Documentary   \n",
              "577                             Dancing with the Birds  Documentary   \n",
              "\n",
              "               Premiere  Runtime  IMDB Score          Language       Date  \n",
              "0        August 5, 2019       58         2.5  English/Japanese 2019-08-05  \n",
              "15    December 19, 2019       25         4.3           Spanish 2019-12-19  \n",
              "20   September 13, 2019       64         4.4           English 2019-09-13  \n",
              "30         May 24, 2019       37         4.6   English/Spanish 2019-05-24  \n",
              "111    October 16. 2019       21         5.5           English 2019-10-16  \n",
              "263        May 22, 2019       30         6.3   English/Spanish 2019-05-22  \n",
              "286      March 29, 2019       87         6.3           English 2019-03-29  \n",
              "290     August 28, 2019       85         6.3           English 2019-08-28  \n",
              "295  September 25, 2019       37         6.4   English/Spanish 2019-09-25  \n",
              "303      April 29, 2020       97         6.4           English 2020-04-29  \n",
              "320    October 28, 2019       28         6.5   English/Spanish 2019-10-28  \n",
              "324      March 21, 2019       60         6.5            French 2019-03-21  \n",
              "334       June 14, 2019       40         6.5   English/Swedish 2019-06-14  \n",
              "353    October 25, 2019      126         6.6           English 2019-10-25  \n",
              "367   November 20, 2019       86         6.7           English 2019-11-20  \n",
              "378    October 28, 2019       19         6.7          Japanese 2019-10-28  \n",
              "384       July 10, 2019      106         6.7           Spanish 2019-07-10  \n",
              "392      March 20, 2020       92         6.8           Spanish 2020-03-20  \n",
              "394         May 3, 2019       39         6.8  English/Mandarin 2019-05-03  \n",
              "396         May 6, 2020       89         6.8           English 2020-05-06  \n",
              "401        May 11, 2020       85         6.8           English 2020-05-11  \n",
              "436   November 20, 2019       28         7.0           Spanish 2019-11-20  \n",
              "437  September 15, 2019       64         7.0           Spanish 2019-09-15  \n",
              "442      April 26, 2019       48         7.0           English 2019-04-26  \n",
              "443        May 17, 2019       84         7.0           English 2019-05-17  \n",
              "444      March 22, 2019       70         7.0           English 2019-03-22  \n",
              "455      April 22, 2020       92         7.1           English 2020-04-22  \n",
              "458   December 27, 2019       73         7.1           Spanish 2019-12-27  \n",
              "460  September 10, 2019       96         7.1           English 2019-09-10  \n",
              "462      April 20, 2019       97         7.1           English 2019-04-20  \n",
              "466         May 1, 2019       87         7.1           English 2019-05-01  \n",
              "476       July 24, 2019      114         7.1           English 2019-07-24  \n",
              "484      April 10, 2020       92         7.2           English 2020-04-10  \n",
              "494       June 19, 2019      121         7.2        Portuguese 2019-06-19  \n",
              "511    February 8, 2019       64         7.3           English 2019-02-08  \n",
              "520     August 21, 2019      110         7.4           English 2019-08-21  \n",
              "521    November 1, 2019       39         7.4           English 2019-11-01  \n",
              "523    January 31, 2020       85         7.4           English 2020-01-31  \n",
              "524   February 12, 2019       26         7.4     English/Hindi 2019-02-12  \n",
              "527        June 7, 2019      118         7.4           English 2019-06-07  \n",
              "536      April 17, 2019      137         7.5           English 2019-04-17  \n",
              "545       June 12, 2019      144         7.6           English 2019-06-12  \n",
              "546    October 18, 2019       85         7.6           English 2019-10-18  \n",
              "554      April 19, 2019       76         7.7           English 2019-04-19  \n",
              "555      March 25, 2020      108         7.7           English 2020-03-25  \n",
              "563      April 29, 2020       82         7.9           English 2020-04-29  \n",
              "577    October 23, 2019       51         8.3           English 2019-10-23  "
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-816fdfab-f7c2-4518-a792-7552254cb654\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Title</th>\n",
              "      <th>Genre</th>\n",
              "      <th>Premiere</th>\n",
              "      <th>Runtime</th>\n",
              "      <th>IMDB Score</th>\n",
              "      <th>Language</th>\n",
              "      <th>Date</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>Enter the Anime</td>\n",
              "      <td>Documentary</td>\n",
              "      <td>August 5, 2019</td>\n",
              "      <td>58</td>\n",
              "      <td>2.5</td>\n",
              "      <td>English/Japanese</td>\n",
              "      <td>2019-08-05</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>15</th>\n",
              "      <td>After the Raid</td>\n",
              "      <td>Documentary</td>\n",
              "      <td>December 19, 2019</td>\n",
              "      <td>25</td>\n",
              "      <td>4.3</td>\n",
              "      <td>Spanish</td>\n",
              "      <td>2019-12-19</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>20</th>\n",
              "      <td>Hello Privilege. It's Me, Chelsea</td>\n",
              "      <td>Documentary</td>\n",
              "      <td>September 13, 2019</td>\n",
              "      <td>64</td>\n",
              "      <td>4.4</td>\n",
              "      <td>English</td>\n",
              "      <td>2019-09-13</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>30</th>\n",
              "      <td>After Maria</td>\n",
              "      <td>Documentary</td>\n",
              "      <td>May 24, 2019</td>\n",
              "      <td>37</td>\n",
              "      <td>4.6</td>\n",
              "      <td>English/Spanish</td>\n",
              "      <td>2019-05-24</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>111</th>\n",
              "      <td>Ghosts of Sugar Land</td>\n",
              "      <td>Documentary</td>\n",
              "      <td>October 16. 2019</td>\n",
              "      <td>21</td>\n",
              "      <td>5.5</td>\n",
              "      <td>English</td>\n",
              "      <td>2019-10-16</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>263</th>\n",
              "      <td>A Tale of Two Kitchens</td>\n",
              "      <td>Documentary</td>\n",
              "      <td>May 22, 2019</td>\n",
              "      <td>30</td>\n",
              "      <td>6.3</td>\n",
              "      <td>English/Spanish</td>\n",
              "      <td>2019-05-22</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>286</th>\n",
              "      <td>The Legend of Cocaine Island</td>\n",
              "      <td>Documentary</td>\n",
              "      <td>March 29, 2019</td>\n",
              "      <td>87</td>\n",
              "      <td>6.3</td>\n",
              "      <td>English</td>\n",
              "      <td>2019-03-29</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>290</th>\n",
              "      <td>Travis Scott: Look Mom I Can Fly</td>\n",
              "      <td>Documentary</td>\n",
              "      <td>August 28, 2019</td>\n",
              "      <td>85</td>\n",
              "      <td>6.3</td>\n",
              "      <td>English</td>\n",
              "      <td>2019-08-28</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>295</th>\n",
              "      <td>Birders</td>\n",
              "      <td>Documentary</td>\n",
              "      <td>September 25, 2019</td>\n",
              "      <td>37</td>\n",
              "      <td>6.4</td>\n",
              "      <td>English/Spanish</td>\n",
              "      <td>2019-09-25</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>303</th>\n",
              "      <td>Murder to Mercy: The Cyntoia Brown Story</td>\n",
              "      <td>Documentary</td>\n",
              "      <td>April 29, 2020</td>\n",
              "      <td>97</td>\n",
              "      <td>6.4</td>\n",
              "      <td>English</td>\n",
              "      <td>2020-04-29</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>320</th>\n",
              "      <td>A 3 Minute Hug</td>\n",
              "      <td>Documentary</td>\n",
              "      <td>October 28, 2019</td>\n",
              "      <td>28</td>\n",
              "      <td>6.5</td>\n",
              "      <td>English/Spanish</td>\n",
              "      <td>2019-10-28</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>324</th>\n",
              "      <td>Antoine Griezmann: The Making of a Legend</td>\n",
              "      <td>Documentary</td>\n",
              "      <td>March 21, 2019</td>\n",
              "      <td>60</td>\n",
              "      <td>6.5</td>\n",
              "      <td>French</td>\n",
              "      <td>2019-03-21</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>334</th>\n",
              "      <td>Life Overtakes Me</td>\n",
              "      <td>Documentary</td>\n",
              "      <td>June 14, 2019</td>\n",
              "      <td>40</td>\n",
              "      <td>6.5</td>\n",
              "      <td>English/Swedish</td>\n",
              "      <td>2019-06-14</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>353</th>\n",
              "      <td>It Takes a Lunatic</td>\n",
              "      <td>Documentary</td>\n",
              "      <td>October 25, 2019</td>\n",
              "      <td>126</td>\n",
              "      <td>6.6</td>\n",
              "      <td>English</td>\n",
              "      <td>2019-10-25</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>367</th>\n",
              "      <td>Bikram: Yogi, Guru, Predator</td>\n",
              "      <td>Documentary</td>\n",
              "      <td>November 20, 2019</td>\n",
              "      <td>86</td>\n",
              "      <td>6.7</td>\n",
              "      <td>English</td>\n",
              "      <td>2019-11-20</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>378</th>\n",
              "      <td>Little Miss Sumo</td>\n",
              "      <td>Documentary</td>\n",
              "      <td>October 28, 2019</td>\n",
              "      <td>19</td>\n",
              "      <td>6.7</td>\n",
              "      <td>Japanese</td>\n",
              "      <td>2019-10-28</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>384</th>\n",
              "      <td>Parchis: The Documentary</td>\n",
              "      <td>Documentary</td>\n",
              "      <td>July 10, 2019</td>\n",
              "      <td>106</td>\n",
              "      <td>6.7</td>\n",
              "      <td>Spanish</td>\n",
              "      <td>2019-07-10</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>392</th>\n",
              "      <td>A Life of Speed: The Juan Manuel Fangio Story</td>\n",
              "      <td>Documentary</td>\n",
              "      <td>March 20, 2020</td>\n",
              "      <td>92</td>\n",
              "      <td>6.8</td>\n",
              "      <td>Spanish</td>\n",
              "      <td>2020-03-20</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>394</th>\n",
              "      <td>All in My Family</td>\n",
              "      <td>Documentary</td>\n",
              "      <td>May 3, 2019</td>\n",
              "      <td>39</td>\n",
              "      <td>6.8</td>\n",
              "      <td>English/Mandarin</td>\n",
              "      <td>2019-05-03</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>396</th>\n",
              "      <td>Becoming</td>\n",
              "      <td>Documentary</td>\n",
              "      <td>May 6, 2020</td>\n",
              "      <td>89</td>\n",
              "      <td>6.8</td>\n",
              "      <td>English</td>\n",
              "      <td>2020-05-06</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>401</th>\n",
              "      <td>Have a Good Trip: Adventures in Psychedelics</td>\n",
              "      <td>Documentary</td>\n",
              "      <td>May 11, 2020</td>\n",
              "      <td>85</td>\n",
              "      <td>6.8</td>\n",
              "      <td>English</td>\n",
              "      <td>2020-05-11</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>436</th>\n",
              "      <td>Lorena, Light-Footed Woman</td>\n",
              "      <td>Documentary</td>\n",
              "      <td>November 20, 2019</td>\n",
              "      <td>28</td>\n",
              "      <td>7.0</td>\n",
              "      <td>Spanish</td>\n",
              "      <td>2019-11-20</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>437</th>\n",
              "      <td>Los Tigres del Norte at Folsom Prison</td>\n",
              "      <td>Documentary</td>\n",
              "      <td>September 15, 2019</td>\n",
              "      <td>64</td>\n",
              "      <td>7.0</td>\n",
              "      <td>Spanish</td>\n",
              "      <td>2019-09-15</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>442</th>\n",
              "      <td>ReMastered: Devil at the Crossroads</td>\n",
              "      <td>Documentary</td>\n",
              "      <td>April 26, 2019</td>\n",
              "      <td>48</td>\n",
              "      <td>7.0</td>\n",
              "      <td>English</td>\n",
              "      <td>2019-04-26</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>443</th>\n",
              "      <td>ReMastered: The Lion's Share</td>\n",
              "      <td>Documentary</td>\n",
              "      <td>May 17, 2019</td>\n",
              "      <td>84</td>\n",
              "      <td>7.0</td>\n",
              "      <td>English</td>\n",
              "      <td>2019-05-17</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>444</th>\n",
              "      <td>ReMastered: The Miami Showband Massacre</td>\n",
              "      <td>Documentary</td>\n",
              "      <td>March 22, 2019</td>\n",
              "      <td>70</td>\n",
              "      <td>7.0</td>\n",
              "      <td>English</td>\n",
              "      <td>2019-03-22</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>455</th>\n",
              "      <td>Circus of Books</td>\n",
              "      <td>Documentary</td>\n",
              "      <td>April 22, 2020</td>\n",
              "      <td>92</td>\n",
              "      <td>7.1</td>\n",
              "      <td>English</td>\n",
              "      <td>2020-04-22</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>458</th>\n",
              "      <td>El Pepe: A Supreme Life</td>\n",
              "      <td>Documentary</td>\n",
              "      <td>December 27, 2019</td>\n",
              "      <td>73</td>\n",
              "      <td>7.1</td>\n",
              "      <td>Spanish</td>\n",
              "      <td>2019-12-27</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>460</th>\n",
              "      <td>Evelyn</td>\n",
              "      <td>Documentary</td>\n",
              "      <td>September 10, 2019</td>\n",
              "      <td>96</td>\n",
              "      <td>7.1</td>\n",
              "      <td>English</td>\n",
              "      <td>2019-09-10</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>462</th>\n",
              "      <td>Grass Is Greener</td>\n",
              "      <td>Documentary</td>\n",
              "      <td>April 20, 2019</td>\n",
              "      <td>97</td>\n",
              "      <td>7.1</td>\n",
              "      <td>English</td>\n",
              "      <td>2019-04-20</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>466</th>\n",
              "      <td>Knock Down the House</td>\n",
              "      <td>Documentary</td>\n",
              "      <td>May 1, 2019</td>\n",
              "      <td>87</td>\n",
              "      <td>7.1</td>\n",
              "      <td>English</td>\n",
              "      <td>2019-05-01</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>476</th>\n",
              "      <td>The Great Hack</td>\n",
              "      <td>Documentary</td>\n",
              "      <td>July 24, 2019</td>\n",
              "      <td>114</td>\n",
              "      <td>7.1</td>\n",
              "      <td>English</td>\n",
              "      <td>2019-07-24</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>484</th>\n",
              "      <td>LA Originals</td>\n",
              "      <td>Documentary</td>\n",
              "      <td>April 10, 2020</td>\n",
              "      <td>92</td>\n",
              "      <td>7.2</td>\n",
              "      <td>English</td>\n",
              "      <td>2020-04-10</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>494</th>\n",
              "      <td>The Edge of Democracy</td>\n",
              "      <td>Documentary</td>\n",
              "      <td>June 19, 2019</td>\n",
              "      <td>121</td>\n",
              "      <td>7.2</td>\n",
              "      <td>Portuguese</td>\n",
              "      <td>2019-06-19</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>511</th>\n",
              "      <td>ReMastered: The Two Killings of Sam Cooke</td>\n",
              "      <td>Documentary</td>\n",
              "      <td>February 8, 2019</td>\n",
              "      <td>64</td>\n",
              "      <td>7.3</td>\n",
              "      <td>English</td>\n",
              "      <td>2019-02-08</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>520</th>\n",
              "      <td>American Factory</td>\n",
              "      <td>Documentary</td>\n",
              "      <td>August 21, 2019</td>\n",
              "      <td>110</td>\n",
              "      <td>7.4</td>\n",
              "      <td>English</td>\n",
              "      <td>2019-08-21</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>521</th>\n",
              "      <td>Fire in Paradise</td>\n",
              "      <td>Documentary</td>\n",
              "      <td>November 1, 2019</td>\n",
              "      <td>39</td>\n",
              "      <td>7.4</td>\n",
              "      <td>English</td>\n",
              "      <td>2019-11-01</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>523</th>\n",
              "      <td>Miss Americana</td>\n",
              "      <td>Documentary</td>\n",
              "      <td>January 31, 2020</td>\n",
              "      <td>85</td>\n",
              "      <td>7.4</td>\n",
              "      <td>English</td>\n",
              "      <td>2020-01-31</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>524</th>\n",
              "      <td>Period. End of Sentence.</td>\n",
              "      <td>Documentary</td>\n",
              "      <td>February 12, 2019</td>\n",
              "      <td>26</td>\n",
              "      <td>7.4</td>\n",
              "      <td>English/Hindi</td>\n",
              "      <td>2019-02-12</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>527</th>\n",
              "      <td>The Black Godfather</td>\n",
              "      <td>Documentary</td>\n",
              "      <td>June 7, 2019</td>\n",
              "      <td>118</td>\n",
              "      <td>7.4</td>\n",
              "      <td>English</td>\n",
              "      <td>2019-06-07</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>536</th>\n",
              "      <td>Homecoming: A Film by Beyonce</td>\n",
              "      <td>Documentary</td>\n",
              "      <td>April 17, 2019</td>\n",
              "      <td>137</td>\n",
              "      <td>7.5</td>\n",
              "      <td>English</td>\n",
              "      <td>2019-04-17</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>545</th>\n",
              "      <td>Rolling Thunder Revue: A bob Dylan Story by Ma...</td>\n",
              "      <td>Documentary</td>\n",
              "      <td>June 12, 2019</td>\n",
              "      <td>144</td>\n",
              "      <td>7.6</td>\n",
              "      <td>English</td>\n",
              "      <td>2019-06-12</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>546</th>\n",
              "      <td>Tell Me Who I Am</td>\n",
              "      <td>Documentary</td>\n",
              "      <td>October 18, 2019</td>\n",
              "      <td>85</td>\n",
              "      <td>7.6</td>\n",
              "      <td>English</td>\n",
              "      <td>2019-10-18</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>554</th>\n",
              "      <td>Brene Brown: The Call to Courage</td>\n",
              "      <td>Documentary</td>\n",
              "      <td>April 19, 2019</td>\n",
              "      <td>76</td>\n",
              "      <td>7.7</td>\n",
              "      <td>English</td>\n",
              "      <td>2019-04-19</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>555</th>\n",
              "      <td>Crip Camp: A Disability Revolution</td>\n",
              "      <td>Documentary</td>\n",
              "      <td>March 25, 2020</td>\n",
              "      <td>108</td>\n",
              "      <td>7.7</td>\n",
              "      <td>English</td>\n",
              "      <td>2020-03-25</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>563</th>\n",
              "      <td>A Secret Love</td>\n",
              "      <td>Documentary</td>\n",
              "      <td>April 29, 2020</td>\n",
              "      <td>82</td>\n",
              "      <td>7.9</td>\n",
              "      <td>English</td>\n",
              "      <td>2020-04-29</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>577</th>\n",
              "      <td>Dancing with the Birds</td>\n",
              "      <td>Documentary</td>\n",
              "      <td>October 23, 2019</td>\n",
              "      <td>51</td>\n",
              "      <td>8.3</td>\n",
              "      <td>English</td>\n",
              "      <td>2019-10-23</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-816fdfab-f7c2-4518-a792-7552254cb654')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-816fdfab-f7c2-4518-a792-7552254cb654 button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-816fdfab-f7c2-4518-a792-7552254cb654');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 5
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# İngilizce çekilen filmeler içerisinde hangi türün en yüksek IMDB puanına sahip olduğunu buluyoruz."
      ],
      "metadata": {
        "id": "GORP9txcmwkd"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "NetflixOriginals[NetflixOriginals[\"Language\"] == \"English\"].sort_values(by = \"IMDB Score\", ascending = False).head(1)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 81
        },
        "id": "RQG9ouO6m4sl",
        "outputId": "201ac2a3-9e70-4cc3-d41f-2539419da69c"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "                                        Title        Genre         Premiere  \\\n",
              "583  David Attenborough: A Life on Our Planet  Documentary  October 4, 2020   \n",
              "\n",
              "     Runtime  IMDB Score Language       Date  \n",
              "583       83         9.0  English 2020-10-04  "
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-b4641755-69ab-4291-a214-05ca2e3709a0\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Title</th>\n",
              "      <th>Genre</th>\n",
              "      <th>Premiere</th>\n",
              "      <th>Runtime</th>\n",
              "      <th>IMDB Score</th>\n",
              "      <th>Language</th>\n",
              "      <th>Date</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>583</th>\n",
              "      <td>David Attenborough: A Life on Our Planet</td>\n",
              "      <td>Documentary</td>\n",
              "      <td>October 4, 2020</td>\n",
              "      <td>83</td>\n",
              "      <td>9.0</td>\n",
              "      <td>English</td>\n",
              "      <td>2020-10-04</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-b4641755-69ab-4291-a214-05ca2e3709a0')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-b4641755-69ab-4291-a214-05ca2e3709a0 button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-b4641755-69ab-4291-a214-05ca2e3709a0');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 6
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# \"Hindi\" dilinde çekilmiş olan filmlerin ortalama \"Runtime\" suresini buluyoruz."
      ],
      "metadata": {
        "id": "ciIZRbtVm7sa"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "print(NetflixOriginals[(NetflixOriginals[\"Language\"] == \"Hindi\")].agg({\"Runtime\" : \"mean\"}))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "c4tc9u6QnIrR",
        "outputId": "1fc4fa4f-c487-4f80-dba3-913b486d41f8"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Runtime    115.787879\n",
            "dtype: float64\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# \"Genre\"nin hangi kategorilerden oluştuğunu görselleştiriyoruz."
      ],
      "metadata": {
        "id": "JDlryczSnLwE"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "NetflixGenre= pd.DataFrame(NetflixOriginals['Genre'].value_counts())\n",
        "\n",
        "plt.figure(figsize = (18,9))\n",
        "sns.barplot(x = NetflixGenre.index, y = NetflixGenre['Genre'] , data = NetflixGenre)\n",
        "plt.xticks(rotation = 85)\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 731
        },
        "id": "b9sbdEJAojBq",
        "outputId": "54e5ac83-9a19-469c-fcc9-1c2a3876423d"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 1296x648 with 1 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Veri setindeki filmlerde en çok kullanılan 3 dili sıralıyoruz."
      ],
      "metadata": {
        "id": "wSECFfbeoouv"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "NetflixOriginals['Language'].value_counts()[0:3]"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "HSOB-e7OouXn",
        "outputId": "d22ac432-343b-40ae-9bbf-c5a3af1c45cc"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "English    401\n",
              "Hindi       33\n",
              "Spanish     31\n",
              "Name: Language, dtype: int64"
            ]
          },
          "metadata": {},
          "execution_count": 9
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# IMDB puanı en yüksek 10 filmi gösteriyoruz."
      ],
      "metadata": {
        "id": "sUdiGlTzoxml"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "NetflixOriginals.sort_values(\"IMDB Score\", ascending= False).head(10)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 363
        },
        "id": "c6QkuYKCo21z",
        "outputId": "366e3040-873c-422d-dc91-49cae59fe8dd"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "                                           Title  \\\n",
              "583     David Attenborough: A Life on Our Planet   \n",
              "582    Emicida: AmarElo - It's All For Yesterday   \n",
              "581                      Springsteen on Broadway   \n",
              "580  Winter on Fire: Ukraine's Fight for Freedom   \n",
              "579        Taylor Swift: Reputation Stadium Tour   \n",
              "578   Ben Platt: Live from Radio City Music Hall   \n",
              "577                       Dancing with the Birds   \n",
              "576                      Cuba and the Cameraman    \n",
              "573                                        Klaus   \n",
              "571                                         13th   \n",
              "\n",
              "                                    Genre           Premiere  Runtime  \\\n",
              "583                           Documentary    October 4, 2020       83   \n",
              "582                           Documentary   December 8, 2020       89   \n",
              "581                          One-man show  December 16, 2018      153   \n",
              "580                           Documentary    October 9, 2015       91   \n",
              "579                          Concert Film  December 31, 2018      125   \n",
              "578                          Concert Film       May 20, 2020       85   \n",
              "577                           Documentary   October 23, 2019       51   \n",
              "576                           Documentary  November 24, 2017      114   \n",
              "573  Animation/Christmas/Comedy/Adventure  November 15, 2019       97   \n",
              "571                           Documentary    October 7, 2016      100   \n",
              "\n",
              "     IMDB Score                  Language       Date  \n",
              "583         9.0                   English 2020-10-04  \n",
              "582         8.6                Portuguese 2020-12-08  \n",
              "581         8.5                   English 2018-12-16  \n",
              "580         8.4  English/Ukranian/Russian 2015-10-09  \n",
              "579         8.4                   English 2018-12-31  \n",
              "578         8.4                   English 2020-05-20  \n",
              "577         8.3                   English 2019-10-23  \n",
              "576         8.3                   English 2017-11-24  \n",
              "573         8.2                   English 2019-11-15  \n",
              "571         8.2                   English 2016-10-07  "
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-106e256b-0269-4648-8afd-e00c702c9394\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Title</th>\n",
              "      <th>Genre</th>\n",
              "      <th>Premiere</th>\n",
              "      <th>Runtime</th>\n",
              "      <th>IMDB Score</th>\n",
              "      <th>Language</th>\n",
              "      <th>Date</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>583</th>\n",
              "      <td>David Attenborough: A Life on Our Planet</td>\n",
              "      <td>Documentary</td>\n",
              "      <td>October 4, 2020</td>\n",
              "      <td>83</td>\n",
              "      <td>9.0</td>\n",
              "      <td>English</td>\n",
              "      <td>2020-10-04</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>582</th>\n",
              "      <td>Emicida: AmarElo - It's All For Yesterday</td>\n",
              "      <td>Documentary</td>\n",
              "      <td>December 8, 2020</td>\n",
              "      <td>89</td>\n",
              "      <td>8.6</td>\n",
              "      <td>Portuguese</td>\n",
              "      <td>2020-12-08</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>581</th>\n",
              "      <td>Springsteen on Broadway</td>\n",
              "      <td>One-man show</td>\n",
              "      <td>December 16, 2018</td>\n",
              "      <td>153</td>\n",
              "      <td>8.5</td>\n",
              "      <td>English</td>\n",
              "      <td>2018-12-16</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>580</th>\n",
              "      <td>Winter on Fire: Ukraine's Fight for Freedom</td>\n",
              "      <td>Documentary</td>\n",
              "      <td>October 9, 2015</td>\n",
              "      <td>91</td>\n",
              "      <td>8.4</td>\n",
              "      <td>English/Ukranian/Russian</td>\n",
              "      <td>2015-10-09</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>579</th>\n",
              "      <td>Taylor Swift: Reputation Stadium Tour</td>\n",
              "      <td>Concert Film</td>\n",
              "      <td>December 31, 2018</td>\n",
              "      <td>125</td>\n",
              "      <td>8.4</td>\n",
              "      <td>English</td>\n",
              "      <td>2018-12-31</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>578</th>\n",
              "      <td>Ben Platt: Live from Radio City Music Hall</td>\n",
              "      <td>Concert Film</td>\n",
              "      <td>May 20, 2020</td>\n",
              "      <td>85</td>\n",
              "      <td>8.4</td>\n",
              "      <td>English</td>\n",
              "      <td>2020-05-20</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>577</th>\n",
              "      <td>Dancing with the Birds</td>\n",
              "      <td>Documentary</td>\n",
              "      <td>October 23, 2019</td>\n",
              "      <td>51</td>\n",
              "      <td>8.3</td>\n",
              "      <td>English</td>\n",
              "      <td>2019-10-23</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>576</th>\n",
              "      <td>Cuba and the Cameraman</td>\n",
              "      <td>Documentary</td>\n",
              "      <td>November 24, 2017</td>\n",
              "      <td>114</td>\n",
              "      <td>8.3</td>\n",
              "      <td>English</td>\n",
              "      <td>2017-11-24</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>573</th>\n",
              "      <td>Klaus</td>\n",
              "      <td>Animation/Christmas/Comedy/Adventure</td>\n",
              "      <td>November 15, 2019</td>\n",
              "      <td>97</td>\n",
              "      <td>8.2</td>\n",
              "      <td>English</td>\n",
              "      <td>2019-11-15</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>571</th>\n",
              "      <td>13th</td>\n",
              "      <td>Documentary</td>\n",
              "      <td>October 7, 2016</td>\n",
              "      <td>100</td>\n",
              "      <td>8.2</td>\n",
              "      <td>English</td>\n",
              "      <td>2016-10-07</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-106e256b-0269-4648-8afd-e00c702c9394')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-106e256b-0269-4648-8afd-e00c702c9394 button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-106e256b-0269-4648-8afd-e00c702c9394');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 10
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# IMDB puanı ile \"Runtime\" arasındaki korelasyonu görselleştiriyoruz."
      ],
      "metadata": {
        "id": "tfXZtTYno7hE"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "plt.title('Correlation Matrix')\n",
        "sns.heatmap(NetflixOriginals.corr(), annot=True)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 298
        },
        "id": "64HVVXoppF0U",
        "outputId": "99e2d08b-d72b-4b0e-f16e-833beb3a9472"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<matplotlib.axes._subplots.AxesSubplot at 0x7fc806a5d9d0>"
            ]
          },
          "metadata": {},
          "execution_count": 11
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 432x288 with 2 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# IMDB puanı en yüksek 10 \"Genre\"yi görselleştiriyoruz."
      ],
      "metadata": {
        "id": "fRxkDdqopSR5"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "pd.pivot_table(NetflixOriginals, index='Genre', values='IMDB Score').sort_values(\"IMDB Score\", ascending=False).head(10)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 394
        },
        "id": "zDo81-41pX-N",
        "outputId": "00c42cb7-5ca7-4107-ce5a-78dc351d9488"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "                                      IMDB Score\n",
              "Genre                                           \n",
              "Animation/Christmas/Comedy/Adventure    8.200000\n",
              "Musical / Short                         7.700000\n",
              "Concert Film                            7.633333\n",
              "Anthology/Dark comedy                   7.600000\n",
              "Animation / Science Fiction             7.500000\n",
              "Making-of                               7.450000\n",
              "Action-adventure                        7.300000\n",
              "Historical drama                        7.200000\n",
              "Coming-of-age comedy-drama              7.200000\n",
              "Drama-Comedy                            7.200000"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-03ef574c-6b36-4cce-9c48-389bb6eda9e3\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>IMDB Score</th>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Genre</th>\n",
              "      <th></th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>Animation/Christmas/Comedy/Adventure</th>\n",
              "      <td>8.200000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Musical / Short</th>\n",
              "      <td>7.700000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Concert Film</th>\n",
              "      <td>7.633333</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Anthology/Dark comedy</th>\n",
              "      <td>7.600000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Animation / Science Fiction</th>\n",
              "      <td>7.500000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Making-of</th>\n",
              "      <td>7.450000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Action-adventure</th>\n",
              "      <td>7.300000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Historical drama</th>\n",
              "      <td>7.200000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Coming-of-age comedy-drama</th>\n",
              "      <td>7.200000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Drama-Comedy</th>\n",
              "      <td>7.200000</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-03ef574c-6b36-4cce-9c48-389bb6eda9e3')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-03ef574c-6b36-4cce-9c48-389bb6eda9e3 button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-03ef574c-6b36-4cce-9c48-389bb6eda9e3');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 12
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# \"Runtime\"ı en yüksek 10 filmi görselleştiriyoruz."
      ],
      "metadata": {
        "id": "FsRRKQWupcVQ"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "ilk_10_runtime = NetflixOriginals.groupby(\"Title\").agg({\"Runtime\": \"max\"}).sort_values(by = \"Runtime\", ascending = False)[:10].reset_index()\n",
        "plt.figure(figsize=(19,9))\n",
        "\n",
        "sns.barplot(x=\"Runtime\", y=\"Title\", data= ilk_10_runtime)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 568
        },
        "id": "Gn3nn4HDph8j",
        "outputId": "07e0970a-8c40-4739-9488-b9c0acf8cb00"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<matplotlib.axes._subplots.AxesSubplot at 0x7fc8051c9ed0>"
            ]
          },
          "metadata": {},
          "execution_count": 13
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 1368x648 with 1 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Yıllara göre film sayılarını görselleştiriyoruz."
      ],
      "metadata": {
        "id": "c2IDHURR0Qr1"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "NetflixOriginals['Year'] = NetflixOriginals['Date'].dt.year\n",
        "print(NetflixOriginals['Year'].value_counts())\n",
        "\n",
        "plt.figure(figsize  = (19,7))\n",
        "sns.barplot(NetflixOriginals['Year'].value_counts().index ,NetflixOriginals['Year'].value_counts().values)\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 639
        },
        "id": "6jSt5029ptZJ",
        "outputId": "7a9dca18-45cb-445a-a099-629779c276b0"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "2020    183\n",
            "2019    125\n",
            "2018     99\n",
            "2021     71\n",
            "2017     66\n",
            "2016     30\n",
            "2015      9\n",
            "2014      1\n",
            "Name: Year, dtype: int64\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "/usr/local/lib/python3.7/dist-packages/seaborn/_decorators.py:43: FutureWarning: Pass the following variables as keyword args: x, y. From version 0.12, the only valid positional argument will be `data`, and passing other arguments without an explicit keyword will result in an error or misinterpretation.\n",
            "  FutureWarning\n"
          ]
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 1368x504 with 1 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Dillere göre IMDB puanlarını düşükten başlayarak görselleştiriyoruz."
      ],
      "metadata": {
        "id": "qJIcAei9pywE"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "NetflixOriginals.groupby(\"Language\").agg({\"IMDB Score\" : \"mean\"}).sort_values(by = \"IMDB Score\").head().reset_index()\n",
        "plt.figure(figsize=(16,7))\n",
        "plt.xticks(rotation=90)\n",
        "sns.barplot(x= \"Language\", y= \"IMDB Score\", data=NetflixOriginals.groupby(\"Language\").agg({\"IMDB Score\" : \"mean\"}).sort_values(by = \"IMDB Score\").reset_index())\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 591
        },
        "id": "a1intzGWp5vj",
        "outputId": "39e07c58-b3c2-4def-a639-84783540feeb"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<matplotlib.axes._subplots.AxesSubplot at 0x7fc8028e2310>"
            ]
          },
          "metadata": {},
          "execution_count": 15
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 1152x504 with 1 Axes>"
            ],
            "image/png": "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RMwbtm8ADp7l4yuGGTMT04iIiIiZDgReAxxh+ypJmwFfHfM1RUTMC5IeAbwZ2JTanNL2rkOPmXYxERERERERsaokXQwcBSwF7uodH6ZNzIoxMzGNiIiIKCR9y/betX6m06SPaUQESFpqe7tWx8zENCIiIqKQtJHtayVtMujzqn1MRMSiJukw4LfAd4Hbesdt/37oMTMxjYiIiIiIiFUl6aoBh237YUOPmYlpRERERCHpZgak8AKiPHStN+JLiohYFNLHNCIiIqJi+z621xvwdZ9MSiNisZN0SO31Xn2fva/R2ImYRkREREwnaYMBh2+2fcfILyYiYp6QtMz2tv2vB71fXYmYRkRERMy0DPgd8B/Ar6vXyyUtk9RqJcqIiAmiWV4Per9aMjGNiIiImOkU4Fm2N7R9f2AP4ATgtcCnx3plERHj41leD3q/WpLKGxEREdFH0qW2t+47dontx0i6yPZjx3VtERHjIuku4I+U6Og9gVt6HwFLbK897NhrNb+8iIiIiAXnWklvAb5Zvd8HuF7SmsDd47usiIjxsb1mV2MnYhoRERHRR9KGwKHAE6tDZwOHAzcBD7V9xbiuLSJiIcrENCIiIiIiIsYqqbwRERERfSQ9AngzsCm15yXbu47rmiIiFrJETCMiIiL6SLoYOApYCtzVO2576dguKiJiAcvENCIiIqKPpKW20680ImJEMjGNiIiI6CPpMOC3wHeB23rHbf9+XNcUEbGQZWIaERER0UfSVQMO2/bDRn4xERGLQCamERERERERMVZrjPsCIiIiIuYLSYfUXu/V99n7Rn9FERGLQyamEREREVNeUnv9tr7Pdh/lhURELCaZmEZERERM0SyvB72PiIiWZGIaERERMcWzvB70PiIiWpLiRxEREREVSXcBf6RER+8J3NL7CFhie+1xXVtExEKWiWlERERERESMVVJ5IyIiIiIiYqwyMY2IiIiIiIixysQ0IiJiFpL+b9zXEBERsRhkYhoRERERERFjlYlpRETEapC0p6TzJF0o6VRJD6yOHybpC5JOk3SlpNfVfs+7JP27pLMkHSPpzdXx0yRtX73eUNLy6vWmks6UtKz62rk6voakT0u6XNIpkk6U9OLqs+0knS5pqaQfSdpoxH80ERERQ8vENCIiYvWcBexo+3HAN4FDap89Cngm8ATgUElrS3o88CJgG2APYPtVOMdvgd1sbwvsA3yiOv5CYFNgS+BlwE4AktYGjgRebHs74AvAEQ3+HyMiIkZqrXFfQERExITZGPjXKiJ5D+Cq2mc/sH0bcJuk3wIPBHYBjrd9K3CrpO+vwjnWBj4p6bHAXcAjquNPBI61fTdwnaSfVscfCWwFnCIJYE3g2ib/kxEREaOUiWlERMTqORL4qO3vSXoKcFjts9tqr+9i7p+zdzKVvbSkdvwNwPWUKOsawK1zjCPgF7Z3muO/i4iImJeSyhsREbF67gv8pnp9wCr892cDe0paImld4Dm1z5YD21WvX9x3jmuryOjLKBHQ3lgvqvaaPhB4SnX834EHSFqR2ivp0av1fxURETFGmZhGRETM7l6Srql9vZESIT1W0lLghrkGsP1z4HvAJcAPgUuBm6qPPwz8jaQLgQ1rv+3TwAGSLqbsW/1jdfw44Brgl8DXgGXATbZvp0xsP1D9nouAnYf/346IiBgt2R73NURERCxokta1/X+S7gWcAbzK9rKGY90fOB/YxfZ1bV5vRETEqGWPaURERPeOlrQlZR/pl4edlFZOkLQ+pfDSezMpjYiIhSAR04iIiIiIiBir7DGNiIiIiIiIscrENCIiIiIiIsYqE9OIiIiIiIgYq0xMIyIiIiIiYqwyMY2IiIiIiIixysQ0IiIiIiIixur/AzPQrzL7omKWAAAAAElFTkSuQmCC\n"
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Hangi yılın toplam \"Runtime\" süresinin en fazla olduğunu buluyoruz."
      ],
      "metadata": {
        "id": "R1UVSBS2p-bT"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "pd.pivot_table(NetflixOriginals, index='Year', values='Runtime', aggfunc='sum').sort_values(\"Runtime\", ascending=False).head(1)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 112
        },
        "id": "D1cnLTXlqDaR",
        "outputId": "272c9850-671d-4543-c805-dde57f935af6"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "      Runtime\n",
              "Year         \n",
              "2020    17384"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-ff50cd5e-b712-42e1-b1bb-ab107a38c511\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Runtime</th>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Year</th>\n",
              "      <th></th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>2020</th>\n",
              "      <td>17384</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-ff50cd5e-b712-42e1-b1bb-ab107a38c511')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-ff50cd5e-b712-42e1-b1bb-ab107a38c511 button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-ff50cd5e-b712-42e1-b1bb-ab107a38c511');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 16
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Her bir dilin en fazla kullanıldığı \"Genre\"yi buluyoruz.\n"
      ],
      "metadata": {
        "id": "UjOE01V2qMbh"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "NetflixOriginals.groupby([\"Language\"])[\"Genre\"].value_counts(sort=True).groupby(level=0).head(1)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "gbrRlATTqTz_",
        "outputId": "d495bf88-fcdd-4595-b8a0-1b7468153a90"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "Language                    Genre                \n",
              "Bengali                     Documentary                1\n",
              "Dutch                       Crime drama                1\n",
              "English                     Documentary              120\n",
              "English/Akan                War drama                  1\n",
              "English/Arabic              Documentary                1\n",
              "English/Hindi               Documentary                2\n",
              "English/Japanese            Crime drama                1\n",
              "English/Korean              Action-adventure           1\n",
              "English/Mandarin            Documentary                2\n",
              "English/Russian             Documentary                1\n",
              "English/Spanish             Documentary                5\n",
              "English/Swedish             Documentary                1\n",
              "English/Taiwanese/Mandarin  Drama                      1\n",
              "English/Ukranian/Russian    Documentary                1\n",
              "Filipino                    Drama                      1\n",
              "French                      Documentary                6\n",
              "Georgian                    Documentary                1\n",
              "German                      Drama                      1\n",
              "Hindi                       Drama                     13\n",
              "Indonesian                  Drama                      3\n",
              "Italian                     Drama                      4\n",
              "Japanese                    Anime/Science fiction      2\n",
              "Khmer/English/French        Drama                      1\n",
              "Korean                      Drama                      2\n",
              "Malay                       Action comedy              1\n",
              "Marathi                     Drama                      2\n",
              "Norwegian                   Horror                     1\n",
              "Polish                      Horror                     1\n",
              "Portuguese                  Comedy                     6\n",
              "Spanish                     Documentary                8\n",
              "Spanish/Basque              Black comedy               1\n",
              "Spanish/Catalan             Documentary                1\n",
              "Spanish/English             Documentary                1\n",
              "Swedish                     Thriller                   1\n",
              "Tamil                       Drama                      1\n",
              "Thai                        Documentary                1\n",
              "Thia/English                Documentary                1\n",
              "Turkish                     Comedy                     2\n",
              "Name: Genre, dtype: int64"
            ]
          },
          "metadata": {},
          "execution_count": 17
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Veri setinde outlier veri var mıdır? Açıklayınız."
      ],
      "metadata": {
        "id": "AegAcFRa_5Cq"
      }
    },
    {
      "cell_type": "code",
      "execution_count": 83,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 368
        },
        "id": "6CJH4tHRXWEE",
        "outputId": "9510ef0f-f559-4bb3-de35-479f0a9f51a6"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "/usr/local/lib/python3.7/dist-packages/seaborn/_decorators.py:43: FutureWarning: Pass the following variable as a keyword arg: x. From version 0.12, the only valid positional argument will be `data`, and passing other arguments without an explicit keyword will result in an error or misinterpretation.\n",
            "  FutureWarning\n",
            "/usr/local/lib/python3.7/dist-packages/seaborn/_decorators.py:43: FutureWarning: Pass the following variable as a keyword arg: x. From version 0.12, the only valid positional argument will be `data`, and passing other arguments without an explicit keyword will result in an error or misinterpretation.\n",
            "  FutureWarning\n"
          ]
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 432x288 with 2 Axes>"
            ],
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAAWAAAAEGCAYAAABbzE8LAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADh0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uMy4yLjIsIGh0dHA6Ly9tYXRwbG90bGliLm9yZy+WH4yJAAATuklEQVR4nO3de3Bc5XnH8d9jXZBsJ04Q4AEZR3YEJW5oTOKhNEkZ7jW0hmTaTkPJ2LTp2M2AMTYpJUUTzIwyTTuNqe0EDxRSbMoAmVwaCo7CJc2lU0JiEwcTMLARBiyMcQQlMdbFkp/+cY7EWtZqpb3oWUnfz4zHe87Zc86zZ9/z23fP7r4ydxcAYPxNiy4AAKYqAhgAghDAABCEAAaAIAQwAASpHsudjzvuOG9qaipTKZjqtm/f/mt3P36890u7RjmN1K7HFMBNTU3atm1baaoChjCzlyL2S7tGOY3UrrkEAQBBCGAACEIAA0AQAhgAghDAABCEAAaAIAQwAAQhgAEgCAEMAEEIYAAIQgADQBACGACCEMAAEIQABoAgBDAABCGAASAIAQwAQQhgAAhCAANAkDH9TbipaOPGjcpkMsMu6+jokCQ1NjbmXL+5uVkrV64sS23AeBrpXBjJaM6TXCb7+UMA55HJZLTj6WfVP/3Yo5ZVHXxLkvRaz/CHsergG2WtDRhPI50LI8l3nuReb/KfPwTwKPRPP1Zdp11y1Pz6XVsladhl2cuBySLXuTCSfOdJvvUmM64BA0AQAhgAghDAABCEAAaAIAQwAAQhgAEgCAEMAEEIYAAIQgADQBACGACCEMAAEIQABoAgBDAABCGAASAIAQwAQQhgAAhCAANAEAIYAIIQwAAQhAAGgCAEMAAEIYABIAgBDABBCGAACEIAA0AQAhgAghDAABCEAAaAIAQwAAQhgAEgCAEMAEEIYAAIQgADQBACGACCEMAAEIQABoAgBDAABCGAASAIAQwAQQhgAAhCAANAkEkTwBs3btTGjRujyyi7qfI4pzKe48pSzuejuixbDZDJZKJLGBdT5XFOZTzHlaWcz8ek6QEDwERDAANAEAIYAIIQwAAQhAAGgCAEMAAEIYABIAgBDABBCGAACEIAA0AQAhgAghDAABCEAAaAIAQwAAQhgAEgCAEMAEEIYAAIQgADQBACGACCEMAAEIQABoAgBDAABCGAASAIAQwAQQhgAAhCAANAEAIYAIIQwAAQhAAGgCAEMAAEIYABIAgBDABBCGAACEIAA0AQAhgAghDAABCEAAaAIAQwAASpLsVGOjs7dfPNN+uaa67RunXr1N3drVdffVUnnHCC9u3bJ3dXb2+v1qxZo02bNqmvr099fX066aST1NnZqYaGBnV0dEiSamtrNW3aNJ144okyM73yyis6dOjQ4L6uu+46bdq0SbNmzdJrr72mmpoazZkzR3v37tW8efNK8XAmhEwmo6uvvlo9PT36whe+oDvvvFN79uzRihUrtGXLFp188sm6/vrrtWHDBt10001qaGiILnmwnVRKPfkM1Lt06VLddNNNWr9+vZqbm8e07sBjzZ6WdMSyTCajVatWjWn7qCyFtu2S9IA3b96snTt3qrW1Vc8884za29vV3d2tl19+WT09Pert7ZUk3XLLLerq6tKhQ4fk7uro6FB3d/dg+EpSb2+vuru79eKLL6q9vf2I8JWkdevW6eDBg9q7d+9gsLe3t6urq0v79u0rxcOZEFpbW9Xd3S131xe/+EXt2bNHknTbbbepq6tLzz//vFpbW7Vz505t2bIluNrEQDuplHryGah37dq1evvtt9Xa2jrmdQcea/b00GWtra1j3j4qS6Ftu+gA7uzsVFtbm9xdu3fvHvG+7l7s7kbcRmdnpzo7O4veR6U7ePDgEce6r69v2Pvt3r1b7q62trbw45LdTiqhnnyy6z1w4ICk5HhmMpkxrdvW1qZMJjM4/d3vfveIZdu2bRt8Lke7fVSWYtp20ZcgNm/erMOHDxe7mZJZvny55syZU7LtZTIZTest7IVjWvdvlMn8VqtWrSppPV1dXWNap7+/X1u2bNHq1atLVsdYZbeTSqgnn1zturW1VXfdddeo1+3v71dra+vgdPY7uv7+fq1du/ao7R84cEBdXV0lbTelUMy5UIhynD+FyGQyqq+vz7m8mLadtwdsZsvNbJuZbdu/f/9Ryx999NGcPbAIb775ZnQJZTfWF7y+vj498sgjZapmdLLbSSXUU2i7zvcub+i6fX192r179+C0uw++i+vr6xvsXY9l+6gsxbTtvD1gd79d0u2StGjRoqNe/i644AJt3bq1YkJ4yZIlJe1ZrVq1StvbC7u2fLju3WqeP1vr168vaT27du1ST0/PqNeprq7WhRde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\n"
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ],
      "source": [
        "fig, axs = plt.subplots(ncols=2)\n",
        "sns.boxplot(NetflixOriginals['Runtime'], ax = axs[0])\n",
        "sns.boxplot(NetflixOriginals['IMDB Score'], ax = axs[1])\n",
        "plt.show()"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "* **Aykırı değer analizi yaparken görsel açıdan bilgi sahibi olmak için boxplot grafiğini kullanırız.**\n",
        "* **Grafiklere baktığımızda bazı değerlerin yüksek olduğunu görüyoruz ancak bu yükseklikler aykırı değer olduğu anlamına gelmeyebilir.**\n",
        "* **IMDB puanı grafiğinde boxplot dışında yer alan noktalara aykırı değer diyemeyiz çünkü en fazla 10 olabileceğini biliyoruz.**\n",
        "* **Runtime grafiğinde filmlerin süresi belirtilmektedir. Bazı değerlerin diğerlerinden uzak olması aykırı olduğu anlamına gelmez.**\n",
        "\n"
      ],
      "metadata": {
        "id": "HfYPJvlmq1KD"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def outlier_var_mi(degisken, ust_limit , alt_limit):\n",
        "  boolean = False\n",
        "  if(NetflixOriginals[(NetflixOriginals[str(degisken)] > ust_limit) | (NetflixOriginals[str(degisken)] <  alt_limit)].any(axis = None)):\n",
        "    boolean = True\n",
        "  return boolean\n",
        "\n",
        "factor = 2.5\n",
        "\n",
        "runtime_ust = np.abs(NetflixOriginals['Runtime'].mean() + NetflixOriginals['Runtime'].std() * factor)\n",
        "runtime_alt = np.abs(NetflixOriginals['Runtime'].mean() - NetflixOriginals['Runtime'].std() * factor)\n",
        "\n",
        "imdb_ust = NetflixOriginals['IMDB Score'].mean() + NetflixOriginals['IMDB Score'].std() * factor\n",
        "imdb_alt = NetflixOriginals['IMDB Score'].mean() - NetflixOriginals['IMDB Score'].std() * factor\n",
        "\n",
        "print(outlier_var_mi('Runtime' , runtime_ust , runtime_alt))\n",
        "print(outlier_var_mi('IMDB Score' , imdb_ust , imdb_alt))\n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "qURXJLqmJblw",
        "outputId": "b08339ed-beb6-4fc1-80aa-bf23eff43447"
      },
      "execution_count": 84,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "True\n",
            "True\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def iqr(df, degisken):\n",
        "    q1 = np.quantile(NetflixOriginals[degisken], 0.25)\n",
        "    q3 = np.quantile(NetflixOriginals[degisken], 0.75)\n",
        "    diff = q3 - q1\n",
        "    alt_limit = q1 - (1.5 * diff)\n",
        "    ust_limit = q3 + (1.5 * diff)\n",
        "    return NetflixOriginals[(NetflixOriginals[degisken] < alt_limit) | (NetflixOriginals[degisken] > ust_limit)]\n",
        "\n",
        "Runtime = iqr(NetflixOriginals, \"Runtime\")\n",
        "IMDB = iqr(NetflixOriginals, \"IMDB Score\")\n",
        "\n",
        "print(len(Runtime), len(IMDB))\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "URMtcaiQJfxw",
        "outputId": "7009f3ca-aaf8-4488-a590-ede7f7ea1f91"
      },
      "execution_count": 85,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "75 9\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "* **Fonksiyonu çalıştırdığımızda belirlediğimiz kurala göre aykırı olarak bulunan değerleri birer değişkene atadık. Her bir tabloda ne kadar kayıt olduğuna baktığımızda sırasıyla “Runtime” değişkeninde 75, “IMDB Score” değişkeninde 9 aykırı değer filtrelendiğini görüyoruz.**"
      ],
      "metadata": {
        "id": "ec8iAS9xJkzg"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 8))\n",
        "\n",
        "ax1.hist(NetflixOriginals[\"Runtime\"])\n",
        "ax1.set_title(\"Runtime\")\n",
        "\n",
        "ax2.hist(NetflixOriginals[\"IMDB Score\"])\n",
        "ax2.set_title(\"IMDB Score\")\n",
        "\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 499
        },
        "id": "YoLiOUxhJimu",
        "outputId": "322a8fed-cb7b-4c5f-a1db-4ddbd5ec07ac"
      },
      "execution_count": 86,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 1440x576 with 2 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    }
  ]
}