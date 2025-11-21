import os
from datetime import datetime

from random_user_agent import RandomUserAgent

def create_temp_file() -> str:
    now: str = datetime.now().strftime("%d%m%y_%H:%M:%S")
    temp_filename: str = "temp_file_" + now + "txt"

    android_ua: str = "Mozilla/5.0 (Linux; U; Android 4.0.3; en-us; KFTT Build/IML74K) AppleWebKit/537.36 (KHTML, like Gecko) Silk/3.68 like Chrome/39.0.2171.93 Safari/537.36"
    ios_ua: str = "Mozilla/5.0 (iPad; CPU OS 8_4_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) CriOS/45.0.2454.68 Mobile/12H321 Safari/600.1.4"
    windows_ua: str = "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:39.0) Gecko/20100101 Firefox/39.0"
    macintosh_ua: str = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/600.6.3 (KHTML, like Gecko) Version/7.1.6 Safari/537.85.15"

    with open(temp_filename, "w") as file:
        file.write(android_ua + '\n')
        file.write(windows_ua + '\n')
        file.write(ios_ua + '\n')
        file.write(macintosh_ua + '\n')

    return temp_filename


def del_temp_file(temp_filename: str):
    if os.path.exists(temp_filename):
        os.remove(temp_filename)


def test_get_random_desktop_agent():
    a = RandomUserAgent()
    result = a.get_random_desktop_agent()
    print("DESKTOP USER AGENT: ", result)
    assert isinstance(result, str)
    assert len(result) > 0

    temp_file_w_agents = create_temp_file()
    b = RandomUserAgent(file_w_agents=temp_file_w_agents)
    result_b = b.get_random_desktop_agent()
    assert isinstance(result_b, str)
    assert len(result_b) > 0

    del_temp_file(temp_file_w_agents)


def test_get_random_modile_agent():
    a = RandomUserAgent()
    result = a.get_random_mobile_agent()
    print("MOBILE USER AGENT: ", result)
    assert isinstance(result, str)
    assert len(result) > 0

    temp_file_w_agents = create_temp_file()
    b = RandomUserAgent(file_w_agents=temp_file_w_agents)
    result_b = b.get_random_mobile_agent()
    assert isinstance(result_b, str)
    assert len(result_b) > 0

    del_temp_file(temp_file_w_agents)


def test_get_random_desktop_agent_benchmark(benchmark):
    ua = RandomUserAgent()
    benchmark(ua.get_random_desktop_agent)


def test_get_random_mobile_agent_benchmark(benchmark):
    ua = RandomUserAgent()
    benchmark(ua.get_random_mobile_agent)

