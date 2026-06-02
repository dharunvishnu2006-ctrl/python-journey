import numpy as np

prices = np.array([100, 250, 500, 750, 1000])
gst_prices = prices * 1.18

print("Original:", prices)
print("With GST:", gst_prices)