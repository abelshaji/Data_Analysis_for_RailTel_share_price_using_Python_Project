
{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "d8994e22",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "import seaborn as sns\n",
    "import matplotlib.pyplot as plt\n",
    "df=pd.read_csv('C:\\\\Users\\\\Jessica\\\\Desktop\\\\pandas\\\\RAILTEL_NEW.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "5d53752f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
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
       "      <th>Date</th>\n",
       "      <th>Open</th>\n",
       "      <th>High</th>\n",
       "      <th>Low</th>\n",
       "      <th>Close</th>\n",
       "      <th>% Change</th>\n",
       "      <th>% Change vs Average</th>\n",
       "      <th>Volume</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>24-03-2023</td>\n",
       "      <td>101.30</td>\n",
       "      <td>101.80</td>\n",
       "      <td>99.00</td>\n",
       "      <td>99.35</td>\n",
       "      <td>-1.39</td>\n",
       "      <td>-1.98</td>\n",
       "      <td>6,04,472</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>27-03-2023</td>\n",
       "      <td>99.80</td>\n",
       "      <td>99.90</td>\n",
       "      <td>96.70</td>\n",
       "      <td>99.05</td>\n",
       "      <td>-0.30</td>\n",
       "      <td>-0.89</td>\n",
       "      <td>12,05,927</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>28-03-2023</td>\n",
       "      <td>99.00</td>\n",
       "      <td>99.75</td>\n",
       "      <td>96.25</td>\n",
       "      <td>97.05</td>\n",
       "      <td>-2.02</td>\n",
       "      <td>-2.61</td>\n",
       "      <td>13,58,690</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>29-03-2023</td>\n",
       "      <td>97.05</td>\n",
       "      <td>100.45</td>\n",
       "      <td>96.95</td>\n",
       "      <td>99.65</td>\n",
       "      <td>2.68</td>\n",
       "      <td>2.09</td>\n",
       "      <td>9,39,351</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>31-03-2023</td>\n",
       "      <td>99.95</td>\n",
       "      <td>102.80</td>\n",
       "      <td>99.65</td>\n",
       "      <td>101.10</td>\n",
       "      <td>1.46</td>\n",
       "      <td>0.87</td>\n",
       "      <td>12,88,953</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "         Date    Open    High    Low   Close  % Change  % Change vs Average  \\\n",
       "0  24-03-2023  101.30  101.80  99.00   99.35     -1.39                -1.98   \n",
       "1  27-03-2023   99.80   99.90  96.70   99.05     -0.30                -0.89   \n",
       "2  28-03-2023   99.00   99.75  96.25   97.05     -2.02                -2.61   \n",
       "3  29-03-2023   97.05  100.45  96.95   99.65      2.68                 2.09   \n",
       "4  31-03-2023   99.95  102.80  99.65  101.10      1.46                 0.87   \n",
       "\n",
       "      Volume  \n",
       "0   6,04,472  \n",
       "1  12,05,927  \n",
       "2  13,58,690  \n",
       "3   9,39,351  \n",
       "4  12,88,953  "
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head(5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "132c2293",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Date                    object\n",
       "Open                   float64\n",
       "High                   float64\n",
       "Low                    float64\n",
       "Close                  float64\n",
       "% Change               float64\n",
       "% Change vs Average    float64\n",
       "Volume                  object\n",
       "dtype: object"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.dtypes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "30d515b4",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
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
       "      <th>Open</th>\n",
       "      <th>High</th>\n",
       "      <th>Low</th>\n",
       "      <th>Close</th>\n",
       "      <th>% Change</th>\n",
       "      <th>% Change vs Average</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>248.000000</td>\n",
       "      <td>248.00000</td>\n",
       "      <td>248.000000</td>\n",
       "      <td>248.000000</td>\n",
       "      <td>248.000000</td>\n",
       "      <td>248.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>233.691734</td>\n",
       "      <td>240.71996</td>\n",
       "      <td>227.759879</td>\n",
       "      <td>233.635685</td>\n",
       "      <td>0.589798</td>\n",
       "      <td>-0.000242</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>106.541892</td>\n",
       "      <td>110.83386</td>\n",
       "      <td>102.344552</td>\n",
       "      <td>105.857453</td>\n",
       "      <td>3.883895</td>\n",
       "      <td>3.883893</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>97.050000</td>\n",
       "      <td>99.75000</td>\n",
       "      <td>96.250000</td>\n",
       "      <td>97.050000</td>\n",
       "      <td>-20.000000</td>\n",
       "      <td>-20.590000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>131.012500</td>\n",
       "      <td>132.67500</td>\n",
       "      <td>128.687500</td>\n",
       "      <td>130.750000</td>\n",
       "      <td>-1.287500</td>\n",
       "      <td>-1.877500</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>221.125000</td>\n",
       "      <td>225.85000</td>\n",
       "      <td>216.400000</td>\n",
       "      <td>221.250000</td>\n",
       "      <td>0.380000</td>\n",
       "      <td>-0.210000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>299.612500</td>\n",
       "      <td>309.52500</td>\n",
       "      <td>294.462500</td>\n",
       "      <td>299.637500</td>\n",
       "      <td>2.512500</td>\n",
       "      <td>1.922500</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>473.500000</td>\n",
       "      <td>491.45000</td>\n",
       "      <td>448.250000</td>\n",
       "      <td>469.950000</td>\n",
       "      <td>15.500000</td>\n",
       "      <td>14.910000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "             Open       High         Low       Close    % Change  \\\n",
       "count  248.000000  248.00000  248.000000  248.000000  248.000000   \n",
       "mean   233.691734  240.71996  227.759879  233.635685    0.589798   \n",
       "std    106.541892  110.83386  102.344552  105.857453    3.883895   \n",
       "min     97.050000   99.75000   96.250000   97.050000  -20.000000   \n",
       "25%    131.012500  132.67500  128.687500  130.750000   -1.287500   \n",
       "50%    221.125000  225.85000  216.400000  221.250000    0.380000   \n",
       "75%    299.612500  309.52500  294.462500  299.637500    2.512500   \n",
       "max    473.500000  491.45000  448.250000  469.950000   15.500000   \n",
       "\n",
       "       % Change vs Average  \n",
       "count           248.000000  \n",
       "mean             -0.000242  \n",
       "std               3.883893  \n",
       "min             -20.590000  \n",
       "25%              -1.877500  \n",
       "50%              -0.210000  \n",
       "75%               1.922500  \n",
       "max              14.910000  "
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "812ca270",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Date                   0\n",
       "Open                   0\n",
       "High                   0\n",
       "Low                    0\n",
       "Close                  0\n",
       "% Change               0\n",
       "% Change vs Average    0\n",
       "Volume                 0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.isnull().sum()\n",
    "#Now we can make sure there are no null values in our data set"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "89954600",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Text(0, 0.5, 'Price In Rupees')"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAABNYAAAHBCAYAAAClnjY7AAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjcuMSwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy/bCgiHAAAACXBIWXMAAA9hAAAPYQGoP6dpAACnuElEQVR4nOzdd3hUddrG8e8kk0x6Jw1C7wSQ3hSQKopdsQv2vmJZ67qiruJr79hYEVHB3kVlBaSI9N5LSCCNkN4nM+f9YzIDMQkkkGQScn+ua65lzpw555kYV3Ln+f0ek2EYBiIiIiIiIiIiIlIrHu4uQEREREREREREpClSsCYiIiIiIiIiInICFKyJiIiIiIiIiIicAAVrIiIiIiIiIiIiJ0DBmoiIiIiIiIiIyAlQsCYiIiIiIiIiInICFKyJiIiIiIiIiIicAAVrIiIiIiIiIiIiJ0DBmoiIiIiIiIiIyAlQsCYiIiJuNWvWLEwmk+thNpuJiYnh8ssvZ9euXSd83bZt2zJlyhTX84SEBEwmE7NmzXIdW758OdOmTSM7O/uE7zNt2jRMJlONzv3ll18YN24csbGxWCwWYmNjGTlyJM8++2yF80wmE3feeecJ19TQ0tLSeOihh+jZsycBAQH4+PjQqVMn7r777gr/DGvztWpoVX0ftmrViuuuu46DBw/W6BpTpkyhbdu29VuoiIiINCpmdxcgIiIiAvDBBx/QtWtXiouLWbZsGU8//TQLFy5k+/bthIaG1vp6X3/9NUFBQcc8Z/ny5TzxxBNMmTKFkJCQE6y8Zt5++21uu+02Lr74Yt544w3CwsJISkpi+fLlfPHFFzz00EP1ev/6snLlSiZOnIhhGNx5550MGTIEb29vduzYwZw5cxg4cCBZWVnuLrPGnN+HRUVF/PHHH0yfPp3FixezadMm/P39j/nexx57jLvvvruBKhUREZHGQMGaiIiINArx8fH0798fgJEjR2Kz2Xj88cf55ptvuO6662p9vT59+tR1iSdl+vTpDB8+nC+++KLC8WuuuQa73d7g9VitVldn1onKzc3l/PPPx8fHh+XLl9OqVSvXayNHjuSWW26p9Hkbu6O/D88880xsNhtPPfUU33zzDVdddVWV7yksLMTPz48OHTo0ZKkiIiLSCGgpqIiIiDRKznAjLS3Nday4uJj77ruP0047jeDgYMLCwhgyZAjffvttpff/fSno302bNo1//vOfALRr1861BHDRokWuc+bNm8eQIUPw9/cnICCA8ePHs27duhP6PIcPHyYmJqbK1zw8qv4r2UcffUS3bt3w8/Ojd+/e/PDDDxVe3717N9dddx2dOnXCz8+Pli1bcu6557Jp06YK5y1atAiTycRHH33EfffdR8uWLbFYLOzevRuABQsWMHr0aIKCgvDz82PYsGH873//O+5neu+990hNTeW5556rEKod7ZJLLjnmNex2O8899xxdu3bFYrEQGRnJtddey4EDByqct27dOiZOnEhkZKRrGe0555xT4TzDMHjrrbc47bTT8PX1JTQ0lEsuuYS9e/ce97NUZ/DgwQDs378fcCz3DAgIYNOmTYwbN47AwEBGjx7teu3vS0Htdjuvv/66q6aQkBAGDx7Md999V+G8uvxeExERkYajYE1EREQapX379gHQuXNn17GSkhIyMzO5//77+eabb/j00085/fTTueiii5g9e3atrn/jjTdy1113AfDVV1/x559/8ueff9K3b18AnnnmGa644gq6d+/OZ599xkcffUReXh5nnHEGW7durfXnGTJkCF9++SXTpk1jw4YN2Gy2Y57/448/8sYbb/Dkk0/y5ZdfEhYWxoUXXlghJEpOTiY8PJxnn32W+fPn8+abb2I2mxk0aBA7duyodM2HH36YxMRE3n77bb7//nsiIyOZM2cO48aNIygoiA8//JDPPvuMsLAwxo8ff9xw7ddff8XT05Nzzz231l8Pp9tuu40HH3yQsWPH8t133/HUU08xf/58hg4dSkZGBgAFBQWMHTuWtLQ03nzzTX777TdeeeUVWrduTV5enutat9xyC1OnTmXMmDF88803vPXWW2zZsoWhQ4dWCGhrwxk+tmjRwnWstLSU8847j1GjRvHtt9/yxBNPVPv+KVOmcPfddzNgwADmzZvH3LlzOe+880hISHCdU9ffayIiItKADBERERE3+uCDDwzAWLFihWG1Wo28vDxj/vz5RnR0tDF8+HDDarVW+96ysjLDarUaN9xwg9GnT58Kr7Vp08aYPHmy6/m+ffsMwPjggw9cx55//nkDMPbt21fhvYmJiYbZbDbuuuuuCsfz8vKM6OhoY9KkSa5jjz/+uFGTv1Lt3r3biI+PNwADMHx9fY3Ro0cbb7zxhlFaWlrhXMCIiooycnNzXcdSU1MNDw8PY/r06dXeo6yszCgtLTU6depk3HPPPa7jCxcuNABj+PDhFc4vKCgwwsLCjHPPPbfCcZvNZvTu3dsYOHDgMT9T165djejo6ON+dqe/f622bdtmAMbtt99e4by//vrLAIxHHnnEMAzDWL16tQEY33zzTbXX/vPPPw3AePHFFyscT0pKMnx9fY0HHnjgmLVV9X34ww8/GC1atDACAwON1NRUwzAMY/LkyQZg/Pe//610jcmTJxtt2rRxPf/jjz8MwHj00UervW9tvtdERESk8VHHmoiIiDQKgwcPxsvLi8DAQM466yxCQ0P59ttvK+0B9vnnnzNs2DACAgIwm814eXkxc+ZMtm3bVme1/PLLL5SVlXHttddSVlbmevj4+DBixIgKy0VrqkOHDmzYsIHFixfzxBNPMGbMGFatWuXa8L+4uLjC+WeeeSaBgYGu51FRUURGRrqWJAKUlZXxzDPP0L17d7y9vTGbzXh7e7Nr164qvx4XX3xxhefLly8nMzOTyZMnV/icdruds846i1WrVlFQUFDrz1pTCxcuBKi0ZHfgwIF069bN1THXsWNHQkNDefDBB3n77ber7OL64YcfMJlMXH311RU+S3R0NL17967xP7Ojvw8nTpxIdHQ0P//8M1FRURXO+/vXsio///wzAHfccUe159TH95qIiIg0HA0vEBERkUZh9uzZdOvWjby8PObNm8c777zDFVdc4QonwLFkc9KkSVx66aX885//JDo6GrPZzIwZM/jvf/9bZ7U4lw0OGDCgyter2xPteDw8PBg+fDjDhw8HHEscb7jhBubNm8d///tfbr/9dte54eHhld5vsVgoKipyPb/33nt58803efDBBxkxYgShoaF4eHhw4403VjjP6e97vDk/57H2QcvMzKx2Gmbr1q3ZtWsXBQUFx52YWZXDhw9XWRdAbGysK0QMDg5m8eLFPP300zzyyCNkZWURExPDTTfdxL/+9S+8vLxIS0vDMIxKAZhT+/bta1ST8/vQbDYTFRVVZW1+fn7HnTgLcOjQITw9PYmOjq72nPr6XhMREZGGoWBNREREGoVu3bpVmsb4/vvv88UXX7iCnzlz5tCuXTvmzZuHyWRyvbekpKROa4mIiADgiy++oE2bNnV67aP5+/vz8MMPM2/ePDZv3lzr98+ZM4drr72WZ555psLxjIwMQkJCKp1/9NcMjnzO119/3bVJ/99VF1QBjB8/nl9//ZXvv/+eyy+/vJbVHwkPU1JSKg0/SE5OdtUH0LNnT+bOnYthGGzcuJFZs2bx5JNP4uvry0MPPURERAQmk4klS5ZgsVgq3auqY1U5+vuwOn//OlanRYsW2Gw2UlNTqx1c0VDfayIiIlI/9CswERERaZSee+45QkND+fe//43dbgccgYa3t3eFYCM1NbXKqaA14Qxb/t7dNX78eMxmM3v27KF///5VPmorJSWlyuPOJZuxsbG1vqbJZKoUGP34448cPHiwRu8fNmwYISEhbN26tdrP6e3tXe37b7jhBqKjo3nggQeqvedXX31V7ftHjRoFOALCo61atYpt27a5pm0ezWQy0bt3b15++WVCQkJYu3YtABMnTsQwDA4ePFjl5+jZs+dxvx51bcKECQDMmDGj2nPq43tNREREGo461kRERKRRCg0N5eGHH+aBBx7gk08+4eqrr2bixIl89dVX3H777VxyySUkJSXx1FNPERMTw65du2p9D2fY8uqrrzJ58mS8vLzo0qULbdu25cknn+TRRx9l7969rj3f0tLSWLlyJf7+/secBFmVHj16MHr0aCZMmECHDh0oLi7mr7/+4sUXXyQqKoobbrih1vVPnDiRWbNm0bVrV3r16sWaNWt4/vnnK3V/VScgIIDXX3+dyZMnk5mZySWXXEJkZCSHDh1iw4YNHDp06JihUHBwMN9++y0TJ06kT58+rv3inPu8zZkzhw0bNnDRRRdV+f4uXbpw88038/rrr+Ph4cGECRNISEjgscceIy4ujnvuuQdw7J/21ltvccEFF9C+fXsMw+Crr74iOzubsWPHAo6Q8Oabb+a6665j9erVDB8+HH9/f1JSUli6dCk9e/bktttuq+VX+OScccYZXHPNNfznP/8hLS2NiRMnYrFYWLduHX5+ftx111318r0mIiIiDUfBmoiIiDRad911F2+88QZPPvkkV1xxBddddx3p6em8/fbb/Pe//6V9+/Y89NBDHDhw4ITCh5EjR/Lwww/z4Ycf8t5772G321m4cKHrePfu3Xn11Vf59NNPKSkpITo6mgEDBnDrrbfW+l7PPvssv/zyC08//TSpqamUlZURFxfHlVdeyaOPPlrtUsFjefXVV/Hy8mL69Onk5+fTt29fvvrqK/71r3/V+BpXX301rVu35rnnnuOWW24hLy+PyMhITjvttEpDBaoycOBANm3axMsvv8xnn33G//3f/2Gz2YiLi2P06NG88cYbx3z/jBkz6NChAzNnzuTNN98kODiYs846i+nTp7uWinbq1ImQkBCee+45kpOT8fb2pkuXLsyaNYvJkye7rvXOO+8wePBg3nnnHd566y3sdjuxsbEMGzaMgQMH1vhrUpdmzZpF3759mTlzJrNmzcLX15fu3bvzyCOPuM6p6+81ERERaTgmwzAMdxchIiIiIiIiIiLS1GiPNRERERERERERkROgYE1EREREREREROQEKFgTERERERERERE5AQrWREREREREREREToCCNRERERERERERkROgYE1EREREREREROQEmN1dQGNgt9tJTk4mMDAQk8nk7nJERERERERERMRNDMMgLy+P2NhYPDyO3ZOmYA1ITk4mLi7O3WWIiIiIiIiIiEgjkZSURKtWrY55joI1IDAwEHB8wYKCgtxcjYiIiIiIiIiIuEtubi5xcXGuvOhYFKyBa/lnUFCQgjUREREREREREanRdmEaXiAiIiIiIiIiInICFKyJiIiIiIiIiIicAAVrIiIiIiIiIiIiJ0DBmoiIiIiIiIiIyAlQsCYiIiIiIiIiInICFKyJiIiIiIiIiIicAAVrIiIiIiIiIiIiJ0DBmoiIiIiIiIiIyAlQsCYiIiIiIiIiInICFKyJiIiIiIiIiIicAAVrIiIiIiIiIiIiJ0DBmoiIiIiIiIiIyAlQsCYiIiIiIiIiInICFKyJiIiIiIiIiACGYbDnUD52u+HuUqSJULAmIiIiIiIiIgJ8uz6Z0S8uZsbiPe4uRZoIBWsiIiIiIiIiIsC6xCwAvlx7wM2VSFOhYE1EREREREREBEjLLQFg76ECEjIK3FyNNAUK1kREREREREREgLS8Yteff9+e7sZKpKlQsCYiIiIiIiIiAqSXd6wBLNyhYE2OT8GaiIiIiIiIiDR7hmGQflTH2oq9h8kvKXNjRdIUKFgTERERERERkWYvq9CK1WYA0DLEF6vNYOmuDDdXJY2dgjURERERERERafbSch3dahEB3oztHgXAQu2zJsehYE1EREREREREmj1nsBYZ6MOorpGAY581u91wZ1nSyClYExEREREREZFmzzm4IDLIwqD2Yfh5e5KeV8KW5Fw3VyaNmYI1EREREREREWn2nB1rUYE+WMyenN4xAoDfa7kcNCmzkItnLOfb9QfrvEZpfBSsiYiIiIiIiEizl1Y+ETQqyALgWg76+47aBWvv/rGXNfuzmLFoT90WKI2SgjURERERERERafbSXEtBfQA4szxY25CUzaG8khpdo6TMxvcbkwHYnppHZkFpPVQqjYmCNRERERERERFp9tKdS0HLg7WoIB96xAYBsKiGXWsLt6eTXWh1PV+573AdVymNjYI1EREREREREWn2nB1rzqWgAKPLu9YWbEur0TW+XOvYV83b7IhbVuzNrMsSpRFqNMHa9OnTMZlMTJ061XVsypQpmEymCo/BgwdXeF9JSQl33XUXERER+Pv7c95553HgwIEGrl5EREREREREmiqb3eBQvjNY83EdH9cjGoBftqTx06aUY17jcH4JC8sHHdw+sgMAK/aqY+1U1yiCtVWrVvHuu+/Sq1evSq+dddZZpKSkuB4//fRThdenTp3K119/zdy5c1m6dCn5+flMnDgRm83WUOWLiIiIiIiISBOWWVCKzW5gMkG4v7freHzLYK4f1g6Aez9bz+aDOdVe4/sNyZTZDXq2DObqwW0A7bPWHLg9WMvPz+eqq67ivffeIzQ0tNLrFouF6Oho1yMsLMz1Wk5ODjNnzuTFF19kzJgx9OnThzlz5rBp0yYWLFjQkB9DRERERERERJqotPL91SICLJg9K0Ylj5zdleGdW1BstXPT7NWkl08P/TvnMtCL+7YkIsBC56gAQPusnercHqzdcccdnHPOOYwZM6bK1xctWkRkZCSdO3fmpptuIj39yIaBa9aswWq1Mm7cONex2NhY4uPjWb58eb3XLiIiIiIiIiJNnzMsO3p/NSezpwdvXNmHDi38Sckp5ubZayi2VlwltzMtj00HczB7mDi3dywAg9uHA9pn7VTn1mBt7ty5rF27lunTp1f5+oQJE/j444/5/fffefHFF1m1ahWjRo2ipMSx7jk1NRVvb+9KnW5RUVGkpqZWe9+SkhJyc3MrPERERERERESkeXINLgj0qfL1IB8v3p88gGBfL9YnZXP/5xsoKClzvf7lWsde72d2jSQ8wBHOHQnW1LF2KnNbsJaUlMTdd9/NnDlz8PGp+hv3sssu45xzziE+Pp5zzz2Xn3/+mZ07d/Ljjz8e89qGYWAymap9ffr06QQHB7secXFxJ/VZRERERERERKTpci4FjQyqOp8AaBfhz1tX9cXTw8QPG1MY8fxCPli2j6JSG9+sO7IM1GlgO8dWVttT88jSPmunLLcFa2vWrCE9PZ1+/fphNpsxm80sXryY1157DbPZXOXwgZiYGNq0acOuXbsAiI6OprS0lKysrArnpaenExUVVe29H374YXJyclyPpKSkuv1wIiIiIiIiItJkuDrWqlgKerRhHSN495p+tAn3IyO/lCe+38rQZ/9HWm4JIX5enNk10nXu0fus/bVPy0FPVW4L1kaPHs2mTZtYv36969G/f3+uuuoq1q9fj6enZ6X3HD58mKSkJGJiYgDo168fXl5e/Pbbb65zUlJS2Lx5M0OHDq323haLhaCgoAoPEREREREREWme0nOde6xV37HmNLpbFAvuHcHTF8YTFWQhq9AKwLm9YrGYK2YZWg566jO768aBgYHEx8dXOObv7094eDjx8fHk5+czbdo0Lr74YmJiYkhISOCRRx4hIiKCCy+8EIDg4GBuuOEG7rvvPsLDwwkLC+P++++nZ8+e1Q5DEBERERERERE5WtoxhhdUxcvTg6sGteHivq2Y/WcC65OyuePMjpXOG9w+nNl/7lewdgpzW7B2PJ6enmzatInZs2eTnZ1NTEwMZ555JvPmzSMwMNB13ssvv4zZbGbSpEkUFRUxevRoZs2aVWXHm4iIiIiIiEhD25qcy/2fb+C+cZ0Z3a36bYvEfZxLQSOrGV5QHR8vT24e3qHa1/++z1qov/eJFymNUqMK1hYtWuT6s6+vL7/88stx3+Pj48Prr7/O66+/Xo+ViYiIiIiIiJyYX7emsjUll6/XHVSw1giV2ewczi8P1mrYsVZTzn3Wdqbl89e+TM6Kj67T64v7uW2PNREREREREZHmwDkRMlOTIRulwwWl2A3w9DAR7l+3wRpon7VTnYI1ERERERERkXp0WMFao5ZWPrigRYAFTw9TnV/fGawt3JHOweyiOr++uJeCNREREREREZF6lFWoYK0xc+6vVtPBBbU1uH04ARYz+w8Xcubzi3j8282uKaTS9ClYExEREREREalHmQVWwBGwGYZR4/fV5lw5cc6Otcig2g0uqKkwf28+uWkQQzuEU2qz8+Gf+znjuYW89OsO/TM+BShYExEREREREalHmQWOjiirzSCvpKxG7/l8dRKnPfkbC3ek1/g+8zen8sAXGygq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",
      "text/plain": [
       "<Figure size 1500x500 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.figure(figsize=(15,5))\n",
    "plt.plot(df[\"Close\"])\n",
    "plt.title('Railtel Share Close Price',fontsize=12)\n",
    "plt.ylabel('Price In Rupees')\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "d5c5b3a7",
   "metadata": {},
   "outputs": [],
   "source": [
    "df['Volume']=df['Volume'].str.replace(',','')\n",
    "#We should remove the comma to convert the data type of the volume column into float"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "aa8f8f8c",
   "metadata": {},
   "outputs": [],
   "source": [
    "df['Volume']=df['Volume'].astype(float)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "3815ea8e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Date                    object\n",
       "Open                   float64\n",
       "High                   float64\n",
       "Low                    float64\n",
       "Close                  float64\n",
       "% Change               float64\n",
       "% Change vs Average    float64\n",
       "Volume                 float64\n",
       "dtype: object"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.dtypes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "67ad3cd4",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\Jessica\\AppData\\Local\\Temp\\ipykernel_14848\\702665920.py:4: MatplotlibDeprecationWarning: Auto-removal of overlapping axes is deprecated since 3.6 and will be removed two minor releases later; explicitly call ax.remove() as needed.\n",
      "  plt.subplot(2,3,i+1)\n"
     ]
    },
    {
     "data": {
      "image/png": "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",
      "text/plain": [
       "<Figure size 2000x1000 with 3 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.subplots(figsize=(20,10))\n",
    "a=['Open','Close','Volume']\n",
    "for i, col in enumerate(a):\n",
    " plt.subplot(2,3,i+1)\n",
    " sns.boxplot(df[col])\n",
    "plt.show()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c766f174",
   "metadata": {},
   "outputs": [],
   "source": [
    "#from datetime import datetime\n",
    "#df['Date']=pd.to_datetime(df['Date'])\n",
    "#df['Date']=df['Date'].astype(datetime64)\n",
    "#sb.regplot(x=to_datetime(df['Date']),y=df['Close'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "074b02df",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Date                    object\n",
       "Open                   float64\n",
       "High                   float64\n",
       "Low                    float64\n",
       "Close                  float64\n",
       "% Change               float64\n",
       "% Change vs Average    float64\n",
       "Volume                 float64\n",
       "dtype: object"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.dtypes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "63d7a606",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
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
       "      <th>Date</th>\n",
       "      <th>Open</th>\n",
       "      <th>High</th>\n",
       "      <th>Low</th>\n",
       "      <th>Close</th>\n",
       "      <th>% Change</th>\n",
       "      <th>% Change vs Average</th>\n",
       "      <th>Volume</th>\n",
       "      <th>day</th>\n",
       "      <th>month</th>\n",
       "      <th>year</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>24-03-2023</td>\n",
       "      <td>101.3</td>\n",
       "      <td>101.80</td>\n",
       "      <td>99.00</td>\n",
       "      <td>99.35</td>\n",
       "      <td>-1.39</td>\n",
       "      <td>-1.98</td>\n",
       "      <td>604472.0</td>\n",
       "      <td>24.0</td>\n",
       "      <td>3</td>\n",
       "      <td>2023</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>27-03-2023</td>\n",
       "      <td>99.8</td>\n",
       "      <td>99.90</td>\n",
       "      <td>96.70</td>\n",
       "      <td>99.05</td>\n",
       "      <td>-0.30</td>\n",
       "      <td>-0.89</td>\n",
       "      <td>1205927.0</td>\n",
       "      <td>27.0</td>\n",
       "      <td>3</td>\n",
       "      <td>2023</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>28-03-2023</td>\n",
       "      <td>99.0</td>\n",
       "      <td>99.75</td>\n",
       "      <td>96.25</td>\n",
       "      <td>97.05</td>\n",
       "      <td>-2.02</td>\n",
       "      <td>-2.61</td>\n",
       "      <td>1358690.0</td>\n",
       "      <td>28.0</td>\n",
       "      <td>3</td>\n",
       "      <td>2023</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "         Date   Open    High    Low  Close  % Change  % Change vs Average  \\\n",
       "0  24-03-2023  101.3  101.80  99.00  99.35     -1.39                -1.98   \n",
       "1  27-03-2023   99.8   99.90  96.70  99.05     -0.30                -0.89   \n",
       "2  28-03-2023   99.0   99.75  96.25  97.05     -2.02                -2.61   \n",
       "\n",
       "      Volume   day  month  year  \n",
       "0   604472.0  24.0      3  2023  \n",
       "1  1205927.0  27.0      3  2023  \n",
       "2  1358690.0  28.0      3  2023  "
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "split=df['Date'].str.split('-',expand=True)\n",
    "df['day'] = split[0].astype('float')\n",
    "df['month'] = split[1].astype('int')\n",
    "df['year'] = split[2].astype('int')\n",
    "df.head(3)\n",
    "# we have seperated the date column in three columns as day,month,year"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "d5b4830f",
   "metadata": {},
   "outputs": [],
   "source": [
    "df[\"is_quater\"]=np.where(df['month']%3==0,1,0)\n",
    "#Now we can seperate the data in quaterly wise to analyze the company performance when the quartely results are published"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "dbeae386",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\Jessica\\AppData\\Local\\Temp\\ipykernel_14848\\316346549.py:1: FutureWarning: The default value of numeric_only in DataFrameGroupBy.mean is deprecated. In a future version, numeric_only will default to False. Either specify numeric_only or select only columns which should be valid for the function.\n",
      "  df.groupby('is_quater').mean()\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<div>\n",
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
       "      <th>Open</th>\n",
       "      <th>High</th>\n",
       "      <th>Low</th>\n",
       "      <th>Close</th>\n",
       "      <th>% Change</th>\n",
       "      <th>% Change vs Average</th>\n",
       "      <th>Volume</th>\n",
       "      <th>day</th>\n",
       "      <th>month</th>\n",
       "      <th>year</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>is_quater</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>229.153614</td>\n",
       "      <td>236.372590</td>\n",
       "      <td>223.735542</td>\n",
       "      <td>229.727711</td>\n",
       "      <td>0.770</td>\n",
       "      <td>0.17994</td>\n",
       "      <td>7.437773e+06</td>\n",
       "      <td>15.86747</td>\n",
       "      <td>6.000000</td>\n",
       "      <td>2023.259036</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>242.878659</td>\n",
       "      <td>249.520732</td>\n",
       "      <td>235.906707</td>\n",
       "      <td>241.546951</td>\n",
       "      <td>0.225</td>\n",
       "      <td>-0.36500</td>\n",
       "      <td>6.602905e+06</td>\n",
       "      <td>15.50000</td>\n",
       "      <td>7.426829</td>\n",
       "      <td>2023.195122</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                 Open        High         Low       Close  % Change  \\\n",
       "is_quater                                                             \n",
       "0          229.153614  236.372590  223.735542  229.727711     0.770   \n",
       "1          242.878659  249.520732  235.906707  241.546951     0.225   \n",
       "\n",
       "           % Change vs Average        Volume       day     month         year  \n",
       "is_quater                                                                      \n",
       "0                      0.17994  7.437773e+06  15.86747  6.000000  2023.259036  \n",
       "1                     -0.36500  6.602905e+06  15.50000  7.426829  2023.195122  "
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.groupby('is_quater').mean()\n",
    "#prices are higher in the months which are quater end when companred with non quater months\n",
    "#The volume of trade is also less in quater end months"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "61a753ac",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1    139\n",
       "0    109\n",
       "Name: target, dtype: int64"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['open-close']=df['Open']-df['Close']\n",
    "df['low-high']=df['Low']-df['High']\n",
    "df['target']=np.where(df['Close'].shift(-1)>df['Close'],1,0)\n",
    "df['target'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "78c496d3",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAYUAAAGFCAYAAAASI+9IAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjcuMSwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy/bCgiHAAAACXBIWXMAAA9hAAAPYQGoP6dpAAAqMUlEQVR4nO3dd3hUVcIG8Hd6kknvJCQQSgDphCKICEoRy4oFG2Lb3U92bYirq+u6ru4q8u2uuivqJ3YFlRUVlKJ0aRI6QmghJKT3XqbP98fgYCCUZDJzbnl/z5MHchMnb4KZd849956jcbvdbhAREQHQig5ARETSwVIgIiIvlgIREXmxFIiIyIulQEREXiwFIiLyYikQEZEXS4GIiLxYCkRE5MVSICIiL5YCERF5sRSIiMiLpUBERF4sBSIi8mIpEBGRF0uBiIi8WApEROTFUiAiIi+WAhERebEUiIjIi6VAREReLAUiIvJiKRARkRdLgYiIvFgKRETkxVIgIiIvlgIREXmxFIiIyIulQAG3adMmXH/99UhKSoJGo8HSpUtFRyKiU1gKFHBNTU0YPHgw5s+fLzoKEZ1BLzoAqc/UqVMxdepU0TGIqA0cKRARkRdLgYiIvFgKRETkxVIgIiIvlgIREXnx6iMKuMbGRhw/ftz7fm5uLvbt24fo6GikpqYKTEZEGrfb7RYdgtRl48aNmDBhwlnH77nnHnz44YeBD0REXiwFIiLy4pwCERF5sRSIiMiLpUBERF4sBSIi8mIpEBGRF0uBiIi8ePMaKY7D6UJ1sw01TXZUNVlR02RHdZMVjVYnbA4XbE4n7E43bA4X7E6X9083AKNOC6NeC5NeB5NBC6NOC5PB836IUYdosxGxoUZEm02ICTUiPMgg+tsl6lQsBZKd2mYb8qubcbKqGfnVzcivasbJ6iaU1VtR1WhFg9WBQN19Y9RrEWM2IibUiPiwIKRGh6BbTAi6x5jRLSYEKdEhMOg4ICf54M1rJFnlDRYcLmnA4ZJ6HCmpR05FE05WNaHe4hAd7aLptBokRQahe4wZPWLN6J8UgQHJEUhPCIWeZUESxFIgSahqtGJvfi0OFNV53yoarKJj+Y1Rr0W/xDD0T47AwOQIDEiKQJ/EMBj1LAoSi6VAQlQ1WpGZW43tJ6qw/UQVsssbA3bKR6pMei2GpERiVFo0RvWIQUa3KAQZdKJjkcqwFCgg6prt2JpTyRJoB6NOi2HdIjG2Vywu6xWLQV0jodNqRMcihWMpkN8U1jRjzaEyrM4qw868ajhc/F/NF5EhBlzVNwGT+yfgivQ4jiLIL1gK1KkOFtV5iuBQGQ6X1IuOo1jBBh3Gpcdi8iWJmNgvAREhvDSWOgdLgXx2vLwRX+4pxDf7ilFU2yI6jurotRqMTIvGdYOScP3gLgjjvRPkA5YCdUhtsw3f7i/Gkj1F2F9QKzoOnRJk0GJK/0RMz0jBmJ4x0HIOgtqJpUAXzeF0YcPRCny5uxDrj5TD5nSJjkTnkRwZjJuGJeOWjK7oFmMWHYdkgqVAF1TZaMWi7flYmHlS0fcOKNnItGjcM7o7rh6QyCuY6LxYCnROWcV1+GBrHr7ZXwybg6MCJegaFYx7RnfHbSNTuG4TtYmlQK24XG6sPlSG97fmYkduteg45CehJj1uyeiK+y9LQ2pMiOg4JCEsBQIA2Bwu/HdXAd7elIOCal5BpBZaDTCxXwJmje+JYalRouOQBLAUVM7u9JTBmxtyeDmpyo3vE4c5k9IxqGuk6CgkEEtBpexOF77YVYg3NhxnGVArE/vFY/bEdAxIjhAdhQRgKaiM3enCkt2FmL+eZUDnptEAk/ol4LFJ6ejXJVx0HAogloKKrD9Shr+vOIwTFU2io5BMaDTAdYOS8NTUvkiODBYdhwKApaAC2WUN+NuKw9h0rEJ0FJKpIIMWs67oiVlX9ORCfArHUlCw2mYbXl1zDIsy87lCKXWK5MhgPDW1L64fnCQ6CvkJS0GBHE4XPtl+Eq+tzUZdi110HFKgkWnReO76S9A/iZPRSsNSUJgDhXV48sufuGw1+Z1WA9w5KhVPTe2HUJNedBzqJCwFhbDYnXh17TG8uzkXTp4qogBKigjCSzcNxPg+8aKjUCdgKShA5okqPPXVAeRW8qoiEuemYcl47rr+3PBH5lgKMtZgsePlVUfw6Y587ndMkhAXZsLfpw3AlP6JoqNQB7EUZGpLdiWeWLIfJXUW0VGIznLtoC544Vf9ERNqEh2F2omlIDM2hwv/XH0U72w+wdEBSVp8mAmv3T4EY3rGio5C7cBSkJGcikY88tleZBXzyiKSB60GeGhCLzw6MZ2b+8gES0EmvtxdiGeXHUSzzSk6ClG7jUyLxn9uH4rEiCDRUegCWAoS12xz4NmlWfhyT6HoKEQ+iQox4J/TB+Oqfgmio9B5sBQkLK+yCb/9eBeyyxtFRyHqNPdfloY/XdMXep1WdBRqA0tBorZkV+LBT/dwmQpSpFFp0XhzxjBenSRBLAUJen9LLl5ceZh3JpOiJUcGY8HdGVw/SWJYChJic7jwzNcH8MVuzh+QOgQbdHjl1sGYOrCL6Ch0CktBIioarJi1cDd2n6wRHYUooDQa4PFJ6Xjoyt6ioxBYCpJwtLQB936wg3cnk6rdODQZ824eBKOeE9AisRQE25VXjV9/tIsTykQALusVgwUzh8PMpbiFYSkItO5wGR78dA8sdpfoKESSMbhrBD68bySizEbRUVSJpSDIkt2FeOrLn7hNJlEbesWH4pNfj0SXiGDRUVSHpSDAgk05mLvqCBe0IzqP5MhgfPLrkegRFyo6iqqwFAJs7srDeHvTCdExiGQhxmzER/ePxIBk3ssQKCyFAHrh20N4f2uu6BhEshJq0uOj+0cgo1u06CiqwGu/AmTuysMsBKIOaLQ6cO/7O7G/oFZ0FFVgKQTAP74/wlNGRD5osDpw9/s7kFVcJzqK4rEU/OzVNcfwxoYc0TGIZK+uxY6Z7+3A0dIG0VEUjaXgR/PXZ+Pf67JFxyBSjOomG2a8m4mcCi4n7y8sBT9ZsCkH/1x9THQMIsWpbLTizne242RVk+goisRS8IOle4swd9UR0TGIFKus3oo738lEeQPXC+tsLIVOti2nEk8u+Yk3phH5WVFtC3794S402xyioygKS6ETHStrwAOf7IbNybWMiALhQFEdHvlsLzek6kQshU5SVm/Bve/vQIOFr1qIAmnt4XI8/22W6BiKwVLoBI1WB+79YCeKuR8CkRAf/3gS727mvUCdgaXgI6fLjd8t3I3DJfWioxCp2osrD2PVgRLRMWSPpeCjl1cdxubsStExiFTP7QYe++8+HCjkXc++YCn4YPlPxXhnM9czIpIKi92F3y3ajdpmm+gossVVUjsou6wB097YiiabU3QU2andsgh1Wz9rdUxrjkTKQwu979srC1Dzwwew5B8E4IYhJhVx0/4IfXj8OR+36ehW1G1eCHttCQyRXRA5biZC0sd4P96YtQG1P3wEt92C0EGTETXhfu/HHHVlKFv8LLrc8xq0ppDO+2ZJiPF94vD+PSOg1WpER5EdboTaAQ0WOx74ZDcLwQeG2FQk3Pbi6QPa04NWe00JShc9idBBkxA5dgY0JjPsVQXQ6M69PaO16DAql81D5OV3ISR9NJqP/YiKZfOQOON/YUrqA2dzHaq/ex0x18yGPjIR5Uuehyl1IEJ6jgAAVH3/JqKuuJeFoBAbj1bgP+uzMXtiuugossNSaCe3243H/7sfJyp5i71PtDroQqPa/FDtpo8R3HN4q1fyhsjE8z5c/a5vENR9KCJG3woAiBidAkvBQdTvWoa4Xz0JR20pNKYQmPuNAwAEpQ6CvTIf6DkCTYc2QqPTI6TPmPN9CZKZ/6zLxpCUSIzvc+7RJZ2Ncwrt9ObGHKw+VCY6huw5aopR+MbdKPy/X6Ni2TzYa0sBAG63Cy0ndkEflYSyxc+i4PUZKPl4DpqP/Xjex7MWHUFw2tBWx4LThsFadBgAoI9Ohttuha0sB86WBthKjsEY1x3OlgbUbl6E6Emz/PONkjAuNzB78T4U1jSLjiIrLIV22JlXjX+tPio6huyZuvRBzLVzEH/rC4i5+mE4m2pQuvAPcLbUw9VUB7etBfWZSxDcIwMJt/4NIemjUfH1S7DkHzjnYzqbaqAzR7Y6pjNHwtlU4/l7UChir30MlctfQenHc2AecCWCe2SgZsN7CMu4Do66MhR/8AiK3/s9mo5s8ee3TwFU22zH7xbugdXBU70Xi6ePLlKDxY7HFu8D76b3XXDP4affiQNMSX1RtOA3aDqwDiGnTu8E97oU4SOmAQCMCT1gLTqMhn2rEJQ68DyP3HpS0XMNxeljIeljWk08W/J/gr3iJKInzULxgv9B7PVPQGeOQsnHcxCUMuCskiF5OlBUh1dWH8PT1/QTHUUWOFK4SH/95hAKa1pEx1AkrTEIxtjusNcUQxcSDmh1MMSmtPocQ0wKnPUV53wMnTnKOyr4mau57pxP7G6HHdWr30L0lAfhqCmB2+VEUOpAGGK6whCdDGsJR4RK8s7mE8g8USU6hiywFC7CqgMl+HJPoegYiuV22GGvKoAuNBoanQGmxN5wVBe1+hx7dRF057kc1ZTcFy15e1sda8ndC1Ny268Oa7d9jqAeGTAl9gLcLsB1+vSC2+UAXFzUUElcbuDxL/aj0cq1yS6EpXABZfUW/Onrc5/LpvarWf8eLPkHYK8thbX4KCqWvgSXrRmhA64CAISPuglNhzejYd93sNcUo373t2g5vgNhw67xPkbl8n+h5ocPve+HZfwKlty9qNu+BPaqAtRtXwLLyX0IH37DWV/fVnESzUc2IXLsXQAAfXRXQKNFw/7VaM7ZCXtVIYxdevv3h0ABV1jTgue/4cJ5F8Kb187D7Xbj7vd3cBmLTlaxbB6shVlwNtdDFxIOU1JfRFx+F4yxqd7PafxpNeq2fwFnQxX00cmIHDsDIb0v9X689NOnoI9IQOy1j3mPNR3ZgtrNC+GoLYU+MhFR4+4+6zJTt9uNskVPIvzS6QjpNdJ7vPn4DlSveQtupx2Rl89E2OApfvwJkEgLZmZgcv/zX+KsZiyF8/hoWx6e4ysLIkWJMRvx/WPjEBtqEh1Fknj66ByKalsw7ztuqUmkNFVNNjzDU8LnxFI4h+eWZaGZy1gQKdL3WWVYy5tQ28RSaMP3WaVYe5j/wxAp2XPfZKGFL/zOwlI4Q5PVgb9yHoFI8YpqW/Cf9dmiY0gOS+EMr6w5hhJuq0mkCu9uPoHssgbRMSSFpfALB4vq8OG2PNExiChA7E43/rz0oOgYksJSOMXtduOZpQfh5OJGRKqSmVuNL3dzxYKfsRRO+WpPEfYX1IqOQUQCzF11GA0Wu+gYksBSAGCxO/FPLolNpFqVjTYs2HRCdAxJYCkAeGfTCU4uE6ncu5tzUd7A5wHVl0JloxVv8xUCkeq12J14bS0vUVV9Kcxff5zL6RIRAOC/OwuQU9EoOoZQqi6FgupmfJqZLzoGEUmEw+XGP75T9/yiqkvhX6uPwubkZipEdNp3WaXYk19z4U9UKNWWwomKRnyzv1h0DCKSoHmr1LtCsmpL4a2NOeB9akTUlszcatXu6azKUiiqbcHSfUUX/kQiUq35G46LjiCEKkthwQ85sDs5TCCic9ucXYmfCmtFxwg41ZVCZaMVi3cViI5BRDLwhgpHC6orhfe25MJi5xVHRHRhaw6V4YTK7ltQVSnUW+xY+ONJ0TGISCZcbuCdzbmiYwSUqkrhs8x8NPDuZSJqh6/2FKKiwSo6RsCophRcLjcW8e5lImonq8OFz3ao57lDNaXwQ3YF8qubRccgIhlavLMALpXc2KSaUli0nXMJRNQxRbUt2HC0XHSMgFBFKRTVtmD9EXX8gxKRf6jl9LMqSuHTzJNc0oKIfLLxaDmKaltEx/A7xZeC3enC4p3clJuIfONyA5+rYMJZ8aXwfVYpKhvVczkZEfnP4p0FcCh8uX3Fl8JXe7jwHRF1jvIGK9YpfH5S0aVQ02TD5uwK0TGISEG+2afsfVgUXQorD5ZwNVQi6lTrj5Sj2abclREUXQpKb3QiCrwWuxNrDpWJjuE3ii2F0joLduZVi45BRAr07f4S0RH8RrGlsPynYt6bQER+selYBepa7KJj+IViS2EZTx0RkZ/YnC6szioVHcMvFFkK+VXNOFBUJzoGESnYtz8p8xSSIkth/RHlTgIRkTRsO16JeovyTiEpshQ2HOW9CUTkXw6XG1uzK0XH6HSKKwWL3YntJ6pExyAiFfjhmPJegCquFLblVMLqUPbaJEQkDSwFGdjIU0dEFCAldRYcLW0QHaNTKa4U1LI7EhFJww/HlPWco6hSOF7eiIJq5W+CQUTSobRTSIoqha3HlXclABFJ287cGkUtkKeoUuBaR0QUaDanC3tO1oqO0WkUVQp7TtaIjkBEKrRbQc89iimF4toWFNdZRMcgIhXak89SkBwlNTURycve/Bq43cpYlpmlQETko3qLAzkVjaJjdArFlMKuk5xkJiJxlDLZrIhSaLY5cKREWXcVEpG8KOVshSJKIau4Hg5us0ZEAillslkRpXBEYWuPEJH85FQ0wmJ3io7hM0WUwjGWAhEJ5nJDEZPNiiiFo2UsBSISL7uMpSAJ2SwFIpKA7HL5PxfJvhTK6y2oaVbePqlEJD/HOFIQj6eOiEgqlHDWQv6lwElmIpKI/Opm2V+BJPtSyK1sEh2BiAiAMq5Akn0pFNVypzUiko6C6mbREXwi+1IoqeVy2UQkHcUyf06SfSkUc6RARBJSWs9SEKbBYkeDVTl7oxKR/JXIfLMvWZeC3IdpRKQ8JTI/eyHzUpD3D5+IlIcjBYGK61gKRCQt5Q0WuGS8lL+sS6Gs3io6AhFRK3anG5WN8n1uknUp1DbbREcgIjpLVZN8n5tkXgpcCI+IpKdRxldFyrsUWlgKRCQ9jRaWghD1LAUikiA53z8l61JokvEPnoiUiyMFQVgKRCRFjVb5nsWQdSnIeTKHiJSrgSMFMVpkvpkFESkTS0EQGd80SEQKZnXI9wWrzEuBrUBE0uOU8StWWZcCO4GIpEjGnSDvUiAikiI5L4inFx2go9wcJlAn0Glc+H3Xk5hh/AERlmLRcUghbGGTAAwRHaNDZFsKMi5ikoB+oc14pstOXFq3EvqKAtFxSGGCUwaLjtBhsi0FjhSovX4eFdxl2ID40o3QFMj3skGSOK1OdIIOk20paDQa0RFIJvqHNeFPibswqnYF9BWFouOQGmhl+9Qq31LQaTUw6rSwOV2io5AE6TQuPJiShxn6DYgv/YGjAgosloIYZpMOtmaWAp12elSwHPryItFxSK00PH0khNmkRw032lE9ncaFh7rmYYZhPeJKfoCmQL53k5JC6AyiE3SYrEsh1CTr+OSjgWFNeDpxJ0bWroC+gqMCkpDgKNEJOkzWz6pmloLq6DQuPJyShxn69YjlqICkyhwnOkGHyfpZNcQo3/N21D6tRgWcKyCpYymIwdNHyqbTuPBISh7u5KiA5CaUpSAES0GZBoU34umEXRjBUQHJFUcKYsSFmURHoE5i0LrxcNcTuEO3HrGlmzgqIHljKYiRGBEkOgL5yDMq2IkRtSs5KiBlMIYBhmDRKTpM1qWQEM5SkCOD1o1HUk7gDu06xJRu5qiAlMUcKzqBT2RdCoksBVkZEt6IpxJ2YETNSujKuEw1KZSMTx0Bci8Fnj6SPIPWjUe65uAO/XrElGyCpoDLkpDCsRTEiQ01QafVyHo/VKUacmquYHjNcujKS0THIQocGV+OCsi8FHRaDeJCTSitt4iOQvCMCh7tmoPbdT/PFXBUQCrEkYJYiRFBLAXBhkU04o/xOzC8ZgVHBURhXUQn8InsSyEt1ox9BbWiY6iOQevGoyk5uEO7DtEcFRCdFt9PdAKfyL4UesWHio6gKsMiGvBU/A5kVK+ArqxUdBwi6Ym/RHQCn8i+FHrGsRT8zaR14ZGUHNyuXc9RAdH5hCcDwZGiU/hE9qXQO4Gl4C8cFRC1k8xPHQEKKIVu0SEw6DSwO3lZamcwaV14NCUHt2nXIbp0C0cFRO0h81NHgAJKQa/TonuMGdnljaKjyNqwiAY8HZ+JYdUrOSog6qiE/qIT+Ez2pQB4JptZCu1n0rowOyUHt2nWIqpsK0cFRL7iSEEaeieEYdVBvrq9WMMjGvBU/HYMrV4JXVmZ6DhEyqDVA3F9RKfwmSJKYWByhOgIkmfSuvBYynHcql2HqFKOCog6XXRPQC//PV4UUQpDUyNFR5CskZH1+GNcJoZUr4CurFx0HCLlSpD/qSNAIaUQG2pC16hgFNa0iI4iCSatC3NSjmO6Zu2pUQGvzCLyOwXMJwAKKQUAGJoapfpS4KiASCCWgrQMTYnEt/vVt3FLkNaJOak5mI41iCzdxlEBkRAaIGWU6BCdQjmloLJ5hVGR9XgybjuGVK+ErpSjAiKh4i+R/T4KP1NMKfRPioBRr4XNodyraoJ1TjyWchzTsZajAiIp6TFedIJOo5hSMOq1GJAUjj35taKjdLrRUXV4InY7hlSthLa0QnQcIjpTjytEJ+g0iikFALisV6xiSiFY58SclGzcgnUcFRBJmdYAdLtMdIpOo6hSGJceh9fXHxcdwyeeUUEmhlQth7a0UnQcIrqQrsMBk3JWa1ZUKQxNiUSYSY8Gq0N0lHYJ1jnxeMpx3II1iCj9kaMCIjlR0HwCoLBS0Ou0GN0zBqsPyWM9n9FRdXgydjsGV63gqIBIrlgK0jYuPU7SpRCsc+IPKdm4GWs5KiCSO2MYkDxcdIpOpbhSuCJdmtcKXxZVhydif8SgqpUcFRApRffLAJ2ynkaV9d0ASIkOQVqsGbmVTaKjwKxzYU7qUdzsXouI0u0cFRApjcJOHQEKLAXAM1oQWQpjo+vwRMw2DKxcBW0JRwVEisVSkIepAxLx4ba8gH5Ns86Fx1OP4mbXGoSXZULTzFEBkaJFpgLx/USn6HSKLIUR3aOREG5CWb3V71+LowIilRo4XXQCv1BkKWi1Gkwd0MVvowWzzoU/pBzFTW6OCohUa9DtohP4hSJLAQCuG9T5pTAuuhaPx/yIgZUroS2t6tTHJiIZ6TIEiEsXncIvFFsKGd2i0CUiCCV1Fp8ex6xz4YnUo7jRtQYRZduB5k4KSETyNeg20Qn8RrGloNF4TiG9vzW3Q//9FTE1eDz6RwyoXAVtCUcFRHSKRgcMvEV0Cr9RbCkAwLWD2lcKZr0TT6YcxTTXGkSUZQLib3UgIqnpMR4IjRedwm8UXQrDUiORGh2C/Orzn/M5PSpYCW1JdYDSEZEsKfjUEaDwUtBoNJie0RX/WnPsrI/9PCq48dR9BRwVENEFGcxAv+tEp/ArRZcCAEwfnoLX1mXD6fJcNjo+ugaPx2xD/8pVHBUQUfv0vRYwmkWn8CvFl0JiRBCu6ReFEc2bMc21BuFlO3gFERF1jMJPHQGAxu12K//Oq6PfAZ8p/x+TiPzIHA88fgTQ6kQn8Sut6AAB0XsyEJEqOgURydnQGYovBEAtpaDVAsPvE52CiORKZwJGzRKdIiDUUQoAMOxuzz8sEVF7DboVCEsUnSIg1FMK5lig/zTRKYhIdjTAZY+KDhEw6ikFABjxW9EJiEhu+lwDxPYWnSJg1FUKKSOA1DGiUxCRnKholACorRQAYMLTohMQkVykjAJSR4lOEVDqK4W0cUC3saJTEJEcqGyUAKixFACOFojowmLTPfMJKqPOUug+Fuh+uegURCRlYx4GNBrRKQJOnaUAABP+JDoBEUlVaKJi92C+EPWWQrcxQNoVolMQkRRdOgvQG0WnEEK9pQBwtEBEZwvvqpolLdqi7lJIvRToMUF0CiKSkol/BQzBolMIo+5SADhaIKLTuo4ABt4iOoVQLIWUkUCviaJTEJFwGmDKXFVecfRLLAUAuPLPgIY/CiJVG3CzZykcleMzIQAkDQUyuN8CkWrpg4FJz4tOIQkshZ9NfM6z3R4Rqc+Yh4CIrqJTSAJL4WdBEcCUl0SnIKJAC+sCjH1MdArJYCn80qDpQI/xolMQUSBd+SxgNItOIRkshTNd+wq37SRSiy5DgCF3ik4hKSyFM8X05FCSSC2u5iWoZ2IptOXyOUBML9EpiMifRvzGswYatcJSaIveBFz7L9EpiMhfonsCk/4mOoUksRTOpcd4YOB00SmIqLNpdMCNbwPGENFJJImlcD5TXvJcqkqKN3ezFZrn6zH7O0ubH3/g2xZonq/Ha9utF3ysLw/ZcckbjTD9vR6XvNGIrw/bW3180U92pLzagOh59Xhideuvl1frQvrrjai3ujv+zdD5jX2Mdy6fB0vhfELjgatfFp2C/GxnkRML9tgwKKHtX4elR+zILHIiKezCE5I/Fjhw25IWzBxkwP5ZZswcZMCtS1qQWegAAFQ2u/Cbb1vwz0lB+P4uMz7ab8eKY6dL43crWvDyRBPCTZz89IvEQcD4p0SnkDSWwoUMuVO1OzCpQaPNjRlfteCd64MRFXT2E3FRvQsPrbRg0U3BMFzEb8trmTZM6qnD05eb0DfW8+dVaTq8lmkDAJyocSPCpMFtAwwYkazDhDQdDlW4AACfHrDDqNPgpn6GTv0e6RSdCbhpAaDjz/d8WAoX47pXgJjeolOQHzy40oJre+sxsYf+rI+53G7M/LoFT4wxon+87qIe78cCJyaf8VhTeuqxrcAJAOgdrUWz3Y29JU5Ut7ixs8iJQQk6VLe48ZcNFsyfGuT7N0Vtu+pZIL6f6BSSx1K4GEYzMP1DQM9fWCX5/KAde0qcmDux7ZsV522xQa8FHhl18dsylja6kRDa+tcqIVSL0kbPHEFUsAYfTQvG3UtbMPKdRtw92IApvfT4w2oLHh5pRG6tC0PfbsSANxux5JC9rS9BHdFtLHDpg6JTyMLZL4+obYkDPDe6LOeNbUpQUOfCo99ZsPquEATpzz5ttLvYiX9n2rDnATM07by56czPdrtbH7uxnwE3/uIU0cY8Bw6UOzH/miD0+k8jPrs5GImhGox8twnjuukQb+ZrN58Yw4Ab3wK0/DleDJZCewy/H8jdDGR9JToJ+Wh3iRPlTW5kLGjyHnO6gU0nnZi/w4Z5E00ob3Ij9dXGVh9/fLUVr223IW92WJuPmxiqQWmjq9Wx8iYXEkLbLharw43fr7Bg4U3BOF7tgsMFXNHd82uZHqNFZqET1/fhk5lPpr4MRKaKTiEbLIX2uv7fQPFeoCZXdBLywVVpehz4XetF0O5b1oK+sTr88TIjuoRqMKXXGXMDC5sxc5AB9w0590Tl6BQd1pxw4rHRp4+tPuHAmJS25yT+tsmKqb30GNZFh70lTjhcpy9FtTs9RUQ+uGQaMPQu0SlkhaXQXkHhnvmF9yYBTpvoNNRBYSYNBpwxeWw2aBATfPp4zBn3Nhm0npFAn9jT/93dX7cgOUyDuRM9802PjjJi3AfNmLfFihv66rHsiANrTzix5b6zb5TKKndicZYD+x7wlFPfWC20Gg3e22NDYqgGRypdGJF0cRPc1Ib4/sC0N0WnkB2WQkckDQEm/x1Y9aToJCRYfp0L2l9s5TomRY/PbwnGn9db8ewGK3pGa7H4lmCM6tr6V83tduN/llvw6hQTzEbPqaVggwYfTgvCgystsDqA+dcEITmcp446JCgSuH0Rl8TuAI3b7eYAtaM+nwEcWS46BRH9kkYLzPgC6DVRdBJZ4ssQX9zwhmdhLSKSjqv+wkLwAUvBF8GRwF1fAuY40UmICAAG3ML9UHzEUvBVdBpw538BA89dEgmVMooTy52ApdAZkod5rkjSct6eSIjIbsDtn3r2QiGfsBQ6S/pk4LpXRacgUh9ThGdi2RwrOokisBQ607C7gSu4LC9RwGj1wK0fAXF9RCdRDJZCZ5vwNDB0pugURMqn0QK/mg/0nCA6iaKwFPzhuteAXpNEpyBSMI1nyZkhd4gOojgsBX/QnRrSdhkiOgmRAmk883fD7hYdRJFYCv5iNHsmv6K6i05CpCzX/AMYfp/oFIrFUvCn0Hjgnm+B6B6ikxApw9XzgJG/FZ1C0VgK/haZCtz3HRDHbQCJfDLlJeDSWaJTKB5LIRDCEoD7VnKOgaijJj4PjOZ2moHAUgiUkGjPqaTU0Rf+XCI67cpngbGzRadQDZZCIAWFA3d9BfTgddVEF2X808C4P4hOoSrcT0EEhxX44j7g6ArRSYgkSgNc+WcWggAsBVGcDmDpLODAF6KTEEmLzuRZ7XTgLaKTqBJLQSSXC1g+G9jzkegkRNIQEgPc/hmQOkp0EtViKUjB6j8D214XnYJIrNh0z94k0Wmik6gaS0Eq9i4Els8BnFbRSYgCL20ccOsnnt0MSSiWgpQU7QYWzwTqi0QnIQqcoXd5FpHUGUQnIbAUpKexAvjiHuDkVtFJiPxMA1z1F+DyOaKD0C+wFKTI6QC+/xOw423RSYj8Qx8M3Ph/QP9popPQGVgKUrbvM8/VSQ6L6CREnSesC3DbQqDrcNFJqA0sBakr3gt8fhdQXyg6CZHv+l4H/Op1z7IvJEksBTloqgS+uBfI2yw6CVHHGEKAKS8Cw+8XnYQugKUgF04HsPY54Mc3APCfjGQkcSBw8/tAXLroJHQRWApyk7cFWPYgUJMnOgnRBWg8y11f9RygN4oOQxeJpSBHtiZg7V+BHe+AowaSpNBE4Ma3gJ5Xik5C7cRSkLO8LcCyh4CaXNFJiE5Lnwrc8AZgjhGdhDqApSB3tuZTo4YF4KiBhNIHA1P+Doz4jegk5AOWglLkbT0118BRAwnQezJw9ctATE/RSchHLAUlsTUD654HMt8GRw0UEFFpnjLoc7XoJNRJWApKdHIb8M3DQNVx0UlIqQwhwNg5wGWPAHqT6DTUiVgKSuW0e65O+mEeYKkVnYaU5JIbgMkvApEpopOQH7AUlK65Gtj4MrDrPcDlEJ2G5Cy2D3DN/wI9xotOQn7EUlCLymzPDm/HvhOdhOTGGAaM/yMwahb3PFABloLa5G31TEYXZIpOQlKnNQCDbweufBYISxCdhgKEpaBWR78D1v8NKDsoOglJjT4IGDoTuOxRzhuoEEtBzVwu4OCXwIYXeX8DAcZQYPh9wOiHOTJQMZYCAS4ncPhbYPtbQMF20Wko0IIigJEPAJf+jvscEEuBzlC021MOWUsBl110GvKnkFhg9O+BEb8FgsJFpyGJYClQ2+qLPfc57P4QaKkWnYY6U1gSMOZhIONewBgiOg1JDEuBzs/eAuz/3DN6qDwqOg11lEYH9LoKGDID6HMN9zegc2Ip0MVxu4GcdZ5yOL4OXFtJJmJ6eYpg8B1AeBfRaUgGWArUftW5QNZXwMGvgbIDotPQmYxhQP9pnstKU0eJTkMyw1Ig31RmA1lfAwe/AioOi06jYhqg+1jPqOCSGzhXQB3GUqDOU37YUw5ZX3GF1kBJHOiZIxh8BxCdJjoNKQBLgfyj5CfPCCLrK6AmT3Qa5QiKBHpOAHpN8kwchyWKTkQKw1Ig/ys94NlPOm+LZ68HXuLaDhqgy2Cg9yRPEXQdDmh1okORgrEUKLDcbs9pppNbT5XEVqCpQnQqaQmOBnpe6SmCnlcBoXGiE5GKsBRIvIpjwMktnhVcT24FGkpEJwocrQFI6A8kDwOShnn+jOsHaLWik5FKsRRIeqpPAGVZQOUxz9VNlceAyuOAtU50Mt8Yw4CES4D4SzxFkDTUM1HM7SxJQlgKJB8NpacK4pdlkQ3UFUISN9NptIA5zjP5G5bk+TOi6+kSiEwFNBrRKYnOi6VA8mdrBmrzPRPYLTWn3mp/8fdfvFlOHbfUw1skGi2g1Z96M3gmcrV6zy5jP/9dawB0RsAcc/oJP/zUn2FdPG+hCYBOL/AHQeQ7lgKpk8vpedMZ+Oqd6BdYCkRE5MVLHIiIyIulQEREXiwFIiLyYikQEZEXS4FIQt58802kpaUhKCgIGRkZ2Lx5s+hIpDIsBSKJWLx4MWbPno1nnnkGe/fuxeWXX46pU6ciPz9fdDRSEV6SSiQRo0aNwrBhw/DWW295j/Xr1w/Tpk3D3LlzBSYjNeFIgUgCbDYbdu/ejcmTJ7c6PnnyZGzbtk1QKlIjlgKRBFRWVsLpdCIhIaHV8YSEBJSWlgpKRWrEUiCSEM0ZS2643e6zjhH5E0uBSAJiY2Oh0+nOGhWUl5efNXog8ieWApEEGI1GZGRkYM2aNa2Or1mzBmPGjBGUitSI6/wSScScOXMwc+ZMDB8+HKNHj8aCBQuQn5+PWbNmiY5GKsJSIJKI2267DVVVVXjhhRdQUlKCAQMGYOXKlejWrZvoaKQivE+BiIi8OKdAREReLAUiIvJiKRARkRdLgYiIvFgKRETkxVIgIiIvlgIREXmxFIiIyIulQEREXiwFIiLyYikQEZEXS4GIiLxYCkRE5MVSICIiL5YCERF5sRSIiMiLpUBERF4sBSIi8mIpEBGRF0uBiIi8WApEROTFUiAiIi+WAhERebEUiIjIi6VAREReLAUiIvJiKRARkRdLgYiIvFgKRETkxVIgIiKv/wcWAvs6WH8A7wAAAABJRU5ErkJggg==",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.pie(df['target'].value_counts().values,labels=[1,0],autopct='%1.1f%%')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "a1541d76",
   "metadata": {},
   "outputs": [],
   "source": [
    "df['days']=range(248)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "a620538d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
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
       "      <th>Open</th>\n",
       "      <th>Close</th>\n",
       "      <th>% Change</th>\n",
       "      <th>Volume</th>\n",
       "      <th>days</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Open</th>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.993732</td>\n",
       "      <td>-0.076568</td>\n",
       "      <td>0.308018</td>\n",
       "      <td>0.957838</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Close</th>\n",
       "      <td>0.993732</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.026446</td>\n",
       "      <td>0.352648</td>\n",
       "      <td>0.957348</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>% Change</th>\n",
       "      <td>-0.076568</td>\n",
       "      <td>0.026446</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.474604</td>\n",
       "      <td>-0.024339</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Volume</th>\n",
       "      <td>0.308018</td>\n",
       "      <td>0.352648</td>\n",
       "      <td>0.474604</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.287858</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>days</th>\n",
       "      <td>0.957838</td>\n",
       "      <td>0.957348</td>\n",
       "      <td>-0.024339</td>\n",
       "      <td>0.287858</td>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "              Open     Close  % Change    Volume      days\n",
       "Open      1.000000  0.993732 -0.076568  0.308018  0.957838\n",
       "Close     0.993732  1.000000  0.026446  0.352648  0.957348\n",
       "% Change -0.076568  0.026446  1.000000  0.474604 -0.024339\n",
       "Volume    0.308018  0.352648  0.474604  1.000000  0.287858\n",
       "days      0.957838  0.957348 -0.024339  0.287858  1.000000"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df[['Open','Close','% Change','Volume','days']].corr()\n",
    "#Correlation analysis measures the strength of the realtionship between two variables\n",
    "#The correlation between close and volume is lesser than with days column"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "67509294",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<Axes: xlabel='days', ylabel='Close'>"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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Z7t4niZnu7SlLRJhk2uXL5rSmblJDXZmz57N//t//4/nn3+e559/nosvvph3vvOdpYDmtttu4/bbb+db3/oWzz33HA0NDVx22WX09vaWXmPFihU89NBDPPjggzz11FNkMhne/va347ruZH0sIYSYdvK2y67uHN39U5DTOZuvPbKRTz/4Mm/sy5auq44F+ce3LeH//dVSZlVFeWlHN3es2si2zgzJSABXa7TWOK6mvTdP1naIBE0aKsJkLJe7V2/B6z8W8zzN2l0pVm/sYO2uVOlxceQta65j5ZVLWdKYJGs5tGcsspbDksbklG87B1BaD55hOblqamr46le/ykc/+lGamppYsWIFX/jCFwA/izNz5kxuvfVWrrnmGlKpFPX19dx33328973vBaC1tZU5c+bw8MMPc8UVV4zoPdPpNJWVlaRSKSoqpm4aTgghjjTP0+zrK9Cb99vJtdb8/vV27np8C93Z8u3kf3lKI584fyGJiF8hYSrFzQ+tZePeXhoqInRlC+zpyZd1Z5mGYm5NlEQ4SM52yVoOd//tGazdneKBZ3fQnrb8oYQKGioivO/suVx99twpnUWYzqbaBOWRfn9PmZod13X52c9+Rl9fH+eddx7btm2jra2Nyy+/vHRNOBxm+fLlrFmzhmuuuYYXXngB27bLrmlqauKkk05izZo1Bwx2LMvCsqzSr9Pp9MR9MCGEOEplCw6dvQUczz+e2t2d487HNvHC9vIC5AV1cT57aQsnzfILkLX2pyVvbO9l094MVbEgfQXXD1z6f6b49eh6ml3dOWZXK2JBk46Cy6cffIld3Tk8T1MsD1Eo9vUV+NdfreMnz+3g5rcumfLZhOnIMNSUbS8/mEkPdtauXct5551HPp8nkUjw0EMPccIJJ7BmzRoAZs6cWXb9zJkz2b59OwBtbW2EQiGqq6uHXNPW1nbA97zlllv48pe/PM6fRAghpgfX0+zrs8jk/XbyguPxk+d38uOnt2O7+/My4YDBB8+bx3vOmE2gvy35tdY0Dzy3g20dffRZLr2WTZ9l4wHewIOEYrSj/WxBR69FRTRAb96mz3JAawIG2KUyIE1A+de+tifNjT/7M//+7pM5v6V+wn8/xNFv0oOd4447jpdffpmenh7++7//mw996EOsXr269PzgAUZa60NuvT3UNTfffDM33nhj6dfpdJo5c+aM8RMI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mWeeCfqd6upq2e12HTp0SJK0bNkypaWlyeVyyev16vHHHw/PyQEIKcoOgD5h8eLFKi0tVUlJiT788EOVlZVp3759gf1+v1/Lly/Xl19+qR07dujIkSOaNWuWJMlms2n27NkqKioKesyNGzdq0qRJGjZsmN544w09++yzWrdunWpqarRjxw5lZmaG8xQBhAifeg7gitfQ0KCkpCRt2bJFeXl5kqSff/5ZKSkpmjdvnp577rlOv1NRUaGxY8fK5/MpLi5OtbW1Sk1NVXl5ucaOHavW1lYNHTpUK1euVH5+vlavXq1169apurpaDocjzGcIIJS4sgPginfo0CH5/X6NHz8+sC0xMVEjRowI/FxZWanp06crPT1d8fHxysnJkSQdO3ZMkuTxeHTPPfdo48aNkqS3335b586d08yZMyVJM2fOVHNzs6699lrNnTtXJSUlamtrC9MZAgglyg6AK153F6AbGxuVm5uruLg4bd26VRUVFSopKZF0/uWtCx5++GEVFxerublZRUVFysvLU//+/SVJqampOnDggNauXauYmBg9+uijys7OVmtra+hODEBYUHYAXPGGDx8uh8OhvXv3BradPn1aBw8elCR9++23OnnypAoLCzVp0iSNHDkysDj5H919992KjY3VSy+9pPfee0+zZ88O2h8TE6Np06bp+eefV1lZmT7//HNVVVWF9uQAhFx0pAcAAN2Ji4vTnDlztHjxYiUlJSk5OVlLliyR3X7+77W0tDQ5nU698MILmj9/vqqrq7V8+fJOjxMVFaVZs2bpqaee0vDhw4NeFtu0aZPa29s1btw49e/fX6+88opiYmKUnp4etvMEEBpc2QHQJ6xcuVLZ2dmaNm2a7rjjDk2cOFFZWVmSpMGDB2vTpk16/fXXdcMNN6iwsLDT28wvmDNnjvx+f6erOgMHDtT69et122236aabbtLHH3+st956S0lJSSE/NwChxbuxAFxVPvvsM+Xk5OjEiRNKTk6O9HAAhAFlB8BVoaWlRcePH9e8efPk8Xi0bdu2SA8JQJjwMhaAq8Krr76qESNG6MyZM1qxYkWkhwMgjLiyAwAALI0rOwAAwNIoOwAAwNIoOwAAwNIoOwAAwNIoOwAAwNIoOwAAwNIoOwAAwNIoOwAAwNL+HwlPnFQtoOcxAAAAAElFTkSuQmCC",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "#Positive Linear relationship \n",
    "sns.regplot(x='days',y='Close',data=df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "23fbe298",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Linear Regression"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "ece06757",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<style>#sk-container-id-1 {color: black;}#sk-container-id-1 pre{padding: 0;}#sk-container-id-1 div.sk-toggleable {background-color: white;}#sk-container-id-1 label.sk-toggleable__label {cursor: pointer;display: block;width: 100%;margin-bottom: 0;padding: 0.3em;box-sizing: border-box;text-align: center;}#sk-container-id-1 label.sk-toggleable__label-arrow:before {content: \"▸\";float: left;margin-right: 0.25em;color: #696969;}#sk-container-id-1 label.sk-toggleable__label-arrow:hover:before {color: black;}#sk-container-id-1 div.sk-estimator:hover label.sk-toggleable__label-arrow:before {color: black;}#sk-container-id-1 div.sk-toggleable__content {max-height: 0;max-width: 0;overflow: hidden;text-align: left;background-color: #f0f8ff;}#sk-container-id-1 div.sk-toggleable__content pre {margin: 0.2em;color: black;border-radius: 0.25em;background-color: #f0f8ff;}#sk-container-id-1 input.sk-toggleable__control:checked~div.sk-toggleable__content {max-height: 200px;max-width: 100%;overflow: auto;}#sk-container-id-1 input.sk-toggleable__control:checked~label.sk-toggleable__label-arrow:before {content: \"▾\";}#sk-container-id-1 div.sk-estimator input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-1 div.sk-label input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-1 input.sk-hidden--visually {border: 0;clip: rect(1px 1px 1px 1px);clip: rect(1px, 1px, 1px, 1px);height: 1px;margin: -1px;overflow: hidden;padding: 0;position: absolute;width: 1px;}#sk-container-id-1 div.sk-estimator {font-family: monospace;background-color: #f0f8ff;border: 1px dotted black;border-radius: 0.25em;box-sizing: border-box;margin-bottom: 0.5em;}#sk-container-id-1 div.sk-estimator:hover {background-color: #d4ebff;}#sk-container-id-1 div.sk-parallel-item::after {content: \"\";width: 100%;border-bottom: 1px solid gray;flex-grow: 1;}#sk-container-id-1 div.sk-label:hover label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-1 div.sk-serial::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: 0;}#sk-container-id-1 div.sk-serial {display: flex;flex-direction: column;align-items: center;background-color: white;padding-right: 0.2em;padding-left: 0.2em;position: relative;}#sk-container-id-1 div.sk-item {position: relative;z-index: 1;}#sk-container-id-1 div.sk-parallel {display: flex;align-items: stretch;justify-content: center;background-color: white;position: relative;}#sk-container-id-1 div.sk-item::before, #sk-container-id-1 div.sk-parallel-item::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: -1;}#sk-container-id-1 div.sk-parallel-item {display: flex;flex-direction: column;z-index: 1;position: relative;background-color: white;}#sk-container-id-1 div.sk-parallel-item:first-child::after {align-self: flex-end;width: 50%;}#sk-container-id-1 div.sk-parallel-item:last-child::after {align-self: flex-start;width: 50%;}#sk-container-id-1 div.sk-parallel-item:only-child::after {width: 0;}#sk-container-id-1 div.sk-dashed-wrapped {border: 1px dashed gray;margin: 0 0.4em 0.5em 0.4em;box-sizing: border-box;padding-bottom: 0.4em;background-color: white;}#sk-container-id-1 div.sk-label label {font-family: monospace;font-weight: bold;display: inline-block;line-height: 1.2em;}#sk-container-id-1 div.sk-label-container {text-align: center;}#sk-container-id-1 div.sk-container {/* jupyter's `normalize.less` sets `[hidden] { display: none; }` but bootstrap.min.css set `[hidden] { display: none !important; }` so we also need the `!important` here to be able to override the default hidden behavior on the sphinx rendered scikit-learn.org. See: https://github.com/scikit-learn/scikit-learn/issues/21755 */display: inline-block !important;position: relative;}#sk-container-id-1 div.sk-text-repr-fallback {display: none;}</style><div id=\"sk-container-id-1\" class=\"sk-top-container\"><div class=\"sk-text-repr-fallback\"><pre>LinearRegression()</pre><b>In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook. <br />On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.</b></div><div class=\"sk-container\" hidden><div class=\"sk-item\"><div class=\"sk-estimator sk-toggleable\"><input class=\"sk-toggleable__control sk-hidden--visually\" id=\"sk-estimator-id-1\" type=\"checkbox\" checked><label for=\"sk-estimator-id-1\" class=\"sk-toggleable__label sk-toggleable__label-arrow\">LinearRegression</label><div class=\"sk-toggleable__content\"><pre>LinearRegression()</pre></div></div></div></div></div>"
      ],
      "text/plain": [
       "LinearRegression()"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from sklearn.linear_model import LinearRegression\n",
    "lm=LinearRegression()\n",
    "lm"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "ed63e097",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<style>#sk-container-id-2 {color: black;}#sk-container-id-2 pre{padding: 0;}#sk-container-id-2 div.sk-toggleable {background-color: white;}#sk-container-id-2 label.sk-toggleable__label {cursor: pointer;display: block;width: 100%;margin-bottom: 0;padding: 0.3em;box-sizing: border-box;text-align: center;}#sk-container-id-2 label.sk-toggleable__label-arrow:before {content: \"▸\";float: left;margin-right: 0.25em;color: #696969;}#sk-container-id-2 label.sk-toggleable__label-arrow:hover:before {color: black;}#sk-container-id-2 div.sk-estimator:hover label.sk-toggleable__label-arrow:before {color: black;}#sk-container-id-2 div.sk-toggleable__content {max-height: 0;max-width: 0;overflow: hidden;text-align: left;background-color: #f0f8ff;}#sk-container-id-2 div.sk-toggleable__content pre {margin: 0.2em;color: black;border-radius: 0.25em;background-color: #f0f8ff;}#sk-container-id-2 input.sk-toggleable__control:checked~div.sk-toggleable__content {max-height: 200px;max-width: 100%;overflow: auto;}#sk-container-id-2 input.sk-toggleable__control:checked~label.sk-toggleable__label-arrow:before {content: \"▾\";}#sk-container-id-2 div.sk-estimator input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-2 div.sk-label input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-2 input.sk-hidden--visually {border: 0;clip: rect(1px 1px 1px 1px);clip: rect(1px, 1px, 1px, 1px);height: 1px;margin: -1px;overflow: hidden;padding: 0;position: absolute;width: 1px;}#sk-container-id-2 div.sk-estimator {font-family: monospace;background-color: #f0f8ff;border: 1px dotted black;border-radius: 0.25em;box-sizing: border-box;margin-bottom: 0.5em;}#sk-container-id-2 div.sk-estimator:hover {background-color: #d4ebff;}#sk-container-id-2 div.sk-parallel-item::after {content: \"\";width: 100%;border-bottom: 1px solid gray;flex-grow: 1;}#sk-container-id-2 div.sk-label:hover label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-2 div.sk-serial::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: 0;}#sk-container-id-2 div.sk-serial {display: flex;flex-direction: column;align-items: center;background-color: white;padding-right: 0.2em;padding-left: 0.2em;position: relative;}#sk-container-id-2 div.sk-item {position: relative;z-index: 1;}#sk-container-id-2 div.sk-parallel {display: flex;align-items: stretch;justify-content: center;background-color: white;position: relative;}#sk-container-id-2 div.sk-item::before, #sk-container-id-2 div.sk-parallel-item::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: -1;}#sk-container-id-2 div.sk-parallel-item {display: flex;flex-direction: column;z-index: 1;position: relative;background-color: white;}#sk-container-id-2 div.sk-parallel-item:first-child::after {align-self: flex-end;width: 50%;}#sk-container-id-2 div.sk-parallel-item:last-child::after {align-self: flex-start;width: 50%;}#sk-container-id-2 div.sk-parallel-item:only-child::after {width: 0;}#sk-container-id-2 div.sk-dashed-wrapped {border: 1px dashed gray;margin: 0 0.4em 0.5em 0.4em;box-sizing: border-box;padding-bottom: 0.4em;background-color: white;}#sk-container-id-2 div.sk-label label {font-family: monospace;font-weight: bold;display: inline-block;line-height: 1.2em;}#sk-container-id-2 div.sk-label-container {text-align: center;}#sk-container-id-2 div.sk-container {/* jupyter's `normalize.less` sets `[hidden] { display: none; }` but bootstrap.min.css set `[hidden] { display: none !important; }` so we also need the `!important` here to be able to override the default hidden behavior on the sphinx rendered scikit-learn.org. See: https://github.com/scikit-learn/scikit-learn/issues/21755 */display: inline-block !important;position: relative;}#sk-container-id-2 div.sk-text-repr-fallback {display: none;}</style><div id=\"sk-container-id-2\" class=\"sk-top-container\"><div class=\"sk-text-repr-fallback\"><pre>LinearRegression()</pre><b>In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook. <br />On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.</b></div><div class=\"sk-container\" hidden><div class=\"sk-item\"><div class=\"sk-estimator sk-toggleable\"><input class=\"sk-toggleable__control sk-hidden--visually\" id=\"sk-estimator-id-2\" type=\"checkbox\" checked><label for=\"sk-estimator-id-2\" class=\"sk-toggleable__label sk-toggleable__label-arrow\">LinearRegression</label><div class=\"sk-toggleable__content\"><pre>LinearRegression()</pre></div></div></div></div></div>"
      ],
      "text/plain": [
       "LinearRegression()"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x=df[['days']]\n",
    "y=df[['Close']]\n",
    "lm.fit(x,y)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "c99a1600",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.9165143869659251"
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "lm.score(x,y)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
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
   "version": "3.11.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
