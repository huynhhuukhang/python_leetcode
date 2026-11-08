import numpy as np
import pandas as pd

def moving_avg(d, extra_periods=4, n=3):
    d = np.array(d, dtype=float)
    cols = len(d)
    d_extended = np.append(d, [np.nan] * extra_periods)
    f = np.full(cols + extra_periods, np.nan)
    
    for t in range(n, cols):
        f[t] = np.mean(d[t-n:t])
        
    for t in range(cols, cols + extra_periods):
        f[t] = np.mean(d[t-n:t])
        
    df = pd.DataFrame({
        'Demand': d_extended[:cols], 
        'Forecast': f[:cols], 
        'Error': d_extended[:cols] - f[:cols]
    })
    return df, f

sales_data = [
    362, 385, 432, 341, 
    382, 409, 498, 387, 
    473, 513, 582, 474, 
    544, 582, 681, 557, 
    628, 707, 773, 592, 
    627, 725, 854, 661
]

n_periods = 3
df_result, full_forecast = moving_avg(sales_data, extra_periods=4, n=n_periods)

df_result.index.name = "Period"
print(df_result.head(10))

errors = df_result["Error"].dropna()
MAE = errors.abs().mean()
RMSE = np.sqrt((errors**2).mean())

print(f"\n--- KẾT QUẢ ĐÁNH GIÁ (n = {n_periods}) ---")
print(f"MAE: {round(MAE, 2)}")
print(f"RMSE: {round(RMSE, 2)}")

print("\n--- DỰ BÁO 4 KỲ NĂM 95 ---")
for i, val in enumerate(full_forecast[len(sales_data):], start=1):
    print(f"Năm 95 - Quý {i}: {round(val, 2)}")