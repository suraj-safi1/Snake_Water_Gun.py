{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Snake_Water_Gun_game.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyM8MPaCXxukOR4uucz7g9eX",
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
        "<a href=\"https://colab.research.google.com/github/suraj-safi1/Snake_Water_Gun.py/blob/main/Snake_Water_Gun_game.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 3,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "GovRcZj3UmBf",
        "outputId": "4467c7ac-e75b-4574-9dff-6322b45d4089"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "comp turn: Snake(s) Water(w) Gun(g)?\n",
            "2\n",
            "Your turn:Snake(s) Water(w) or Gun(g)?s\n",
            "Computer Choose:- w\n",
            "You Choose:- s\n",
            "suraj win\n"
          ]
        }
      ],
      "source": [
        "import random\n",
        "def gameWin(comp,suraj):\n",
        "  if comp == suraj:\n",
        "      return None\n",
        "  elif comp == 's':\n",
        "    if suraj=='w':\n",
        "      return False\n",
        "    elif suraj == 'g':\n",
        "      return True\n",
        "  elif comp=='w':\n",
        "    if suraj=='g':\n",
        "      return False\n",
        "    elif suraj=='s':\n",
        "      return True\n",
        "  elif comp=='g':\n",
        "    if suraj=='s':\n",
        "      return False\n",
        "    elif suraj=='w':\n",
        "      return True\n",
        "\n",
        "print(\"comp turn: Snake(s) Water(w) Gun(g)?\")\n",
        "randNo= random.randint(1,3)\n",
        "print(randNo)\n",
        "if randNo== 1:\n",
        "   comp = 's'\n",
        "elif randNo==2:\n",
        "   comp='w'\n",
        "elif randNo==3:\n",
        "   comp='g'\n",
        "\n",
        "suraj=input(\"Your turn:Snake(s) Water(w) or Gun(g)?\")\n",
        "a=gameWin(comp,suraj)\n",
        "print(f'Computer Choose:- {comp}')\n",
        "print(f'You Choose:- {suraj}')\n",
        "if a == None:\n",
        "  print(\"The game is a tie\")\n",
        "elif a:\n",
        "  print(f\"suraj win\")\n",
        "else:\n",
        "  print(\"suraj lose\")"
      ]
    }
  ]
}