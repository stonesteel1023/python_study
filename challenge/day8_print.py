import csv
import os
import time
import requests
import traceback
from typing import List, Dict
from multiprocessing import Process, Manager, Queue, cpu_count
from bs4 import BeautifulSoup

alba_url = "http://www.alba.co.kr"


def soup_page(response_text: str) -> BeautifulSoup:
    soup = BeautifulSoup(response_text, "html.parser")
    return soup


def get_companies() -> List[Dict[str, str]]:
    company_info_list: List[Dict[str, str]] = []
    response = requests.get(alba_url)
    if response.status_code != 200:
        return company_info_list

    soup = soup_page(response.text)

    company_elements = (
        soup.find("div", id="MainSuperBrand")
        .find("ul", class_="goodsBox")
        .find_all("li")
    )
    for company_element in company_elements:
        if "noInfo" in company_element["class"]:
            continue

        name = company_element.find("span", class_="company").text
        url = company_element.find("a").get("href")
        company_info: Dict[str, str] = {"name": name, "url": url}
        company_info_list.append(company_info)

    return company_info_list


def get_company_detail(queue: Queue):
    while not queue.empty():
        company_info = queue.get(True, 1)
        try:
            name = company_info["name"]
            url = company_info["url"]
            recruit_info_list: List[Dict[str, str]] = []
            response = requests.get(url)
            if response.status_code != 200:
                return

            soup = soup_page(response.text)

            recruit_div = soup.find("div", id="NormalInfo").find("tbody")
            if recruit_div:
                recruit_info_elements = recruit_div.find_all("tr")
                for recruit_element in recruit_info_elements:
                    if (
                        "해당 조건/분류에 일치하는 채용정보가 없습니다" in recruit_element.text
                        or "summaryView" in recruit_element.get("class")
                    ):
                        continue

                    place = recruit_element.find("td", class_="local").text
                    title = (
                        recruit_element.find("td", class_="title")
                        .find("span", class_="title")
                        .text
                    )
                    time = ""
                    time_element = recruit_element.find("td", class_="data").find(
                        "span", class_="time"
                    )
                    if time_element:
                        time = time_element.text
                    pay = recruit_element.find("td", class_="pay").text
                    date = recruit_element.find("td", class_="regDate").text

                    if place and title and time and pay and date:
                        recruit_info = {
                            "place": place,
                            "title": title,
                            "time": time,
                            "pay": pay,
                            "date": date,
                        }
                        recruit_info_list.append(recruit_info)

            if not os.path.exists("./data"):
                os.mkdir("./data")
            with open(
                f"./data/{name}.csv", "w", newline="", encoding="utf-8"
            ) as csvfile:
                writer = csv.DictWriter(
                    csvfile, fieldnames=["place", "title", "time", "pay", "date"]
                )
                for recruit_info in recruit_info_list:
                    writer.writerow(recruit_info)

        except ConnectionError:
            print(f"{company_info['url']} is down!")

        except Exception as e:
            print(e)
            print(traceback.format_exc())


class Worker:
    def __init__(self):
        self.manager = Manager()
        self.queue = self.manager.Queue()
        self.num_of_process = cpu_count()
        self.processes = []

    def put_data(self, data_list: List[Dict[str, str]]):
        for data in data_list:
            self.queue.put(data)

    def start(self, consumer, count):
        self.processes = [
            Process(target=consumer, args=(self.queue,)) for _ in range(0, count)
        ]

    def join(self):
        for process in self.processes:
            process.start()

        for process in self.processes:
            process.join()


class Timer:
    def __init__(self):
        self.elapsed_time = 0
        self.start = 0
        self.end = 0

    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, *args):
        self.end = time.time()
        self.elapsed_time = self.end - self.start


if __name__ == "__main__":
    try:
        company_info_list = get_companies()

        if not company_info_list:
            exit(0)

        with Timer() as timer:
            worker = Worker()
            worker.put_data(company_info_list)
            worker.start(get_company_detail, cpu_count())
            worker.join()

        print("실행 시간: {:.5f}초".format(timer.elapsed_time))

    except ConnectionError:
        print(f"{alba_url} is down!")
