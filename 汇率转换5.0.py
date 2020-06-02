"""
功能：汇率转换
作者：周润发
时间：20200530
版本:2.0
新增功能：根据输入判断人民币还是美元
版本：3.0
新增功能：用户选择退出时才能退出，否则一直执行
版本：4.0
新增功能：函数封装
版本：5.0
新增功能：程序结构化
"""

USD_VS_RMB = 6.77

# #def convert_currency(im, er):
#     """
#     汇率函数
#     :param im:
#     :param er:
#     :return:
#     """
#     return im * er

def main():
    """
    主函数
    :return:
    """

    print("*********************************************************")
    currency_str_value = input("请输入带单位的货币（CNY/USD）数量（退出请输入Q）：")


    while currency_str_value != "Q":
        unit = currency_str_value[-3:]
        if unit == 'CNY' :
            exchange_rate = 1 / USD_VS_RMB
            unit_out = "USD"

        elif unit == 'USD' :
            exchange_rate = USD_VS_RMB
            unit_out = "CNY"

        else:
            exchange_rate = -1
            print("Current version is not support this unit")

        if exchange_rate != -1:
            value_number = eval(currency_str_value[:-3])
            #使用lambda函数
            convert_currency2 = lambda x: x * exchange_rate


            #调用函数
            #out_value = convert_currency(value_number, exchange_rate)
            out_value = convert_currency2(value_number)

            print("汇率计算结果为：%.2f" % out_value, unit_out)
            print("*********************************************************")
            currency_str_value = input("请输入带单位的货币（CNY/USD）数量（退出请输入Q）：")
        else:
            print("不支持该种货币")
            break
    print("程序已退出，感谢您的使用！")

if __name__ == "__main__":
    main()