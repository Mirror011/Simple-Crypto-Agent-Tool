import requests

def get_crypto_price(coin_id='bitcoin'):
    """
    这是一个简单的 AI Agent 核心功能：获取实时市场数据
    """
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies=usd"
    try:
        response = requests.get(url)
        data = response.json()
        price = data[coin_id]['usd']
        print(f"【Agent 通知】当前 {coin_id.upper()} 的价格为: ${price} USD")
        
        # 简单的逻辑判断（Agent 的初步决策模拟）
        if price < 50000:
            print("策略建议: 当前价格较低，适合定投。")
        else:
            print("策略建议: 市场处于高位，建议观望。")
            
    except Exception as e:
        print(f"获取数据失败: {e}")

if __name__ == "__main__":
    get_crypto_price('bitcoin')
