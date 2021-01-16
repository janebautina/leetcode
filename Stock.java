public class Stock {
    public int maxProfit(int[] prices) {
        if(prices == null | prices.length == 0)
          return 0;
        int maxP = Integer.MIN_VALUE;
        int localMin = prices[0];
        for (int i = 0; i < prices.length; i++) {
            if(prices[i] >= localMin) {
                if(prices[i] - localMin > maxP)
                    maxP = prices[i] - localMin;
            }
            else{
               localMin = prices[i];
            }
        }
        return maxP;
    }
}
