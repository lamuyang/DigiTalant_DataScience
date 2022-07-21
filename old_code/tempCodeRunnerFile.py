)[1])
    # print(T_time[i])
    a = all_weather[Taipei["測站"].to_list()[i].split("\'")[1]]["Unnamed: 18"].to_list().index(T_time[i])
    # print(a)
    precp = all_weather[Taipei["測站"].to_list()[i].split("\'")[1]]["Precp"].to_list()[a]
    if precp == "t":
        precp = float(0.0)
    WS = all_weather[Taipei["測站"].to_list()[i].split("\'")[1]]["WS"].to_list()[a]
    WSGust = all_weather[Taipei["測站"].to_list()[i].split("\'")[1]]["WSGust"].to_list()[a]
    if WSGust == "...":
        WSGust = float(0.0)
    print([precp,WS,WSGust])
    DataWithWeather.append([float(precp),float(WS),float(WSGust)])