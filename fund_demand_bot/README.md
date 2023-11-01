# demand zone funding rate algo

overview
when the price gets to a demand zone, we are going to check the funding rate and if the funding rate is below -5 (test this) then we will buy. if the funding rate is positive still, we wont buy that demand zone, we will wait until we are at a new demand zone. 

resources: 

todo
0. import funding rate data - DONE
1. build the backtest
    - update the code so it properly identifies the dz
    - make sure to only buy -X funding