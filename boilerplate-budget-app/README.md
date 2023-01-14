# Budget App

The budget app can display and expenditure ledger:

Here is an example of the output:

    *************Food*************
    initial deposit        1000.00
    groceries               -10.15
    restaurant and more foo -15.89
    Transfer to Clothing    -50.00
    Total: 923.96   
    
It will also display an expenditure chart, using the `create_spend_chart` function, showing the percentage expenditure in each category:

An example output of the chart is:

    Percentage spent by category
    100|          
    90|          
    80|          
    70|          
    60| o        
    50| o        
    40| o        
    30| o        
    20| o  o     
    10| o  o  o  
    0| o  o  o  
        ----------
        F  C  A  
        o  l  u  
        o  o  t  
        d  t  o  
           h     
           i     
           n     
           g     

The unit tests for this project are in `test_module.py`.
