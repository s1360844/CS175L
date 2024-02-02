# CS175L
# Jared Mishen
# Stocks

commission_rate_stockpurchase = float(input('Enter commission rate percentage on stock purchase: '))
commission_rate_stocksale = float(input('Enter commission rate percentage on stock sale: '))
number_of_shares_purchased = int(input('Enter number of shares purchased: '))
number_of_shares_sold = int(input('Enter number of shares sold: '))
purchase_price_per_share = float(input('Enter purchase price per share: '))
sell_price_per_share = float(input('Enter sell price per share: '))


amount_paid_for_stock = number_of_shares_purchased*purchase_price_per_share
purchase_commission = commission_rate_stockpurchase * amount_paid_for_stock
total_paid = amount_paid_for_stock + purchase_commission
stock_sold_for = number_of_shares_purchased * sell_price_per_share
selling_commission = commission_rate_stockpurchase * stock_sold_for
total_received = stock_sold_for - selling_commission
profit_or_loss = total_received - total_paid

print("")
display_amount_paid_stock = "Amount paid for stock: ${:,.2f}"
print(display_amount_paid_stock.format(amount_paid_for_stock))
display_commission_paid_purchase = "Commission paid on the purchase: ${:,.2f}"
print(display_commission_paid_purchase.format(purchase_commission))
display_amount_stock_sold = "Amount the stock sold for: ${:,.2f}"
print(display_amount_stock_sold.format(stock_sold_for))
display_commission_paid_sale = "Commission paid on the sale ${:,.2f}"
print(display_commission_paid_sale.format(selling_commission))
display_profit = "Profit (or loss if negative): ${:,.2f}"
print(display_profit.format(profit_or_loss))


        
