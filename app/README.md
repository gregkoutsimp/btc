## Bitcoin Price Chart

#### Introduction 

This repositiry contains the source code of the Image for the Bitcoin Price Chart, available on Docker Hub as `gregkoutsimp/btc`.

#### Dependecies 

The Image created by the source code is part of a multi-container application. 
Data are stored in a MongoDB instance. 
It is strongly recomended to be used as part of the multi-container application and not independently.


#### API

##### /daily
Returns the daily valatily of Bitcoin price using the opening price and the current price. Also display the current price.

##### /statistics 
Returns the highest and lowest price of Bitcoin during the last 30 days and the day they occur.

##### /monthly 
Returns a plot of the Bitcoin price during the last 30 days.














