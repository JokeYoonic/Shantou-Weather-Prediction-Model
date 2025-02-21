import pandas as pd
import os

def load_and_merge_shantou_data():
    base_path = '../data/raw'
    temperature_humidity_file = os.path.join(base_path, 'temperature_and_humidity_data.txt')
    temperature_pressure_file = os.path.join(base_path, 'temperature_and_pressure_data.txt')
    wind_direction_file = os.path.join(base_path, 'wind_direction_data.txt')
    wind_speed_file = os.path.join(base_path, 'wind_speed_data.txt')
    output_csv_file = os.path.join(base_path, 'shantou_data.csv')

    # 加载温度和湿度数据
    temperature_humidity_df = pd.read_csv(temperature_humidity_file, sep=',', header=None, names=['timestamp', 'temperature', 'unit1', 'humidity', 'unit2'])
    temperature_humidity_df = temperature_humidity_df[['timestamp', 'temperature', 'humidity']]
    temperature_humidity_df['timestamp'] = pd.to_datetime(temperature_humidity_df['timestamp'])

    # 加载温度和气压数据
    temperature_pressure_df = pd.read_csv(temperature_pressure_file, sep=',', header=None, names=['timestamp', 'temperature', 'unit1', 'pressure', 'unit2'])
    temperature_pressure_df = temperature_pressure_df[['timestamp', 'temperature', 'pressure']]
    temperature_pressure_df['timestamp'] = pd.to_datetime(temperature_pressure_df['timestamp'])

    # 加载风向数据
    wind_direction_df = pd.read_csv(wind_direction_file, sep=',', header=None, names=['timestamp', 'wind_direction', 'unit1', 'wind_direction_name', 'unit2'])
    wind_direction_df = wind_direction_df[['timestamp', 'wind_direction', 'wind_direction_name']]
    wind_direction_df['timestamp'] = pd.to_datetime(wind_direction_df['timestamp'])

    # 加载风速数据
    wind_speed_df = pd.read_csv(wind_speed_file, sep=',', header=None, names=['timestamp', 'wind_speed', 'unit'])
    wind_speed_df = wind_speed_df[['timestamp', 'wind_speed']]
    wind_speed_df['timestamp'] = pd.to_datetime(wind_speed_df['timestamp'])

    # 合并数据
    merged_df = temperature_humidity_df.merge(
        temperature_pressure_df, on='timestamp', suffixes=('_th', '_tp'), how='outer'
    ).merge(
        wind_direction_df, on='timestamp', how='outer'
    ).merge(
        wind_speed_df, on='timestamp', how='outer'
    )

    # 保存到CSV文件
    merged_df.to_csv(output_csv_file, index=False)

    print(f"Merged data saved to {output_csv_file}")

if __name__ == "__main__":
    load_and_merge_shantou_data()