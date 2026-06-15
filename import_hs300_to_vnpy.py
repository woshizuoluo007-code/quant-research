import pandas as pd
from datetime import datetime
from zoneinfo import ZoneInfo

from vnpy.trader.object import BarData
from vnpy.trader.constant import Exchange, Interval
from vnpy.trader.database import get_database


df = pd.read_csv("hs300.csv")

bars = []

for _, row in df.iterrows():
    dt = datetime.strptime(row["date"], "%Y-%m-%d")
    dt = dt.replace(tzinfo=ZoneInfo("Asia/Shanghai"))

    bar = BarData(
        symbol="000300",
        exchange=Exchange.SSE,
        datetime=dt,
        interval=Interval.DAILY,
        volume=row["volume"],
        turnover=0,
        open_interest=0,
        open_price=row["open"],
        high_price=row["high"],
        low_price=row["low"],
        close_price=row["close"],
        gateway_name="DB",
    )

    bars.append(bar)

database = get_database()
database.save_bar_data(bars)

print(f"Saved {len(bars)} bars into vn.py database.")